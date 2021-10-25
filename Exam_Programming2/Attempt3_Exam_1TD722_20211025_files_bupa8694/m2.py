"""
Solutions to exam tasks for module 2
Name: Pallimulla Kapugamage Buddhika Chaturanga
Code: BUPA8694
email bupa8694@student.uu.se
"""

from tokenize import TokenError
import tokenize
import io
from turtle import update

import result as result


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


variables = {'ans': 0}
update_variables = True

def assignment(wtok, update = True):
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            if update:
                variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected name after '=' ", wtok)
        wtok.next()
    return result


def expression(wtok, update = True):
    result = term(wtok, update)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok)
        else:
            wtok.next()
            result = result - term(wtok)
    return result


def term(wtok, update=True):
    result = factor(wtok, update)
    while wtok.get_current() in ('*', '/'):
        op = wtok.get_current()
        wtok.next()
        if op == '*':
            result = result * factor(wtok, update)
        else:
            try:
                if op == '/':
                    result = result / factor(wtok, update)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
    return result


def factor(wtok, update = True):

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, update)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'", wtok)
        else:
            wtok.next()
    if wtok.get_current() == '|':
        wtok.next()
        result = assignment(wtok)
        if wtok.get_current() != '|':
            raise SyntaxError("Expected '|'", wtok)
        else:
            wtok.next()
            result = abs(result)

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
        result = -factor(wtok)

    else:
        raise SyntaxError(
            "Expected number, word or '('", wtok)

    if wtok.get_current() == '**':
        wtok.next()
        exp = factor(wtok)
        base = result
        if base == 0 or exp <= 0 and base < 0 and exp is not int:
            raise EvaluationError(
                f"Zero Cannot be raised to power : '{wtok.get_current()}'")
        result = base ** exp

    return result



def vars_print():
    for name, value in sorted(variables.items()):
        print(f"   {name:<5} : {value}")


def file_name(wtok):
    file = 'test.txt'
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

def statement(input_buffer):
    line = ''
    while True:
        if len(input_buffer) == 0:
            break
        line = input_buffer.pop(0).strip()
        print(f"File  :{line}")
        if len(line) != 0 and line[0] != '#':
            break
        
    if line == '':
        line = input('\nInput : ')
        while line == '':
            line = input("Input : ")
    wtok = TokenizeWrapper(line)
    if wtok.get_current() == 'vars':
        vars_print()
    elif wtok.get_current() == 'quit':
        print('Bye')
        exit()
    elif wtok.get_current() == 'file':
        input_buffer.extend(lines_from_file(wtok))
    else:
        result = assignment(wtok)
        if wtok.is_at_end() == False:
            raise SyntaxError('Expected end of line or an operator', wtok)
        variables['ans'] = result
        print('Result:', result)
   

def main():
    print("Numerical calculator")
    input_buffer = []             # For input lines from file
    try:
        with open('test.txt', 'r') as f:
            input_buffer.extend(f.readlines())
    except FileNotFoundError:
        print('*** No init file: ')
    while True:
        try:
            statement(input_buffer)
        except EvaluationError as e:
            print("*** Evaluation error: ", e)

        except SyntaxError as se:
            print("*** Syntax error: ", se)
            print(
                f"Error occurred at '{se.wtok.get_current()}' just after '{se.wtok.get_previous()}'")

        except TokenError as te:
            print('*** Error!')
            print('*** Unbalanced parentheses')
        update_variables = True


if __name__ == "__main__":
    main()
