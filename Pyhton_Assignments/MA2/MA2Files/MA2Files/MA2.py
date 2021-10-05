"""
Solutions to module 2 - A calculator
Student: 
Mail:
Reviewed by:
Reviewed date:
"""


from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper

PI =3.14

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
    
def assignment(wtok, dict):
    result = expression(wtok, dict)
    ctok = wtok.get_current()
    while ctok == '=':
        wtok.next()
        ctok =  wtok.get_current()
        print(ctok)
        if ctok not in dict:
            dict[ctok] = result
        else:
            result = dict[ctok]
    return result

def expression(wtok, dict):
    result = term(wtok,dict)
    ctok = wtok.get_current()
    while ctok == '+' or ctok == '-' :
        wtok.next()
        result = (result + term(wtok,dict)) if ctok == '+' else (result - term(wtok,dict))
        ctok =  wtok.get_current()
    return result


def term(wtok, dict):
    result = factor(wtok, dict)
    ctok = wtok.get_current()
    while ctok == '*' or ctok == '/' :
        wtok.next()
        result = (result * factor(wtok,dict)) if ctok == '*' else (result / factor(wtok,dict))
        ctok =  wtok.get_current()
    return result


def factor(wtok, dict):
    if wtok.get_current() == '(':
        wtok.next()
        result = expression(wtok,dict)
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    elif wtok.get_current() in dict:
        result = dict[wtok.get_current()]
        wtok.next()
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok,dict)
       
    else:
        raise SyntaxError('Expected number or (')
    return result


def main():
    var_dict={}
    fn1_dict={}
    fnl_dict={}
    print("Calculator version 0.1")
    while True:
        line = input("Input : ")
        wtok = TokenizeWrapper(line)
        try:
            if wtok.get_current() == 'quit':
                break
            else:
                result = assignment(wtok,var_dict)
                #result = expression(wtok)
                if wtok.is_at_end():
                    print('Result: ', result)
                else:
                    raise SyntaxError('Unexpected token')

        except SyntaxError as se:
            print("*** Syntax: ", se.arg)
            print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")

        except TokenError:
            print('*** Syntax: Unbalanced parentheses')
            
        except ZeroDivisionError:
             print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
            
    print('Bye!')


if __name__ == "__main__":
    main()
