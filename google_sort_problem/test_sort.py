import unittest
import sort

class Test(unittest.TestCase):


    def testSorted(self):
        A = [1, 2, 3, 4, 5]
        actual, cost = sort.sort(A)
        self.assertEquals(actual, A)
        self.assertEquals(cost, 0)

    def testSample(self):
        A = [4, 5, 2, 1, 3]
        actual, cost = sort.sort(A)
        self.assertEquals(actual, [3,3,3])
        self.assertEquals(cost, 6)


    def test_keep10(self):
        A = [10, 1, 1, 1, 1]
        actual, cost = sort.sort(A)
        self.assertEquals(actual, [10])
        self.assertEquals(cost, 4)


    def test_remove10(self):
        A = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        actual, cost = sort.sort(A)
        self.assertEquals(actual, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEquals(cost, 9)


if __name__ == "__main__":
    unittest.main()
