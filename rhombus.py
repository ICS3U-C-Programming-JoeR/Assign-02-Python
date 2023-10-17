#!/usr/bin/env python3
# Created by: Joe Rugezo
# Created on: oct. 11, 2023
# This program asks the user for three side and then t calculates the area of two of the three sides 
#and the perimeter of the other side

import math

def main():
    # input
    print("Today we will calculate the area and")
    print("perimeter of a rhombus")
    side_q = int(input("Enter side Q : "))
    side_p = int(input("Enter side P : "))
    side_a = int(input("Enter side A : "))
    john = input("Enter unit of measurement: ")
    # process
    area = side_p * side_q / 2
    perimeter = 4 * side_a 

    # output
    print("")
    print ("Area = {} {}^2". format (area,john))
    print ("Perimeter = {} {}". format (perimeter,john))


if __name__ == "__main__":
  main()