"""
Solutions to module 2 - A calculator
Student: 
Mail:
Reviewed by:
Reviewed date:
"""


from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg


def expression(wtok):
    result = term(wtok)
    while wtok.get_current() == '+':
        wtok.next()
        result = result + term(wtok)
    while wtok.get_current() == '-':
        wtok.next()
        result = result - term(wtok)
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() == '*':
        wtok.next()
        result = result * factor(wtok)
    while wtok.get_current() == '/':
        wtok.next()
        result = result / factor(wtok)
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()
        result = expression(wtok)
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    else:
        raise SyntaxError('Expected number or (')
    return result


def main():
    print("Calculator version 0.1")
    while True:
        line = input("Input : ")
        wtok = TokenizeWrapper(line)
        try:
            if wtok.get_current() == 'quit':
                break
            else:
                result = expression(wtok)
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

    print('Bye!')


if __name__ == "__main__":
    main()
