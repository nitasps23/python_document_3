
def getSqrFt():

    # a function to calculate the square footage of a house
    # Reminder of Formula: Length X Width == Area

    getLength = float(input("Enter the length (in feet): "))
    getWidth = float(input("Enter the width (in feet): "))

    print(f"The square footage of the house is {getLength * getWidth} square feet.")



def getCircumference():

    # a function to calculate the circumference of a circle
    import math

    getR = float(input("Enter radius: "))

    print(f"The area of the circle is: {math.pi * getR ** 2}")
    print(f"The circumference of the circle is: {2 * math.pi * getR}")

