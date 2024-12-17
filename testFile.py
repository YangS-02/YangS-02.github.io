from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory


class TestCar:
    def test_constructor(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        assert c1.make == "HONDA"
        assert c1.model == "CRV"
        assert c1.year == 2007
        assert c1.price == 8000

    def test_gt_and_lt(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        c2 = Car("Honda", "Accord", 2015, 15000)
        c3 = Car("Honda", "Accord", 2018, 20000)
        c4 = Car("Honda", "Accord", 2018, 25000)
        c5 = Car("BMW", "X5", 2020, 40000)
        assert c1 > c5  # Compare make
        assert c1 > c2  # Same make, compare model
        assert c2 < c3  # Same make, same model, compare year
        assert c4 > c3  # Same make, same model, same year, compare price

    def test_gt_and_lt_False(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        c1_2 = Car("Honda", "CRV", 2007, 8000)
        assert ((c1_2 > c1) and (c1_2 < c1)) is False

    def test_eq(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        c1_2 = Car("Honda", "CRV", 2007, 8000)
        assert c1 == c1_2

    def test_eq_False(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        c2 = Car("Honda", "Accord", 2015, 15000)
        assert (c1 == c2) is False

    def test_str(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        assert str(c1) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"


class TestCarInventoryNode:
    def test_constructor(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        car_node = CarInventoryNode(c1)
        assert car_node.make == "HONDA"
        assert car_node.model == "CRV"
        assert car_node.cars == [c1]
        assert car_node.parent is None
        assert car_node.left is None
        assert car_node.right is None

    def test_all_get_and_set(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        car_node = CarInventoryNode(c1)
        assert car_node.get_make() == "HONDA"
        assert car_node.get_model() == "CRV"
        assert car_node.get_parent() is None
        c2 = Car("Honda", "Accord", 2015, 15000)
        car_node_2 = CarInventoryNode(c2)
        car_node.set_parent(car_node_2)
        assert car_node.get_parent() == car_node_2
        car_node.set_left(car_node_2)
        car_node.set_right(car_node_2)
        assert car_node.get_left() is car_node_2
        assert car_node.get_right() is car_node_2

    def test_Node_total_price(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        car_node = CarInventoryNode(c1)
        c2 = Car("Honda", "Accord", 2015, 15000)
        car_node.cars.append(c2)
        assert car_node.Node_total_price() == 23000

    def test_str(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        car_node = CarInventoryNode(c1)
        c2 = Car("Honda", "Accord", 2015, 15000)
        car_node.cars.append(c2)
        assert str(car_node) == \
               """\
Make: HONDA, Model: CRV, Year: 2007, Price: $8000
Make: HONDA, Model: ACCORD, Year: 2015, Price: $15000
"""

    def test_lt_and_gt(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        car_node = CarInventoryNode(c1)
        c1_2 = Car("Honda", "CRV", 2007, 8000)
        car_node4 = CarInventoryNode(c1_2)
        c2 = Car("Honda", "Accord", 2015, 15000)
        car_node2 = CarInventoryNode(c2)
        c5 = Car("BMW", "X5", 2020, 40000)
        car_node3 = CarInventoryNode(c5)
        assert car_node2 < car_node3  # Compare make
        assert car_node3 > car_node2
        assert car_node < car_node2  # Compare model
        assert car_node2 > car_node
        assert (car_node4 > car_node) is False

    def test_eq(self):
        c1 = Car("Honda", "CRV", 2007, 8000)
        car_node = CarInventoryNode(c1)
        c1_2 = Car("Honda", "CRV", 2007, 8000)
        car_node2 = CarInventoryNode(c1_2)
        c2 = Car("Honda", "Accord", 2015, 15000)
        car_node3 = CarInventoryNode(c2)
        c3 = None
        assert car_node == car_node2
        assert (car_node3 == car_node) is False
        assert (car_node != car_node2) is False
        assert (car_node3 == c3) is False


class TestCarInventor:
    def test_constructor(self):
        inventory = CarInventory()
        assert inventory.root is None

    def test_add_car_left_unbalanced(self):
        bst = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car6 = Car("Audi", "A4", 2023, 34000)
        bst.add_car(car1)
        bst.add_car(car2)
        bst.add_car(car3)
        bst.add_car(car6)
        assert bst.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
"""

    def test_add_car_right_unbalanced(self):
        bst = CarInventory()
        car5 = Car("Audi", "A4", 2017, 28000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car11 = Car("BMW", "X6", 2021, 60000)
        car10 = Car("BMW", "X7", 2020, 60000)
        bst.add_car(car5)
        bst.add_car(car9)
        bst.add_car(car11)
        bst.add_car(car10)
        assert bst.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X6, Year: 2021, Price: $60000
Make: BMW, Model: X7, Year: 2020, Price: $60000
"""

    def test_add_car_complex_case(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car10 = Car("BMW", "X7", 2020, 60000)
        best_car.add_car(car1)
        assert best_car.root.cars[0] == car1
        best_car.add_car(car2)
        assert best_car.root.left.cars[0] == car2
        best_car.add_car(car3)
        assert best_car.root.left.left.cars[0] == car3
        best_car.add_car(car4)
        assert best_car.root.left.left.cars[1] == car4
        best_car.add_car(car5)
        assert best_car.root.left.left.left.cars[0] == car5
        best_car.add_car(car6)
        assert best_car.root.left.left.left.cars[1] == car6
        best_car.add_car(car7)
        assert best_car.root.right.cars[0] == car7
        best_car.add_car(car8)
        assert best_car.root.left.left.right.cars[0] == car8
        best_car.add_car(car9)
        assert best_car.root.left.left.left.right.cars[0] == car9
        best_car.add_car(car10)
        assert best_car.root.left.left.left.right.right.cars[0] == car10
        assert best_car.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""

    def test_does_car_exist(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        assert best_car.does_car_exist(car1) is True
        assert best_car.does_car_exist(car2) is True
        assert best_car.does_car_exist(car3) is False
        assert best_car.does_car_exist(car4) is False
        assert best_car.does_car_exist(car5) is True
        assert best_car.does_car_exist(car6) is True
        assert best_car.does_car_exist(car7) is True

    def test_inorder(self):
        best_car = CarInventory()
        assert best_car.inorder() == ""
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        assert best_car.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""

    def test_preorder(self):
        best_car = CarInventory()
        assert best_car.preorder() == ""
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        assert best_car.preorder() == \
               """\
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""

    def test_postorder(self):
        best_car = CarInventory()
        assert best_car.postorder() == ""
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        assert best_car.postorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
"""

    def test_get_best_car(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car10 = Car("BMW", "X7", 2020, 60000)
        assert best_car.get_best_car("Toyota", "Corolla") is None
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car9)
        best_car.add_car(car10)
        assert best_car.get_best_car("Audi", "A4") == car6
        assert best_car.get_best_car("Mercedes", "G-wagon") is None
        assert best_car.get_best_car("BMW", "X7") == car10

    def test_get_worst_car(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car10 = Car("BMW", "X7", 2020, 60000)
        assert best_car.get_worst_car("Toyota", "Corolla") is None
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car9)
        best_car.add_car(car10)
        assert best_car.get_worst_car("Mercedes", "Sprinter") == car4
        assert best_car.get_worst_car("Audi", "A4") == car5
        assert best_car.get_worst_car("BMW", "x7") == car10

    def test_get_total_inventory_price(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car10 = Car("BMW", "X7", 2020, 60000)
        assert best_car.get_total_inventory_price() == 0
        best_car.add_car(car1)
        assert best_car.get_total_inventory_price() == 22000
        best_car.add_car(car2)
        assert best_car.get_total_inventory_price() == 122000
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car9)
        best_car.add_car(car10)
        assert best_car.get_total_inventory_price() == 404000

    def test_get_successor(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car10 = Car("BMW", "X7", 2020, 60000)
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car9)
        best_car.add_car(car10)
        assert best_car.get_successor("Toyota", "Corolla") == best_car.root.right
        assert best_car.get_successor("Toyota", "A4") is None
        assert best_car.get_successor("Volkswagen", "Jetta") is None
        assert best_car.get_successor("BMW", "X7") == best_car.root.left.left
        assert best_car.get_successor("Audi", "A4") == best_car.root.left.left.left.right
        car11 = Car("BMW", "X4", 2020, 60000)
        car12 = Car("BMW", "X3", 2020, 60000)
        best_car.add_car(car11)
        best_car.add_car(car12)
        assert best_car.get_successor("Audi", "A4") == best_car.root.left.left.left.right.left.left

    def test_remove_car_left_unbalanced(self):
        bst = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car6 = Car("Audi", "A4", 2023, 34000)
        bst.add_car(car1)
        bst.add_car(car2)
        bst.add_car(car3)
        bst.add_car(car6)
        assert bst.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
"""
        assert bst.remove_car("Audi", "A3", 2023, 34000) is False  # Case where there's no such car
        assert bst.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
"""
        assert bst.remove_car("Audi", "A4", 2023, 34000) is True
        assert bst.inorder() == \
            """\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
"""
        assert bst.remove_car("Toyota", "Corolla", 2020, 22000) is True
        assert bst.inorder() == \
               """\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
"""
        assert bst.root.parent is None  # Just make sure that when you make delete the root node, and switch it with
        # another node, you have to make sure you have the parent attribute is updated to None again.
        assert bst.remove_car("Mercedes", "Sprinter", 2022, 40000) is True
        assert bst.inorder() == \
               """\
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
"""
        assert bst.remove_car("Tesla", "ModelY", 2020, 100000) is True
        assert bst.inorder() == ""

    def test_remove_car_right_unbalanced(self):
        bst = CarInventory()
        car5 = Car("Audi", "A4", 2017, 28000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car11 = Car("BMW", "X6", 2021, 60000)
        car10 = Car("BMW", "X7", 2020, 60000)
        bst.add_car(car5)
        bst.add_car(car9)
        bst.add_car(car11)
        bst.add_car(car10)
        assert bst.inorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X6, Year: 2021, Price: $60000
Make: BMW, Model: X7, Year: 2020, Price: $60000
"""
        assert bst.remove_car("BMW", "X7", 2020, 60000) is True
        assert bst.inorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X6, Year: 2021, Price: $60000
"""
        assert bst.remove_car("Audi", "A4", 2017, 28000) is True
        assert bst.inorder() == \
               """\
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X6, Year: 2021, Price: $60000
"""
        assert bst.remove_car("BMW", "X6", 2021, 60000) is True
        assert bst.inorder() == \
               """\
Make: BMW, Model: X5, Year: 2020, Price: $40000
"""
        assert bst.remove_car("BMW", "X5", 2020, 40000) is True
        assert bst.inorder() == ""
        assert bst.remove_car("Audi", "A4", 2019, 25000) is False

    def test_remove_car_complex_case(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car9 = Car("BMW", "X5", 2020, 40000)
        car10 = Car("BMW", "X7", 2020, 60000)
        best_car.add_car(car1)
        best_car.add_car(car2)
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car5)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car9)
        best_car.add_car(car10)
        assert best_car.remove_car("Mercedes", "Sprinter", 2002, 40000) is False
        assert best_car.remove_car("Mercedes", "Sprinter", 2022, 40000) is True
        assert best_car.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""
        assert best_car.remove_car("Tesla", "ModelY", 2020, 100000) is True
        assert best_car.inorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""
        car11 = Car("BMW", "X9", 2020, 60000)
        best_car.add_car(car11)
        car12 = Car("BMW", "X8", 2020, 60000)
        best_car.add_car(car12)
        assert best_car.remove_car("BMW", "X9", 2020, 60000) is True
        assert best_car.inorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: BMW, Model: X8, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""
        assert best_car.remove_car("Mercedes", "Sprinter", 2014, 25000) is True
        assert best_car.inorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X5, Year: 2020, Price: $40000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: BMW, Model: X8, Year: 2020, Price: $60000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""

    def test_remove_car_complex_case_two(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car10 = Car("BMW", "X7", 2020, 60000)
        car11 = Car("BMW", "X9", 2020, 60000)
        car12 = Car("BMW", "X8", 2020, 60000)
        best_car.add_car(car5)
        best_car.add_car(car2)
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car1)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car10)
        best_car.add_car(car11)
        best_car.add_car(car12)
        assert best_car.remove_car("BMW", "X7", 2020, 60000) is True
        assert best_car.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X8, Year: 2020, Price: $60000
Make: BMW, Model: X9, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""
        assert best_car.remove_car("Toyota", "Corolla", 2020, 22000) is True
        assert best_car.inorder() == \
               """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X8, Year: 2020, Price: $60000
Make: BMW, Model: X9, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TESLA, Model: MODELY, Year: 2020, Price: $100000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""

    def test_remove_car_complex_case_three(self):
        best_car = CarInventory()
        car1 = Car("Toyota", "Corolla", 2020, 22000)
        car2 = Car("Tesla", "ModelY", 2020, 100000)
        car3 = Car("Mercedes", "Sprinter", 2022, 40000)
        car4 = Car("Mercedes", "Sprinter", 2014, 25000)
        car5 = Car("Audi", "A4", 2017, 28000)
        car6 = Car("Audi", "A4", 2023, 34000)
        car7 = Car("Volkswagen", "Jetta", 2020, 23000)
        car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
        car10 = Car("BMW", "X7", 2020, 60000)
        car11 = Car("BMW", "X9", 2020, 60000)
        car12 = Car("BMW", "X8", 2020, 60000)
        best_car.add_car(car5)
        best_car.add_car(car2)
        best_car.add_car(car3)
        best_car.add_car(car4)
        best_car.add_car(car1)
        best_car.add_car(car6)
        best_car.add_car(car7)
        best_car.add_car(car8)
        best_car.add_car(car10)
        best_car.add_car(car11)
        best_car.add_car(car12)
        assert best_car.remove_car("Tesla", "ModelY", 2020, 100000) is True
        assert best_car.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: BMW, Model: X8, Year: 2020, Price: $60000
Make: BMW, Model: X9, Year: 2020, Price: $60000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""
        assert best_car.remove_car("Mercedes", "Sprinter", 2022, 40000) is True
        assert best_car.remove_car("Mercedes", "Sprinter", 2014, 25000) is True
        assert best_car.inorder() == \
            """\
Make: AUDI, Model: A4, Year: 2017, Price: $28000
Make: AUDI, Model: A4, Year: 2023, Price: $34000
Make: BMW, Model: X7, Year: 2020, Price: $60000
Make: BMW, Model: X8, Year: 2020, Price: $60000
Make: BMW, Model: X9, Year: 2020, Price: $60000
Make: MERCEDES-BENZ, Model: C-CLASS, Year: 2018, Price: $32000
Make: TOYOTA, Model: COROLLA, Year: 2020, Price: $22000
Make: VOLKSWAGEN, Model: JETTA, Year: 2020, Price: $23000
"""
