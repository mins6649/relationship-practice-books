
class Review:

    all = []
    
    def __init__(self, reader, book, rating):
        self.reader = reader
        self.book = book
        self.rating = rating
        Review.all.append(self)

    # rating property goes here!
    def get_rating(self):
        return self._rating 
    def set_rating(self, rating):
        if type(rating) == int and 5 >= rating >= 1:
            self._rating = rating
        else:
            print("please enter valid rating")
    rating = property(get_rating, set_rating)

    # reader property goes here!
    def get_reader(self):
        return self._reader
    def set_reader(self, reader):
        from lib.reader import Reader
        if(isinstance(reader,Reader)):
            self._reader= reader
    reader = property(get_reader, set_reader)

    # book property goes here!
    def get_book(self):
        return self._book
    def set_book(self, book):
        from lib.book import Book
        if(isinstance(book,Book)):
            self._book= book
    book = property(get_book, set_book)
