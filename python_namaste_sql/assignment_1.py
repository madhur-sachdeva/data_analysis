# input function
# name=input("enter your name: ")
# print(name)
# -----------------------------------------------------
# 1- write a program which takes 2 inputs from the user : 
# weight(kg) and height(meter) and prints the BMI in the output.

# BMI = weight / (square of height)

weight = int(input())
height = float(input()) # in meters

BMI = weight / (height * height)
print(round(BMI,2))

# -----------------------------------------------------

