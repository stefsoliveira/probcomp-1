def right_or_left(plain, planet):
    a = plain[0]
    b = plain[1]
    c = plain[2]
    d = plain[3]
    x = planet[0]
    y = planet[1]
    z = planet[2]
    if (a * x + b * y + c * z - d) > 0:
        return "d"
    elif (a * x + b * y + c * z - d) < 0:
        return "e"   #e quando é igual a zero? no plano?

def check_region(plains, planet):
    region = ""
    for p in range(len(plains)):
        region += right_or_left(plains[p],planet)
    return region

parameters = input().split()
num_plains = int(parameters[0])
num_planets = int(parameters[1])
plains = [None for i in range(num_plains)]
regions = {}

for i in range(num_plains):
    plains[i] = list(map(int, input().split(" ")))

for j in range(num_planets):
    planet = list(map(int, input().split(" ")))
    r = check_region(plains, planet)
    if r in regions:
        regions[r] += 1
    else:
        regions[r] = 1


highest_number = 0
for key in regions:
    if highest_number < regions[key]:
        highest_number = regions[key]

print(highest_number)