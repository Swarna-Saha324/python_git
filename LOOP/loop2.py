num = [1,4,9,16,25,36,49,64,81,100]
hero = ["Superman","thor","piderman","batman", "hulk"]
index = 0

while index < len(num):
    print(num[index])
    index += 1
nu = [1,4,9,16,25,36,49,64,81,100]
x=36
index = 0
while index < len(nu):
    if num[index] == x:
        print("Found the number:", x) #linear search
    else:
        print("Finding..")
    index += 1
#traversing through a list
i=0
while i < len(hero):
    print(hero[i])
    i += 1