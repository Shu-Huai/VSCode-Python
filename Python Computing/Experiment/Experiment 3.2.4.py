class Customer(object):
    def __init__(self) -> None:
        super().__init__()
        self.__foodList_ = []

    def PlaceOrder(self, employee, food):
        return self.__foodList_.append(employee.TakeOrder(food))

    def PrintFood(self):
        print("The food list is: ", end="")
        for food in self.__foodList_:
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
        self.__food = food

    def __str__(self):
        return self.__food


class Lunch(object):
    def __init__(self) -> None:
        super().__init__()
        self.__customer_ = Customer()
        self.__employee_ = Employee()

    def Order(self, food):
        self.__customer_.PlaceOrder(self.__employee_, food)

    def Result(self):
        self.__customer_.PrintFood()


lunch = Lunch()
foodList = input("Please input the food list: ").split()
for food in foodList:
    lunch.Order(food)
lunch.Result()