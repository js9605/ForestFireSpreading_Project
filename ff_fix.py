from scipy.misc import imsave
import numpy
import random as rd


# IDEAS
# - add feature where you can create non - square maps
# https://github.com/rafibarash/forest-fire/blob/master/README.md     GOOD EXAMPLE
# poczytaj: turtle graphics
# poczytaj numpy do tego projektu
# density
# wind
# how many trees in fire
# is there a road?   (one line from top to bot or left to right)

# 0 - empy space
# 1 - tree on fire
# 2 - tree

class Forest_fire:

    def __init__(self):
        self.forrest_density = 0.9
        self.map_size = 100
        self.time_limit = 10
        self.map = []
        self.trees_on_fire_amount = 1
        self.trees_on_fire_amount -= 1
        self.time = 0
        self.i = 0
        self.rows = []
        self.cols = []
        self.rows2 = []
        self.cols2 = []


    def set_on_fire_around_one(self, i, j):

        self.map[i][j] = 0

        try:
            if self.map[i - 1][j - 1] == 2:
                self.map[i - 1][j - 1] = 1
                self.rows2.append( i - 1)
                self.cols2.append(j - 1)
        except IndexError:
            pass

        try:
            if self.map[i - 1][j] == 2:
                self.map[i - 1][j] = 1
                self.rows2.append(i - 1)
                self.cols2.append(j)
        except IndexError:
            pass

        try:
            if self.map[i - 1][j + 1] == 2:
                self.map[i - 1][j + 1] = 1
                self.rows2.append(i - 1)
                self.cols2.append(j + 1)
        except IndexError:
            pass

        try:
            if self.map[i][j - 1] == 2:
                self.map[i][j - 1] = 1
                self.rows2.append(i)
                self.cols2.append(j - 1)
        except IndexError:
            pass

        try:
            if self.map[i][j + 1] == 2:
                self.map[i][j + 1] = 1
                self.rows2.append(i)
                self.cols2.append(j + 1)
        except IndexError:
            pass

        try:
            if self.map[i + 1][j - 1] == 2:
                self.map[i + 1][j - 1] = 1
                self.rows2.append(i + 1)
                self.cols2.append(j - 1)
        except IndexError:
            pass

        try:
            if self.map[i + 1][j] == 2:
                self.map[i + 1][j] = 1
                self.rows2.append(i + 1)
                self.cols2.append(j)
        except IndexError:
            pass

        try:
            if self.map[i + 1][j + 1] == 2:
                self.map[i + 1][j + 1] = 1
                self.rows2.append(i + 1)
                self.cols2.append(j + 1)
        except IndexError:
            pass

    def create_map(self):
        for i in range(self.map_size):
            self.map.append([])
            for j in range(self.map_size):
                self.map[i].append(0)

    def create_forest(self):

        # normal trees
        self.amount_of_trees = self.map_size * self.map_size * self.forrest_density
        self.amount_of_trees = int(self.amount_of_trees)
        for i in range(self.amount_of_trees):
            row = rd.randint(0, self.map_size - 1)
            col = rd.randint(0, self.map_size - 1)
            if self.map[row][col] == 0:
                self.map[row][col] = 2

        #trees on fire
        while self.trees_on_fire_amount >= 0:
            row = rd.randint(0,self.map_size - 1)
            col = rd.randint(0,self.map_size - 1)
            self.rows.append(row)
            self.cols.append(col)
            if self.map[row][col] == 2:
                self.map[row][col] = 1
                self.trees_on_fire_amount -= 1
                print("PODPALA DRZEWO")

    def spread_fire(self):
        print("ROZPRZESTRZENIA OGIEN")
        # for i in range(len(self.rows)):
        while self.i <= len(self.rows) - 1:
            print(self.i)
            Forest_fire.set_on_fire_around_one(self, self.rows[self.i], self.cols[self.i])
            self.i += 1
        self.rows = self.rows2.copy()
        self.cols = self.cols2.copy()
        self.rows2.clear()
        self.cols2.clear()
        print("self.rows: ", self.rows)

    def show_map_as_matrix(self):
        for i in range(len(self.map)):
            print(self.map[i])

    def save_png(self, time):
        time = str(self.time)
        name = 'forrest_fire_' + time + ".png"
        name = str(name)
        imsave(name, self.map)

    def main(self):
        Forest_fire.create_map(self)
        Forest_fire.create_forest(self)
        while self.time <= self.time_limit:
            print("ZAPISUJE PNG")
            Forest_fire.save_png(self, self.time)
            Forest_fire.spread_fire(self)
            self.time += 1


forest_fire = Forest_fire()
forest_fire.main()

