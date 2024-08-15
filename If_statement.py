"""
#Temprature
temperature=float(input("Enter current Temperature: "))
if temperature>30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature>20:
    print("It's a nice day")
elif temperature>10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Bye.")
"""
weight=int(input("Weight:"))
kl=input("(K)g Or (L)bs:")
if kl.upper()=="k":
    convert=weight*0.45
    print("Weight in Kg:" + str(convert))
else:
    convert = weight / 0.45
    print("Weight in Lbs:" + str(convert))
