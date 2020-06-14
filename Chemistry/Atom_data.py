import numpy as np
import pandas as pd
import os 
import io


global_cwd = os.getcwd()


def General_data():
    global global_cwd
    cwd = global_cwd

    if "Atom_info" not in os.listdir(cwd):
        cwd += "\Chemistry\Atom_info" 
    else:
        cwd += "\Atom_info"
    with open (cwd) as file:

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
    return Data

def Valence():
    global global_cwd
    cwd = global_cwd
    a = []


    if "Valence" not in os.listdir(cwd):
        cwd += "\Chemistry\Valence" 
    else:
        cwd += "\Valence"
    with io.open (cwd, encoding="utf-8") as file:

        lines = file.readlines()
        for word in lines:
            print (word) 
        
         

#print(Valence())

