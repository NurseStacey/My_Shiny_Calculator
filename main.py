##################Main.py#########################
#############Everything Starts Here##################
##########Nothing Imported from Here################

from one_number import *


X=one_number_class('123')
Y=one_number_class('5')
Z=one_number_class('99')

print(X<Y)
print(Y==Y)
print(Z==X)


input_file = open('calculator Testing - Comparison Operators.csv','r')
output_file = open('results.txt','w')

line_number = number_zero
which_operator = number_zero
for one_line in input_file.readlines():
    one_line = one_line.replace('\n','')
    three_pieces = one_line.split(',')
    first_number = one_number_class(three_pieces[0])
    second_number = one_number_class(three_pieces[1])
    answer = three_pieces[2]

    if line_number==one_number_class('37'):
        pass
    
    calculated_answer = None
    if which_operator==number_zero:
        calculated_answer=first_number>second_number
    elif which_operator==number_one:
        calculated_answer=first_number<second_number
    elif which_operator==one_number_class('2'):
        calculated_answer=first_number<=second_number
    else:
        calculated_answer=first_number>=second_number

    output_file.write('Line {}    Calculated Answer  {}    Correct Answer {}\n'.format(line_number,calculated_answer,answer))

    if which_operator==one_number_class('3'):
        which_operator=number_zero
    else:
        which_operator = which_operator + number_one

    line_number = line_number + number_one

output_file.close