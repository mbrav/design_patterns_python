from abc import ABC, abstractmethod


class Chair():
    """Chair Class"""

    def __init__(self) -> None:
        pass


class Table():
    """Table Class"""

    def __init__(self) -> None:
        pass


class Sofa():
    """Sofa Class"""

    def __init__(self) -> None:
        pass


class FurnitureFactory(ABC):
    """Abstract Furniture Factory class"""

    def __init__(self) -> None:
        pass

    @abstractmethod
    @staticmethod
    def create_chair(self):
        """Chair creation abstract method """
        pass

    @abstractmethod
    @staticmethod
    def create_table(self):
        """Chair creation abstract method """
        pass

    @abstractmethod
    @staticmethod
    def create_sofa(self):
        """Chair creation abstract method """
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    """Victorian Furniture Factory class"""

    def create_chair(self):
        print('Victorian chair created')

    def create_table(self):
        print('Victorian table created')

    def create_sofa(self):
        print('Victorian sofa created')


class ModernFurnitureFactory(FurnitureFactory):
    """Modern Furniture Factory class"""

    def create_chair(self):
        print('Modern chair created')

    def create_table(self):
        print('Modern table created')

    def create_sofa(self):
        print('Modern sofa created')


class ArtDecoFurnitureFactory(FurnitureFactory):
    """ArtDeco Furniture Factory class"""

    def create_chair(self):
        print('ArtDeco chair created')

    def create_table(self):
        print('ArtDeco table created')

    def create_sofa(self):
        print('ArtDeco sofa created')


class AbstractFactory:
    """Abstract Factory class"""

    @staticmethod
    def createDeliveryRoute(*args, **kwargs):
        return DeliveryRoute(*args, **kwargs)

    @staticmethod
    def createTruck(*args, **kwargs):
        return Truck(*args, **kwargs)

    @staticmethod
    def createTrain(*args, **kwargs):
        return Train(*args, **kwargs)

    @staticmethod
    def createShip(*args, **kwargs):
        return Ship(*args, **kwargs)

    @staticmethod
    def createLogistics():
        return Logistics()
