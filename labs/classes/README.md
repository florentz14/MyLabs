# Object-oriented programming (`labs/classes`)

Small, self-contained Python modules for practicing **classes**, **inheritance**, **`__str__` / `__repr__`**, **`@dataclass`**, and simple **domain modeling** (people, invoices, appliances).

Run scripts from the **repository root** (with the venv activated if you use one):

```bash
python3 labs/classes/basic_oop.py
```

## Scripts

| File | Role | Description |
| --- | --- | --- |
| `basic_oop.py` | OOP intro | Entry point: `Person` with `__init__`, `greet()`, `__repr__` — minimal runnable example. |
| `employee.py` | String forms | `Employee` with `__str__` vs `__repr__` for readable vs debug output. |
| `person.py` | Dataclass / inheritance | `@dataclass` `Person`; `User` → `Seller` / `Vendor` / `Student` — inheritance stacks, `from_dict`, email check. |
| `invoice.py` | Domain model | `InvoiceDetails` + `Invoice`; tax/discount math, line items, **`tabulate`** grid output (`pip install tabulate` or project `requirements.txt`). |
| `microwave.py` | Stateful object | `Microwave` simulator (timer, express cook, tick loop) — attributes and methods driving behavior. |

## Suggested order

1. **`basic_oop.py`** — attributes, methods, string representation.  
2. **`employee.py`** — `__str__` / `__repr__`.  
3. **`person.py`** — dataclasses and small inheritance hierarchies.  
4. **`invoice.py`** — composition (`Invoice` holds `InvoiceDetails`) and formatting.  
5. **`microwave.py`** — larger class with internal state and side effects (`print`).

## Concepts checklist

| File | Role | Description |
| --- | --- | --- |
| Constructors, instance attributes | Concept | `basic_oop.py`, `employee.py` |
| `__repr__` vs `__str__` | Concept | `basic_oop.py`, `employee.py` |
| `@dataclass`, `field(default_factory=…)` | Concept | `person.py` |
| Inheritance / `super` patterns (implicit via dataclass) | Concept | `person.py` (`User`, `Seller`, `Vendor`, `Student`) |
| Composition | Concept | `invoice.py` |
| Encapsulation and state machines | Concept | `microwave.py` |

## Dependencies

- **Standard library** for most files.
- **`invoice.py`** needs **`tabulate`** (listed in the repo root `requirements.txt`).

## Related course work

For a graded **pet management** mini-project (dogs, puppies, list loop), see **`labs/ITSE-1003/pet_management_system.py`** and **`labs/ITSE-1003/README.md`** (Lab 1).

## Other labs

- Tables and analysis: [../pandas/README.md](../pandas/README.md)
- Text/CSV I/O (stdlib): [../files/README.md](../files/README.md)
