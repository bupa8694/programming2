"""
Solutions to module 2 - A calculator
Student: 
Mail:
Reviewed by:
Reviewed date:
"""


from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper
from MA2_math import *

PI =3.141592653589793
E = 2.718281828459045

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg

def assignment(wtok, dict):
    result = expression(wtok, dict)
    ctok = wtok.get_current()
    while ctok == '=':
        wtok.next()
        ctok =  wtok.get_current()
        if wtok.is_number():
            raise SyntaxError("Required varianle name")
        dict[ctok] = result
        result = dict[ctok]
        wtok.next()
        ctok = wtok.get_current()
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
        val = factor(wtok,dict)
        if ctok == '/' and val == 0:
            raise EvaluationError("Dvision by zero")
        result = (result * val) if ctok == '*' else (result / val)
        ctok =  wtok.get_current()
    return result

def function_1(wtok, dict):
    if wtok.is_name():
        if wtok.get_current() in fn_1:
            return True
    return False


def function_n(wtok, dict):
    if wtok.is_name():
        if wtok.get_current() in fn_n:
            return True
    return False

def factor(wtok, dict):
    #result = function_1(wtok, dict)
    if wtok.get_current() == '(':
        wtok.next()
        #while wtok.get_current() != ')':
        result = assignment(wtok,dict)
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")
    elif function_1(wtok, dict):
        func_name =''
        func_name = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
                wtok.next()
                n = assignment(wtok,dict)
                if func_name == 'log' and n < 0:
                    raise EvaluationError("Invalid argument for {}".format(func_name))
                elif (func_name == 'fib' or func_name == 'fac') and not  n.is_integer():
                    raise EvaluationError("Invalid argument for {}".format(func_name))
                result = fn_1[func_name](n)
                if wtok.get_current() == ')':
                    wtok.next()
        else:
            raise SyntaxError("Expected '(' after function name")
    elif function_n(wtok, dict):
        func_name =''
        func_name = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            element_list=[]
            wtok.next()
            while wtok.get_current() !=')':
                ele = assignment(wtok,dict)
                element_list.append(ele)
                if wtok.get_current() == ',':
                    wtok.next()
                elif wtok.get_current() != ')':
                    raise SyntaxError("Expected ',' after argument")
                
            result = fn_n[func_name](element_list)
            wtok.next()
        else:
            raise SyntaxError("Expected '(' after function name")
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    elif wtok.get_current() in dict:
        result = dict[wtok.get_current()]
        wtok.next()
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok,dict)
    elif wtok.get_current() not in dict:
        raise SyntaxError('Variable not defined') 
    else:
        raise SyntaxError('Expected number or (')
    return result


def main():
    var_dict={'E':E,'PI':PI,'ans':0}
    file_lines=[]
    n_lines = 0
    print("Calculator version 0.1")
    while True :
        line = input("Input : ") if  len(file_lines) == 0  else file_lines[n_lines]
        wtok = TokenizeWrapper(line)
        try:
            if wtok.get_current() == 'quit':
                break
            elif wtok.get_current() == 'vars':
                for k,v in var_dict.items():
                    print(k,"   :",v) 
            elif wtok.get_current() == 'file':
                filename = input("Filename : ")
                with open(filename) as fp:
                        line = fp.readline()
                        file_lines.append(line.split("#")[0].rstrip() if '#' in line else line.rstrip())
                        cnt = 1
                        while line:
                            #print("{}".format(line.rstrip()))
                            line = fp.readline()
                            if line.isspace():
                                continue
                            file_lines.append(line.split("#")[0].rstrip() if '#' in line else line.rstrip())
                            cnt += 1
                            
                        #for e in file_lines:
                            # print("{}".format(e))
                        #n_lines = cnt
                continue
            else:
                result = assignment(wtok,var_dict)
                var_dict['ans'] = result
                #result = expression(wtok)
                if wtok.is_at_end():
                    print('Result: ', result)
                else:
                    raise SyntaxError('Unexpected token')

        except SyntaxError as se:
            print("*** Syntax: ", se.arg)
            print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")

        except EvaluationError as se:
            print("*** Evaluation error: ", se.arg)

        except TokenError:
            print('*** Syntax: Unbalanced parentheses')
        
        except ValueError:
             print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
        except TypeError:
             print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
        except ZeroDivisionError:
             print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
        n_lines =  (n_lines+1) if n_lines < len(file_lines) else 0
        if n_lines == len(file_lines) - 1:
            file_lines.clear()
                  

    print('Bye!')


if __name__ == "__main__":
    main()
