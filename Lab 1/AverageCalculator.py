import sys

n = len(sys.argv)   # n = length of the list 
                    # items in the list 'n' (./easy.py , 3.14, 5, 7)
n-=1                # n = n - 1

# nameofpythonfile = sys.argv[0]

a = float(sys.argv[1])      #int is 1, 2, 3, 4... 
b = float(sys.argv[2])      #float is 1.0, 1.1, 2.1,2.222222, 3.0 etc...
c = float(sys.argv[3])

add = 0.0           # initialize 'add' 
add = a + b + c     # add them together and store results in 'add'
average = add/n     # divide the sum of numbers with the number of numbers 
                    # / vs // ?

print ("Average:", str('%.2f'%((round(average,2)))))    # fomatting the output