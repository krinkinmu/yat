class Scope:
    def __init__(self, parent = None):
        pass

class Node:
    def evaluate(self, scope):
        pass

class Number(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'Number({})'.format(self.value)

class Function(Node):
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'Function([{}], [{}])'.format(','.join(arg for arg in self.args),
            ';'.join(repr(stm) for stm in self.body))
               

class FunctionDefinition(Node):
    def __init__(self, name, function):
        self.name = name
        self.func = function

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'FunctionDefinition({}, {})'.format(self.name, repr(self.func))

class Conditional(Node):
    def __init__(self, condition, if_true, if_false = None):
        self.cond = condition
        self.if_true = if_true
        self.if_false = if_false

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'Conditional({}, [{}], [{}])'.format(repr(self.cond),
            ';'.join(repr(stm) for stm in self.if_true),
            ';'.join(repr(stm) for stm in self.if_false))

class Print(Node):
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'Print({})'.format(repr(self.expr))

class Read(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'Read({})'.format(self.name)

class FunctionCall(Node):
    def __init__(self, fun_expr, args):
        self.fexpr = fun_expr
        self.args = args

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'FunctionCall({}, [{}])'.format(repr(self.fexpr),
            ','.join(repr(arg) for arg in self.args))

class Reference(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'Reference({})'.format(self.name)

class BinaryOperation(Node):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'BinaryOperation({}, {}, {})'.format(repr(self.lhs), self.op,
            repr(self.rhs))

class UnaryOperation(Node):
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        pass

    def __repr__(self):
        return 'UnaryOperation({})'.format(repr(self.expr))
