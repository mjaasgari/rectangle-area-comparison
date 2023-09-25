# Author: Mohammad Javad Asgari Pirbalouti
# Student Number: 80787336
# Source File Name: rectangle_area_comparison.py
# Source File Purpose: Calculate and compare the areas of two rectangles.
# Source File Description:

# This Python script defines variables for the length and width of two rectangles, calculates their areas,
# and compares the areas to determine if they are equal. The goal of this script is to demonstrate how to
# work with variables and expressions without using if statements or loops. It follows the following steps:

# 1. Define variables for the length and width of two rectangles (rect1 and rect2).
# 2. Calculate the area of each rectangle using the formula: area = length * width.
# 3. Compare the areas of the two rectangles to check if they are equal and store the result in a boolean variable.
# 4. Print the areas of both rectangles and whether their areas are equal or not.

# Note: In this process none of the if statements or loops have been used.

# -----------------------------------------------------------------------------------------------------------------

# def main() ?????

# Step 1: Define variables for the length and width of two rectangles
length_rect1 = 2.0
width_rect1 = 9.0

length_rect2 = 6.0
width_rect2 = 3.0

# Step 2: Calculate the area of both rectangles
area_rect1 = length_rect1 * width_rect1
area_rect2 = length_rect2 * width_rect2

# Step 3: Define a boolean variable to compare the areas
are_areas_equal = area_rect1 == area_rect2

# Step 4: Print the areas and the boolean value
print("Area of Rectangle 1:", area_rect1)
print("Area of Rectangle 2:", area_rect2)
print("Are the areas equal?", are_areas_equal)
