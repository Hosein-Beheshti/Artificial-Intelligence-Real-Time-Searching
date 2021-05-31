import random
#check if at least one red and blue mushroom eaten return true
def goalCheck():
    global redMushroomEaten
    global blueMushroomEaten
    if redMushroomEaten >= 1 and blueMushroomEaten >= 1:
        return True
    return False

#heuristic -> mushrooms number
def heuristic1():
    global redMushrooms
    global blueMushrooms
    numberOfremainMushrooms = 0
    for i in range(len(redMushrooms)):
        if int(redMushrooms[i][0]) > 0 and int(redMushrooms[i][1]) > 0:
            numberOfremainMushrooms = numberOfremainMushrooms + 1
    for i in range(len(blueMushrooms)):
        if int(blueMushrooms[i][0]) > 0 and int(blueMushrooms[i][1]) > 0:
            numberOfremainMushrooms = numberOfremainMushrooms + 1
    return numberOfremainMushrooms

#heuristic -> shortest distance to any mushroom
def heuristic2():
    global eachMushroomsNumber
    global redMushrooms
    global blueMushrooms
    global x
    global y
    cost = 0
    mincost = 0
    for i in range(len(redMushrooms)):
        if int(redMushrooms[i][0]) > 0 and int(redMushrooms[i][1]) > 0:
            cost = 0
            cost = cost + abs(int(redMushrooms[i][0]) - x)
            cost = cost + abs(int(redMushrooms[i][1]) - y)
            if mincost == 0:
                mincost = cost
            else:
                if cost < mincost:
                    mincost = cost

    for i in range(len(blueMushrooms)):
        if int(blueMushrooms[i][0]) > 0 and int(blueMushrooms[i][1]) > 0:
            cost = 0
            cost = cost + abs(int(blueMushrooms[i][0]) - x)
            cost = cost + abs(int(blueMushrooms[i][1]) - y)
            if mincost == 0:
                mincost = cost
            else:
                if cost < mincost:
                    mincost = cost
    print("min cost = " , mincost)
    return mincost

#heuristic -> longest distance between any both mushrooms
def heuristic3():
    global eachMushroomsNumber
    global redMushrooms
    global blueMushrooms
    global x
    global y
    cost = 0
    maximum = 0
    remainMushrooms = []
    for i in range(len(redMushrooms)):
        temp = []
        if int(redMushrooms[i][0]) > 0 and int(redMushrooms[i][1]) > 0:
            temp.append(int(redMushrooms[i][0]))
            temp.append(int(redMushrooms[i][1]))
            remainMushrooms.append(temp)
    for i in range(len(blueMushrooms)):
        temp = []
        if int(blueMushrooms[i][0]) > 0 and int(blueMushrooms[i][1]) > 0:
            temp.append(int(blueMushrooms[i][0]))
            temp.append(int(blueMushrooms[i][1]))
            remainMushrooms.append(temp)


    for i in range(len(remainMushrooms)):
        for j in range(i + 1, len(remainMushrooms)):
            cost = 0
            cost = cost + abs(remainMushrooms[i][0] - remainMushrooms[j][0])
            cost = cost + abs(remainMushrooms[i][1] - remainMushrooms[j][1])
            if maximum < cost:
                maximum = cost

    print("max cost = " , maximum)
    return maximum


#read from file
f = open("F:\\Python\AI project\project2\Mario.txt", "r")

n = int(f.readline()[0])
m = int(f.readline()[0])
#read index of mario
temp = f.readline()
x, y = map(int , temp.split())

eachMushroomsNumber = int(f.readline()[0])
mushrooms=[]
#read red mushrooms index
redMushrooms=[]
for i in range(0,eachMushroomsNumber):
    inputs = list(f.readline().split())
    redMushrooms.append(inputs)
    mushrooms.append(inputs)
#read blue mushrooms index
blueMushrooms=[]
for i in range(0,eachMushroomsNumber):
    inputs = list(f.readline().split())
    blueMushrooms.append(inputs)
    mushrooms.append(inputs)
#read obstacles index
# obstaclesNumber = len(f.readlines())
obstacles=[]
while(True):
    inputs = list(f.readline().split())
    if len(inputs) == 0:
        break
    obstacles.append(inputs)

mushroomsNumber = eachMushroomsNumber * 2

print(n)
print(m)
print(x)
print(y)
print(redMushrooms)
print(blueMushrooms)
print(obstacles)


states = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(-1)
    states.append(tmp)

actions = []
for i in range(n):
    tmp1 = []
    for j in range(m):
        tmp = []
        for k in range(4):
            tmp.append(-1)
        tmp1.append(tmp)
    actions.append(tmp1)

DoActions = []
for i in range(n):
    tmp1 = []
    for j in range(m):
        tmp = []
        for k in range(4):
            tmp.append(False)
        tmp1.append(tmp)
    DoActions.append(tmp1)
