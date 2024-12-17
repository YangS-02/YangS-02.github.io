from CarInventoryNode import CarInventoryNode
from Car import Car


class CarInventory:
    def __init__(self):
        self.root = None

    def add_car(self, car):
        # If the BST is empty, then the root node will be CarInventoryNode(car).
        if self.root is None:
            self.root = CarInventoryNode(car)
        # If it's not empty:
        else:
            self.add_car_recursively(self.root, car)

    def add_car_recursively(self, parentNode, car):
        # Just make a new node for the purpose of comparison of CarInventoryNode and car object. And also, if a new node
        # of this make and model is needed, just use this one.
        comparison_or_newNode = CarInventoryNode(car)
        # Compare the make and model of this car to the parent, if same make and model, simply use ".append" to
        # append the car at the end of the "cars" list.
        if parentNode == comparison_or_newNode:
            parentNode.cars.append(car)
        # If the car is grater than parentNode, we are going to put the car onto the left side of the branch.
        elif comparison_or_newNode > parentNode:
            # If left node is empty, add the new node.
            if parentNode.left is None:
                # Fill the left node and link it to the parentNode
                parentNode.left = comparison_or_newNode
                comparison_or_newNode.parent = parentNode
            # If left node is already filled, recursively put the car and left node again into add_car_recursively.
            else:
                self.add_car_recursively(parentNode.left, car)
        # If the car is less than parentNode, we are going to put the car onto the right side of the branch.
        else:
            # Similar process
            if parentNode.right is None:
                parentNode.right = comparison_or_newNode
                comparison_or_newNode.parent = parentNode
            else:
                self.add_car_recursively(parentNode.right, car)

    def does_car_exist(self, car):
        # We need another helper function just so that we can pass one more parameter into the function and allow for a
        # recursive traversal.
        if self.does_car_exist_helper(self.root, car):
            return True
        else:
            return False

    def does_car_exist_helper(self, parentNode, car):
        # Again, similar to the one in the add_car_recursively, we make a new node object just for comparison
        comparison = CarInventoryNode(car)
        if parentNode is None:
            return False
        # if we find that the parentNode equals to comparison, we just need to loop through cars list to see if anything
        # matches.
        elif parentNode == comparison:
            for item in parentNode.cars:
                if item == car:
                    return True
        elif parentNode < comparison:
            return self.does_car_exist_helper(parentNode.left, car)
        else:
            return self.does_car_exist_helper(parentNode.right, car)

    def inorder(self):
        result = ""
        if self.root is None:
            return result
        else:
            return self.inorder_helper(self.root)

    def inorder_helper(self, node):
        result = ""
        if node.left is not None:
            result += self.inorder_helper(node.left)
        result += str(node)
        if node.right is not None:
            result += self.inorder_helper(node.right)
        return result

    def preorder(self):
        result = ""
        if self.root is None:
            return result
        else:
            return self.preorder_helper(self.root)

    def preorder_helper(self, node):
        result = str(node)
        if node.left is not None:
            result += self.preorder_helper(node.left)
        if node.right is not None:
            result += self.preorder_helper(node.right)
        return result

    def postorder(self):
        result = ""
        if self.root is None:
            return result
        else:
            return self.postorder_helper(self.root)

    def postorder_helper(self, node):
        result = ""
        if node.left is not None:
            result += self.postorder_helper(node.left)
        if node.right is not None:
            result += self.postorder_helper(node.right)
        result += str(node)
        return result

    def get_best_car(self, make, model):
        # print(f"the root is {self.root}".rstrip())
        car_node = self.get_car_helper(self.root, make, model)
        if car_node is False:
            return None
        car_list = car_node.cars
        # The get_car_helper will return a list, the list will be processed and best car will be returned.
        best = car_list[0]
        for item in car_list:
            if item > best:
                best = item
        return best

    def get_car_helper(self, parentNode, make, model):
        # print(f"|--->Helper: node passed into the function is {parentNode}".rstrip())
        if parentNode is None:
            # print("\t|--->Helper first step: make sure it is not None")
            return False
        elif parentNode.make == make.upper() and parentNode.model == model.upper():
            # print(f"\t\t|--->⚠️Helper second step: node passed equal to make and model,
            # returned {parentNode.cars[0]}")
            return parentNode
        elif (parentNode.make > make.upper()) or (parentNode.make == make.upper()
                                                  and parentNode.model > model.upper()):
            # print(f"\t\t\t|--->Helper third step: parent_node.make > make and model")
            return self.get_car_helper(parentNode.left, make, model)
        elif (parentNode.make < make.upper()) or (parentNode.make == make.upper()
                                                  and parentNode.model < model.upper()):
            # print(f"\t\t\t\t|--->Helper fourth step: parent_node.make < make and model")
            return self.get_car_helper(parentNode.right, make, model)

    # Get worst and get best both have the same error: Test Failed: 'NoneType' object has no attribute 'make',
    # So the problem is probably over here; but the first if statement already filtered the situation where a none
    # type try to use the make attribute.

    def get_worst_car(self, make, model):
        car_node = self.get_car_helper(self.root, make, model)
        if car_node is False:
            return None
        car_list = car_node.cars
        best = car_list[0]
        for item in car_list:
            if item < best:
                best = item
        return best

    def get_total_inventory_price(self):
        result = 0
        if self.root is None:
            return result
        else:
            return self.get_total_inventory_price_helper(self.root)
            # Forgot to add the return.....Stupid mf mistake.....

    def get_total_inventory_price_helper(self, parentNode):
        result = parentNode.Node_total_price()
        # print(f"Current node total price{result}")
        if parentNode.left is not None:
            # print(f"\t|--->Left SubNode of {parentNode}")
            result += self.get_total_inventory_price_helper(parentNode.left)
        if parentNode.right is not None:
            # print(f"\t|--->Right SubNode of {parentNode}")
            result += self.get_total_inventory_price_helper(parentNode.right)
        # print(f"final total price is {result}")
        return result

    def get_successor(self, make, model):
        # Use get_car_helper to first locate the node with same make and model
        # Make some modification to the get_car_helper so that it will return the node instead of the list.
        car_node = self.get_car_helper(self.root, make, model)
        if car_node is False:  # get_car_helper will return False if there is no node with specified make and model
            return None
        else:  # We find the node with the same make and model!
            if car_node.right is None:  # check if it has a right subtree, if None, we check ancestor.
                return self.get_successor_helper_ancestor(car_node)
            else:  # We have a right subtree.
                target = car_node.right  # Don't need a recursive helper, just a while traversal will do.
                while target.left is not None:
                    target = target.left
                return target

    def get_successor_helper_ancestor(self, car_node):
        """
        We use this function so that we can recursively find the closest ancestor for which the give node is in its
        left subtree.
        :param car_node: CarInventoryNode object
        :return: the closest ancestor for which the give node is in its left subtree
        """
        if car_node.parent is None:  # If car_node is already at the top of the tree, no ancestor for sure
            return None
        elif car_node.parent.left == car_node:  # Base case, we find the parent we want, return the parent
            return car_node.parent
        else:
            return self.get_successor_helper_ancestor(car_node.parent)  # Recursive case

    def remove_car(self, make, model, year, price):
        """
        Attempts to find the Car with the specified make, model, year, and price, and removes it the CarInventoryNode’s
        cars list
        :param make: Car attribute.
        :param model: Car attribute.
        :param year: Car attribute.
        :param price: Car attribute.
        :return: Returns True if the Car was successfully removed, and False if the Car is not present in the
        CarInventory.
        """
        node = self.get_car_helper(self.root, make.upper(), model.upper())

        if node is False:
            # print("Cannot Find such node based on the required make, model")
            # print(f"Cannot find such node with specified make and model")
            return False  # This mean that the node with give make and model is not found, so car with also the same
            # year and price will not exist, so just return False

        if len(node.cars) > 1:  # if the length of cars list is larger than one, that means you don't have to do
            # anything to the list
            # print("Node to be removed has more than one car object")
            for index, car in enumerate(node.cars):
                # print(f"Specified year({year}) and model({model}) is compared with this car's {car.year} {car.price}")
                if car.year == year and car.price == price:
                    node.cars.pop(index)
                    # print("\t\tWe are done!")
                    return True
            return False

        if len(node.cars) == 1:  # This means that we are going to remove this node altogether. Three cases:
            # print("Node to be removed has only one car object")
            if node.cars[0].year == year and node.cars[0].price == price:
                # print("\tWe found the such node with specified year, and price")

                # First case: the node to be deleted has no children:
                if (node.left is None) and (node.right is None):
                    # print("\t\tFirst case: the node to be deleted has no children")
                    if node.parent is None:
                        self.root = None
                        return True
                    if node == node.parent.left:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                    # print("\t\tWe are done!")
                    return True

                # Second case: the node to be deleted has only one child
                if (node.left is not None) and (node.right is None):  # has only the left child
                    # print("\t\tSecond case: the node to be deleted has only one left child")
                    # print(f"\t\tThe parent of the node is {node.parent}")
                    if node.parent is None:  # If the current node has no parent, then it is the root:
                        # change the root of to the left child of the node
                        # print("\t\tNode to be deleted is the root")
                        self.root = node.left
                        self.root.parent = None
                        # print("\t\tWe are done!")
                        return True
                    if node == node.parent.left:  # If the current node is the left child of the parent node:
                        # update the parent reference of the left child to point to the parent of the current node
                        # print("\t\tNode to be deleted is the left child of the parent node")
                        node.left.parent = node.parent
                        # update the left child reference of the parent to point to the current node’s left child
                        node.parent.left = node.left
                        # print("\t\tWe are done!")
                        return True
                    if node == node.parent.right:  # if the current node is the right child of the parent node:
                        # update the parent reference of the left child to point to the parent of the current node:
                        # print("\t\tNode to be deleted is the right child of the parent node")
                        node.left.parent = node.parent
                        # update the right child reference of the parent to point to the current node’s left child:
                        node.parent.right = node.left
                        # print("\t\tWe are done!")
                        return True

                if (node.left is None) and (node.right is not None):  # has only the right child
                    # print("\t\tSecond case: the node to be deleted has only one right child")
                    # print(f"\t\tThe parent of the node is {node.parent}")
                    if node.parent is None:  # If  the current node has no parent, then it is the root:
                        self.root = node.right
                        self.root.parent = None
                        # print("\t\tWe are done!")
                        return True
                    if node == node.parent.left:  # If the current node is the left child of the parent node:
                        # update the parent reference of the right child to point to the parent of the current node
                        # print("\t\tNode to be deleted is the left child of the parent node")
                        node.right.parent = node.parent
                        # update the left child reference of the parent to point to the current node’s right child
                        node.parent.left = node.right
                        # print("\t\tWe are done!")
                        return True
                    if node == node.parent.right:  # if the current node is the right child of the parent node:
                        # update the parent reference of the right child to point to the parent of the current node:
                        # print("\t\tNode to be deleted is the right child of the parent node")
                        node.right.parent = node.parent
                        # update the right child reference of the parent to point to the current node’s right child:
                        node.parent.right = node.right
                        # print("\t\tWe are done!")
                        return True

                # Third case: the node to be deleted has two children
                if (node.left is not None) and (node.right is not None):
                    print("\t\tThird case: the node to be deleted has two children")
                    # Call to the find successor method. (since we already cover the case where the node to be removed
                    # only have the left child, so we don't have to worry about the case when we try to find the
                    # ancestor because there's no right child)
                    # Find the successor:
                    successor = self.get_successor(make, model)  # the thing about successor is that it doesn't have
                    #  a left child, cus then the left child would be the actual successor.
                    print(f"\t\t\tThe successor is {successor}".rstrip("\n"))
                    # Thus, we can delete the successor by just change the reference
                    # So, we located the problem, we couldn't correctly remove the node from the tree
                    if successor.parent == node and successor.right is None:
                        node.right = None
                    # if successor.right is None and successor.parent != node:
                    #     print("\t\t\tThe successor has no right child")
                    #     successor.parent.left = None
                    if successor.right is not None:
                        print("\t\t\tThe successor has right child")
                        print(f"\t\t\tThe successor has no right child: {successor.right.cars[0]}")
                        successor.right.parent = successor.parent
                        successor.parent.right = successor.right
                    # set the deleted node to be the successor
                    print("\t\t\tset the deleted node to be the successor")
                    node.make = successor.make
                    node.model = successor.model
                    node.cars = successor.cars
                    print("We are done!")
                    return True

            # else:
            #     print("\tWe couldn't find such node with specified make, model, year, and price")
            #     return False


