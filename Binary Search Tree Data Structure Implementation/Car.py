class Car:
    def __init__(self, make, model, year, price):
        """
        Class constructor for car class.
        :param make: string value representing the brand of the car; must be stored in uppercase;
        :param model: string value representing the model of the car; must be stored in uppercase also;
        :param year: integer value representing the year of the car
        :param price: integer value representing the price value of the car
        """
        self.make = make.upper()
        self.model = model.upper()
        self.year = int(year)
        self.price = int(price)

    def __gt__(self, rhs):  # Don't really need another __lt__.
        if self.make != rhs.make:  # Compare make.
            return self.make > rhs.make
        else:
            if self.model != rhs.model:  # Same make, compare model.
                return self.model > rhs.model
            else:
                if self.year != rhs.year:  # Same make, same model, compare year.
                    return self.year > rhs.year
                else:
                    if self.price != rhs.price:  # Same make, same model, same year, compare price.
                        return self.price > rhs.price
                    else:
                        return False

    def __eq__(self, other):
        if (self.make == other.make and self.model == other.model and self.year == other.year
                and self.price == other.price):
            return True
        else:
            return False

    def __str__(self):
        detail = f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}"
        return detail

    # def get_make(self):
    #     return self.make
    #
    # def get_model(self):
    #     return self.model
    #
    # def get_year(self):
    #     return self.year
    #
    # def get_price(self):
    #     return self.price


if __name__ == "__main__":
    c1 = Car("Honda", "CRV", 2007, 8000)
    c2 = Car("Honda", "Accord", 2015, 15000)
    c3 = Car("Honda", "Accord", 2018, 20000)
    c4 = Car("Honda", "Accord", 2018, 25000)
    c5 = Car("BMW", "X5", 2020, 40000)
    assert c1 > c5  # Compare make
    assert c1 > c2  # Same make, compare model
    assert c2 < c3  # Same make, same model, compare year
    assert c4 > c3  # Same make, same model, same year, compare price
