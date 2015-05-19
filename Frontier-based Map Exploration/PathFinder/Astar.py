__author__ = 'Ahmed Hani Ibrahim'
from Structures.Cell import Cell
from Structures.Point import Point
from Utilities.Utilities import *


class Astar(object):
    __directions = []
    __path = [[]]
    __source = Cell
    __destination = Cell
    __map = [[]]

    def __init__(self, map):
        self.__map = map
        self.__path = [[0 for j in range(0, len(self.__map[0]))] for i in range(0, len(self.__map))]

    def __initDirections(self):
        self.__directions = [
            Point(1, 0), Point(0, 1), Point(1, 1),
            Point(0, -1), Point(-1, 0), Point(-1, 1),
            Point(1, -1), Point(-1, -1)
        ]

    def aStarPathFinder(self, source, destination):
        self.__initDirections()
        self.__source = source
        self.__destination = destination
        PQ = [0.0 for i in range(0, len(self.__map) * len(self.__map[0]))]
        closeList = [[False for j in range(0, len(self.__map[0]))] for i in range(0, len(self.__map))]
        visited = [[False for j in range(0, len(self.__map[0]))] for i in range(0, len(self.__map))]
        fgh = [[0 for j in range(0, len(self.__map[0]))] for i in range(0, len(self.__map))]

        currentCell = Cell.Cell
        currentCell.position = source
        currentCell.g = 0.0
        currentCell.h = Utilities.getEuclideanDistance(source.position, destination.position)
        currentCell.f = currentCell.g + currentCell.h

        PQ.append(currentCell)
        nextCell = Cell.Cell

        while PQ.__len__() != 0:
            PQ.sort(key=lambda it: it.f, reverse=True)
            currentCell = PQ.pop(0)

            if currentCell.position == destination:
                return self.__getPath(source, destination)

            closeList[currentCell.position.x, currentCell.position.y] = True

            for i in range(0, 8):
                nextCell.position.x = currentCell.position.x + self.__directions[i].x
                nextCell.position.y = currentCell.position.y + self.__directions[i].y

                if visited[nextCell.position.x][nextCell.position.y]:
                    nextCell = fgh[nextCell.position.x][nextCell.position.y]

                if nextCell.position.x >= 0 and nextCell.position.x < len(self.__map) \
                    and nextCell.position.y >= 0 and nextCell.position.y < len(self.__map[0]):

                    if self.__map[nextCell.position.x, nextCell.position.y] != None: #Wall to be handled
                        continue

                    currentG = currentCell.g + self.__map[nextCell.position.x][nextCell.position.y]

                    if self.__isDiagonal(currentCell.position, nextCell.position):
                        currentG += 5 #Heu

                    if closeList[nextCell.position.x][nextCell.position.y] == False:
                        closeList[nextCell.position.x][nextCell.position.y] = True
                        visited[nextCell.position.x][nextCell.position.y] = True
                        self.__path[nextCell.position.x][nextCell.position.y] = currentCell.position
                        nextCell.h = Utilities.getEuclideanDistance(currentCell.position, destination) * 10.0
                        nextCell.g = currentG
                        nextCell.f = nextCell.g + nextCell.h
                        fgh[nextCell.position.x][nextCell.position.y] = nextCell
                        PQ.append(nextCell)

                    elif currentG < nextCell.g:
                        closeList[nextCell.position.x][nextCell.position.y] = True
                        visited[nextCell.position.x][nextCell.position.y] = True
                        PQ.remove(nextCell)
                        nextCell.h = Utilities.getEuclideanDistance(currentCell.position, destination) * 10.0
                        nextCell.g = currentG
                        nextCell.f = nextCell.g + nextCell.h
                        fgh[nextCell.position.x][nextCell.position.y] = nextCell
                        PQ.append(nextCell)
                        self.__path[nextCell.position.x][nextCell.position.y] = currentCell.position

            return None

    def __getPath(self, source, destination):
        resultedPath = []
        currentPoint = Point

        while currentPoint != source:
            resultedPath.append(currentPoint)
            currentPoint = self.__path[currentPoint.x, currentPoint.y]

        resultedPath = resultedPath.reverse()

        return resultedPath

    def __isDiagonal(self, nextPoint, currentPoint):
        return True if ((nextPoint.y < currentPoint.y and nextPoint.x > currentPoint.x)
                        or (nextPoint.y < currentPoint.y and nextPoint.X < currentPoint.X)
                        or (nextPoint.y > currentPoint.y and nextPoint.X > currentPoint.X)
                        or (nextPoint.y > currentPoint.y and nextPoint.X < currentPoint.X)) else False
