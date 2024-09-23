# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
print("Insert your weight in kg")
weight = float(input())
print("Insert your height in m")
height = float(input())


#code here
def bmi_index (weight: float, height: float) -> float:
    if weight <= 0 or height <= 0:
        print('Insert positive values!')
    else:
        return weight / height**2
    
print(bmi_index(weight, height))
