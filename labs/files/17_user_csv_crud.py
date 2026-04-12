import csv
import hashlib
import os
import secrets
import tempfile
from settings import CSV_PATH

DATA_FILE = CSV_PATH / "users.csv"

DISPLAY_FIELDS = [
    "id",
    "username",
    "first_name",
    "last_name",
    "email",
    "dob",
    "gender",
    "is_active",
    "last_login",
    "phone",
]

PASSWORD_FIELD = "password_hash"


def load_users():
    """Load user rows from CSV into a list of dictionaries."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"CSV file not found: {DATA_FILE}")

    with DATA_FILE.open("r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        fieldnames = list(reader.fieldnames or [])
        users = [dict(row) for row in reader]

    if "id" not in fieldnames:
        fieldnames.insert(0, "id")
        for index, user in enumerate(users, start=1):
            user["id"] = str(index)
        save_users(users, fieldnames)

    return users, fieldnames


def save_users(users, fieldnames):
    """Save user rows back to CSV using a temporary file."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        newline="",
        encoding="utf-8",
        delete=False,
        dir=str(DATA_FILE.parent),
    ) as temp_file:
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(users)
        temp_name = temp_file.name

    os.replace(temp_name, DATA_FILE)


def list_users(users):
    """Return a list of users represented as dictionaries."""
    return users


def find_user(users, key, value):
    """Return the first user that matches the key/value pair."""
    return next((user for user in users if user.get(key) == value), None)


def is_email_unique(email, users, current_user=None):
    normalized = email.strip().lower()
    for user in users:
        if user.get("email", "").strip().lower() == normalized:
            if current_user is None or user.get("id") != current_user.get("id"):
                return False
    return True


def hash_password(password):
    """Create a salted hash for the given password."""
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100_000,
    )
    return f"{salt}${digest.hex()}"


def validate_user_data(user, users, current_user=None):
    """Validate user data for create or update operations."""
    errors = []
    email = user.get("email", "").strip()
    first_name = user.get("first_name", "").strip()
    last_name = user.get("last_name", "").strip()
    password = user.get("password", "")

    if current_user is None or "email" in user:
        if not email:
            errors.append("El email es obligatorio.")
        elif "@" not in email or "." not in email:
            errors.append("El email no tiene formato válido.")
        elif not is_email_unique(email, users, current_user):
            errors.append("El email ya existe.")

    if current_user is None or "first_name" in user:
        if not first_name:
            errors.append("El first_name no puede estar vacío.")

    if current_user is None or "last_name" in user:
        if not last_name:
            errors.append("El last_name no puede estar vacío.")

    if current_user is None or "password" in user:
        if current_user is None and not password:
            errors.append("La contraseña es obligatoria.")
        if password and len(password) < 8:
            errors.append("La contraseña debe tener al menos 8 caracteres.")

    if "id" in user and user.get("id"):
        if any(
            u.get("id") == user["id"]
            and (current_user is None or u.get("id") != current_user.get("id"))
            for u in users
        ):
            errors.append("El id ya existe.")

    return errors


def create_user(users, fieldnames, new_user):
    """Add a new user dictionary to the list and save."""
    errors = validate_user_data(new_user, users)
    if errors:
        raise ValueError("; ".join(errors))

    if "password" in new_user:
        new_user[PASSWORD_FIELD] = hash_password(new_user.pop("password"))

    max_id = max((int(user.get("id", 0)) for user in users), default=0)
    new_user["id"] = str(max_id + 1)
    users.append(new_user)
    save_users(users, fieldnames)
    return new_user


def update_user(users, fieldnames, user_id, updates):
    """Update an existing user by id."""
    user = find_user(users, "id", str(user_id))
    if not user:
        return None

    if not updates:
        return user

    errors = validate_user_data(updates, users, current_user=user)
    if errors:
        raise ValueError("; ".join(errors))

    if "password" in updates:
        updates[PASSWORD_FIELD] = hash_password(updates.pop("password"))

    for key, value in updates.items():
        if key in fieldnames and value is not None:
            user[key] = value

    save_users(users, fieldnames)
    return user


def delete_user(users, fieldnames, user_id):
    """Remove a user by id."""
    original_count = len(users)
    users[:] = [user for user in users if user.get("id") != str(user_id)]
    deleted = len(users) < original_count
    if deleted:
        save_users(users, fieldnames)
    return deleted


def format_user(user):
    """Format a single user for display."""
    return {field: user.get(field, "") for field in DISPLAY_FIELDS}


def prompt_for_user(fieldnames):
    """Prompt the user to enter values for a new user."""
    print("Crear usuario nuevo. Deja vacío para omitir un campo opcional.")
    user = {}
    for field in fieldnames:
        if field in {"id", PASSWORD_FIELD}:
            continue
        value = input(f"{field}: ").strip()
        if value:
            user[field] = value

    password = input("password: ").strip()
    if password:
        user["password"] = password
    return user


def prompt_for_updates(fieldnames):
    """Prompt the user for fields to update."""
    print("Ingresa los nuevos valores. Deja vacío para no cambiar el campo.")
    updates = {}
    for field in fieldnames:
        if field in {"id", PASSWORD_FIELD}:
            continue
        value = input(f"{field} (actual): ").strip()
        if value:
            updates[field] = value

    password = input("password nueva (dejar vacío para conservar la actual): ").strip()
    if password:
        updates["password"] = password
    return updates


def print_users(users):
    """Print a simple table of users."""
    header = ", ".join(DISPLAY_FIELDS)
    print(header)
    print("-" * len(header))
    for user in users:
        row = [str(user.get(field, "")) for field in DISPLAY_FIELDS]
        print(", ".join(row))


def main():
    try:
        users, fieldnames = load_users()
    except FileNotFoundError as exc:
        print(exc)
        return

    while True:
        print("\nCRUD de usuarios con CSV")
        print("1. Listar usuarios")
        print("2. Buscar usuario por email")
        print("3. Agregar usuario")
        print("4. Actualizar usuario por id")
        print("5. Eliminar usuario por id")
        print("6. Salir")

        choice = input("Selecciona una opción: ").strip()

        if choice == "1":
            print_users(list_users(users))
        elif choice == "2":
            email = input("Email: ").strip()
            user = find_user(users, "email", email)
            print(user if user else "No se encontró el usuario.")
        elif choice == "3":
            new_user = prompt_for_user(fieldnames)
            if not new_user:
                print("No se ingresaron datos. Operación cancelada.")
                continue
            try:
                created = create_user(users, fieldnames, new_user)
                print(f"Usuario creado: {created}")
            except ValueError as exc:
                print(f"Error de validación: {exc}")
        elif choice == "4":
            user_id = input("ID del usuario a actualizar: ").strip()
            updates = prompt_for_updates(fieldnames)
            try:
                updated = update_user(users, fieldnames, user_id, updates)
                print(updated if updated else "No se encontró el usuario o no se actualizó.")
            except ValueError as exc:
                print(f"Error de validación: {exc}")
        elif choice == "5":
            user_id = input("ID del usuario a eliminar: ").strip()
            deleted = delete_user(users, fieldnames, user_id)
            print("Usuario eliminado." if deleted else "No se encontró el usuario.")
        elif choice == "6":
            print("Saliendo.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
