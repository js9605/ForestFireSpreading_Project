from scipy.misc import imsave
import numpy
import random as rd


# IDEAS
# - add feature where you can create non - square maps
# https://github.com/rafibarash/forest-fire/blob/master/README.md     GOOD EXAMPLE
# poczytaj: turtle graphics
# poczytaj numpy do tego projektu


class Forest_fire:
    # black - tree
    # grey - tree on fire
    # white - empty space


    def __init__(self):
        self.forrest_density = 0.9
        self.map_size = 10
        self.time_limit = 5
        self.map = []
        self.trees_on_fire_amount = 5
        self.time = 0

    def create_map(self):
        for i in range(self.map_size):
            self.map.append([])
            for j in range(self.map_size):
                self.map[i].append(2)

    def create_forest(self):
        #trees on fire
        for i in range(self.trees_on_fire_amount):
            row = rd.randint(0,self.map_size - 1)
            col = rd.randint(0,self.map_size - 1)
            if self.map[row][col] == 2:
                self.map[row][col] = 1

        # normal trees
        self.amount_of_trees = self.map_size * self.map_size * self.forrest_density
        self.amount_of_trees = int(self.amount_of_trees)
        for i in range(self.amount_of_trees):
            row = rd.randint(0, self.map_size - 1)
            col = rd.randint(0, self.map_size - 1)
            if self.map[row][col] == 2:
                self.map[row][col] = 0

        # density
        # wind
        # how many trees in fire
        # is there a road?   (one line from top to bot or left to right)

    def spread_fire(self):
        for self.time in range(self.time_limit):

            self.time += 1

    def show_map(self):
        for i in range(len(self.map)):
            print(self.map[i])

    def save_png(self):
        self.time = str(self.time)
        name = 'forrest_fire_' + self.time + ".png"
        imsave(name, self.map)

forest_fire = Forest_fire()
forest_fire.create_map()
forest_fire.create_forest()
forest_fire.show_map()
forest_fire.save_png()

