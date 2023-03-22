from review import Review
class Book:
    
    def __init__(self, title):
        self.title = title
        # self.set_title(title)

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
        return sum(ratings)/ len(ratings)

    @classmethod
    def highest_rated(cls):
        reviews = Review.reviews
        max_review = reviews[0]
        for review in reviews:
            if(review.rating > max_review.rating):
                max_review = review 

