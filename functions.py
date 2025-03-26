def area(radius):
    result = 22/7 * radius ** 2
    return result

def say_hi(name):
    print("Good morning", name)

print(area(7))#called
print(area(6.5))
print(area(89.345))
say_hi("Jim")
say_hi("Robert")

a1 = area(66.67)
print(round(a1))