import unittest
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

    # tester function
    @staticmethod
    def TestSorted(alist):
        """
        checks if a collection is sorted
        :param alist: a list
        :return: true if the collection is sorted in ascending order false otherwise.
        """
        return all(alist[i] <= alist[i+1] for i in range(len(alist)-1))

    def test_BubbleSort_sorted(self):
        """
        tests if the bubblesort sorts the collection
        """
        #stub
        stub1 = [1,2,-3,4,2,1,2,34,45,32,12,4]
        stub2 = [13, -22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41]
        stub3 = [-122, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41]

        #test
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub1)))
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub2)))
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub3)))

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

    def test_BubbleSort_Letters(self):
        """
        Test to see if it works with letters
        """
        stub1= list("Hello World")
        stub2= ["ab","acc","tea","fish"]
        stub3= list("")
        stub4= list("zyxwvutsrqponmlkjihgfedcba")

        # test
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub1)))
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub2)))
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub3)))
        self.assertTrue(MyTestCase.TestSorted(BubbleSort(stub4)))

    def test_BubbleSort_Zeros(self):
        """
        Test if the function works with zeros
        """
        stub1=[0]
        stub2=[1,0,-1]
        stub3=[0,0,0,0,0,0,0,0,0,-5]

        #expected results
        expected1=[0]
        expected2=[-1,0,1]
        expected3=[-5,0,0,0,0,0,0,0,0,0]
        #tests:
        self.assertEqual(BubbleSort(stub1),expected1)
        self.assertEqual(BubbleSort(stub2), expected2)
        self.assertEqual(BubbleSort(stub3), expected3)







if __name__ == '__main__':
    unittest.main()
