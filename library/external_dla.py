# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:16:52 2021

@author: Tillmann Tristan Bosch

Here you find an implementation of external dla. Note that it is not claimed that this simulation is close to its original mathematical definition. 
"""

import cmath
import random
from math import pi

import incremental_aggregation as ia


class External_DLA(ia.Incremental_Aggregation):
    def __init__(self):
        super().__init__()

        self.init_surround_circle()
        self.isnotnear_counter = 0
        
        
    def run_process(self, iterations):
        for k in range(iterations):
            new_position = self.get_next_particle(self.get_random_start_position())

            self.particles.append(new_position)
            self.actualize_cluster_radius()
            self.actualize_boundary_set()

            self.actualize_surround_circle()

            print(k)
        print("number of notnear: " + str(self.isnotnear_counter))


    def get_next_particle(self, position):
        isnear_counter = 0
        while True:
            if position in self.boundary_set:
                return position
            else:
                position = random.choice(self.get_neighbours(position))

            if isnear_counter == self.cluster_radius // 2:
                if not self.isNear(position):
                    position = self.get_random_start_position()
                    self.isnotnear_counter += 1
                isnear_counter = 0
            else:
                isnear_counter += 1

    
    # start position of the next random walk
    def get_random_start_position(self):
        radius = self.surround_circle["radius"]
        startpos = cmath.rect(radius, random.random() * 2 * pi)
        return int(startpos.real) + int(startpos.imag) * 1j


    def init_surround_circle(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0

        # how far shall be the surround_circle be away of the outest particles?
        self.helpSpaceDelta = 40
        # this a circle closely around the cluster
        self.surround_circle = {
            "middlePoint": self.particles[0], "radius": self.helpSpaceDelta}


    def actualize_surround_circle(self):
        x, y = self.particles[-1].real, self.particles[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY = min(self.minY, y), max(self.maxY, y)

        self.surround_circle["middlePoint"] = (self.minX + self.maxX) / 2 + ((self.minY + self.maxY) / 2) * 1j
        dx, dy = self.maxX - self.minX, self.maxY - self.minY
        self.surround_circle["radius"] = abs(dx + dy * 1j) / 2 + self.helpSpaceDelta


    def isNear(self, pos):
        return abs(pos) < self.surround_circle["radius"] + 5


