#!/usr/bin/env python3
import ipdb;

from lib.book import Book
from lib.reader import Reader
from lib.review import Review


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    b1 = Book("Book1")
    b2 = Book("Book2")
    b3 = Book("Book3")
    r1 = Reader("r1")
    r2 = Reader("r2")
    re1 = Review(r1, b1, 2)
    re2 = Review(r1, b2, 5)
    re3 = Review(r2, b1, 3)
    re4 = Review(r2, b2, 1)






# DO NOT REMOVE THIS
    ipdb.set_trace()
