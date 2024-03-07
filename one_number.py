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

    def float_length(self):
        return len(self.the_float)                    
    
    def Is_Zero(self):

        return len([x for x in self.the_float if not x=='0'])==0 and len([x for x in self.the_integer if not x=='0'])==0
    
    def add_a_zero(self, which):
        
        if which=='Integer':
            self.the_integer.append('0')
        else:
            self.the_float.append('0')


    def undo_exp_notation(self):

        if self.the_exponent==None:
            return
        
        while not self.the_exponent.Is_Zero():
            if self.the_exponent.is_negative():
                if len(self.the_integer)>0:
                    one_digit = self.the_integer.pop(0)
                else:
                    one_digit = '0'
                    
                self.the_float.insert(0,one_digit)
                self.the_exponent = self.the_exponent  + number_one
            else:
                if len(self.the_float)>0:
                    one_digit = self.the_float.pop(0)
                else:
                    one_digit = '0'
                    
                self.the_integer.insert(0,one_digit)
                self.the_exponent = self.the_exponent  - number_one                    

        if len(self.the_float)==0:
            return
        
        while self.the_float[-1]=='0':
            self.the_float.pop(-1)
            if len(self.the_float)==0:
                break

###############################Arithmatic Operators############################
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

######################Comparison Operators############################
    
    def __eq__(self,other):
        return not self>other and not  other>self

    def __lt__(self, other):
        return other>self

    def __le__(self,other):
        return not self>other

    def __gt__(self,other):
        
        X=copy.deepcopy(self)
        Y=copy.deepcopy(other)
        
        X.undo_exp_notation()
        Y.undo_exp_notation()

        if X.Is_Zero() and Y.is_negative():
            return  True

        if X.Is_Zero() and not Y.is_negative():
            return  False

        if Y.Is_Zero() and X.is_negative():
            return  False

        if Y.Is_Zero() and X.is_negative():
            return  True

        if X.is_negative() and not Y.is_negative():
            return False
        
        if not X.is_negative() and Y.is_negative():
            return True

        
        while X.integer_length()<Y.integer_length():
            X.add_a_zero('Integer')

        if X.is_negative() and Y.is_negative():
            Z=X
            X=Y
            Y=Z
            return X<Y

        if X.integer_length()>Y.integer_length():
            return True
        
        while Y.integer_length()<X.integer_length():
            Y.add_a_zero('Integer')        

        comparison_pieces_A = [''.join(y) for y in list(zip(X.the_integer,Y.the_integer))]

        for one_piece in reversed(comparison_pieces_A):
            if the_digit_comparison[one_piece]=='False':
         
                return False
            
            elif the_digit_comparison[one_piece]=='True':

                return True
 
        #now look at the float portion because the integers must be equal
        while Y.float_length()<X.float_length():
            Y.add_a_zero('Float')                  

        while X.float_length()<Y.float_length():
            X.add_a_zero('Float')              

        comparison_pieces_A = [''.join(y) for y in list(zip(X.the_float,Y.the_float))]

        for one_piece in comparison_pieces_A:
            if the_digit_comparison[one_piece]=='False':
         
                return False
            
            elif the_digit_comparison[one_piece]=='True':

                return True
                        
        return False
    def __ge__(self,other):
        return other<=self
    
number_one = one_number_class('1')
number_zero = one_number_class('0')  