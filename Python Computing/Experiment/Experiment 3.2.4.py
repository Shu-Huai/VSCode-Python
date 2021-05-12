class Customer(object):
    def __init__(self) -> None:
        super().__init__()
        self.foodList = []

    def PlaceOrder(self, employee, food):
        return self.foodList.append(employee.TakeOrder(food))

    def PrintFood(self):
        print("The food list is: ", end="")
        for food in self.foodList:
            print(food, end=" ")
        print(".\n", end="")


class Employee(object):
    def __init__(self) -> None:
        super().__init__()

    def TakeOrder(self, food):
        return Food(food)


class Food(object):
    def __init__(self, food) -> None:
        super().__init__()
        self.food =   food

    def __str__(self):
        return self.food


class Lunch(object):
    def __init__(self) -> None:
        super().__init__()
        self.customer = Customer()
        self.employee = Employee()

    def Order(self, food):
        self.customer.PlaceOrder(self.employee, food)

    def Result(self):
        self.customer.PrintFood()


lunch = Lunch()
foodList = input("Please input the food list: ").split()
for food in foodList:
    lunch.Order(food)
lunch.Result()