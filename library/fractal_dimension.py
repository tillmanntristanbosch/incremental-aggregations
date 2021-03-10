# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:08:41 2021

@author: Tillmann Tristan Bosch
"""


from numpy import polyfit
from math import log
from math import exp, pi


#try to approximate "full" fractal dimension
def fractal_dimension_approximation_1(particles, ratio_range = [0,1]):
    radius = max([abs(x + y*1j) for x,y in particles])
    min_radius, max_radius = ratio_range[0] * radius, ratio_range[1] * radius
    
    radius_list, cardinal_list = [], []
    
    radius_value = min_radius
    while radius_value < max_radius:
        radius_list.append(radius_value)
        cardinal_list.append(len([(x,y) for (x,y) in particles if abs(x + y*1j) < radius_value]))
        radius_value += 1
        
    x_list = [log(x) for x in radius_list]
    y_list = [log(x) for x in cardinal_list]
    
    if len(x_list) > 0:
        params = polyfit(x_list, y_list, 1)
        return {"parameters":   (params[0], params[1]), #fractal dimension = params[0], volume ratio = e**params[1]
                "x_list":       x_list, 
                "y_list":       y_list}
    else:
        return {"parameters": (0, 0),
                "x_list": [], 
                "y_list": []}
        

#calculate value log(number of particles) / log(last radius)
def last_fractal_dimension_value(particles):
    radius = max(max([abs(x + y*1j) for x,y in particles]), 2)
    return log(len(particles)) / log(radius)

#calculate the volumina ratio \approx (E_\infty \cap B_n) / (\pi n^2)
def volumina_ratio(particles, ratio_range = [0,1]):
    radius = max([abs(x + y*1j) for x,y in particles])
    min_radius, max_radius = ratio_range[0] * radius, ratio_range[1] * radius
    
    radius_list, cardinal_list = [], []
    
    radius_value = min_radius
    while radius_value < max_radius:
        radius_list.append(radius_value)
        cardinal_list.append(len([(x,y) for (x,y) in particles if abs(x + y*1j) < radius_value]))
        radius_value += 1
        
    x_list = [log(x) for x in radius_list]
    y_list = [log(x) for x in cardinal_list]
    
    if len(x_list) > 0:
        bar_c = 1/len(x_list) * sum([y_list[n] - 2 * x_list[n] for n in range(len(x_list))])
        return round(exp(bar_c) / pi, 4)
    else:
        return 0
                    

            
    
        
    