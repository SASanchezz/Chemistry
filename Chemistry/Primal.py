
import pandas as pd
import numpy as np
import Atom_data as info


class Atom1 (object):
    def __init__(self, ):
        pass



class Molecula1(object):

    def __init__(self, formula):  #Initial formula
        self.molecula = formula



    def making_list(self): # Turning formula up to list
        structure = []
        global molecula_coefficient


        for element in self.molecula: # into list
            try:
                element = int(element)
            except ValueError:
                pass
            structure.append(element)

        if (type(structure[0]) == int or type(structure[0]) == float):  # determining of coefficient
            molecula_coefficient = structure[0]
            structure.pop(0)

        elif type(structure[0]) == str:
            molecula_coefficient = 1

        return structure

    def Repeat(self):
        repetition = 0
        _, values = self.Data_frame()
        #print(Molecula1.values)

        if len(values) != len(set(values)):
            repetition = 1
        return repetition
        #print("repetition: ", Molecula1.repetition)


    def Data_frame(self):
        values = []
        indexes = []

        structure = self.making_list()

        for unit in structure:
            if (type(unit) == str and unit != " "):
                indexes.append(unit)
            elif type(unit) == int:
                values.append(unit)

        pandas_structure = pd.Series(values)
        pandas_structure.index = indexes
        #print ("structure: ",pandas_structure)  # HERE!!!!!!!!!!!!
        return pandas_structure, values


    def Weight(self):
        repetition = self.Repeat()
        global weight
        weight = 0
        Structure, _ = self.Data_frame()


        for index1 in Structure.index: # index1 is actual element of formula
            for element in info.Data["Symbol"]:
                if index1 == element:     # Structure[index] actually is atom coefficient
                    index_of_atom = info.Data[info.Data["Symbol"] == index1].index.tolist()  # index of atom from formula in our DataFrame

                    constant_weight = round(float(info.Data["Atom weight"][index_of_atom]), 3)  # constant weight of atom in DataFrame

                    definite_weight = Structure[index1] * constant_weight  # Multiplying of coefficient and mass

                    weight += definite_weight

            if (index1 not in info.Data["Symbol"].values)  :
                    print("There is no such element: ", index1)

        return round(molecula_coefficient * round(weight, 3), 3)




shor = Molecula1("5 C2H5O5J3")

print(shor.Weight())


#print(shor.repetition)
#print(info.Data["Symbol"])