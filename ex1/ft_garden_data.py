# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 06:40:29 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/24 06:40:29 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

class Plant:
	""" A class representing a plant with a name, height, and age."""
	def __init__(self, name: str, height: float, age: int):
		self.name:str = name
		self.height:float = height
		self.age:int = age

	def show(self)-> None:
		print(f"{self.name}: {int(self.height)}cm, {self.age} days old")

if __name__ == "__main__":
    Rose: Plant = Plant(name="Rose", height=25.0, age=30)
    Sunflower: Plant = Plant(name="Sunflower", height=80.0, age=45)
    Cactus: Plant = Plant(name="Cactus", height=15.0, age=120)
    Rose.show()
    Sunflower.show()
    Cactus.show()
