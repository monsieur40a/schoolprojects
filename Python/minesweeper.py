# Zachary Fortier fort0142

# I understand that this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is academic misconduct and will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

import turtle
import random


class Cell:
    def __init__(self, t, xmin, ymin, width, height):
        self.__t = t
        self.__xmin = xmin
        self.__ymin = ymin
        self.__xmax = xmin + width
        self.__ymax = ymin + height
        self.__bomb = False
        self.__cleared = False

    def isIn(self, x, y):
        if self.__xmin <= x <= self.__xmax and self.__ymin <= y <= self.__ymax:
            return True
        return False

    def setBomb(self):
        self.__bomb = True

    def isBomb(self):
        return self.__bomb

    def clear(self):
        self.__cleared = True

    def isCleared(self):
        return self.__cleared

    def getreadytodraw(self, xcor, ycor):
        self.__t.penup()
        self.__t.goto(xcor, ycor)
        self.__t.pendown()

    def showCount(self, c):  # Puts c, character in center of cell
        mid_cellx = (self.__xmin + self.__xmax)/2
        mid_celly = (self.__ymax + self.__ymin)/2
        self.getreadytodraw(mid_cellx + 2, mid_celly - 8)
        self.__t.write(c, False, align="center", font=("Gothic", 12, "normal"))

    def draw(self):  # Draws a cell and fills it with a color
        if not self.__cleared:
            self.__t.fillcolor("#003B6F")  # Tardis Blue: not cleared
        elif self.__cleared and not self.__bomb:
            self.__t.fillcolor("#989c9a")  # Earl Gray: clear and not bomb
        else:
            self.__t.fillcolor("#830303")  # Blood Red: clear and bomb
        self.getreadytodraw(self.__xmin, self.__ymin)
        self.__t.begin_fill()
        for position in ((self.__xmax, self.__ymin), (self.__xmax, self.__ymax),
                         (self.__xmin, self.__ymax), (self.__xmin, self.__ymin)):
            self.__t.goto(position)
        self.__t.end_fill()

    def clear_draw_show(self, ch=''):
        self.clear()
        self.draw()
        self.showCount(ch)


class Minesweeper:
    def __init__(self, rows, columns, mines, bombsvisible=False):
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__t.speed(0)
        self.__s = self.__t.getscreen()
        self.__s.title("Python Turtle - Epic Minesweeper Game of Epicness")
        self.__s.tracer(0)
        self.__s.onscreenclick(self.__mouseClick)
        self.__s.listen()
        self.__grid = []

        xpos, ypos = -155, -155
        for row in range(rows):
            if row > 0:
                ypos += 22
            self.__grid.append([])
            for column in range(columns):
                self.__grid[row].append(Cell(self.__t, xpos, ypos, 20, 20))
                self.__grid[row][column].draw()
                xpos += 22
            xpos = -155

        totalmines = 0
        while totalmines < mines:
            randrow = random.randint(0, rows - 1)
            randcol = random.randint(0, columns - 1)
            if not self.__grid[randrow][randcol].isBomb():
                self.__grid[randrow][randcol].setBomb()
                totalmines += 1
                if bombsvisible:
                    self.__grid[randrow][randcol].clear_draw_show("*")
        self.__s.update()
        self.__s.mainloop()

    def inGrid(self, row, col):
        if 0 <= row <= len(self.__grid) - 1 and 0 <= col <= len(self.__grid[0]) - 1:
            return True
        return False

    def displayBombs(self):
        for row in self.__grid:
            for cellobj in row:
                if cellobj.isBomb():
                    cellobj.clear_draw_show("*")

    def countBombs(self, row, col):
        bombs = 0
        for rDelta in range(-1, 2):
            for cDelta in range(-1, 2):
                if self.inGrid(row + rDelta, col + cDelta):
                    if self.__grid[row + rDelta][col + cDelta].isBomb():
                        bombs += 1
        return bombs

    def cellsRemaining(self):
        cells = 0
        for row in self.__grid:
            for cellobj in row:
                if not (cellobj.isCleared() or cellobj.isBomb()):
                    cells += 1
        return cells

    def getRowCol(self, x, y):
        for row in range(len(self.__grid)):
            for col in range(len(self.__grid[0])):
                if self.__grid[row][col].isIn(x, y):
                    return row, col
        return -1, -1

    def __mouseClick(self, x, y):
        row, col = self.getRowCol(x, y)
        if not row == -1 == col:
            if self.__grid[row][col].isBomb():
                if not self.__grid[row][col].isCleared():  # Checks for bombsvisible
                    self.displayBombs()
                self.__grid[row][col].getreadytodraw(-65, -180)
                self.__t.write("KaBoom! Game Over - Click to Exit")
                self.__s.exitonclick()
            else:
                self.clearCell(row, col)
                if self.cellsRemaining() == 0:
                    self.displayBombs()
                    self.__grid[row][col].getreadytodraw(-65, -180)
                    self.__t.write("You Win! - Click to Exit")
                    self.__s.exitonclick()

    def clearCell(self, row, col):
        if not self.inGrid(row, col):
            return
        if self.__grid[row][col].isCleared():
            return
        self.__grid[row][col].clear_draw_show()
        count = self.countBombs(row, col)
        if count != 0:
            self.__grid[row][col].showCount(str(count))
            return
        # Loops for neater recursive call of neighbors, still recursively solved
        for rDelta in range(-1, 2):
            for cDelta in range(-1, 2):
                if not cDelta == 0 == rDelta:
                    self.clearCell(row + rDelta, col + cDelta)


def main():
    Minesweeper(14, 14, 15)


if __name__ == '__main__':
    main()
