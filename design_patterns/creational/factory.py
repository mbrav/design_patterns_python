"""*What is this pattern about?
A Factory Is a generational design pattern that defines a common interface 
for creating objects in a superclass, allowing subclasses to change the 
type of objects they create.
*What does this example do?
The code shows a way to localize words in two languages: English and
Greek. "get_localizer" is the factory function that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "localize" will be called
in the same way independently of the language.
*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django:
https://docs.djangoproject.com/en/4.0/topics/forms/formsets/
For example, different types of forms are created using a formset_factory
*TL;DR
Creates objects without having to specify the exact class.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class DeliveryStatus(Enum):
    """Delivery status"""
    created = 'created'
    shipping = 'shipping'
    completed = 'completed'


class DeliveryRoute:
    """DeliveryRoute class"""

    def __init__(
            self,
            to: str,
            fr: str,
            status: DeliveryStatus = DeliveryStatus.created) -> None:
        self.to = to
        self.fr = fr
        self.status = status


class Transport(ABC):
    """Transport abstract class"""

    def __init__(self, route: DeliveryRoute = None) -> None:
        self.routes = []
        if route:
            self.routes.append(route)

    def add_route(self, route: DeliveryRoute) -> None:
        """Add route"""
        self.routes.append(route)


class Truck(Transport):
    """Truck class"""


class Ship(Transport):
    """Ship class"""


class Train(Transport):
    """Train class"""


class Logistics:
    """A Logistics factory class"""

    def __init__(self) -> None:
        self.transport = []

    def deliver(self, name: str) -> str:
        """Plan a delivery route"""
        return self.transport.get(name, name)

    def create_transport(self) -> str:
        """Create transport"""
        return self.transport.get(msg, msg)


def main():
    logistics = Logistics()
    print(logistics)


if __name__ == "__main__":
    main()


# class GreekLocalizer:
#     """A simple localizer a la gettext"""

#     def __init__(self) -> None:
#         self.translations = {"dog": "σκύλος", "cat": "γάτα"}

#     def localize(self, msg: str) -> str:
#         """We'll punt if we don't have a translation"""
#         return self.translations.get(msg, msg)


# class EnglishLocalizer:
#     """Simply echoes the message"""

#     def localize(self, msg: str) -> str:
#         return msg


# def get_localizer(language: str = "English") -> object:
#     """Factory"""
#     localizers = {
#         "English": EnglishLocalizer,
#         "Greek": GreekLocalizer,
#     }

#     return localizers[language]()


# def main():
#     """
#     # Create our localizers
#     >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")
#     # Localize some text
#     >>> for msg in "dog parrot cat bear".split():
#     ...     print(e.localize(msg), g.localize(msg))
#     dog σκύλος
#     parrot parrot
#     cat γάτα
#     bear bear
#     """


# if __name__ == "__main__":
#     import doctest

#     doctest.testmod()
