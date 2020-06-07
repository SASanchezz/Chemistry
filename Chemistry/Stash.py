"""def Weight(self):         #finding out info
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
            additional_number = 1
            for sign2 in range(sign+1, len(Structure)):
                if Structure[sign] == Structure[sign2] :
                    storage.append(str(Structure[sign])+str(additional_number))
                    additional_number += 1
        return Structure.index""" #Previous attempt to calculate weight