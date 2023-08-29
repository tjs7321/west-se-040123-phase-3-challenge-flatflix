#!/usr/bin/env python3
import ipdb
from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer




if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    jim = Viewer('jimmin')
    jam = Viewer('jammin')
    shawshank = Movie('Shawshank Redemption')
    jaws = Movie('Jaws')
    rev1 = Review(jim, shawshank, 5)
    rev2 = Review(jim, jaws, 5)
    rev3 = Review(jim, shawshank, 5)
    rev4 = Review(jim, shawshank, 4)
    rev5 = Review(jim, shawshank, 5)
    rev6 = Review(jim, shawshank, 2)
# DO NOT REMOVE THIS
    print("uncomment ipdb lines if you want to use them")
    ipdb.set_trace()
