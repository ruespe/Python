import os, sys, math
from math import *
import json

PI=3.14159

class calculator:
    def __init__(self, name): self.name=name

    def Add(self,a,b):
      return a+b

def compute_circle_area(radius): return PI*radius*radius

def print_info(calc):

    print("Calculator:",calc.name)

unused_variable = 42

def divide(a,b):
    if b==0:
        return None
    return a/b

def main():
    c=calculator("Prova")
    print_info(c)
    print("Area",compute_circle_area(5))
    print("Sum:",c.Add(2,3))
    print("Div:",divide(4,0))

if __name__=="__main__": main()

