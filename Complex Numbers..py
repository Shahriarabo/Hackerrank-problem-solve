import cmath

# Input
z = complex(input().strip())  # Read the complex number

# Convert to polar coordinates
r = abs(z)         # Modulus (distance from origin)
theta = cmath.phase(z)  # Phase angle (angle with positive x-axis)

# Print the result
print(round(r, 3))
print(round(theta, 3))
