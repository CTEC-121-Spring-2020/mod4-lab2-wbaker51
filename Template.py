"""
CTEC 121
Instructor
Module 4 Lab 2 Demos
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *

def main():
    '''
    startValue = 1
    endValue = 10
    sum = 0
    if startValue % 2 == 1:
        startValue = startValue + 1
    for i in range(startValue, endValue, 2):
        sum = sum + i
    print(sum)
    '''
    # example of setting own coordinates
    win = GraphWin("demo", 800, 800)
    win.setCoords(-4.0, -4.0, 4.0, 4.0)
    p1 = Circle(Point(2, 3), 1)
    p1.setFill("red")
    p1.draw(win)
    p2 = Circle(Point(-3, 1), 1)
    p2.setFill("black")
    p2.draw(win)
    p3 = Circle(Point(-1.5, -2.5), 1)
    p3.setFill("blue")
    p3.draw(win)  

    input()

main()    