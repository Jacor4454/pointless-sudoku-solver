import pygame
import numberlib as lb             ##### needs letterlib imported (see group files)

pygame.init()

win = pygame.display.set_mode((102,102))
win.fill((255,255,255))

def linedraw():
    line = [10,21,32,33,34,45,56,67,68,69,80,91]
    for i in range (0,12):
        pygame.draw.line(win, (0,0,0), (line[i],0), (line[i],102))
        pygame.draw.line(win, (0,0,0), (0,line[i]), (102,line[i]))

global grid

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

enter = False
activesquare = [0,0]
todraw = [0,0]
line = [10,21,32,33,34,45,56,67,68,69,80,91]
lastpressed = [0 for i in range (0,14)]
while enter == False:
    win.fill((255,255,255))
    linedraw()
    for i in range (0,2):
        for j in range (0,12):
            if activesquare[i] == 0:
                todraw[i] = 0
            elif activesquare[i] == j+1:
                todraw[i] = line[j] + 1
    pygame.draw.rect(win, (70,100,255), (todraw[0], todraw[1], 10, 10))
    for x in range (0,9):
        for y in range (0,9):
            gridx = x
            gridy = y
            if grid[y][x] == 0:
                pass
            else:
                if x > 5:
                    gridx = x + 4
                elif x > 2:
                    gridx = x + 2
                if y > 5:
                    gridy = y + 4
                elif y > 2:
                    gridy = y + 2
                if x == 0:
                    todraw[0] = 6
                else:
                    todraw[0] = line[gridx-1]+7
                if y == 0:
                    todraw[1] = 5
                else:
                    todraw[1] = line[gridy-1]+6
                lb.draw(grid[y][x], todraw, win, 1)
                
    pygame.display.flip()
    pygame.event.get()
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == 1:
        xi = 12
        yi = 12
        pos = pygame.mouse.get_pos()
        for i in range (11,-1,-1):
            if pos[0] < line[i]:
                xi = i
        for i in range (11,-1,-1):
            if pos[1] < line[i]:
                yi = i
        if xi == 3 or xi == 4:
            xi = 5
        if xi == 8 or xi == 9:
            xi = 10
        if yi == 3 or yi == 4:
            yi = 5
        if yi == 8 or yi == 9:
            yi = 10
        activesquare = [xi,yi]
    key = pygame.key.get_pressed()     ### key[48] = 0, key[49] = 1 and so on
    for i in range (0,10):
        if key[48+i] == 1  and lastpressed[i] == 0:
            if activesquare[0] > 8:
                gridx = activesquare[0] - 4
            elif activesquare[0] > 3:
                gridx = activesquare[0] - 2
            else:
                gridx = activesquare[0]
            if activesquare[1] > 8:
                gridy = activesquare[1] - 4
            elif activesquare[1] > 3:
                gridy = activesquare[1] - 2
            else:
                gridy = activesquare[1]
            grid[gridy][gridx] = i
            lastpressed[i] = 1
        elif key[48+i] == 1:
            pass
        else:
            lastpressed[i] = 0
    if key[13] == 1:
        enter = True
    if key[273] == 1 and lastpressed[10] == 0:
        if activesquare[1] == 5 or activesquare[1] == 10:
            activesquare[1] -= 3
        elif activesquare[1] != 0:
            activesquare[1] -= 1
        lastpressed[10] = 1
    elif key[273] == 1:
        pass
    else:
        lastpressed[10] = 0
    if key[274] == 1 and lastpressed[11] == 0:
        if activesquare[1] == 2 or activesquare[1] == 7:
            activesquare[1] += 3
        elif activesquare[1] != 12:
            activesquare[1] += 1
        lastpressed[11] = 1
    elif key[274] == 1:
        pass
    else:
        lastpressed[11] = 0
    if key[275] == 1 and lastpressed[12] == 0:
        if activesquare[0] == 2 or activesquare[0] == 7:
            activesquare[0] += 3
        elif activesquare[0] != 12:
            activesquare[0] += 1
        lastpressed[12] = 1
    elif key[275] == 1:
        pass
    else:
        lastpressed[12] = 0
    if key[276] == 1 and lastpressed[13] == 0:
        if activesquare[0] == 5 or activesquare[0] == 10:
            activesquare[0] -= 3
        elif activesquare[0] != 0:
            activesquare[0] -= 1
        lastpressed[13] = 1
    elif key[276] == 1:
        pass
    else:
        lastpressed[13] = 0
    pygame.time.wait(50)


