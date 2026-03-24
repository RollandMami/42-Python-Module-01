# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 07:10:12 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/24 07:10:12 by mamiandr         ###   ########.fr        #
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


if __name__ == "__main__":
    Rose: Plant = Plant(name="Rose", height=24.2, age=30)
    print(f"=== Garden Plant Growth ===")
    total_session_growth:float = 0.0
    for i in range(1, 8):
        print(f"=== Day {i}: ===") 
        daily_growth:float = Rose.grow()
        total_session_growth += daily_growth
        Rose.show()
    print(f"Growth this week: {int(round(total_session_growth, 0))}cm")