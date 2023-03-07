"""
Describe the Train object.
++ The class must contain fields and a method for adding wagons (it is necessary to add objects, instances of the wagon_1
class).
++ Describe the class Wagon together with the train.
++ The Wagon must contain a list of passengers and allow adding passengers.
++ In the Wagon can be 10 passengers for example.
++ When using the len function on a Wagon, I want to see the number of passengers.
++ When using len on a train, I want to see a list of Wagons without a locomotive. Each wagon_1 must have a number.
++ When printing a wagon_1 to the console, I want to see the following "[n]" where n is the number of the wagon_1.

***
++ Implement a train print from task 2. When you print a train, wagons and a locomotive should be displayed in the console
in the following format:
<=[HEAD]-[1]-[2]-[3]-[4]-[...]-[n]-[n-1]
"""
from wagon import Wagon
from train import Train

if __name__ == '__main__':
    train = Train()
    # train.add_wagon(Wagon('HEAD'))
    # train.add_wagon(Wagon(1))
    # train.add_wagon(Wagon(2))
    # train.add_wagon(Wagon(3))
    # train.wagons[1].add_passenger("Geralt")
    # train.wagons[1].add_passenger("Ciri")
    # train.wagons[1].add_passenger("Yen")
    # train.wagons[1].add_passenger("Lutic")
    # train.wagons[1].add_passenger("Triss")
    # train.wagons[1].add_passenger("Zoltan")
    # print(len(train))
    # print(train)
    # print(len(train.wagons[1]))
    # print(train.wagons[1])

    locomotive = Wagon('HEAD')
    wagon_1 = Wagon(1)
    wagon_2 = Wagon(2)
    wagon_3 = Wagon(3)
    locomotive_with_wagons = train + locomotive + wagon_1 + wagon_2 + wagon_3
    wagon_1.add_passenger("Geralt")
    wagon_1.add_passenger("Ciri")
    wagon_1.add_passenger("Yen")
    wagon_1.add_passenger("Lutic")
    print(len(train))
    print(train)
    print(len(wagon_1))
    print(wagon_1)
