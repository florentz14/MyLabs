# -------------------------------------------------
# File Name: pet_management_system.py
# Author: Florentino Baez
# Course: ITSE-1003
# Professor: Mauricio Quiroga
# Date: 18/03/2026
# Description: Lab 1 - Mini project - Pet Management System using OOP.
# -------------------------------------------------

class Dog:
    """Base class for a dog."""

    # constructor for Dog class
    def __init__(self, name: str, age: int) -> None:
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.name = name
        self.age = age

    # describe returns the name and age of the dog
    def describe(self) -> str:
        return f"{self.name} is {self.age} years old"

    # bark returns "Woof!"
    def bark(self) -> str:
        return "Woof!"


class Puppy(Dog):
    """Derived class that inherits from Dog."""

    # play returns "The puppy is playing!"
    def play(self) -> str:
        return "The puppy is playing!"

def main() -> None:
    """Main function to demonstrate the pet management system."""
    # list of pets
    pets: list[Dog] = [
        Dog("Buddy", 3),
        Dog("Rocky", 5),
        Puppy("Max", 1),
    ]

    for pet in pets:
        print(pet.describe())
        if isinstance(pet, Puppy):
            print(pet.play())
        else:
            print(pet.bark())

# run the main function
if __name__ == "__main__":
    main()