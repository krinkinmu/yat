import string
import model

class Token:
    def __init__(self, value, lineno, offset):
        self.value = value
        self.line = lineno
        self.offset = offset

    def __bool__(self):
        return bool(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return 'Token("{}", {}, {})'.format(self.value, self.line, self.offset)

class Generator:
    OPERATORS = ("==", "!=", "<=", ">=", "||", "&&",
                 "+",  "-",  "*",  "/",  "%",  "<", ">", "!")
    PUNCTUATORS = (",", "{", "}", "(", ")", ";")

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 0
        self.offset = 0

    def peek_char(self, offset = 0):
        at = self.position + offset
        if at >= len(self.source):
            return ''
        return self.source[at]

    def peek_chars(self, count = 1):
        return ''.join(self.peek_char(i) for i in range(count))

    def read_char(self):
        char = self.peek_char()
        if not char:
            return char

        self.position += 1
        if char == '\n':
            self.line, self.offset = self.line + 1, 0
        else:
            self.line, self.offset = self.line, self.offset + 1

        return char

    def read_chars(self, count = 1):
        return ''.join(self.read_char() for _ in range(count))

    def extract_token(self, chars):
        line, offset = self.line, self.offset
        word = ""
        char = self.peek_char()
        while char and char in chars:
            word += self.read_char()
            char = self.peek_char()
        return Token(word, line, offset)

    def read_spaces(self):
        return self.extract_token(string.whitespace)

    def read_name(self):
        name_chars = string.ascii_letters + string.digits + '_'
        return self.extract_token(name_chars)

    def read_number(self):
        return self.extract_token(string.digits)

    def read_operator(self):
        token = self.extract_token('+-*/<>!=%&|')
        if token.value not in Generator.OPERATORS:
            raise Exception('Undefined operator "{}"'.format(token.value))
        return token

    def read_punctuator(self):
        token = Token(self.peek_char(), self.line, self.offset)
        self.read_char()
        return token

    def __next__(self):
        self.read_spaces()
        if not self.peek_char():
            raise StopIteration()

        char = self.peek_char()
        if char.isalpha() or char == '_':
            return self.read_name()

        if char.isdigit():
            return self.read_number()

        if char in Generator.PUNCTUATORS:
            return self.read_punctuator()

        return self.read_operator()


class Scanner:
    def __init__(self, filename):
        with open(filename, "r") as source:
            self.source = source.read()

    def __iter__(self):
        return Generator(self.source)


class Parser:
    KEYWORDS = ('if', 'def', 'read', 'write')
    PRECEDENCE = {
        '*': 6, '/': 6, '%': 6,
        '-': 5, '+': 5,
        '<': 4, '>': 4, '<=': 4, '>=': 4,
        '==': 3, '!=': 3,
        '&&': 2,
        '||': 1
    }
    LOWEST_PRECEDENCE = 1
    HIGHEST_PRECEDENCE = 6

    def peek_token(self, offset = 0):
        at = self.position + offset
        if at >= len(self.tokens):
            return Token("", -1, -1)
        return self.tokens[at]

    def drop_tokens(self, count = 1):
        self.position += count

    def ensure_token(self, value):
        token = self.peek_token()
        if token.value != value:
            raise Exception('Expected "{}" at {}:{} instead of "{}"'.format(
                value, token.line, token.offset, token.value))
        self.drop_tokens()

    def is_name(self, value):
        name_chars = string.ascii_letters + string.digits + '_'
        if value in self.KEYWORDS:
            return False
        if not value[0].isalpha():
            return False
        for char in value:
            if char not in name_chars:
                return False
        return True

    def is_unary(self, value):
        return value in ('-', '!')

    def is_number(self, value):
        return value.isdigit()

    def parse_name(self):
        token = self.peek_token()
        if not self.is_name(token.value):
            raise Exception('"{}" at {}:{} is not allowed name'.format(
                token.value, token.line, token.offset))
        self.drop_tokens()
        return token.value

    def parse_number(self):
        token = self.peek_token()
        if not self.is_number(token.value):
            raise Exception('"{}" at {}:{} is not a number'.format(
                token.value, token.line, token.offset))
        self.drop_tokens()
        return int(token.value)

    def parse_arguments(self):
        self.ensure_token('(');
        token = self.peek_token()
        names = []
        while token and token.value != ')':
            names.append(self.parse_name())
            token = self.peek_token()
            if token.value == ',':
                self.drop_tokens()
                token = self.peek_token()
        self.ensure_token(')')
        return names

    def parse_def(self):
        self.ensure_token('def')
        function_name = self.parse_name()
        arguments = self.parse_arguments()
        body = self.parse_block()
        function = model.Function(arguments, body)
        return model.FunctionDefinition(function_name, function)

    def parse_if(self):
        self.ensure_token('if')
        self.ensure_token('(')
        condition = self.parse_expression()
        self.ensure_token(')')
        if_body = self.parse_block()
        else_body = None
        if self.peek_token().value == 'else':
            self.drop_tokens()
            else_body = self.parse_block()
        return model.Conditional(condition, if_body, else_body)

    def parse_read(self):
        self.ensure_token('read')
        name = self.parse_name()
        return model.Read(name)

    def parse_print(self):
        self.ensure_token('print')
        expression = self.parse_expression()
        return model.Print(expression)

    def parse_primary(self):
        token = self.peek_token()
        if self.is_number(token.value):
            return model.Number(self.parse_number())
        if self.is_name(token.value):
            return model.Reference(self.parse_name())

        if token.value == '(':
            self.drop_tokens()
            expr = self.parse_expression()
            self.ensure_token(')')
            return expr
        raise Exception('Unexpected token "{}" at {}:{}'.format(
            token.value, token.line, token.offset))

    def parse_parameters(self):
        self.ensure_token('(')
        expressions = []
        token = self.peek_token()
        while token and token.value != ')':
            expressions.append(self.parse_expression())
            token = self.peek_token()
            if token.value == ',':
                self.drop_tokens()
                token = self.peek_token()
        self.ensure_token(')')
        return expressions

    def parse_unary(self):
        token = self.peek_token()
        if self.is_unary(token.value):
            self.drop_tokens()
            return model.UnaryOperation(token.value, self.parse_unary())

        primary = self.parse_primary()
        while self.peek_token().value == '(':
            parameters = self.parse_parameters()
            primary = model.FunctionCall(primary, parameters)
        return primary

    def parse_binary(self, min_precedence = LOWEST_PRECEDENCE):
        left = self.parse_unary()
        precedence = self.PRECEDENCE.get(self.peek_token().value, 0)
        while precedence >= min_precedence:
            operator = self.peek_token()
            while self.PRECEDENCE.get(operator.value, 0) == precedence:
                self.drop_tokens()
                right = self.parse_binary(precedence + 1)
                left = model.BinaryOperation(left, operator.value, right)
                operator = self.peek_token()
            precedence -= 1
        return left

    def parse_expression(self):
        return self.parse_binary()

    def parse_block(self, parentheses = True):
        if parentheses:
            self.ensure_token('{')
        statements = []
        token = self.peek_token()
        while token and token.value != '}':
            if token.value == 'def':
                statements.append(self.parse_def())
            elif token.value == 'if':
                statements.append(self.parse_if())
            else:
                if token.value == 'read':
                    statements.append(self.parse_read())
                elif token.value == 'print':
                    statements.append(self.parse_print())
                else:
                    statements.append(self.parse_expression())
                self.ensure_token(';')
            token = self.peek_token()
        if parentheses:
            self.ensure_token('}')
        return statements

    def parse(self, tokens):
        self.tokens = [token for token in tokens]
        self.position = 0
        program = self.parse_block(False)
        return model.Function([], program)

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        print(Parser().parse(Scanner(filename)))
