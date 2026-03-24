# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 08:08:19 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/24 08:08:19 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

class Plant:
	""" A class representing a plant with a name, height, and age."""
	def __init__(self, name: str, height: float, age: int):
		self.name:str = name
		self.height:float = height
		self._age:int = age

	def show(self)-> None:
		print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")

	def age(self, days: int=1)-> None:
		self._age += days

	def grow(self, daily_growth: float = 0.8)->float:
		self.height += daily_growth
		self.age()
		return daily_growth

	@classmethod
	def from_dict(cls, dico: dict):
		return cls(**dico)

if __name__ == "__main__":
    factory_plants = [
		{"name": "Rose", "height": 25.0, "age": 30},
		{"name": "Oak", "height": 200.0, "age": 365},
		{"name": "Cactus", "height": 5.0, "age": 90},
		{"name": "Sunflower", "height": 80.0, "age": 45},
		{"name": "Fern", "height": 15.0, "age": 120}
	]
    print("=== Plant Factory Output ===")
    for x in range(len(factory_plants)):
        plant_info = factory_plants[x]
        plant = Plant.from_dict(plant_info)
        print("Created: ",end="")
        plant.show()