if __name__ == "__main__":
    def show_tree(node):
        """
        * -> Indicates the base node
        L -> Indicates the left child of the base node
        R -> Indicates the right child of the base node
        LR -> Indicates the right child of the left child of the base node
        ..... and so on
        """
        import sys
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        if node is None:
            print("No cars in inventory.")
        else:
            print(
                f"Showing Tree Representation of Children under Node - Make: {node.get_make()}, "
                f"Model: {node.get_model()}\n")
            _print_tree(node, 0, "")
            print("\nEnd of the car inventory. \n")
        print("\n" + "=" * 50 + "\n")
        contents = sys.stdout.getvalue()
        sys.stdout = old_stdout
        print(contents)


    def _print_tree(node, level, position):
        if node is not None:
            _print_tree(node.get_right(), level + 1, position + "R")
            print(
                "   " * level + "|----" + f"(Level {level}) {node.get_make()} : {node.get_model()} "
                                          f"({position if position else '*'})")
            _print_tree(node.get_left(), level + 1, position + "L")


    # Test ONE
    # inventory = CarInventory()
    # # Adding some cars
    # inventory.add_car(Car("Toyota", "Camry", 2020, 25000))
    # inventory.add_car(Car("Honda", "Accord", 2019, 23000))
    # inventory.add_car(Car("Toyota", "Corolla", 2018, 20000))
    # inventory.add_car(Car("Honda", "Civic", 2021, 22000))
    # inventory.add_car(Car("Ford", "Fusion", 2017, 18000))
    # inventory.add_car(Car("Chevrolet", "Malibu", 2016, 17000))
    # # Displaying the inventory
    # show_tree(inventory.root)

    # Test TWO
    # bst = CarInventory()
    #
    # car1 = Car("Nissan", "Leaf", 2018, 18000)
    # car2 = Car("Tesla", "Model3", 2018, 50000)
    # car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    # car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    # car5 = Car("Ford", "Ranger", 2021, 25000)
    # bst.add_car(car1)
    # bst.add_car(car2)
    # bst.add_car(car3)
    # bst.add_car(car4)
    # bst.add_car(car5)
    # show_tree(bst.root)
    # print(bst.preorder())
    # print(bst.inorder())
    # print(bst.postorder())
    #     assert bst.inorder() == \
    #            """\
    # Make: FORD, Model: RANGER, Year: 2021, Price: $25000
    # Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
    # Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
    # Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
    # Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
    # """
    #     assert bst.preorder() == \
    #            """\
    # Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
    # Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
    # Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
    # Make: FORD, Model: RANGER, Year: 2021, Price: $25000
    # Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
    # """
    #     assert bst.postorder() == \
    #            """\
    # Make: FORD, Model: RANGER, Year: 2021, Price: $25000
    # Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
    # Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
    # Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
    # Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
    # """
    # assert bst.get_best_car("Nissan", "Leaf") == car1
    # assert bst.get_best_car("Mercedes", "Sprinter") == car3
    # assert bst.get_best_car("Honda", "Accord") is None
    # assert bst.get_best_car("Tesla", "model3") == car2
    #
    # assert bst.get_worst_car("Nissan", "Leaf") == car1
    # assert bst.get_worst_car("Mercedes", "Sprinter") == car4
    # assert bst.get_best_car("Honda", "Accord") is None
    #
    # print(bst.get_total_inventory_price())
    # assert bst.get_total_inventory_price() == 158000

    # Test Three
    # best_car = CarInventory()
    # car1 = Car("Toyota", "Corolla", 2020, 22000)
    # car2 = Car("Tesla", "ModelY", 2020, 100000)
    # car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    # car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    # car5 = Car("Audi", "A4", 2017, 28000)
    # car6 = Car("Audi", "A4", 2023, 34000)
    # car7 = Car("Volkswagen", "Jetta", 2020, 23000)
    # car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
    # car9 = Car("BMW", "X5", 2020, 40000)
    # car10 = Car("BMW", "X7", 2020, 60000)
    # car11 = Car("Audi", "A3", 2018, 12000)
    # car12 = Car("BMW", "X6", 2020, 40000)
    # car13 = Car("BMW", "X3", 2011, 10000)
    #
    # best_car.add_car(car1)
    # best_car.add_car(car2)
    # best_car.add_car(car3)
    # best_car.add_car(car4)
    # best_car.add_car(car5)
    # best_car.add_car(car6)
    # best_car.add_car(car7)
    # best_car.add_car(car8)
    # best_car.add_car(car9)
    # best_car.add_car(car10)
    # best_car.add_car(car11)
    # best_car.add_car(car12)
    # best_car.add_car(car13)
    # show_tree(best_car.root)
    # best_car.remove_car("BMW", "X7", 2020, 60000)
    # show_tree(best_car.root)
    # best_car.remove_car("Audi", "A4", 2017, 28000)
    # show_tree(best_car.root)
    # best_car.remove_car("Audi", "A4", 2023, 34000)
    # show_tree(best_car.root)
    # best_car.remove_car("Tesla", "ModelY", 2020, 100000)
    # show_tree(best_car.root)
    # best_car.remove_car("BMW", "X3", 2011, 10000)
    # show_tree(best_car.root)
    # best_car.remove_car("BMW", "X5", 2020, 40000)
    # show_tree(best_car.root)
    # best_car.remove_car("Mercedes", "Sprinter", 2022, 40000)
    # show_tree(best_car.root)
    # best_car.remove_car("Mercedes", "Sprinter", 2014, 25000)
    # show_tree(best_car.root)
    # best_car.remove_car("Toyota", "Corolla", 2020, 22000)
    # show_tree(best_car.root)
    #
    # # Test THREE
    # print("Prius first")
    # best_car = CarInventory()
    # car1 = Car("TOYOTA", "PRIUS", 2014, 20000)
    # car2 = Car("TOYOTA", "SIENNA", 2007, 35000)
    # car3 = Car("TOYOTA", "PRIUS", 2022, 25000)
    # car4 = Car("TOYOTA", "COROLLA", 2006, 10000)
    # best_car.add_car(car1)
    # best_car.add_car(car2)
    # best_car.add_car(car3)
    # best_car.add_car(car4)
    # print(best_car.remove_car("TOYOTA", "SIENNA", 2007, 35000))
    # print(best_car.inorder())
    # show_tree(best_car.root)
    #
    # # Test 3.1
    # print("SIENNA first")
    # best_car = CarInventory()
    # car1 = Car("TOYOTA", "PRIUS", 2014, 20000)
    # car2 = Car("TOYOTA", "SIENNA", 2007, 35000)
    # car3 = Car("TOYOTA", "PRIUS", 2022, 25000)
    # car4 = Car("TOYOTA", "COROLLA", 2006, 10000)
    # best_car.add_car(car2)
    # best_car.add_car(car1)
    # best_car.add_car(car3)
    # best_car.add_car(car4)
    # print(best_car.remove_car("TOYOTA", "SIENNA", 2007, 35000))
    # print(best_car.inorder())
    # show_tree(best_car.root)
    #
    # # Test 3.2
    # print("COROLLA first")
    # best_car = CarInventory()
    # car1 = Car("TOYOTA", "PRIUS", 2014, 20000)
    # car2 = Car("TOYOTA", "SIENNA", 2007, 35000)
    # car3 = Car("TOYOTA", "PRIUS", 2022, 25000)
    # car4 = Car("TOYOTA", "COROLLA", 2006, 10000)
    # best_car.add_car(car4)
    # best_car.add_car(car3)
    # best_car.add_car(car2)
    # best_car.add_car(car1)
    # print(best_car.remove_car("TOYOTA", "SIENNA", 2007, 35000))
    # print(best_car.inorder())
    # show_tree(best_car.root)

    # Test FOUR
    # best_car = CarInventory()
    # car1 = Car("Toyota", "Corolla", 2020, 22000)
    # car2 = Car("Tesla", "ModelY", 2020, 100000)
    # car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    # car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    # car5 = Car("Audi", "A4", 2017, 28000)
    # car6 = Car("Audi", "A4", 2023, 34000)
    # car7 = Car("Volkswagen", "Jetta", 2020, 23000)
    # car8 = Car("Mercedes-Benz", "C-Class", 2018, 32000)
    # car9 = Car("BMW", "X5", 2020, 40000)
    # car10 = Car("BMW", "X7", 2020, 60000)
    # car11 = Car("Audi", "A3", 2018, 12000)
    # car12 = Car("BMW", "X6", 2020, 40000)
    # car13 = Car("BMW", "X3", 2011, 10000)
    # best_car.add_car(car1)
    # best_car.add_car(car2)
    # best_car.add_car(car3)
    # best_car.add_car(car4)
    # best_car.add_car(car5)
    # best_car.add_car(car6)
    # best_car.add_car(car7)
    # best_car.add_car(car8)
    # best_car.add_car(car9)
    # best_car.add_car(car10)
    # best_car.add_car(car11)
    # best_car.add_car(car12)
    # best_car.add_car(car13)
    # show_tree(best_car.root)
    # best_car.remove_car("Volkswagen", "Jetta", 2020, 23000)
    # show_tree(best_car.root)

    # Test FIVE
    # bst = CarInventory()
    # car1 = Car("toyota", "prius", 2022, 25000)
    # car1A = Car("TOYOTA", "PRIUS", 2022, 30000)
    # car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    # car3 = Car("Chevrolet", "Equinox", 2011, 10000)
    # car4 = Car("Toyota", "Sienna", 2007, 35000)
    # car5 = Car("Toyota", "Corolla", 2006, 10000)
    # car6 = Car("toyota", "camry", 2007, 11000)
    # car7 = Car("TOYOTA", "raV4", 2008, 12000)
    # car8 = Car("toyota", "yaris", 2005, 2000)
    # car9 = Car("toyota", "4runner", 2007, 10000)

    # Expected tree structure
    #                           t,yaris,1
    #                           /
    #                    t,sienna,1
    #                    /
    #                t,rav4,1
    #                /
    #             t,camry,1
    #           /           \
    #    c,equinox,1         t,prius,2
    #        \               /
    #        h,odyssey,1     t,corolla,1
    #           \
    #           t,4runner,1

    # bst.add_car(car8)
    # bst.add_car(car4)
    # bst.add_car(car7)
    # bst.add_car(car6)
    # bst.add_car(car1A)
    # bst.add_car(car5)
    # bst.add_car(car3)
    # bst.add_car(car2)
    # bst.add_car(car1)
    # bst.add_car(car9)
    #
    # show_tree(bst.root)
    # bst.remove_car("toyota", "sienna", 2007, 35000)
    # show_tree(bst.root)

    # Test Six:
    # bst = CarInventory()
    # car1 = Car("Honda", "Odyssey", 2009, 30000)
    # car2 = Car("Toyota", "Sienna", 2007, 35000)
    # car3 = Car("Toyota", "Prius", 2022, 25000)
    # car4 = Car("Toyota", "Prius", 2014, 20000)
    # car5 = Car("Toyota", "Corolla", 2006, 10000)
    #
    # bst.add_car(car1)
    # bst.add_car(car2)
    # bst.add_car(car3)
    # bst.add_car(car4)
    # bst.add_car(car5)
    # show_tree(bst.root)
    # bst.remove_car(car1.make, car1.model, car1.year, car1.price)
    # show_tree(bst.root)
    # print(f"remove {car2.model}")
    # print("root is", bst.root.cars[0])
    # print(f"parent of the root is {bst.root.parent}")
    # show_tree(bst.root)
    # bst.remove_car(car2.make, car2.model, car2.year, car2.price)
    # show_tree(bst.root)


if __name__ == "__main__":
    def show_tree(node):
        """
        * -> Indicates the base node
        L -> Indicates the left child of the base node
        R -> Indicates the right child of the base node
        LR -> Indicates the right child of the left child of the base node
        ..... and so on
        """
        import sys
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        if node is None:
            print("No cars in inventory.")
        else:
            print(
                f"Showing Tree Representation of Children under Node - Make: {node.get_make()}, "
                f"Model: {node.get_model()}\n")
            _print_tree(node, 0, "")
            print("\nEnd of the car inventory. \n")
        print("\n" + "=" * 50 + "\n")
        contents = sys.stdout.getvalue()
        sys.stdout = old_stdout
        print(contents)


    def _print_tree(node, level, position):
        if node is not None:
            _print_tree(node.get_right(), level + 1, position + "R")
            print(
                "   " * level + "|----" + f"(Level {level}) {node.get_make()} : {node.get_model()} "
                                          f"({position if position else '*'})")
            _print_tree(node.get_left(), level + 1, position + "L")

    # Test ONE
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
    show_tree(best_car.root)
    best_car.remove_car("Mercedes", "Sprinter", 2022, 40000)
    best_car.remove_car("Mercedes", "Sprinter", 2014, 25000)
    show_tree(best_car.root)
