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
        self.time_limit = 100
        self.map = []
        self.trees_on_fire_amount = 1
        self.trees_on_fire_amount -= 1
        self.time = 0
        self.burning_tree_position_row = []
        self.burning_tree_position_col = []

    def set_on_fire_around_one(self, i, j):

        self.map[i][j] = 0

        try:
            if self.map[i - 1][j - 1] == 2:
                self.map[i - 1][j - 1] = 1
        except IndexError:
            pass

        try:
            if self.map[i - 1][j] == 2:
                self.map[i - 1][j] = 1
        except IndexError:
            pass

        try:
            if self.map[i - 1][j + 1] == 2:
                self.map[i - 1][j + 1] = 1
        except IndexError:
            pass

        try:
            if self.map[i][j - 1] == 2:
                self.map[i][j - 1] = 1
        except IndexError:
            pass

        try:
            if self.map[i][j + 1] == 2:
                self.map[i][j + 1] = 1
        except IndexError:
            pass

        try:
            if self.map[i + 1][j - 1] == 2:
                self.map[i + 1][j - 1] = 1
        except IndexError:
            pass

        try:
            if self.map[i + 1][j] == 2:
                self.map[i + 1][j] = 1
        except IndexError:
            pass

        try:
            if self.map[i + 1][j + 1] == 2:
                self.map[i + 1][j + 1] = 1
        except IndexError:
            pass

    def create_map(self):
        for i in range(self.map_size):
            self.map.append([])
            for j in range(self.map_size):
                self.map[i].append(0)

    def create_forest(self):

        #trees on fire
        while self.trees_on_fire_amount >= 0:
            row = rd.randint(0,self.map_size - 1)
            col = rd.randint(0,self.map_size - 1)
            if self.map[row][col] == 0:
                self.map[row][col] = 1
                self.trees_on_fire_amount -= 1

        # normal trees
        self.amount_of_trees = self.map_size * self.map_size * self.forrest_density
        self.amount_of_trees = int(self.amount_of_trees)
        for i in range(self.amount_of_trees):
            row = rd.randint(0, self.map_size - 1)
            col = rd.randint(0, self.map_size - 1)
            if self.map[row][col] == 0:
                self.map[row][col] = 2

    def spread_fire(self):
        # for i in range(self.map_size):
        #     for j in range(self.map_size):
        #         if self.map[i][j] == 1:
        #             Forest_fire.set_on_fire_around_one(self, i, j)

        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.map[i][j] == 1:
                    self.burning_tree_position_row.append(i)
                    self.burning_tree_position_col.append(j)

        for i in range(len(self.burning_tree_position_row)):
            Forest_fire.set_on_fire_around_one(self, self.burning_tree_position_row[i], self.burning_tree_position_col[i])


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
            Forest_fire.save_png(self, self.time)
            Forest_fire.spread_fire(self)
            self.time += 1


forest_fire = Forest_fire()
forest_fire.main()

