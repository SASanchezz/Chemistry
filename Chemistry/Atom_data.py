import numpy as np
import pandas as pd


with open ("Atom_info") as file:

    general_list = []

    Number = []
    Atom_weight = []
    Name = []
    Symbol = []


    for line in file:
        general_list.append(line.split())


    for line in general_list:
        if "*" in line:
            line.remove('*')


    #print(general_list)
    for line in range(1, len(general_list)):

        Number.append(int(general_list[line][0]))

        Atom_weight.append(float(general_list[line][1]))

        Name.append(general_list[line][2])

        Symbol.append(general_list[line][3])

Data = pd.DataFrame({
    "Symbol" : Symbol,
    "Name" : Name,
    "Atom weight" : Atom_weight


                        },
index = Number
)
