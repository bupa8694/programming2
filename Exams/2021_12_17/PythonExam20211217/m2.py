"""


"""
"""
Solutions to exam tasks for module 1.
Name: Pallimulla Kapugamage Buddhika Chaturanga
Code: BUPA8694
email bupa8694@student.uu.se
"""

import math
from tokenize import TokenError
import tokenize
import io


class TokenizeWrapper:
    def __init__(self, line):
        self.line = line
        self.tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        self.current = next(self.tokens)
        self.previous = 'START'

    def __str__(self):
        return self.current[0] + self.current[1]

    def get_current(self):
        if self.current[0] > 0:
            return self.current[1]
        else:
            return 'NO MORE TOKENS'

    def get_previous(self):
        return self.previous

    def next(self):
        # The return value is mainly intended for debugging purposes
        if self.has_next():
            self.previous = self.current[1]
            self.current = next(self.tokens)
            #print('next', self.current[0], self.current[1])
            return self.current
        else:
            return (0, 'EOS')

    def is_number(self):
        return self.current[0] == 2

    def is_name(self):
        return self.current[0] == 1

    def is_newline(self):
        return self.current[0] == 4
    
    def is_comment(self):
        return self.current[0] == 55

    def is_at_end(self):
        return self.current[0] == 0 or self.current[0] == 4 or \
               self.current[1][0] == '#'
               #self.current[0] == 55   # This test doesn't work everywhere
                                        # try to check on '#' instead

    def has_next(self):
        return self.current[0] != 0 and self.current[0] != 4


###################################


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class SyntaxError(Exception):
    def __init__(self, arg, wtok):
        self.arg = arg
        self.wtok = wtok
        super().__init__(self.arg)


def assignment(wtok, variables):
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected name after '=' ", wtok)
        wtok.next()
    return result

def factorial(n):
    if n < 0 or int(n) != n:
        raise EvaluationError(f"Illegal argument to factorial: {n}")
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def expression(wtok, variables):
    result = term(wtok, variables)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    result = factor(wtok, variables)
    while wtok.get_current() in ('*', '/'):  
        op = wtok.get_current()
        wtok.next()
        op2 = wtok.get_current()
        if op == '*':
            result = result * factor(wtok, variables)
        if op2 == '/':
            try:
                wtok.next()
                result = result // factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
        else:
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
            
    return result


def factor(wtok, variables):
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'", wtok)
        else:
            wtok.next()
    elif wtok.get_current() == '|':                     
        wtok.next()
        result = abs(assignment(wtok,variables))
        if wtok.get_current() != '|':
            raise SyntaxError("Expected '|'", wtok)
        else:
            wtok.next()
    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(
                f"Undefined variable: '{wtok.get_current()}'")

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result =  -factor(wtok,variables)
    
    else:
        raise SyntaxError(
            "Expected number, word, '-' or '('", wtok)

    if wtok.get_current() == '!':                   
        wtok.next()
        result = factorial(result)

    if wtok.get_current() == '**':                   
        wtok.next()
        e = factor(wtok)
        if result < 0 and not e.is_integer() or result == 0 and e <= 0 :
            raise EvaluationError(f"Illegal operation {result}**{e}")
        else:
            result = result**e
    return result


def vars_print(variables):
    for name, value in sorted(variables.items()):
        print(f"   {name:<5} : {value}")


def file_name(wtok):
    file = 'm2_test.txt'
    if wtok.is_name():
        file = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '.':
            file += '.'
            wtok.next()
            if wtok.is_name():
                file += wtok.get_current()
    return file


def lines_from_file(wtok):
    wtok.next()
    file = file_name(wtok)
    try:
        with open(file, 'r') as f:
            return(f.readlines())
    except FileNotFoundError:
        print('*** No such file: ', file)
        return []


def statement(input_buffer, variables):
    line = ''
    while True:
        if len(input_buffer) == 0:
            break
        line = input_buffer.pop(0).strip()
        print(f"File  : {line}")
        if len(line) != 0 and line[0]!='#':
            break
        
    if line == '':
        line = input('\nInput : ')
        while line == '':
            line = input("Input : ")

    saved_line = line
    wtok = TokenizeWrapper(line)
    if wtok.get_current() == 'vars':
        vars_print(variables)
    elif wtok.get_current() == 'quit':
        print('Bye')
        exit()
    elif wtok.get_current() == 'file':
        input_buffer.extend(lines_from_file(wtok))
    else:
        result = assignment(wtok, variables)
        if wtok.is_at_end() == False:
            raise SyntaxError('Expected end of line or an operator', wtok)
        #wtok = TokenizeWrapper(saved_line)
        #result = assignment(wtok,variables)           
        variables['ans'] = result
        print('Result:', result)
   

def main():
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    input_buffer = []             # For input lines from file
    while True:
        try:
            statement(input_buffer, variables)
        except EvaluationError as e:
            print("*** Evaluation error: ", e)

        except SyntaxError as se:
            print("*** Syntax error: ", se)
            print(
                f"Error occurred at '{se.wtok.get_current()}' just after '{se.wtok.get_previous()}'")

        except TokenError as te:
            print('*** Error!')
            print('*** Unbalanced parentheses')


if __name__ == "__main__":
    main()
