# # a=int(input("sisesta arv a"))
# # b=int(input("sisesta arv b"))

def mySum(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        print ("vale andmetüüp")
### iteratsioon 2 - lisa lahutamine, korrutamine, jagamine.
### lisa valikumenüü (liida, lahuta, korruta, jaga)  
    

def mySubtract(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a-b
    else:
        print("vale andmetüüp")
        
def myMult(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a*b
    else:
        print("vale andmetüüp")

def myDiv(a,b):
    try:
        if isinstance(a,int) and isinstance(b,int):
            return a/b
        else:
            print("vale andmetüüp")
    except ZeroDivisionError:
            print("nulliga ei saa jagada")
        
###iteratsioon 3 - sisendi valideerimine
###kontrolli, et kasutaja sisestab numbreid
def main():
    while True:
            valik=input("millist tehet soovid teha")
            if valik == "1":
                a=int(input("sisesta number 1"))
                b=int(input("sisesta number 2"))
                result = mySum(a,b)
                print("tulemus on: ",result)
            elif valik == "2":
                a=int(input("sisesta number 1"))
                b=int(input("sisesta number 2"))
                result = mySubtract(a,b)
                print("tulemus on: ",result)
            elif valik == "3":
                a=int(input("sisesta number 1"))
                b=int(input("sisesta number 2"))
                result = myMult(a,b)
                print("tulemus on: ",result)
            elif valik == "4":
                a=int(input("sisesta number 1"))
                b=int(input("sisesta number 2"))
                result = myDiv(a,b)
                print("tulemus on: ",result)
            else:
                print("valik puudub")
main()        



#iteratsioon 4 : loogiline täiendamine
def displayInfo():
    print("kokku oli ", sum (myArr))
    print("liitmine töötas", myArr[0], "korda")
    print("lahutamine töötas", myArr[1], "korda")
    print("korrutamine töötas", myArr[2], "korda")
    print("jagamine töötas", myArr[3], "korda")
myArr = [0,0,0,0]

#iteratsioon 5 - parandamine




