"""
Write a Python program to find the volume of a sphere with diameter 12 cm.
"""

PI = 3.14

def vol_of_sphere(diameter):
    radius = diameter/2
    return (4/3) * PI * (radius ** 3)

if __name__=="__main__":
    diameter = 12
    volume = vol_of_sphere(diameter)
    print(volume)

