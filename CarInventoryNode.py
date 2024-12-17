from Car import Car


class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make
        self.model = car.model
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_parent(self):
        return self.parent  # If parent doesn't exist, return None automatically from the constructor

    def set_parent(self, parent):
        self.parent = parent

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def Node_total_price(self):
        result = 0
        for car in self.cars:
            result += car.price
        return result

    def __str__(self):
        """
        Overload the string operator to allow us to get the details of all cars in the CarInventoryNode.
        :return: all car objects in CarInventoryNode in insertion order in a string
        """
        result = ""
        for item in self.cars:
            result += f"{item}\n"
        return result
# Side nots: my understanding so far is that this CarInventoryNode kind of bundle the car that is of same make and model
# up. And in the actual CarInventory class, you only structure the tree by make and model. But through get_worst_car,
# you can still access individual car in the bundle.

    # Set up comparators for latter use as suggested.
    def __lt__(self, other):
        if self.make != other.make:  # Compare make.
            return self.make > other.make
        else:
            if self.model != other.model:  # Same make, compare model.
                return self.model > other.model
            else:
                return False

    def __eq__(self, other):
        if other is None:
            return False
        if self.make == other.make and self.model == other.model:
            return True
        else:
            return False


if __name__ == "__main__":
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    print(carNode)
