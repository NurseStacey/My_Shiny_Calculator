##################Main.py#########################
#############Everything Starts Here##################
##########Nothing Imported from Here################

from one_number import *


X=one_number_class('123')
Y=one_number_class('5')
Z=one_number_class('99')

print(X)
print(Y)
print(Z)

A=X+Y
B=Y+Z

print(A)
print(B)

input_file = open('calculator Testing - Adding_Positive_Integers.csv','r')
output_file = open('results.txt','w')

line_number = one_number_class('0')

for one_line in input_file.readlines():
    one_line = one_line.replace('\n','')
    three_pieces = one_line.split(',')
    first_number = one_number_class(three_pieces[0])
    second_number = one_number_class(three_pieces[1])
    answer = three_pieces[2]
    calculated_answer = first_number+second_number
    output_file.write('Line {}    Calculated Answer  {}    Correct Answer {}\n'.format(line_number,calculated_answer,answer))
                
    line_number = line_number + number_one

output_file.close