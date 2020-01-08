import unittest
from functools import reduce
from src.BubbleSort import BubbleSort


class MyTestCase(unittest.TestCase):

    def test_BubbleSort_integrity(self):
        """
        Tests if the collection contains the same members after the bubble sort
        """
        #stub
        stub1 = [1,2,3,4,2,1,2,34,45,32,12,4]
        stub2 = [13, 22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41]
        stub3 = [123, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41]

        #check integrity func
        def Check_Integrity(alist,blist):
            return all(x in alist for x in blist)
        #test
        self.assertTrue(Check_Integrity(BubbleSort(stub1),stub1))
        self.assertTrue((Check_Integrity(BubbleSort(stub2),stub2)))
        self.assertTrue(Check_Integrity(BubbleSort(stub3),stub3))

    def test_BubbleSort_sorted(self):
        """
        tests if the bubblesort sorts the collection
        """
        #stub
        stub1 = [1,2,-3,4,2,1,2,34,45,32,12,4]
        stub2 = [13, -22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41]
        stub3 = [-122, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41]

        #tester function
        def TestSorted(alist):
            return reduce(lambda x,y:x>y,alist)is False # if all the values are false it's sorted if one is true the array is not sorted.

        #test
        self.assertTrue(TestSorted(BubbleSort(stub1)))
        self.assertTrue(TestSorted(BubbleSort(stub2)))
        self.assertTrue(TestSorted(BubbleSort(stub3)))

    def test_BubbleSort_value(self):
        """
        tests if the bubblesort returns any value
        """
        #stub
        stub1 = [1,2,-3,4,2,1,2,34,45,32,12,4]
        stub2 = [13, -22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41]
        stub3 = [-122, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41]

        #test
        self.assertTrue(BubbleSort(stub1))
        self.assertTrue(BubbleSort(stub2))
        self.assertTrue(BubbleSort(stub3))








if __name__ == '__main__':
    unittest.main()
