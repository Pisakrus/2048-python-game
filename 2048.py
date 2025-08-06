import random
import math

# create the grid

xsize = 4
ysize = 4
score = 0
direction = ""
adjx = 0
adjy = 0
moves = ["LEFT", "RIGHT", "UP", "DOWN"]

def create_grid():
    global grid
    grid = [[0 for _ in range(xsize)] for _ in range(ysize)]

create_grid()

#Shows grid in terminal
def display():
    for i in grid:
        print(i)

#Generate a random number in the grid
def generate(value=0):
    if not value:
        value= random.choice([2, 2, 2, 4])

    x = random.randint(0, xsize - 1)
    y = random.randint(0, ysize - 1)

    while grid[y][x]:
        x = random.randint(0, xsize - 1)
        y = random.randint(0, ysize - 1)
    grid[y][x] = value


#Check if there is no space left, and thus the game is over
def isgameover():
    for row in grid:
        for i in row:
            if i:
                continue
            return False
    return True


#Gets coordinates of the adjacent cell based on direction.
def adjacent_coord(x, y):
    if direction == "RIGHT":
        return x + 1, y
    if direction == "LEFT":
        return x - 1, y
    if direction == "UP":
        return x, y - 1
    if direction == "DOWN":
        return x, y + 1


def merge(x, y, adjx, adjy):
    global score
    score += grid[y][x]
    grid[adjy][adjx] = grid[y][x] * 2
    grid[y][x] = 0


def move(x, y, adjx, adjy):
    grid[adjy][adjx] = grid[y][x]
    grid[y][x] = 0

def totalmove(x, y):
    cell = grid[y][x]

    if not cell:
        pass


    #If the selected cell has a value, proceed to order the cell:
    else:
        adjx, adjy = adjacent_coord(x, y)
        adjacent = grid[adjy][adjx]
        # As long as the cell has adjacent equal or empty, move or merge and then redefine new cell as the one that was adjacent.
        while not adjacent:
            move(x, y, adjx, adjy)
            x, y = adjx, adjy
            cell = adjacent
            adjx, adjy = adjacent_coord(x, y)
            try:
                adjacent = grid[adjy][adjx]
            except IndexError:
                break

# Main instructions in a turn
def totalmoveturn():
    if direction == "RIGHT":
        for y in range(ysize):
            for x in range(xsize - 2, -1, -1):
                totalmove(x, y)
    elif direction == "LEFT":
        for y in range(ysize):
            for x in range(1, xsize):
                totalmove(x, y)
    elif direction == "UP":
        for y in range(1, ysize):
            for x in range(xsize):
                totalmove(x, y)
    elif direction == "DOWN":
        for y in range(ysize - 2, -1, -1):
            for x in range(xsize):
                totalmove(x, y)

def totalmerge():
    if direction == "RIGHT":
        for y in range(ysize):
            for x in range(xsize - 2, -1, -1):
                adjx, adjy = adjacent_coord(x, y)
                cell = grid[y][x]
                adjacent = grid[adjy][adjx]
                if cell == adjacent:
                    merge(x, y, adjx, adjy)
    elif direction == "LEFT":
        for y in range(ysize):
            for x in range(1, xsize):
                adjx, adjy = adjacent_coord(x, y)
                cell = grid[y][x]
                adjacent = grid[adjy][adjx]
                if cell == adjacent:
                    merge(x, y, adjx, adjy)
    elif direction == "UP":
        for y in range(1, ysize):
            for x in range(xsize):
                adjx, adjy = adjacent_coord(x, y)
                cell = grid[y][x]
                adjacent = grid[adjy][adjx]
                if cell == adjacent:
                    merge(x, y, adjx, adjy)
    elif direction == "DOWN":
        for y in range(ysize - 2, -1, -1):
            for x in range(xsize):
                adjx, adjy = adjacent_coord(x, y)
                cell = grid[y][x]
                adjacent = grid[adjy][adjx]
                if cell == adjacent:
                    merge(x, y, adjx, adjy)

if __name__ == "__main__":
    create_grid()
    generate()
    # Main loop
    while True:
        display()
        print("Score: " + str(score))
        direction = input("Make a move (up, down, right, left): ").upper()
        while not direction in moves:
            print("Please, try again.")
            direction = input("Make a move (up, down, right, left): ").upper()
        totalmoveturn()
        totalmerge()
        totalmoveturn()
        generate()

        if isgameover():
            display()
            print("Game Over.")
            print("Score: " + str(score))
            input("Type anything to play again:")
            create_grid()
            generate()
