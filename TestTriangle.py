# -*- coding: utf-8 -*-
"""


@author: Arjun Khatri
I pledge my honor that I have abided by the Stevens Honor System 
"""
import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(4,2,3),'Scalene','4,2,3 is a Scalene triangle')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,3),'Isosceles','5,5,3 is an Isosceles triangle')
        
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(4,6,6),'Isosceles','4,6,6 is an Isosceles triangle')
    
    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(1,10,12),'NotATriangle','1,10,12 cannot form a triangle')
    
    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle','10,1,1 cannot form a triangle')
        
    def testInvalidInputs(self): 
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','Negative numbers are not valid inputs')
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','Zero is not a valid input')
        self.assertEqual(classifyTriangle(0.5,1,1),'InvalidInput','Floats are not valid inputs')
        self.assertEqual(classifyTriangle(3e300,3e300,3e300),'InvalidInput','Extremely large numbers are not valid inputs')

    def testBoundaryCase(self): 
        self.assertNotEqual(classifyTriangle(3,4,6),'Right','3,4,6 is close but not a Right triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

