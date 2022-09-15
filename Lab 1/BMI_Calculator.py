import sys

### Get the arguments from the command-line except the filename
nameofpythonfile = sys.argv[0]  
units = float(sys.argv[1])      
a = float(sys.argv[2])      
b = float(sys.argv[3])

"""
Check if units = imperial or metric. (if...else...)

Calculate BMI with the corresponding units.
BMI = weight(kg)/height2(m2) (Metric Units)
BMI = 703·weight(lb)/height2(in2) (U.S. Units)

Check BMI category.
"""

### A function to check the BMI category
def BMI_Category(BMI):
        if (BMI <= 15):
            return '\tSevere Thinness'
        elif (16<= BMI <= 17):
            return '\tModerate Thinness'
        ### ...
        ### ...
        ### ...
        elif (BMI > 40):
            return '\tObese Class III'  