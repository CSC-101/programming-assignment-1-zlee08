import data
import math

from data import Circle, Point, Book


class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents
# Write your functions for each part in the space below.

# Part 1
def vowel_count(my_string):
    letters = [x for x in my_string if x in 'aeiouAEIOU']
    number_of_vowel = len(letters)
    return number_of_vowel

# Part 2
def short_list(my_list):
    list1=[x for x in my_list if len(x) == 2]
    return list1

# Part 3
def ascending_pairs(my_list):
    new_list = []
    for ls in my_list:
        if len(ls) == 2:
            ls.sort()
        new_list.append(ls)
    return new_list

# Part 4
def add_prices(p1, p2):
    return Price(p1.dollars + p2.dollars + (p1.cents + p2.cents) // 100,
                 (p1.cents + p2.cents) % 100)

# Part 5
def rectangle_area(my_rect):
    area = (my_rect.top_left.y - my_rect.bottom_right.y) * (my_rect.bottom_right.x - my_rect.top_left.x)
    return area


# Part 6
def books_by_author(author: str, books: list[Book]) -> list[Book]:
    author_books: list[Book] = []
    for book in books:
        for cur_author in book.authors:
            if cur_author == author:
                author_books.append(book)
    return author_books

# Part 7
def circle_bound(my_rect):
    circle = Circle((Point({},{})),{})
    circle.center.y = (my_rect.top_left.y + my_rect.bottom_right.y) / 2
    circle.center.x = (my_rect.bottom_right.x + my_rect.top_left.x) / 2
    circle.radius =  math.sqrt(((circle.center.x - my_rect.top_left.x) ** 2) + ((circle.center.y - my_rect.bottom_right.y) ** 2))
    return circle

# Part 8
def below_pay_average(my_list):
    if not my_list:
        #return "list is empty"
        return []
    else:
        average = sum(x.pay_rate for x in my_list) / len(my_list)
        #print("average is " + str(average))
        emp = [x for x in my_list if x.pay_rate < average]
        return emp

