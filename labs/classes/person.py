from dataclasses import dataclass, asdict
from typing import Optional, Dict
import re


@dataclass
class Person:
    first_name: str
    last_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> "Person":
        return cls(
            first_name=data.get("first_name") or data.get("firstName") or data.get("name", ""),
            last_name=data.get("last_name") or data.get("lastName"),
            age=data.get("age"),
            email=data.get("email"),
        )

    def is_valid_email(self) -> bool:
        if not self.email:
            return False
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.email) is not None

from dataclasses import field
from typing import List


@dataclass
class User(Person):
    username: str = ""
    roles: List[str] = field(default_factory=list)
    active: bool = True

    def is_admin(self) -> bool:
        return "admin" in (self.roles or [])

    def greet(self) -> str:
        return f"Hello, {self.full_name()} ({self.username})"


@dataclass
class Seller(User):
    store_name: Optional[str] = None
    rating: Optional[float] = None

    def sell_item(self, item: str) -> str:
        store = f" from {self.store_name}" if self.store_name else ""
        return f"Selling {item}{store}"


@dataclass
class Vendor(User):
    company: Optional[str] = None
    products: List[str] = field(default_factory=list)

    def list_products(self) -> List[str]:
        return list(self.products)


@dataclass
class Student(Person):
    student_id: str = ""
    major: Optional[str] = None
    gpa: Optional[float] = None

    def is_passing(self, threshold: float = 2.0) -> bool:
        return (self.gpa or 0.0) >= threshold

