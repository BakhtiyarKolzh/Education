# dataclass
from dataclasses import dataclass


@dataclass
class Clent:
    # def __init__(self, name: str, city: str):
    #     self.name=name
    #     self.city=city
    #
    # def __str__(self):
    #     return f"{self.name} from {self.city} city"
    #
    name: str
    city: str
    age: int


client=Clent(name="Timur", city="Almaty", age=18)
print(client)