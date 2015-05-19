__author__ = 'Ahmed Hani Ibrahim'
import math
from Structures import Cell


class Utilities():

    @classmethod
    def getEuclideanDistance(self, source, destination):
        return math.sqrt((source.x * source.x) + (source.y * source.y))