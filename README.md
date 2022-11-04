[![UnitTest and MyPy CI](https://github.com/mbrav/design_patterns_python/actions/workflows/unittest.yml/badge.svg?branch=main)](https://github.com/mbrav/design_patterns_python/actions/workflows/unittest.yml)
[![wakatime](https://wakatime.com/badge/user/54ad05ce-f39b-4fa3-9f2a-6fe4b1c53ba4/project/2133ea0a-1269-478f-99d6-e6645f69c2ff.svg)](https://wakatime.com/badge/user/54ad05ce-f39b-4fa3-9f2a-6fe4b1c53ba4/project/2133ea0a-1269-478f-99d6-e6645f69c2ff)

# Design Patterns

A collection of design patterns in Python

## Classification of Design Patterns

Design Patterns are categorized mainly into three categories: *Creational Design Pattern*, *Structural Design Pattern*, and *Behavioral Design Pattern*. These are differed from each other on the basis of their level of detail, complexity, and scale of applicability to the entire system being design.

There are also two types of patterns - *idioms* and *architectural* patterns.

### 1. Creational Design Patterns

As the name suggests, it provides the object or classes creation mechanism that enhance the flexibilities and reusability of the existing code. They reduce the dependency and controlling how the use interaction with our class so we wouldn't deal with the complex construction. Below are the various design pattern of creational design pattern.

- **Factory Method** ([creational/factory.py](design_patterns/creational/factory.py) - Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses. The pattern has creational purpose and applies to classes where deals with relationships through inheritence ie. they are static-fixed at compile time. In contrast to *Abstract Factory*, Factory Method contain method to produce only one type of product.

- **Abstract Factory** ([creational/abstract_factory.py](design_patterns/creational/abstract_factory.py)) - Abstract factory pattern has creational purpose and provides an interface for creating families of related or dependent objects without specifying their concrete classes. Pattern applies to object and deal with object relationships, which are more dynamic. In contrast to *Factory Method*, Abstract Factory pattern produces family of types that are related, ie. it has more than one method of types it produces.

- **Builder** ([creational/builder.py](design_patterns/creational/builder.py)) - A generative design pattern, which allows you to copy objects without going into details of their implementation.
  
- **Prototype** ([creational/prototype.py](design_patterns/creational/prototype.py)) - It is used to create a new object from an existing object,

- **Singleton**([creational/singleton.py](design_patterns/creational/singleton.py)) - Singleton design pattern make sure that only one instance of an object is created.

### 2. Structural Design Patterns (TODO)

Structural Design Patterns mainly responsible for assemble object and classes into a larger structure making sure that these structure should be flexible and efficient. They are very essential for enhancing readability and maintainability of the code. It also ensure that functionalities are properly separated, encapsulated. It reduces the minimal interface between interdependent things.

- **Adapter** ([structural/adapter.py](design_patterns/structural/adapter.py)) - It provides us for two incompatible classes to work together by wrapping an interface around one of the existing classes.

- **Bridge** ([structural/bridge.py](design_patterns/structural/bridge.py))  - It decouples an abstraction so that two classes can vary independently.

- **Composite** ([structural/composite.py](design_patterns/structural/adapter.py))  - It wraps a group of objects into a single object.

- **Decorator** ([structural/decorator.py](design_patterns/structural/decorator.py))  - It extends the object behavior dynamically at the run time.

- **Facade** ([structural/facade.py](design_patterns/structural/facade.py))  - It offers a simple interface to more complex underlying objects.

- **Flyweight** ([structural/flyweight.py](design_patterns/structural/flyweight.py))  - It decreases the cost of complex object model.

- **Proxy** ([structural/proxy.py](design_patterns/structural/proxy.py))  - It reduces the cost, reduce complexity, and provide the placeholder interface to an underlying object to control access.

### 3. Behavior Design Pattern (TODO)

Behavior Design Patterns are responsible for how one class communicates with others.

*Chain of Responsibility* - It representatives the command to a chain of processing object.

- **Command** - It generates the objects which encapsulate actions of parameters.

- **Interpreter** - It implements a specialized language.

- **Iterator** - It accesses all the element of an object sequentially without violating its underlying representation.

- **Mediator** - It provides the loose coupling between classes by being the only class that has detailed knowledge of their existing methods.

- **Memento** - It restores an object in the previous state.

- **Observer** - It allows a number of observer objects to see an event.

- **State** - It allows an object to modify its behavior when it's internal states changes.

- **Strategy** - It provides one of the families of algorithm to be selected at the runtime.

- **Template Method** - It allows the subclasses to provide concrete behavior. It also defines the skeleton of an algorithm as an abstract class.

- **Visitor** - It separates an algorithm from an object structure by moving the hierarchy of methods into one object.

## Application Structure Patterns

- **Layered** -  Layered is a classic pattern, but usually leads to monolit drawbacks where it is hard to separate different logic into separate parts.

- **Microkernel** - The microkernel consists of a "Core" which is augmented by extension parts. The core itself is independent from its extensions.

- **Command Query Responsibility Segregation (CQRS)** - Reduces the amount of complex queries and allows for creation of scenario-specific queries, but requires synchronization. The model is separated into read logic and write logic.

- **Event sourcing** - Stores everything in the current state. All events are things that happen in the past.  The advantage is that it is possible to trace, audit and replay events. There is no need to update database. The disadvantage, is that it becomes hard to identify which events are new, and which ones are replays, which makes it non-trivial.

## Additional resources

- [python-patterns.guide](https://python-patterns.guide/)
- [faif/python-patterns](https://github.com/faif/python-patterns)
