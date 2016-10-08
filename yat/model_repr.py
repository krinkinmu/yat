class Scope:
    def __init__(self, parent = None):
        pass

class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Number({})'.format(self.value)

class Function:
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def __repr__(self):
        return 'Function([{}], [{}])'.format(','.join(arg for arg in self.args),
            ';'.join(repr(stm) for stm in self.body))
               

class FunctionDefinition:
    def __init__(self, name, function):
        self.name = name
        self.func = function

    def __repr__(self):
        return 'FunctionDefinition({}, {})'.format(self.name, repr(self.func))

class Conditional:
    def __init__(self, condition, if_true, if_false = None):
        self.cond = condition
        self.if_true = if_true
        self.if_false = if_false

    def __repr__(self):
        return 'Conditional({}, [{}], [{}])'.format(repr(self.cond),
            ';'.join(repr(stm) for stm in self.if_true),
            ';'.join(repr(stm) for stm in self.if_false))

class Print:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return 'Print({})'.format(repr(self.expr))

class Read:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Read({})'.format(self.name)

class FunctionCall:
    def __init__(self, fun_expr, args):
        self.fexpr = fun_expr
        self.args = args

    def __repr__(self):
        return 'FunctionCall({}, [{}])'.format(repr(self.fexpr),
            ','.join(repr(arg) for arg in self.args))

class Reference:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Reference({})'.format(self.name)

class BinaryOperation:
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def __repr__(self):
        return 'BinaryOperation({}, {}, {})'.format(repr(self.lhs), self.op,
            repr(self.rhs))

class UnaryOperation:
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def __repr__(self):
        return 'UnaryOperation({}({}))'.format(self.op, repr(self.expr))
