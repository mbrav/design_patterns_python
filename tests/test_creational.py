import unittest

from design_patterns.creational.abstract_factory import AbstractFactory
from design_patterns.creational.builder import (Engine, Fuel, Transmission,
                                                VehicleBlueprint,
                                                VehicleBuilder, VehicleBuilt)
from design_patterns.creational.factory import Factory


class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        FactoryTestCase.logistics = Factory.createLogistics()

    def test_00_init_logistics(self):
        self.logistics = Factory.createLogistics()
        self.assertEqual(len(self.logistics), 0,
                         'Incorrect logistics size')

    def test_01_add_routes(self):
        FactoryTestCase.london_paris = Factory.createDeliveryRoute(
            'London', 'Paris')
        FactoryTestCase.bangkok_beijing = Factory.createDeliveryRoute(
            'Bangkok', 'Beijing')
        FactoryTestCase.berlin_rome = Factory.createDeliveryRoute(
            'Berlin', 'Rome')

        self.assertEqual(self.london_paris.fr, 'London',
                         'Incorrect from destination')
        self.assertEqual(self.bangkok_beijing.fr, 'Bangkok',
                         'Incorrect from destination')
        self.assertEqual(self.berlin_rome.fr, 'Berlin',
                         'Incorrect from destination')

        self.assertEqual(self.london_paris.to, 'Paris',
                         'Incorrect to destination')
        self.assertEqual(self.bangkok_beijing.to, 'Beijing',
                         'Incorrect to destination')
        self.assertEqual(self.berlin_rome.to, 'Rome',
                         'Incorrect to destination')

    def test_02_reverse_routes(self):
        FactoryTestCase.london_paris.reverse()

        self.assertEqual(self.london_paris.fr, 'Paris',
                         'Incorrect reversed from destination')

        FactoryTestCase.london_paris.reverse()

        self.assertEqual(self.london_paris.fr, 'London',
                         'Incorrect from destination')

    def test_03_add_transport(self):
        FactoryTestCase.truck1 = Factory.createTruck(self.london_paris)
        FactoryTestCase.truck2 = Factory.createTruck(self.berlin_rome)
        FactoryTestCase.train1 = Factory.createTrain(self.london_paris)
        FactoryTestCase.train2 = Factory.createTrain(self.berlin_rome)
        FactoryTestCase.ship1 = Factory.createShip(self.bangkok_beijing)

        self.assertEqual(self.truck1.name, 'Truck',
                         'Incorrect transport name')
        self.assertEqual(self.train1.name, 'Train',
                         'Incorrect transport name')
        self.assertEqual(self.ship1.name, 'Ship',
                         'Incorrect transport name')

    def test_04_add_logistics(self):
        self.logistics.add_transport(self.truck1)
        self.logistics.add_transport(self.truck2)
        self.logistics.add_transport(self.train1)
        self.logistics.add_transport(self.train2)
        self.logistics.add_transport(self.ship1)

        self.assertEqual(len(self.logistics), 5,
                         'Incorrect logistics size')

    def test_05_deliver_logistics(self):
        self.logistics.add_transport(self.truck1)
        self.logistics.add_transport(self.train1)
        self.logistics.add_transport(self.ship1)

        self.assertEqual(len(self.logistics), 3,
                         'Incorrect logistics size')

        self.logistics.deliver()
        self.assertEqual(len(self.logistics), 2,
                         'Incorrect logistics size')

        self.logistics.deliver()
        self.assertEqual(len(self.logistics), 1,
                         'Incorrect logistics size')

        self.logistics.deliver()
        self.assertEqual(len(self.logistics), 0,
                         'Incorrect logistics size')


class AbstractFactoryTestCase(unittest.TestCase):

    def test_00_init_factory(self):
        VictorianFurnitureFactory = AbstractFactory.new(style='victorian')
        ModernFurnitureFactory = AbstractFactory.new(style='modern')
        ArtDecoFurnitureFactory = AbstractFactory.new(style='art_deco')

        self.assertEqual(VictorianFurnitureFactory.style.value, 'victorian',
                         'Incorrect Factory style')
        self.assertEqual(ModernFurnitureFactory.style.value, 'modern',
                         'Incorrect Factory style')
        self.assertEqual(ArtDecoFurnitureFactory.style.value, 'art_deco',
                         'Incorrect Factory style')

    def test_01_bad_style_factory(self):
        with self.assertRaises(Exception):
            AbstractFactory.new(style='punk')

    def test_02_style_furniture_check(self):
        VictorianFurnitureFactory = AbstractFactory.new(style='victorian')

        chair = VictorianFurnitureFactory.make_chair()

        self.assertEqual(chair.style.value, 'victorian',
                         'Incorrect Furniture style')


class BuilderTestCase(unittest.TestCase):

    def test_00_init_builder(self):
        BuilderTestCase.builder_ford_f_100 = VehicleBuilder(
            VehicleBlueprint(
                engine=Engine(Fuel.diesel, 6),
                transmission=Transmission.manual,
                wheels=4,
                seats=6
            )
        )

        BuilderTestCase.builder_tesla_model_3 = VehicleBuilder(
            VehicleBlueprint(
                engine=Engine(Fuel.gasoline, 4),
                transmission=Transmission.automatic,
                wheels=2,
                seats=2
            )
        )

        BuilderTestCase.builder_kawasaki_ninja_1000 = VehicleBuilder(
            VehicleBlueprint(
                engine=Engine(Fuel.electric),
                transmission=Transmission.automatic,
                wheels=4,
                seats=6
            )
        )

    def test_01_test_bad_config(self):
        with self.assertRaises(Exception):
            VehicleBlueprint(
                engine=Engine(engine=Fuel.electric, cylinders=1),
                transmission=Transmission.automatic,
                wheels=4,
                seats=6
            )
        with self.assertRaises(Exception):
            VehicleBlueprint(
                engine=Engine(engine=Fuel.diesel, cylinders=0),
                transmission=Transmission.automatic,
                wheels=4,
                seats=6
            )

    def test_02_test_builder_incomplete(self):

        self.builder_ford_f_100.build_engine()
        self.builder_ford_f_100.build_transmission()
        self.builder_ford_f_100.build_wheels()

        exported_ford = self.builder_ford_f_100.export()
        self.assertIsNone(exported_ford)
        self.assertIsNotNone(self.builder_ford_f_100.vehicle.engine)
        self.assertIsNotNone(self.builder_ford_f_100.vehicle.transmission)
        self.assertIsNotNone(self.builder_ford_f_100.vehicle.wheels)
        self.assertIsNone(self.builder_ford_f_100.vehicle.seats)

    def test_03_test_builder_complete(self):

        self.builder_ford_f_100.build_seats()
        exported_ford = self.builder_ford_f_100.export()

        self.assertIsNotNone(exported_ford)
        self.assertIsInstance(exported_ford, VehicleBuilt)


if __name__ == '__main__':
    unittest.main()
