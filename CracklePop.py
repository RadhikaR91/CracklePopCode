def CracklePop(lowerLimit,upperLimit):
    for x in range (lowerLimit,upperLimit):
        if((x % 3 == 0)and (x % 5 == 0)):
            print("CracklePop")
        elif x % 3 == 0:
            print("Crackle")
        elif x % 5 == 0:
            print("Pop")
        else :
            print(x)


CracklePop(0,101)