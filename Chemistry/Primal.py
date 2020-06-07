
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





    def Weight(self):         #finding out info
        repetition = self.Repeat()
        global weight
        weight = 0
        Structure, _ = self.Data_frame()

        if repetition == 0:

            for sign in Structure:
                elem_from_Structure = Structure[Structure == sign].index[0]
                print("element: ", elem_from_Structure) # HERE!!!!!!!!!!!!
                for element in info.Data["Symbol"]:
                    if elem_from_Structure == element :

                        atom_coefficient = Structure[elem_from_Structure] # multiplier of atom weight

                        index_of_atom = info.Data[info.Data["Symbol"] == elem_from_Structure].index.tolist() # index of atom from formula in our DataFrame

                        constant_weight = round(float(info.Data["Atom weight"][index_of_atom]), 3) #constant weight of atom in DataFrame

                        definite_weight = atom_coefficient * constant_weight #Multiplying of coefficient and mass


                        weight +=  definite_weight

            return round(molecula_coefficient * round(weight, 3), 3)


        elif repetition == 1:
            storage = []
            for sign in range(0, len(Structure)):
                for sign2 in range(sign+1, len(Structure)):
                    if Structure[sign] == Structure[sign2] :
                        storage.append(str(Structure[sign])+"1")
            return storage








shor = Molecula1("5 C2H5O5")

print(shor.Weight())


#print(shor.repetition)
#print(info.Data["Symbol"])