import turtle
from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# print(timmy.shape("turtle"))
# timmy.color("coral")
# #timmy.color("red" , "green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen)
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable
table = PrettyTable()
# print(table)
# table.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])

table.add_column("Pokeman name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])
print(table)