class row():

    def missing(self, row):
        working = grid[row]
        find = [0 for i in range (0,9)]
        for i in range (0,9):
            for j in range (1,10):
                if grid[row][i] == j :
                    find[j-1] = 1

        base = [1,2,3,4,5,6,7,8,9]
        passer = [0 for i in range (0,9)]
        for i in range (0,9):
            for j in range (0,9):
                if base[j] == working[i]:
                    passer[j] = 1

        toreturn = []
        if passer[0] == 0:
            toreturn.append(1)
        if passer[1] == 0:
            toreturn.append(2)
        if passer[2] == 0:
            toreturn.append(3)
        if passer[3] == 0:
            toreturn.append(4)
        if passer[4] == 0:
            toreturn.append(5)
        if passer[5] == 0:
            toreturn.append(6)
        if passer[6] == 0:
            toreturn.append(7)
        if passer[7] == 0:
            toreturn.append(8)
        if passer[8] == 0:
            toreturn.append(9)

        return toreturn

class colombe():

    def missing(self, colombe):
        working = []
        for i in range (0,9):
            working.append(grid[i][colombe])
        
        base = [1,2,3,4,5,6,7,8,9]
        passer = [0 for i in range (0,9)]
        for i in range (0,9):
            for j in range (0,9):
                if base[j] == working[i]:
                    passer[j] = 1

        toreturn = []
        if passer[0] == 0:
            toreturn.append(1)
        if passer[1] == 0:
            toreturn.append(2)
        if passer[2] == 0:
            toreturn.append(3)
        if passer[3] == 0:
            toreturn.append(4)
        if passer[4] == 0:
            toreturn.append(5)
        if passer[5] == 0:
            toreturn.append(6)
        if passer[6] == 0:
            toreturn.append(7)
        if passer[7] == 0:
            toreturn.append(8)
        if passer[8] == 0:
            toreturn.append(9)

        return toreturn

