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

    list_file = []

    valence = []
    index_list = []
    full_name = []
    sign = []

    global global_cwd
    cwd = global_cwd

    if "Valence" not in os.listdir(cwd):
        cwd += "\Chemistry\Valence" 
    else:
        cwd += "\Valence"

    with io.open (cwd, encoding="utf-8") as file:
        for line in file:
            list_file.append(line.strip())
        list_file = list(filter(None, list_file))


        for index_number in list_file[::4]:
            index_list.append(int(index_number))

        for name in list_file[1::4]:
            full_name.append(name)

        for sign1 in list_file[2::4]:
            sign.append(sign1)

        for val in list_file[3::4]:
            temporary_list = []

            if len(val) < 3 :
                valence.append(int(val))
            elif len(val) > 3:
                val = [e for e in list(val) if e not in ("(", ")", " ")]
                for i in range (1, len(val), 3):
                    str1 = ""
                    str1 += val[i - 1]
                    str1 += val[i]
                    try:
                        temporary_list.append(int(str1))
                    except ValueError:
                        temporary_list.append("No info")
                        break
                valence.append(temporary_list)



        Valence_data = pd.DataFrame ({
        "Name" : full_name,
        "Symbol" : sign,
        "Valence" : valence
                            },
    index = index_list
    )

        return  Valence_data
        
         



