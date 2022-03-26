from dataclasses import dataclass


class DataclassWithoutDataClass:
    """Every time a new field is add we need to add in constructor and change __str__ method and a lot of manual stuff
    for data oriented classes"""
    def __init__(self, name, address, pincode, sex, age) -> None:
        self.name=name
        self.address=address
        self.pincode=pincode
        self.sex=sex
        self.age=age

    def __str__(self):
        return f"{self.name}: {self.address}"

@dataclass
class DataclassDemo:
    """Instance varibles are defined as class variables and __init__ and __repr__ are created automatically"""
    name: str
    address: str
    pincode: str
    sex: str
    age: int


if __name__ == "__main__":
    person=DataclassWithoutDataClass("Adi","Aligarh","202001","Male",30)
    print(person)
    other_person=DataclassDemo("Adi","Aligarh","202001","Male",30)
    print(other_person)