class square():

    def __init__(self):
        self.square = [[0 for i in range (0,9)] for j in range (0,9)] 
        self.squarecount = 0
        for i in range (0,3):
            for j in range (0,3):
                self.square[self.squarecount] = [grid[(i*3)][(j*3)],grid[(i*3)][(j*3)+1],grid[(i*3)][(j*3)+2],grid[(i*3)+1][(j*3)],grid[(i*3)+1][(j*3)+1],grid[(i*3)+1][(j*3)+2],grid[(i*3)+2][(j*3)],grid[(i*3)+2][(j*3)+1],grid[(i*3)+2][(j*3)+2]]
                self.squarecount += 1

    def missing(self, quadrent):
        if quadrent == 0:
            active = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        elif quadrent == 3:
            active = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
        elif quadrent == 6:
            active = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
        elif quadrent == 1:
            active = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
        elif quadrent == 4:
            active = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
        elif quadrent == 7:
            active = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
        elif quadrent == 2:
            active = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
        elif quadrent == 5:
            active = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
        elif quadrent == 8:
            active = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]

        base = [1,2,3,4,5,6,7,8,9]
        passer = [0 for i in range (0,9)]
        for i in range (0,9):
            for j in range (0,9):
                if base[j] == grid[active[i][1]][active[i][0]]:
                    passer[j] = 1

        toreturn = []
        if passer[0] == 0:
            toreturn.append(1)
        if passer[1] == 0:
            toreturn.append(2)
        if passer[2] == 0:
            toreturn.append(3)
        if passer[3] == 0:
            toreturn.append(4)
        if passer[4] == 0:
            toreturn.append(5)
        if passer[5] == 0:
            toreturn.append(6)
        if passer[6] == 0:
            toreturn.append(7)
        if passer[7] == 0:
            toreturn.append(8)
        if passer[8] == 0:
            toreturn.append(9)

        return toreturn

    def remaining(self, quadrent):
        if quadrent == 0:
            active = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        elif quadrent == 3:
            active = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
        elif quadrent == 6:
            active = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
        elif quadrent == 1:
            active = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
        elif quadrent == 4:
            active = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
        elif quadrent == 7:
            active = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
        elif quadrent == 2:
            active = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
        elif quadrent == 5:
            active = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
        elif quadrent == 8:
            active = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
        else:
            print("fail2")

        tempsquare = square.missing(quadrent)
        basis = [0 for i in range (0,9)]
        for i in range (0,9):
            if grid[active[i][1]][active[i][0]] == 0:
                tempalong = row.missing(active[i][1])
                tempdown = colombe.missing(active[i][0])
                for j in range (0, len(tempsquare)):
                    for k in range (0, len(tempalong)):
                        if tempsquare[j] == tempalong[k] :
                            for l in range (0,len(tempdown)):
                                if tempsquare[j] == tempdown[l]:
                                    if tempsquare[j] == 1:
                                        basis[0] += 1
                                    elif tempsquare[j] == 2:
                                        basis[1] += 1
                                    elif tempsquare[j] == 3:
                                        basis[2] += 1
                                    elif tempsquare[j] == 4:
                                        basis[3] += 1
                                    elif tempsquare[j] == 5:
                                        basis[4] += 1
                                    elif tempsquare[j] == 6:
                                        basis[5] += 1
                                    elif tempsquare[j] == 7:
                                        basis[6] += 1
                                    elif tempsquare[j] == 8:
                                        basis[7] += 1
                                    elif tempsquare[j] == 9:
                                        basis[8] += 1

        counter = 0
        for i in range (0,9):
            if basis[i] == 1:
                counter += 1
        if counter == 1:
            flick = 9
            for i in range (0,9):
                if basis[i] == 1:
                    return [[i+1]]
        elif counter > 0:
            toreturn = []
            for i in range (0,9):
                if basis[i] == 1:
                    toreturn.append([i+1])
            return [toreturn]
        else:
            return [[0]]

class space():

    def __init__(self):

        self.value = 0

        self.possision = [0,0]

        self.possible = []

        self.square = 0

spaces = [space() for i in range (0, 81)]
row = row()

colombe = colombe()

square = square()

counter = 1                            #036
passer = 0                             #147
global newx, newy                      #258
newx = 0
newy = 0

def just1():
    counter = 1
    passer = 0
    for quadrent in range (0,9):
        for y in range (0,3): #2
            for x in range (0,3): #1
                newx = x
                newy = y
                if quadrent == 1 or quadrent == 4 or quadrent == 7:
                    newy = y +  3
                if quadrent == 2 or quadrent == 5 or quadrent == 8:
                    newy = y + 6
                if quadrent == 3 or quadrent == 4 or quadrent == 5:
                    newx = x + 3
                if quadrent == 6 or quadrent == 7 or quadrent == 8:
                    newx = x + 6
                if grid[newy][newx] == 0:
                    tempalong = row.missing(newy)
                    tempdown = colombe.missing(newx)
                    tempsquare = square.missing(quadrent)
                    possible = []
                    for i in range (0, len(tempalong)):
                        for j in range (0, len(tempdown)):
                            for k in range (0, len(tempsquare)):
                                if tempalong[i] == tempdown[j]:
                                    if tempalong[i]== tempsquare[k]:
                                        possible.append(tempalong[i])
                    if len(possible) == 1:
                        grid[newy][newx] = possible[0]
                    elif len(possible) == 0:
                        print("fail", newx, newy)
                        print("along",tempalong)
                        print("down",tempdown)
                        print("square",tempsquare)


