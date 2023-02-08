def solve(numheads,numlegs):
    rabbits = int((numlegs -2 * numheads) / 2)
    chickens = numheads - rabbits
    print("We have " + str(rabbits) + " rabbits and " + str(chickens) + " chickens!!!")

numheads = int(input())
numlegs = int(input())
solve(numheads,numlegs)