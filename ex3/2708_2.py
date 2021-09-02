print("Have been infected before >> YES")
print("Never been infected before >> NO")
print("Sinovac >> SV ")
print("Astrazeneca >> AZ")
print("Sinopharm >> SP ")
print("None >> NONE ")

X = input("1st dose ")
Y = input("2nd dose ")
Z = input("3rd dose ")
Q = input("Have you ever been infected before? ")

if(X == "SV" ,Y =="SV" and Z == "AZ"):
    print("Do not get Pfizer")
elif(X == "SV" ,Y == "AZ" and Z == "NONE"):
    print("Do not get Pfizer")
elif (x == "AZ" and y == "AZ" and z == "NONE"):
    print("Do not get Pfizer")
elif (x == "SV" and y == "SV" and z == "NONE"):
    print("You get 1 pfizer")
elif (x == "SP" and y == "SP" and z == "NONE"):
    print("You get 1 pfizer")
elif (x == "SV" and y == "NONE" and z == "NONE"):
    print("You get 1 pfizer")
elif (x == "AZ" and y == "NONE" and z == "NONE"):
    print("You get 1 pfizer")
elif (x == "SP" and y == "NONE" and z == "NONE"):
    print("You get 1 pfizer")
elif (x == "NONE" and y == "NONE" and z == "NONE" and Q == "NO"):
    print("You get 1 pfizer")
elif (x == "NONE" and y == "NONE" and z == "NONE" and Q == "YES"):
    print("You get 1 pfizer")
else:
    print("ERROR")