def just2(): #first principle
    for quadrent in range (0,9):
        for y in range (0,3): #2
            for x in range (0,3): #1
                newx = x
                newy = y
                if quadrent == 1 or quadrent == 4 or quadrent == 7:
                    newy = y +  3
                if quadrent == 2 or quadrent == 5 or quadrent == 8:
                    newy = y + 6
                if quadrent == 3 or quadrent == 4 or quadrent == 5:
                    newx = x + 3
                if quadrent == 6 or quadrent == 7 or quadrent == 8:
                    newx = x + 6
                if grid[newy][newx] == 0:
                    tempalong = row.missing(newy)
                    tempdown = colombe.missing(newx)
                    tempsquare = square.missing(quadrent)
                    possible = []
                    for i in range (0, len(tempalong)):
                        for j in range (0, len(tempdown)):
                            for k in range (0, len(tempsquare)):
                                if tempalong[i] == tempdown[j]:
                                    if tempalong[i]== tempsquare[k]:
                                        possible.append(tempalong[i])
                    if len(possible) == 1:
                        grid[newy][newx] = possible[0]
                    elif len(possible) == 0:
                        print("fail", newx, newy)
                        print("along",tempalong)
                        print("down",tempdown)
                        print("square",tempsquare)
                    else:
                        inthesquare = square.remaining(quadrent) #second priciple
                        classifide = 0
                        for i in range(0,len(inthesquare)):
                            for j in range (0, len(possible)):
                                if inthesquare[i][0] == possible[j]:
                                    classifide += 1
                        if classifide == 1:
                            for i in range (0,len(inthesquare)):
                                for j in  range (0,len(possible)):
                                    if inthesquare[i][0] == possible[j]:
                                        grid[newy][newx] = possible[j]
                        elif classifide == 0:
                            pass
                        else:
                            print("fail3")
def just3(): #third principle
    for number in range (1,10):
        alongN = [1 for i in range (0,9)]
        downN = [1 for i in range (0,9)]
        for quadrent in range (0,9):
            for y in range (0,3):
                for x in range (0,3):
                    newx = x
                    newy = y
                    if quadrent == 1 or quadrent == 4 or quadrent == 7:
                        newy = y +  3
                    if quadrent == 2 or quadrent == 5 or quadrent == 8:
                        newy = y + 6
                    if quadrent == 3 or quadrent == 4 or quadrent == 5:
                        newx = x + 3
                    if quadrent == 6 or quadrent == 7 or quadrent == 8:
                        newx = x + 6
                    if grid[newy][newx] == number:
                        alongN[newy] = 0
                        downN[newx] = 0
        counta = 0
        countd = 0
        for i in range (0,9):
            if alongN[i] == 1:
                counta += 1
            if downN[i] == 1:
                countd += 1
        if counta == 1:
            NY = 9
            NX = 9
            for i in range (0,9):
                if alongN[i] == 1:
                    NY = i
                if downN[i] == 1:
                    NX = i
            grid[NY][NX] = number
        elif counta != countd :
            print("fail4")

