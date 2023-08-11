import math

# Input
side_AB = float(input().strip())  # Length of side AB
side_BC = float(input().strip())  # Length of side BC

# Calculate the angle using trigonometric functions
angle_rad = math.atan2(side_AB, side_BC)
angle_deg = math.degrees(angle_rad)

# Round the angle to the nearest integer and print the result
print(str(round(angle_deg)) + '°')
6
