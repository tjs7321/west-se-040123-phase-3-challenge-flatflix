class Movie:

    all = []
    
    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    def __repr__(self):
        return f'(Movie:{self.title})'
    
    def reviews(self):
        from classes.review import Review
        return [rev for rev in Review.all if rev.movie == self]
    
    def reviewers(self):
        from classes.review import Review
        return list(set([rev.viewer for rev in Review.all if rev.movie == self]))
    
    def average_rating(self):
        from classes.review import Review
        ratings = [rev.rating for rev in Review.all if rev.movie == self]
        return sum(ratings)/len(ratings)
    
    @classmethod
    def highest_rated(cls):
        highest_avg = cls.all[0]
        for movie in cls.all:
            if movie.average_rating() > highest_avg.average_rating():
                highest_avg = movie
        return highest_avg

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else: raise Exception('Title must be string greater than 0 characters.')
    
from classes.review import Review
from classes.viewer import Viewer
