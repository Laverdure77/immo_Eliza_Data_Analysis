import data_acquisition.df_attributes as df

attributes = tuple(df.attributes)

immoweb_attributes = (
    "id", #0
    "Locality",
    "Type of property",
    "Subtype of property",
    "Price_attr",
    "Type of sale",
    "Chambres",
    "Surface habitable",
    "Type de cuisine",
    "Meublé", 
    "Combien de feux ouverts ?", #10
    "Terrasse", 
    "Surface de la terrasse",
    "Jardin",
    "Surface du jardin", 
    "Surface du terrain",
    "Nombre de façades",
    "Piscine",
    "État du bâtiment"
)

def immoweb_filter(datas) :
    my_dict = dict()
    for attr, immo_attr in zip(attributes, immoweb_attributes) :
        if(immo_attr in datas.keys()) :
            if(attr in attributes[9] or attr in attributes[11] or attr in attributes[13] or attr in attributes[17]) :
                if(datas[immo_attr] == "Oui") :
                    my_dict[attr] = 1
                else :
                    my_dict[attr] = 0
            elif(attr in attributes[4]) :
                try :
                    my_dict[attr] = int(datas[immo_attr].split(" ")[0].replace("€",""))
                except :
                    my_dict[attr] = None
            elif(attr in attributes[10]):
                try :
                    if(int(datas[immo_attr]) > 0):
                        my_dict[attr] = 1
                    else :
                        my_dict[attr] = 0
                except :
                    my_dict[attr] = None
            elif(attr in attributes[6:8] or attr in attributes[12] or attr in attributes[14:17]) :
                try :
                   my_dict[attr] = int(datas[immo_attr].replace(".","").split(" ")[0])
                except :
                    my_dict[attr] = None
            elif(attr in attributes[8]) :
                if(datas[immo_attr].find("Pas équipée") > -1) :
                    my_dict[attr] = 0
                else :
                    my_dict[attr] = 1
            else : 
                my_dict[attr] = datas[immo_attr]
        else :
            if(attr in attributes[8:11] or attr in attributes[17]) :
                my_dict[attr] = 0
            elif (attr in attributes[11]) :
                if(immoweb_attributes[12] in datas.keys()) :
                    my_dict[attr] = 1
                else :
                    my_dict[attr] = 0
            elif (attr in attributes[13]) :
                if(immoweb_attributes[14] in datas.keys()) :
                    my_dict[attr] = 1
                else :
                    my_dict[attr] = 0
            else :
                my_dict[attr] = None
    
    return my_dict

house_sub_properties = (
    "Bungalow",
    "Château",
    "Maison de campagne",
    "Immeuble à appartements",
    "Maison bel-étage",
    "Villa",
    "Manoir",
    "Chalet",
    "Ferme",
    "Bien exceptionnel",
    "Immeuble mixte",
    "Maison de maître",
    "Autres biens",
    "Pavillon"
)

appartement_sub_properties = (
    "Rez-de-chaussée",
    "Triplex",
    "Penthouse",
    "Logmement étudiant",
    "Duplex",
    "Studio",
    "Loft",
    "Appartement de service"
)

def get_properties(type) :
    if(type == "Maison") :
        return {"Type of property" : type, "Subtype of property" : None}
    elif(type == "Appartement") :
        return {"Type of property" : type, "Subtype of property" : None}
    else :
        if(type in house_sub_properties) :
            return {"Type of property" : "Maison", "Subtype of property" : type}
        elif(type in appartement_sub_properties) :
            return {"Type of property" : "Appartement", "Subtype of property" : type}
        else:
            return {"Type of property" : None, "Subtype of property" : None}

