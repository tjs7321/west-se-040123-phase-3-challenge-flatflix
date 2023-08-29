class Review:

    all = []
    
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.all.append(self)

    def __repr__(self):
        return f'(Reviewer:{self.viewer}, Movie:{self.movie}, Rating:{self.rating})'

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else: raise Exception('Viewer must be viewer instance.')

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else: raise Exception('Movie must be movie instance.')

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        else: raise Exception('Rating must be integer between 1 and 5, inclusive.')
    
from classes.movie import Movie
from classes.viewer import Viewer