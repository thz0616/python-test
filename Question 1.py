shape = input(" Enter shape (pyramid or cone): ").lower()

if shape == "pyramid":
    area = float(input("Enter the area of the base of the pyramid: "))
    height = float(input("Enter the height of the pyramid: "))
    volume = (1/3) * area * height
    print("The volume of the pyramid is: {:.2f}".format(volume))

elif shape == "cone":
    area = float(input("Enter the area of the base of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = (1 / 3) * area * height
    print("The volume of the cone is: {:.2f}".format(volume))

else:
    print("Invalid shape entered. PLease enter 'pyramid' or 'cone'. ")