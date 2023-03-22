from lib.review import Review

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        # self.set_title(title)
        Book.all.append(self)

    # title property goes here!
    def get_title(self):
        return self._title 
    def set_title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            print("please enter valid title")
    title = property(get_title, set_title)

    def average_rating(self):
        ratings = [rev.get_rating() for rev in Review.all if rev.get_book() == self]
   
        if len(ratings) == 0:
            return 0
        
        return sum(ratings)/ len(ratings)

    @classmethod
    def highest_rated(cls):
        result=[]
        for book in cls.all:
            result.append(book.average_rating())
        return [book.title for book in cls.all if book.average_rating() == max(result)]
    



        

