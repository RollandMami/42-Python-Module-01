# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 06:18:43 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/24 06:18:43 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

class Plant:
    """ A class representing a plant with a name, height, and age."""
    def __init__(self, name:str, height:float, age:int):
        self.name:str = name
        self.height:float = height
        self.age:int = age

if __name__ == "__main__":
    my_plant: Plant = Plant("Rose", 15.0, 2)
    print(f"=== Welcome to My Garden ===\n\
Plant: {my_plant.name}\n\
Height: {int(my_plant.height)} cm\n\
Age: {my_plant.age} days\n\n\
=== End of Program ===")