def just4():
    for quadrent in range (0,9):
        if quadrent == 0:
            activeq = [1,2,3,6]
        elif quadrent == 1:
            activeq = [0,2,4,7]
        elif quadrent == 2:
            activeq = [0,1,5,8]
        elif quadrent == 3:
            activeq = [0,4,5,6]
        elif quadrent == 4:
            activeq = [1,3,5,7]
        elif quadrent == 5:
            activeq = [2,3,4,8]
        elif quadrent == 6:
            activeq = [0,3,7,8]
        elif quadrent == 7:
            activeq = [1,4,6,8]
        elif quadrent == 8:
            activeq = [2,5,6,7]

        for number in range (1,10):
            switcher = 0
            for x in range (0,3):
                for y in range (0,3):
                    newx = x
                    newy = y
                    if quadrent == 1 or quadrent == 4 or quadrent == 7:
                        newy = y +  3
                    if quadrent == 2 or quadrent == 5 or quadrent == 8:
                        newy = y + 6
                    if quadrent == 3 or quadrent == 4 or quadrent == 5:
                        newx = x + 3
                    if quadrent == 6 or quadrent == 7 or quadrent == 8:
                        newx = x + 6
                    if grid[newy][newx] == number:
                        switcher += 1
            if switcher > 0:
                pass
            else:
                gradx = [9 for i in range (0,4)]
                grady = [9 for i in range (0,4)]
                for aq in range (0,4):
                    for x in range (0,3):
                        for y in range (0,3):
                            newx = x
                            newy = y
                            if activeq[aq] == 1 or activeq[aq] == 4 or activeq[aq] == 7:
                                newy = y + 3
                            if activeq[aq] == 2 or activeq[aq] == 5 or activeq[aq] == 8:
                                newy = y + 6
                            if activeq[aq] == 3 or activeq[aq] == 4 or activeq[aq] == 5:
                                newx = x + 3
                            if activeq[aq] == 6 or activeq[aq] == 7 or activeq[aq] == 8:
                                newx = x + 6
                            
                            if grid[newy][newx] == number:
                                gradx[aq] = newx
                                grady[aq] = newy

                slap = 0
                stick = 0
                counting = 0
                for x in range (0,3):
                    for y in range (0,3):
                        newx = x
                        newy = y
                        if quadrent == 1 or quadrent == 4 or quadrent == 7:
                            newy = y +  3
                        if quadrent == 2 or quadrent == 5 or quadrent == 8:
                            newy = y + 6
                        if quadrent == 3 or quadrent == 4 or quadrent == 5:
                            newx = x + 3
                        if quadrent == 6 or quadrent == 7 or quadrent == 8:
                            newx = x + 6
                        slap = 0
                        for i in range (0,4):
                            if newx == gradx[i]:
                                slap += 1
                        if slap == 0:
                            stick = 0
                            for j in range (0,4):
                                if newy == grady[j]:
                                    stick += 1
                            if stick == 0:
                                if grid[newy][newx] == 0:
                                    counting += 1

                slap = 0
                stick = 0
                if counting == 1:
                    for x in range (0,3):
                        for y in range (0,3):
                            newx = x
                            newy = y
                            if quadrent == 1 or quadrent == 4 or quadrent == 7:
                                newy = y +  3
                            if quadrent == 2 or quadrent == 5 or quadrent == 8:
                                newy = y + 6
                            if quadrent == 3 or quadrent == 4 or quadrent == 5:
                                newx = x + 3
                            if quadrent == 6 or quadrent == 7 or quadrent == 8:
                                newx = x + 6

                            slap = 0
                            for i in range (0,4):
                                if newx == gradx[i]:
                                    slap += 1
                            if slap == 0:
                                stick = 0
                                for j in range (0,4):
                                    if newy == grady[j]:
                                        stick += 1
                                if stick == 0:
                                    if grid[newy][newx] == 0:
                                        grid[newy][newx] = number

