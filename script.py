#  script.py
#  
#  Copyright 2015 Imagine Publishing
#  Written by: Rob Zwetsloot

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA

# Scenarios: Location, character, text, scene change, game state

# Scene 1    

def scene1(turn):
    scenario = [['vending machine', "You stumbled upon a vending machine."],
                ['0', '0', "You dig into your pockets but you don't have any coins!", '2', '1']]
    return scenario[turn]

# Scene 2

def scene2(turn):
    scenario = [['home', "You ask your mom for coins."],
                ['0', '0', "She said no.", '2', '1']]
    return scenario[turn]
