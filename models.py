itemlist = []
class foodstuff:
    __totalprice = 0
    def __init__(self, name, amount):
        self.__foodname = name
        self.__poundamount = amount
        self.__price = self.__itemlistadd()
        self.__calcprice = self.costcalc()

    def __itemlistadd(self):
        lfoodname = self.__foodname
        if lfoodname == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif lfoodname == "Wagyu Steaks":
            self.__price = 450.00
        elif lfoodname == "Matsutake Mushrooms":
            self.__price = 272.00
        elif lfoodname == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif lfoodname == "Moose Cheese":
            self.__price = 487.20
        elif lfoodname == "White Truffles":
            self.__price = 3600.00
        elif lfoodname == "Blue Fin Tuna":
            self.__price = 3603.00
        elif lfoodname == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0.0

    def costcalcpart1(self):
        cost = self.__price * self.__poundamount
        foodstuff.__totalprice += cost
        return cost
    def costcalc(self):
        return foodstuff.__totalprice