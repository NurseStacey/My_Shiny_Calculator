###############The file with the class for a number##################
from Constants import *
import copy

class one_number_class():
    def __init__(self,the_number_text):

        self.the_integer=[]
        self.the_float=[]
        self.the_sign='+'
        self.the_exponent = None

        if the_number_text[0]=='-':
            the_number_text=the_number_text[1:]
            self.the_sign='-'
        
        two_pieces = the_number_text.partition('.')

        for one_char in reversed(two_pieces[0]):
            self.the_integer.append(one_char)

        for one_char in two_pieces[2]:
            self.the_float.append(one_char)             

    def __repr__(self):

        if self.the_float==[]:
            if self.is_negative():
                return '-'+''.join(reversed(self.the_integer))
            else:
                return ''.join(reversed(self.the_integer))
        else:
            if self.is_negative():
                return '-'+''.join(reversed(self.the_integer)) + '.' + ''.join(self.the_float)
            else:
                return ''.join(reversed(self.the_integer)) + '.' + ''.join(self.the_float)

    def is_negative(self):

        return self.the_sign=='-'

    def integer_length(self):
        return len(self.the_integer)
                    

    def add_a_zero(self, which):
        
        if which=='Integer':
            self.the_integer.append('0')
        else:
            self.the_float.append('0')

    def __add__(self,other):

        new_number=None
        X=copy.deepcopy(self)
        Y=copy.deepcopy(other)

        while X.integer_length()<Y.integer_length():
            X.add_a_zero('Integer')

        while Y.integer_length()<X.integer_length():
            Y.add_a_zero('Integer')

        new_number_pieces_A = [''.join(y) for y in list(zip(X.the_integer,Y.the_integer))]
        new_number_pieces_B=[the_digit_sums[y] for y in new_number_pieces_A]
        new_number=''
        add_ons=[]
        leading_zeros='0'


        for one_piece in new_number_pieces_B:
            if len(one_piece)>1:
                add_ons.append(leading_zeros+'1')
                new_number = one_piece[1] + new_number
            else:
                new_number = one_piece[0]+new_number
            
            leading_zeros = leading_zeros + '0'

        new_number = one_number_class(new_number)

        for one_add_on in add_ons:
            new_number = new_number +one_number_class(one_add_on[::-1])

        return new_number    


number_one = one_number_class('1')
number_zero = one_number_class('0')  