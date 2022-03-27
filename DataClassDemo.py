from dataclasses import dataclass, field
import random
import string

def generate_id():
    return "".join(random.choices(string.ascii_uppercase, k=12))
class PersonWithoutDataClass:
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
class PersonWithDataclass:
    """Instance varibles are defined as class variables and __init__ and __repr__ are created automatically"""
    name: str
    address: str
    pincode: str
    sex: str
    age: int
    active: bool = True # A boolean with Boolean data type with default True value
    # We cannot do default value to [] because at interpret time all instances will have same list.
    # So all will have same email address as all refer same list
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False,repr=False)

def main():
    person=PersonWithoutDataClass("Adi","Aligarh","202001","Male",30)
    print(person)
    other_person=PersonWithDataclass("Adi","Aligarh","202001","Male",30)
    print(other_person)    

if __name__ == "__main__":
    main()
    
    
    
    