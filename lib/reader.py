from lib.review import Review
class Reader:
    
    usernames = []

    def __init__(self, username):
        self.username = username

    # username property goes here!
    def get_username(self):
        return self._username 
    def set_username(self, username):
        if(username not in Reader.usernames):
            if type(username) == str and 16 >= len(username) >= 8:
                self._username = username
                Reader.usernames.append(username)
            else:
                print("please enter valid username")
        else:
            print("user name already exists")
    username = property(get_username, set_username)
    
    def get_reviews(self):
        return [rev for rev in Review.all if rev.reader == self]
        # list of all the reviews by the reader
        # remember that rev.reader is AN OBJECT

    def get_reviewed_books(self):
        return [rev.book for rev in self.get_reviews()]
    
    def reviewed_book(self, book):
        return book in self.get_reviewed_books()

    def rate_book(self, book, rating):
        if self.reviewed_book(book):
            for review in self.get_reviews():
                if(review.get_book() == book):
                    # get_book comes from the Review class
                    review.rating = rating
        else:
            Review(self, book, rating)

    
