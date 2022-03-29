import random
import string
from dataclasses import dataclass

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))
@dataclass
class Person:
    name:str
    address:str

def main() -> None:
    person = Person(name="john", address="yatop-ro 162")
    print(person)

if __name__ == "__main__":
    main()