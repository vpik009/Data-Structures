import unittest
from non_comparison_sorts import *
import random
# class TestRadix(unittest.TestCase):

#     def test_radix(self):
#         test1 = [5,4,3,2,1,0]
#         result1 = [0,1,2,3,4,5]
#         self.assertEqual(radix(test1),result1)


#         test2 = [1242342,1243,764567,556,86,2364]
#         result2 = [86,556,1243,2364,764567,1242342]
#         self.assertEqual(radix(test2),result2)

#         test3 = [32,45,34,23,12]
#         result3 = [12,23,32,34,45]
#         self.assertEqual(radix(test3),result3)

#     def test_best_interval(self):
#         self.assertEquals(best_interval([1, 5, 6], 5),(1, 3))  # (0 - 5) contains 2 items but (1 - 6) contains 3 items
#         self.assertEquals(best_interval([1, 5, 5], 5),(0, 3))  # (0 - 5) contains 3 items
#         self.assertEquals(best_interval([1, 5], 5),(0, 2))  # (0 - 5) contains 2 items
#         self.assertEquals(best_interval([1], 5) , (0, 1))  # (0 - 1) contains 1 items
#         self.assertEquals(best_interval([1], 1) ,(0, 1))  # (0 - 1) contains 1 items
#         self.assertEquals(best_interval([1, 2, 3, 4, 5, 6, 7], 0),(1, 1))
#         self.assertEquals(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 5) , (0, 5))
#         self.assertEquals(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 6) ,(1, 6))
#         self.assertEquals(best_interval([], 6) ,(0, 0))
#         self.assertEquals(best_interval([0], 2),(0, 1))
#         self.assertEquals(best_interval([0], 1) ,(0, 1))
#         self.assertEquals(best_interval([0], 4) , (0, 1))
#         self.assertEquals(best_interval([0, 2, 3], 4), (0, 3))
#         self.assertEquals(best_interval([0, 2, 3], 0),(0, 1))
#         self.assertEquals(best_interval([0], 0),(0, 1))
#         self.assertEquals(best_interval([1], 1),(0, 1))
#         self.assertEquals(best_interval([0], 1),(0, 1))
#         self.assertEquals(best_interval([0, 0, 0, 0, 0], 1),(0, 5))  #######
#         self.assertEquals(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10, 11, 11, 11, 12, 11, 11, 11, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16], 5),(10,21))
#         self.assertEquals(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10],11),(0,9))
#         self.assertEquals(best_interval([1,1,1,1,1,1,1,1], 0),(1, 8))
#         self.assertEquals(best_interval([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2], 0),(2, 10))

class q1(unittest.TestCase):

    ### basic test cases that teacher went through:
    def test1(self):
        transactions, t = [2, 4, 4, 4, 6, 10], 3
        res = best_interval(transactions, t)
        assert res == (1,4), str(res)
    
    def test2(self):
        transactions, t = [7,3,1,9,14,7], 9
        res = best_interval(transactions, t)
        assert res == (0,5), str(res)
    
    def test3(self):
        transactions, t = [5,7,9,11,11,15], 4
        res = best_interval(transactions, t)
        assert res == (7,4), str(res)

    def test4(self):
        ## if this returns (8,4) make sure your best_t is coded properly!
        transactions, t = [5,8,9,11,11,15], 4
        res = best_interval(transactions, t)
        assert res == (7,4), str(res)

    ## stolen from ed https://edstem.org/courses/5287/discussion/401560
    def test5(self):
        transactions, t = [11,11,11,11,11,11,10,10,5], 2
        res = best_interval(transactions, t)
        assert res == (9,8), str(res)
    
    def test6(self):
        transactions, t = [9,9,9,9,9,9,9,9,10,10], 6
        res = best_interval(transactions, t)
        assert res == (4,10), str(res)

    ## testing tiny cases
    def test7(self):
        transactions, t = [], 0
        res = best_interval(transactions, t)
        assert res == (0,0), str(res)
    
    def test8(self):
        transactions, t = [0,0,0],0
        res = best_interval(transactions, t)
        assert res == (0,3), str(res)

    def test9(self):
        transactions,t = [], 10
        res = best_interval(transactions, t)
        assert res == (0,0), str(res)

    ## random big numbers 
    def test10(self):
        random.seed(10)
        transactions, t = random.sample(range(1, 9999), 100), 900
        res = best_interval(transactions, t)
        assert res == (6679, 16), str(res)

    def test11(self):
        random.seed(10)
        transactions, t = random.sample(range(100,99999),1000), 300
        res = best_interval(transactions, t)
        assert res == (55080, 11), "attempt: " + str(res)
   
    # no-negatives
    def test12(self):
        # should not be (-1,3)
        transactions, t = [1,1,1,4,7,10,13], 2
        res = best_interval(transactions, t)
        assert res == (0,3), str(res)

	#single value
    def test13(self):
        random.seed(10)
        transactions, t = random.sample(range(2,10000), 1000), 0        
        res = best_interval(transactions, t)
        assert res == (20,1), str(res) 

    ## blackhole
    def test14(self):
        transactions, t = [30, 40, 50], 0
        res = best_interval(transactions, t)
        assert res == (30, 1), str(res)



if __name__ == "__main__":
    unittest.main() # run all tests




