class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(Device):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Thermostat(Device):
    def turn_on(self):
        print("Thermostat is ON")

    def turn_off(self):
        print("Thermostat is OFF")

class SmartHome:
    def __init__(self, devices):
        self.devices = devices

    def control_devices(self):
        for device in self.devices:
            device.turn_on()
            device.turn_off()

lights = [Light(), Light()]
thermostats = [Thermostat(), Thermostat()]

smart_home_lights = SmartHome(lights)
smart_home_thermostats = SmartHome(thermostats)

smart_home_lights.control_devices()
smart_home_thermostats.control_devices()


# In this example, the Dependency Inversion Principle is applied because:

# We use an abstract Device interface to define the behavior that all devices should have.
# The Light and Thermostat classes implement the Device interface, ensuring they provide the required methods.
# The SmartHome class depends on the Device interface, not on specific implementations. This allows us to control different devices interchangeably.
# If we want to add new types of devices in the future, we can create new classes that implement the Device interface, and the SmartHome class can still control them without any changes. This demonstrates how the Dependency Inversion Principle helps create a more flexible and extensible codebase.







from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))
            
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)