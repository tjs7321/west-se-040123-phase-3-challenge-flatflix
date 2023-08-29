class Viewer:

    all = []

    all_usernames = []
    
    
    def __init__(self, username):
        self.username = username
        Viewer.all.append(self)
        Viewer.all_usernames.append(username)

    def __repr__(self):
        return f'(Viewer:{self.username})'
    
    def reviews(self):
        from classes.review import Review
        return [rev for rev in Review.all if rev.viewer == self]
    
    def reviewed_movies(self):
        from classes.review import Review
        return [rev.movie for rev in Review.all if rev.viewer == self]

    def has_reviewed_movie(self, movie):
        from classes.review import Review
        for rev in Review.all:
            if rev.viewer == self and rev.movie == movie:
                return True

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if username in Viewer.all_usernames:
            raise Exception('Username already taken.')
        elif isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username
        else: raise Exception('Username must be string between 6 and 16 characters, inclusive.')

from classes.review import Review
from classes.movie import Movie