"""
Handles 2D Vectors

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import math

class Vector2D():

    def __init__(self, xParam, yParam):
        """
        Initialize variables.
        """
        self.x = float(xParam)
        self.y = float(yParam)




    def magnitude(self):
        """
        Return the magnitude of the vector.
        """
        return float(math.sqrt(self.x**2 + self.y**2))




    def normalized(self):
        """
        Return a Vector2D which is the vector normalized.
        """
        mag = self.magnitude()
        if (mag == 0):
            return Vector2D(self.x, self.y)
        return Vector2D(self.x/mag, self.y/mag)




    def mulscalar(self, scalar):
        """
        Return a Vector2D which is the vector scaled by some floating point value "scalar".
        """
        return Vector2D(self.x * scalar, self.y * scalar)




    def getX(self):
        """
        Return the x-axis component of this vector.
        """
        return self.x




    def getY(self):
        """
        Return the y-axis component of this vector.
        """
        return self.y




    def __mul__(self, num):
        """
        Overloads the multiply operator.

        @param num: The scalar quality to multiply by.
        """
        return Vector2D(self.x * num, self.y * num)



