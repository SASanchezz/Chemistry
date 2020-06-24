
import pandas as pd
import numpy as np
import Atom_data as info


class Atom1 (object):
    def __init__(self):
        pass



class Molecula1(object):
    def __init__(self, formula):  #Initial formula
        self.molecula = formula



    def making_list(self): # Turning formula up to list
        molecula_list = []
        structure = []

        global molecula_coefficient

           # into list
        for element in self.molecula:
            try:
                element = int(element)
            except ValueError:
                pass
            molecula_list.append(element)  #molecula_list[number] atucally is scroll of formula

        for number in range(0, len(molecula_list) - 1):
            if type(molecula_list[number]) == int:              # if unit is number
                structure.append(molecula_list[number])

            elif (type(molecula_list[number]) == str and
                  type(molecula_list[number + 1]) == int and
                  molecula_list[number].isupper()):             #if unit is upper str before int
                structure.append(molecula_list[number])

            elif (type(molecula_list[number]) == str and
                  molecula_list[number].isupper() and
                  molecula_list[number + 1].islower()):         # if unit is complex str
                structure.append(molecula_list[number] + molecula_list[number + 1])

            elif (type(molecula_list[number]) == str and
                  molecula_list[number].isupper() and
                  molecula_list[number + 1].isupper()):         # if unit is without value
                structure.append(molecula_list[number])
                structure.append(1)

        if (type(molecula_list[-1]) == int or molecula_list[-1].isupper()): # add last value of list
            structure.append(molecula_list[-1])

        if (type(structure[0]) == int or type(structure[0]) == float):  # determining of coefficient
            molecula_coefficient = structure[0]
            structure.pop(0)

        elif type(structure[0]) == str:
            molecula_coefficient = 1

        return structure


    def Data_frame(self):
        add_number = 1
        repeat_list = []
        values = []
        indexes = []
        repetition = False

        structure = self.making_list()

        for unit in structure:   #If there are repetitions of atoms in formula
            if (type(unit) == str and unit != " "):
                indexes.append(str(add_number) + " " + unit)
            if type(unit) == int:
                values.append(unit)
                add_number += 1

        if type(structure[-1]) == str:
            values.append(1)
        pandas_structure = pd.Series(values)
        pandas_structure.index = indexes
        return pandas_structure, values


    def Weight(self):
        global weight
        weight = 0
        Structure, _ = self.Data_frame()


        for index1 in Structure.index: # index1 is actual element of formula
            for element in info.General_data()["Symbol"]:

                if (index1[-2:].strip() == element):     # Structure[index] actually is atom coefficient

                    index_of_atom = info.General_data()[info.General_data()["Symbol"] == index1[-2:].strip()].index.tolist()  # index of atom from formula in our DataFrame

                    constant_weight = round(float(info.General_data()["Atom weight"][index_of_atom]), 3)  # constant weight of atom in DataFrame

                    definite_weight = Structure[index1] * constant_weight  # Multiplying of coefficient and mass

                    weight += definite_weight


            if (index1[-2:].strip() not in info.General_data()["Symbol"].values):
                print("There is no such element: ", index1[-2:].strip())
        return round(molecula_coefficient * round(weight, 3), 3)


    def Add_atom(self):
        Structure, _ = self.Data_frame()
        Valence = info.Valence()

        for element in Structure.index:
            print(element)



shor = Molecula1("C2H5CHO")

print(shor.Weight())


#print(shor.repetition)
#print(info.Data["Symbol"])