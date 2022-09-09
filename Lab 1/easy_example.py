import sys

add = 0.0

n = len(sys.argv)   # n = length of the list 
                    # items in the list 'n' (./easy.py , 3.14, 5, 7)
print(n)

nameofpythonfile = sys.argv[0]
print (nameofpythonfile)

a = float(sys.argv[1])      #int is 1, 2, 3, 4... 
b = float(sys.argv[2])      #float is 1.0, 1.1, 2.1,2.222222, 3.0 etc...
c = float(sys.argv[3])

add = a + b + c

print (add)