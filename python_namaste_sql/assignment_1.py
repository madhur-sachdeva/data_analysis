# input function
# name=input("enter your name: ")
# print(name)
# -----------------------------------------------------
# 1- write a program which takes 2 inputs from the user : 
# weight(kg) and height(meter) and prints the BMI in the output.

# BMI = weight / (square of height)

# weight = int(input())
# height = float(input()) # in meters

# BMI = weight / (height * height)
# print(round(BMI,2))

# -----------------------------------------------------

# 2- write a program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b' and print it.

# name = input()
# name = name.replace('a','b')
# print(name)

# -----------------------------------------------------

# 3- write a program which takes 2 inputs from user as principle amount (int) 
# and rate of annual interest (float) and print the expected total amount  after  2 years.

# amount = int(input())
# interest = float(input())

# total_amount = amount * (1 + (interest / 100)) ** 2
# print(total_amount)


# -----------------------------------------------------

# 4- write a program which takes city name from user input. 
# irrespective of in which case user enters the city name, print the city name in camel case 
# meaning first letter should be capital and rest in small.

# example : input : MYSORE ,  print - > Mysor

# city = input()

# print(city.capitalize())

# -----------------------------------------------------
# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string. 
# if 'a' is not there then return -1.

# test = input()
# check = test.find('a')
# print(f"Index of 'a': {check}")

# -----------------------------------------------------
# 6-  Display the number of letters in the below string
# my_word = "antidisestablishmentarianism"

# print(len(my_word))

# -----------------------------------------------------
# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple 
# first name : MOhit
# last name : sharma 
# age 32


f = input("first name : ")
l = input("last name : ")
# a = input()
c = input("company name : ")

# print(f"first name : {f.capitalize()}\nlast name : {l.capitalize()}\nage {a}")
# print("Display: My name is", f.capitalize(), l.capitalize(), "and I am", a, "years old.")

# -----------------------------------------------------

# 8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example 
# first name : MOhit
# last name : sharma 
# company : infosys

# Display : morma@infosys.com 

# note full email id should -be in lower case


# using previous variables

# print(f"email : {f[0:2].lower()}{l[-3:].lower()}@{c.lower()}.com")



