weight = float(input("What is your weight?: "))
convert = str(input("Do you want that converted to (K)g or (L)bs?: "))

if convert.upper() == "K":
    new_weight = weight / 2.205
    print("Your converted weight is " + str(new_weight) + " Kgs")

if convert.upper() == "L":
    new_weight = weight * 2.205
    print("Your converted weight is " + str(new_weight) + " Lbs")

else:
    print("That is not a valid reply")