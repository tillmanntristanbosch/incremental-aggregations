# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:19:52 2021

@author: Tillmann Tristan Bosch

Here basic geometrical features are provided which are needed in the simulation of the line hitting aggregation. 
"""

from math import sin, cos


class Segment:
    
    def __init__(self, A = 0, B = 1):
        self.A = A
        self.B = B
        
        
class Polygon:
    
    def __init__(self, vertices = [0, 1, 1j, 1+1j]):
        self.vertices = vertices
        self.segments = self.init_segments()
        
    def init_segments(self):
        segments = []
        l = len(self.vertices)
        for k in range(l):
            segments.append(Segment(self.vertices[k], self.vertices[(k+1) % l]))
        return segments
        

class Line:
    
    def __init__(self, parameters = (0,0)):
        
        """
        We use the following representation of points on the line: 
        
        For an angle alpha in [0,pi) we define e_alpha = (cos(alpha), sin(alpha)) and f_alpha = (-sin(alpha), cos(alpha)).
        e_alpha and f_alpha form a base of the real plane and evolve by turning the standard base (1,0), (0,1) by alpha counterclockwise.
        For any x in the real plane we can therefore write x = <x, e_alpha> * e_alpha + <x, f_alpha> * f_alpha where <.,.> is the standard 
        scalar product. The parameters <x, e_alpha> and <x, f_alpha> are unique since e_alpha and f_alpha is a base of the plane. 
        
        The line with parameters (alpha, p) shall be consist of all elements x where <x, e_alpha> = p. The identification of lines
        with such a pair of parameters is unique. 
        """        
        
        self.alpha = parameters[0]
        self.p = parameters[1]
        
    
    def intersects_with_segment(self, segment):
        
        """
        With the representation of points as described above we can determine easily whether a line intersects a segment AB or not.
        A line g intersects AB iff A lies "over" g and B "under" g or the other way around. This can be equivalently stated by:
            
        g interesects segment AB iff (<A,e_alpha> >= p and <B,e_alpha> <= p) or (<A,e_alpha> <= p and <B,e_alpha> >= p)
        """
        
        cos_alpha = cos(self.alpha)
        sin_alpha = sin(self.alpha)
        A_alpha = segment.A.real * cos_alpha + segment.A.imag * sin_alpha # <A,e_alpha>
        B_alpha = segment.B.real * cos_alpha + segment.B.imag * sin_alpha # <B,e_alpha>
        
        if (A_alpha >= self.p and B_alpha <= self.p) or (A_alpha <= self.p and B_alpha >= self.p):
            return True
        return False
    
    
    def intersects_with_polygon(self, polygon):
        for segment in polygon.segments:
            if self.intersects_with_segment(segment):
                return True
        return False

    
    
    
    
    