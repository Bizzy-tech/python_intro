def volume_cylinder(radius, height):
    v = 22/7 * radius **2 * height
    return v
print(volume_cylinder(7.0, 10.0))
print(volume_cylinder(10.65, 32.33))

v1 = volume_cylinder(height=17, radius=10)
    """ Calculatates the volume of a cylinder """
def volume_cone(radius, height, decimals=2):
    v = 1/3 * 22/7 * radius **2 * height
    v = round(v, decimals)
    return v
print(volume_cone(20.0, 15.0))