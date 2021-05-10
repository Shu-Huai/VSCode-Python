class Customer(object):
    def __init__(self) -> None:
        super().__init__()
        self.__foodList = []

    def PlaceOrder(self, employee, food):
        return self.__foodList.append(employee.TakeOrder(food))

    def PrintFood(self):
        print("The food list is: ", end="")
        for food in self.__foodList:
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
        self.__food =   food

    def __str__(self):
        return self.__food


class Lunch(object):
    def __init__(self) -> None:
        super().__init__()
        self.__customer = Customer()
        self.__employee = Employee()

    def Order(self, food):
        self.__customer.PlaceOrder(self.__employee, food)

    def Result(self):
        self.__customer.PrintFood()


lunch = Lunch()
foodList = input("Please input the food list: ").split()
for food in foodList:
    lunch.Order(food)
lunch.Result()