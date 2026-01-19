import math
pos = [0,0]
while True:
    s = input("enter direction: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "RIGHT":
        pos[1] = pos[1]+steps
    elif direction == "LEFT":
        pos[1] = pos[1] -steps
    elif direction == "UP":
        pos[0] = pos[0] +steps
    elif direction == "DOWN":
        pos[0] = pos[0] -steps
    else:
        print("enter valid input")
distance = math.sqrt(pos[1]**2+pos[0]**2)
print(int(distance))