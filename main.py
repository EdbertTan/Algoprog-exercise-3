import calculate
from  calculate import itemlist

def createlist():
    numitem=int(input("how many would you like to buy?"))
    while numitem<1:
        numitem = int(input("number must be higher than 1, enter again"))

    itlist=[]

    for it in range (numitem):
        print("item #")
        food = input("enter food")
        amt = float(input("enter amount of pounds"))
        while amt<0:
            amt = float(input("ampunt must be > 0"))

        myfood = calculate.foodstuff(food,amt)
        itlist.append(myfood)

    return itlist

def displaylist(foodlist):
    print("here is a summary of the items purchased\n--------------------------------------------------------")
    for food in range(len(foodlist)):
        foodlist[food].__str__()


def main():
    myfoodlist = createlist()
    displaylist(myfoodlist)

main()