print(states)
# print(actions)
# print(obstacles)
# for i in range(len(obstacles)):
#     print(obstacles[i][0])
#     print(obstacles[i][1])
#     if int(obstacles[i][0]) == 2 and int(obstacles[i][1]) == 2:
#         print("obstacleeeeeeeeeeeeeeeeee")
redMushroomEaten = 0
blueMushroomEaten = 0
stepsNumber = 0

while(True):

    #is goal
    if goalCheck():
        # for i in reversed(range(m)):
        #     for j in range(n):
        #         print(states[j][i], end ="  ")
        #     print("")
        break

    if states[x - 1][y - 1] == -1:
        states[x - 1][y - 1] = heuristic2()
    #initial action costs for first time with estimated H
    for i in range(4):
        if actions[x - 1][y - 1][i] == -1:
            actions[x - 1][y - 1][i] = states[x - 1][y - 1]
    #update action costs
    while(True):
        change = False
        for i in range(1 , n + 1):
            for j in range(1 , m + 1):
                x1 = j
                y1 = i
                if states[x1 - 1][y1 - 1] > 0:
                    # #update left action
                    if x1 - 1 - 1 >= 0:
                        if states[x1 - 1 - 1][y1 - 1] != -1 and DoActions[x1 - 1][y1 - 1][0] == True:
                            # print("00000000000000000000000000000000000")
                            if actions[x1 - 1][y1 - 1][0] != (states[x1 - 1 - 1][y1 - 1] + 1) and actions[x1 - 1][y1 - 1][0] != -2:
                                print("location x = " , x1 , "location y = " , y1)
                                print("Action = left")
                                print(actions[x1 - 1][y1 - 1][0] , " <- " , states[x1 - 1 - 1][y1 - 1] + 1)
                                actions[x1 - 1][y1 - 1][0] = states[x1 - 1 - 1][y1 - 1] + 1
                                
                    #update up action
                    if y1 - 1 + 1 < n:
                        if states[x1 - 1][y1 - 1 + 1] != -1 and DoActions[x1 - 1][y1 - 1][1] == True:
                            # print("111111111111111111111111111111111111")
                            if actions[x1 - 1][y1 - 1][1] != (states[x1 - 1][y1 - 1 + 1] + 1) and actions[x1 - 1][y1 - 1][1] != -2:
                                print("location x = " , x1 , "location y = " , y1)
                                print("Action = up")
                                print(actions[x1 - 1][y1 - 1][1] , " <- " , states[x1 - 1][y1 - 1 + 1] + 1)

                                actions[x1 - 1][y1 - 1][1] = states[x1 - 1][y1 - 1 + 1] + 1
                    #update right action
                    if x1 - 1 + 1 < m:
                        if states[x1 - 1 + 1][y1 - 1] != -1 and DoActions[x1 - 1][y1 - 1][2] == True:
                            # print("22222222222222222222222222222222222222")

                            if actions[x1 - 1][y1 - 1][2] != (states[x1 - 1 + 1][y1 - 1] + 1) and actions[x1 - 1][y1 - 1][2] != -2:
                                print("location x = " , x1 ,  "location y = " , y1)
                                print("Action = right")
                                print(actions[x1 - 1][y1 - 1][2], " <- " , states[x1 - 1 + 1][y1 - 1] + 1)
                                actions[x1 - 1][y1 - 1][2] = states[x1 - 1 + 1][y1 - 1] + 1
                    #update down action
                    if y1 - 1 - 1 >= 0:
                        if states[x1 - 1][y1 - 1 - 1] != -1 and DoActions[x1 - 1][y1 - 1][3] == True:
                            # print("333333333333333333333333333333333333")

                            if actions[x1 - 1][y1 - 1][3] != (states[x1 - 1][y1 - 1 - 1] + 1) and actions[x1 - 1][y1 - 1][3] != -2:
                                print("location x = " , x1 , "location y = " , y1)
                                print("Action = down")
                                print(actions[x1 - 1][y1 - 1][3], " <- " , states[x1 - 1][y1 - 1 - 1] + 1)
                                actions[x1 - 1][y1 - 1][3] = states[x1 - 1][y1 - 1 - 1] + 1
                    min = -2
                    for i in range(4):
                        if actions[x1 - 1][y1 - 1][i] >= 0 and min == -2:
                            min = actions[x1 - 1][y1 - 1][i]
                        if actions[x1 - 1][y1 - 1][i] < min and actions[x1 - 1][y1 - 1][i] >= 0 and min >= 0:
                            min = actions[x1 - 1][y1 - 1][i]
                    if states[x1 - 1][y1 - 1] != min and min >= 0:
                        print("H Updated // " , states[x1 - 1][y1 - 1] , " <- " , min)

                        states[x1 - 1][y1 - 1] = min

                        change = True
        if change == False:
            break



    #choose an action
    #find minimum cost

    print("##############################")
    print(actions[x - 1][y - 1])
    min = -2
    for i in range(4):
        if actions[x - 1][y - 1][i] >= 0 and min == -2:
            min = actions[x - 1][y - 1][i]
        if actions[x - 1][y - 1][i] < min and actions[x - 1][y - 1][i] >= 0:
            min = actions[x - 1][y - 1][i]
    #choose with randomness between minimum costs
    choices = []
    if actions[x - 1][y - 1][0] == min:
        choices.append(0)
    if actions[x - 1][y - 1][1] == min:
        choices.append(1)
    if actions[x - 1][y - 1][2] == min:
        choices.append(2)
    if actions[x - 1][y - 1][3] == min:
        choices.append(3)
    
    action = random.choice(choices)
    # print(action)
    DoActions[x - 1][y - 1][action] = True

    #mario move
    stepsNumber = stepsNumber + 1
    x1 = x
    oldX = x
    y1 = y
    oldY = y
    isObstacle = False
    #left
    if action == 0:
        print("left")
        if x - 1 > 0:
            for i in range(len(obstacles)):
                if int(obstacles[i][0]) == x - 1 and int(obstacles[i][1]) == y:
                    isObstacle = True
                    
            if isObstacle == False:
                x1 = x - 1
    #up
    if action == 1:
        print("up")
        if y + 1 <= n:
            for i in range(len(obstacles)):
                if int(obstacles[i][0]) == x and int(obstacles[i][1]) == y + 1:
                    isObstacle = True

            if isObstacle == False:
                y1 = y + 1
    #right
    if action == 2:
        print("right")
        if x + 1 <= m:
            for i in range(len(obstacles)):
                if int(obstacles[i][0]) == x + 1 and int(obstacles[i][1]) == y:
                    isObstacle = True

            if isObstacle == False:           
                x1 = x + 1
    #down
    if action == 3:
        print("down")
        if y - 1 > 0:
            for i in range(len(obstacles)):
                if int(obstacles[i][0]) == x and int(obstacles[i][1]) == y - 1:
                    isObstacle = True

            if isObstacle == False:
                y1 = y - 1
    #Collision with an obstacle or out of range
    if x == x1 and y == y1:
        actions[x - 1][y - 1][action] = -2
        print("Collision with an obstacle or out of range")
        # print(actions)
    else:
        x = x1
        y = y1
        #eat red mushroom
        # print("red length = %d" % len(redMushrooms))
        for i in range(len(redMushrooms)):
            if int(redMushrooms[i][0]) == x and int(redMushrooms[i][1]) == y:
                # redMushrooms.pop(i)
                redMushrooms[i][0] = -1
                redMushrooms[i][1] = -1
                print(redMushrooms)
                redMushroomEaten = redMushroomEaten + 1
        #eat blue mushroom
        # print("blue length = %d " % len(blueMushrooms))
        for i in range(len(blueMushrooms)):
            if int(blueMushrooms[i][0]) == x and int(blueMushrooms[i][1]) == y:
                # blueMushrooms.pop(i)
                blueMushrooms[i][0] = -1
                blueMushrooms[i][1] = -1
                print(blueMushrooms)
                blueMushroomEaten = blueMushroomEaten + 1
        #update action cost
        if states[x - 1][y - 1] == -1:
            states[x - 1][y - 1] = heuristic2()
        print("action = " , action)
        print(actions[oldX - 1][oldY - 1][action] , " <- " , states[x - 1][y - 1] + 1)
        actions[oldX - 1][oldY - 1][action] = states[x - 1][y - 1] + 1

        
        #update H for old state

        min = -2
        for i in range(4):
            if actions[oldX - 1][oldY - 1][i] >= 0 and min == -2:
                min = actions[oldX - 1][oldY - 1][i]
            if actions[oldX - 1][oldY - 1][i] < min and actions[oldX - 1][oldY - 1][i] >= 0 and min >= 0:
                min = actions[oldX - 1][oldY - 1][i]
        if min >= 0:
            states[oldX - 1][oldY - 1] = min

        for i in range(1 , n + 1):
            for j in range(1 , m + 1):
                x1 = j
                y1 = i
                if DoActions[x1 - 1][y1 - 1] == True:
                    min = -2
                    
                    for i in range(4):
                        if actions[x1 - 1][y1 - 1][i] >= 0 and min == -2:
                            min = actions[x1 - 1][y1 - 1][i]
                        if actions[x1 - 1][y1 - 1][i] < min and actions[x1 - 1][y1 - 1][i] >= 0 and min >= 0:
                            min = actions[x1 - 1][y1 - 1][i]
                    if min >= 0:
                        states[x1 - 1][y1 - 1] = min

    print("x = ",  x)
    print("y = " , y)
    # print(actions)
    for i in reversed(range(m)):
        for j in range(n):
            print(states[j][i], end ="  ")
        print("")
print("steps number = %d" % stepsNumber)