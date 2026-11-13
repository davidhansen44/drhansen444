import math
from datetime import date

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#calculate the tire's volume 
volume = math.pi * (width ** 2) * aspect_ratio * ((width * aspect_ratio) + (2540 * wheel_diameter)) / 10000000000


#Display the volume 
print(f"The approximate volume is {round(volume, 2)} liters")


#Get todays date
now = date.today()

with open("volumes.txt", "at") as file:
    line = f"{now}, {width}, {aspect_ratio}, {wheel_diameter}, {round(volume, 2)}\n"
    file.write(line)