def just5():
    for quadrent in range (0,9):
        if quadrent == 0:
            activeqx = [1,2]
            activeqy = [3,6]
            activeq = [1,2,3,6]
        elif quadrent == 1:
            activeqx = [0,2]
            activeqy = [4,7]
            activeq = [0,2,4,7]
        elif quadrent == 2:
            activeqx = [0,1]
            activeqy = [5,8]
            activeq = [0,1,5,8]
        elif quadrent == 3:
            activeqx = [4,5]
            activeqy = [0,6]
            activeq = [0,4,5,6]
        elif quadrent == 4:
            activeqx = [3,5]
            activeqy = [1,7]
            activeq = [1,3,5,7]
        elif quadrent == 5:
            activeqx = [3,4]
            activeqy = [2,8]
            activeq = [2,3,4,8]
        elif quadrent == 6:
            activeqx = [7,8]
            activeqy = [0,3]
            activeq = [0,3,7,8]
        elif quadrent == 7:
            activeqx = [6,8]
            activeqy = [1,4]
            activeq = [1,4,6,8]
        elif quadrent == 8:
            activeqx = [6,7]
            activeqy = [2,5]
            activeq = [2,5,6,7]

        for number in range (1,10):
            present = 0
            for x in range (0,3):
                for y in range (0,3):
                    newx = x
                    newy = y
                    if quadrent == 1 or quadrent == 4 or quadrent == 7:
                        newy = y +  3
                    if quadrent == 2 or quadrent == 5 or quadrent == 8:
                        newy = y + 6
                    if quadrent == 3 or quadrent == 4 or quadrent == 5:
                        newx = x + 3
                    if quadrent == 6 or quadrent == 7 or quadrent == 8:
                        newx = x + 6
                    if grid[newy][newx] == number:
                        present += 1
            if present == 0:
                chatter = [0 for i in range (0,4)]
                chatterorder = [1 for i in range (0,4)]
                currentx0 = 0
                currentxcoord0 = 9
                currentx1 = 0
                currentxcoord0 = 9
                currenty0 = 0
                currentycoord0 = 9
                currenty1 = 0
                currentycoord0 = 9
                possiblex = [9 for i in range (0,6)]
                possibley = [9 for i in range (0,6)]
                for aq in range (0,4):
                    for x in range (0,3):
                        for y in range (0,3):
                            newx = x
                            newy = y
                            if activeq[aq] == 1 or activeq[aq] == 4 or activeq[aq] == 7:
                                newy = y + 3
                            if activeq[aq] == 2 or activeq[aq] == 5 or activeq[aq] == 8:
                                newy = y + 6
                            if activeq[aq] == 3 or activeq[aq] == 4 or activeq[aq] == 5:
                                newx = x + 3
                            if activeq[aq] == 6 or activeq[aq] == 7 or activeq[aq] == 8:
                                newx = x + 6

                            if grid[newy][newx] == number:
                                chatter[aq] = 1
                                if activeq[aq] == activeqx[0]:
                                    chatterorder[0] = 0
                                if activeq[aq] == activeqx[1]:
                                    chatterorder[1] = 0
                                if activeq[aq] == activeqy[0]:
                                    chatterorder[2] = 0
                                if activeq[aq] == activeqy[1]:
                                    chatterorder[3] = 0
                                possiblex[aq] = newx
                                possibley[aq] = newy
                            elif grid[newy][newx] == 0 and chatter[aq] == 0:
                                tempalong = row.missing(newy)
                                tempdown = colombe.missing(newx)
                                tempsquare = square.missing(activeq[aq])
                                for al in range (0, len(tempalong)):
                                    if tempalong[al] == number:
                                        for do in range (0, len(tempdown)):
                                            if tempalong[al] == tempdown[do]:
                                                for sq in range (0, len(tempsquare)):
                                                    if tempalong[al] == tempsquare[sq] :
                                                        for xer in range (0,2):
                                                            if activeq[aq] == activeqx[xer] and xer == 0:
                                                                if currentx0 == 0:
                                                                    currentx0 = 1
                                                                    currentxcoord0 = newx
                                                                elif currentx0 == 1:
                                                                    if currentxcoord0 == newx:
                                                                        pass
                                                                    else:
                                                                        currentx0 = 2
                                                            if activeq[aq] == activeqx[xer] and xer == 1:
                                                                if currentx1 == 0:
                                                                    currentx1 = 1
                                                                    currentxcoord1 = newx
                                                                elif currentx1 == 1:
                                                                    if currentxcoord1 == newx:
                                                                        pass
                                                                    else:
                                                                        currentx1 = 2
                                                            if activeq[aq] == activeqy[xer] and xer == 0:
                                                                if currenty0 == 0:
                                                                    currenty0 = 1
                                                                    currentycoord0 = newy
                                                                elif currenty0 == 1:
                                                                    if currentycoord0 == newy:
                                                                        pass
                                                                    else:
                                                                        currenty0 = 2
                                                            if activeq[aq] == activeqy[xer] and xer == 1:
                                                                if currenty1 == 0:
                                                                    currenty1 = 1
                                                                    currentycoord1 = newy
                                                                elif currenty1 == 1:
                                                                    if currentycoord1 == newy:
                                                                        pass
                                                                    else:
                                                                        currenty1 = 2

                if currentx0 == 1 and chatterorder[0] == 1:
                    possiblex[4] = currentxcoord0
                if currentx1 == 1 and chatterorder[1] == 1:
                    possiblex[5] = currentxcoord1
                if currenty0 == 1 and chatterorder[2] == 1:
                    possibley[4] = currentycoord0
                if currenty1 == 1 and chatterorder[3] == 1:
                    possibley[5] = currentycoord1

                if True:
                    slap = 0
                    stick = 0
                    counting = 0
                    for x in range (0,3):
                        for y in range (0,3):
                            newx = x
                            newy = y
                            if quadrent == 1 or quadrent == 4 or quadrent == 7:
                                newy = y +  3
                            if quadrent == 2 or quadrent == 5 or quadrent == 8:
                                newy = y + 6
                            if quadrent == 3 or quadrent == 4 or quadrent == 5:
                                newx = x + 3
                            if quadrent == 6 or quadrent == 7 or quadrent == 8:
                                newx = x + 6
                            slap = 0
                            for i in range (0,6):
                                if newx == possiblex[i]:
                                    slap += 1
                            if slap == 0:
                                stick = 0
                                for j in range (0,6):
                                    if newy == possibley[j]:
                                        stick += 1
                                if stick == 0:
                                    if grid[newy][newx] == 0:
                                        counting += 1

                    slap = 0
                    stick = 0
                    if counting == 1:
                        for x in range (0,3):
                            for y in range (0,3):
                                newx = x
                                newy = y
                                if quadrent == 1 or quadrent == 4 or quadrent == 7:
                                    newy = y +  3
                                if quadrent == 2 or quadrent == 5 or quadrent == 8:
                                    newy = y + 6
                                if quadrent == 3 or quadrent == 4 or quadrent == 5:
                                    newx = x + 3
                                if quadrent == 6 or quadrent == 7 or quadrent == 8:
                                    newx = x + 6

                                slap = 0
                                for i in range (0,6):
                                    if newx == possiblex[i]:
                                        slap += 1
                                if slap == 0:
                                    stick = 0
                                    for j in range (0,6):
                                        if newy == possibley[j]:
                                            stick += 1
                                    if stick == 0:
                                        if grid[newy][newx] == 0:
                                            grid[newy][newx] = number


just1()
zcount = 1
while zcount > 0:
    just2()
    just3()
    just4()
    just5()
    zcount = 0
    for y in range (0,9):
        for x in range (0,9):
            if grid[y][x] == 0:
                zcount += 1
    pygame.event.get()

pygame.event.get()
win.fill((255,255,255))
linedraw()
for x in range (0,9):
    for y in range (0,9):
        gridx = x
        gridy = y
        if grid[y][x] == 0:
            pass
        else:
            if x > 5:
                gridx = x + 4
            elif x > 2:
                gridx = x + 2
            if y > 5:
                gridy = y + 4
            elif y > 2:
                gridy = y + 2
            if x == 0:
                todraw[0] = 6
            else:
                todraw[0] = line[gridx-1]+7
            if y == 0:
                todraw[1] = 5
            else:
                todraw[1] = line[gridy-1]+6
            lb.draw(grid[y][x], todraw, win, 1)
                
pygame.display.flip()

while True:
    pygame.event.get()
