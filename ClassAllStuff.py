# Explanation:
# Instance attributes
# Docstring
# Class attributes

class ShippingContainerInstanceAndClassAttributes:
    """This is the Docstring place, it keeps the info in the help command of what this class does"""
    # Since class do not have any scope, following class attribute is defined in global scope.
    # So to call this class attrib we have qualify it with full name i.e. ShippingContainer.next_serial
    next_serial = 1337

    def __init__(self, owner_code, contents):
        # Instance attributes
        # Assigning values through self.arg_name is how instance attributes come into existance
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainerInstanceAndClassAttributes.next_serial
        ShippingContainerInstanceAndClassAttributes.next_serial += 1

        # BAD CODEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        # Following is invalid code as class attrib we have qualify it with full name
        self.serial = next_serial  # Correction ShippingContainer.next_serial
        next_serial += 1  # ShippingContainer.next_serial += 1

        # Following is valid code but has a bug and some issues
        # It will access the class attribute but is less explicit as we don't if it a class or instance attribute
        self.serial = self.next_serial
        # Bug as self.next_serial will create an new instance attribute and will hide original class attribute
        self.next_serial += 1
        # BAD CODEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE


ins_obj_tes1 = ShippingContainerInstanceAndClassAttributes(
    "YML", ["conti", "bonti", "jonti"])
ins_obj_tes2 = ShippingContainerInstanceAndClassAttributes(
    "KKP", ["honti", "wonti", "konti"])
print(ins_obj_tes1.contents, ins_obj_tes1.owner_code)
print(ins_obj_tes2.contents, ins_obj_tes2.owner_code)
# ['conti', 'bonti', 'jonti'] YML
# ['honti', 'wonti', 'konti'] KKP

#######################################################################################################################
# Explanation:
# Class Methods
# Static Methods


class ShippingContainerWithStaticMethod:

    next_serial = 1337
    # leading underscore(_) is an method means it's an implementation details aka private method and does not intented to use outside.
    # _generate_serial(self), as self is not required as it's not used in the method inside so we use @staticmethod

    @staticmethod
    def _generate_serial():
        result = ShippingContainerWithStaticMethod.next_serial
        ShippingContainerWithStaticMethod.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # don't use self._generate_serial() as it's a static method now
        self.serial = ShippingContainerWithStaticMethod._generate_serial()

#######################################################################################################################
# When to use Class method or Static method?
# Whenever there's a need to the class object to call class methods or constructor use @classmethod
# Whenever there's no need to access class or instance objects use @staticmethod
# @staticmethods are mostly implementation details of class
# @staticmethods can also be moved outside the class to global module scope without the decorator, So it's a design choice as it's merely a logical organization of code


class ShippingContainerWithClassMethod:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # Class method can also be used as a factory function (objects with certain configuration), clients can call to intialize constructer with different configuration
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainerWithClassMethod._generate_serial()

#######################################################################################################################
# Static Method Inheritance
# For Polymorphic dispatch of invoke static method with self


class ShippingContainerStaticMethodInheritance:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # instead ShippingContainerStaticMethodInheritance._make_bic_code use self
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainerStaticMethodInheritance._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainerStaticMethodInheritance):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )

#######################################################################################################################
