import unittest


class MyTestCase(unittest.TestCase):

    def test_BubbleSort_integrity(self):
        """
        Tests if the collection contains the same members after the bubble sort
        """
        #stub
        stub1 = (1,2,3,4,2,1,2,34,45,32,12,4)
        stub2 = (13, 22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41)
        stub3 = (123, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41)

        #expected result
        expected1= {stub1} #put the stub in set
        expected2= {stub2}
        expected3 = {stub3}
        #test
        self.assertSetEqual({BubbleSort.sort(stub1)},expected1)
        self.assertSetEqual({BubbleSort.sort(stub2)},expected2)
        self.assertSetEqual({BubbleSort.sort(stub3)},expected3)

    def test_BubbleSort_sorted(self):
        """
        tests if the bubblesort sorts the collection
        """
        #stub
        stub1 = (1,2,-3,4,2,1,2,34,45,32,12,4)
        stub2 = [13, -22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41]
        stub3 = [-122, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41]

        #expected result
        expected1= sorted(stub1)#put the stub in set
        expected2= sorted(stub2)
        expected3 = sorted(stub3)
        #test
        self.assertSetEqual(BubbleSort.sort(stub1),expected1)
        self.assertSetEqual(BubbleSort.sort(stub2),expected2)
        self.assertSetEqual(BubbleSort.sort(stub3),expected3)

    def test_BubbleSort_value(self):
        """
        tests if the bubblesort returns any value
        """
        #stub
        stub1 = (1,2,-3,4,2,1,2,34,45,32,12,4)
        stub2 = [13, -22, 31, 412, 24, 13, 22, 12, 45, 32, 12, 41]
        stub3 = [-122, 212, 313, 412, 24, 153, 262, 172, 415, 32, 12, 41]

        #expected result
        expected1= sorted(stub1)#put the stub in set
        expected2= sorted(stub2)
        expected3 = sorted(stub3)
        #test
        self.assertTrue(BubbleSort.sort(stub1),expected1)
        self.assertTrue(BubbleSort.sort(stub2),expected2)
        self.assertTrue(BubbleSort.sort(stub3),expected3)








if __name__ == '__main__':
    unittest.main()
