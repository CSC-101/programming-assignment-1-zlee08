import data
import hw1
import unittest

from data import Rectangle, Point, Circle, Employee, Book
from hw1 import Price


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        input1 = "what"
        result = hw1.vowel_count(input1)
        expected = 1
        self.assertEqual(expected, result)

    def test_vowel_count2(self):
        input2 = "Cal Poly"
        hw1.vowel_count(input2)

    # Part 2
    def test_short_lists1(self):
        input1 = [[1,2],[0,1,2],[0,1,2,3]]
        result = hw1.short_list(input1)
        expected = [[1,2]]
        self.assertEqual(expected, result)

    def test_short_lists2(self):
        input2 = [[1,2],[0,1,2],["a","b"],[1],[1,2,3,4]]
        result = hw1.short_list(input2)
        expected = [[1,2],['a','b']]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs1(self):
        input1 = [[2, 1], [0, 1, 2], ["b", "a"], [1], [4,2,1,3]]
        result = hw1.ascending_pairs(input1)
        expected = [[1, 2], [0, 1, 2], ["a", "b"], [1], [4,2,1,3]]
        self.assertEqual(expected, result)

    def test_ascending_pairs2(self):
        input2 = [[2,1],[0,1,2]]
        result = hw1.ascending_pairs(input2)
        expected = [[1, 2], [0, 1, 2]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices1(self):
        input1 = (Price(1,45), Price(0,70))
        result = hw1.add_prices(input1[0], input1[1])
        expected = Price(2,15)
        self.assertEqual((expected.dollars, expected.cents), (result.dollars, result.cents))

    def test_add_prices2(self):
        input2 = (Price(1,45), Price(0,30))
        result = hw1.add_prices(input2[0], input2[1])
        expected = Price(1,75)
        self.assertEqual((expected.dollars, expected.cents), (result.dollars, result.cents))

    # Part 5
    def test_rectangle_area1(self):
        input1 = Rectangle(Point(1,4), Point(2,2))
        result = hw1.rectangle_area(input1)
        expected = 2
        self.assertEqual(expected, result)

    def test_rectangle_area2(self):
        input2 = Rectangle(Point(0.5,5), Point(2.5,3))
        result = hw1.rectangle_area(input2)
        expected = 4.0
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author1(self):
        input = ("Tim", [Book(["Tim", "Tom"], "Book 1"),
                        Book(["Tim", "Jim"], "Book 2"),
                        Book(["Bob", "Emily"], "Book 3")])
        result = hw1.books_by_author(input[0], input[1])
        expected = [input[1][0], input[1][1]]
        self.assertEqual(expected, result)

    def test_books_by_author2(self):
        input = ("Rose", [Book(["Tim", "Tom"], "Book 1"),
                         Book(["Tim", "Jim"], "Book 2"),
                         Book(["Bob", "Emily"], "Book 3")])
        result = hw1.books_by_author(input[0], input[1])
        expected = []
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound1(self):
        input1 = Rectangle(Point(1,4),Point(2,2))
        result = hw1.circle_bound(input1)
        expected = Circle(Point(1.5,3.0), 1.118033988749895)
        self.assertEqual(expected, result)

    def test_circle_bound2(self):
        input2 = Rectangle(Point(0,0), Point(2,2))
        result = hw1.circle_bound(input2)
        expected = Circle(Point(1.0,1.0), 1.4142135623730951)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average1(self):
        input1 = [Employee("E1", 15),Employee("E2",14),
                  Employee("E3", 15),Employee("E3",15),
                  Employee("E4",15),Employee("E5",15),
                  Employee("E6",15)]
        result = hw1.below_pay_average(input1)
        #expected = "average is 14.857142857142858",
        expected = [Employee("E2",14)]
        self.assertEqual(expected, result)

    '''
    def test_below_pay_average2(self):
        input2 = [Employee("E1",15), Employee("E2",14),
                  Employee("E3",15),Employee("E3",15),
                  Employee("E4",14),Employee("E5",15),
                  Employee("E6",15),]
        result = hw1.below_pay_average(input2)
        #expected = ("average is 14.714285714285714",
        expected = [Employee('E2', 14), Employee('E4', 14)]
        self.assertEqual(expected, result)
    '''
    def test_below_pay_average2(self):
        input2 = []
        result = hw1.below_pay_average(input2)
        expected = []
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
