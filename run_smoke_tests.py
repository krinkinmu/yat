#!/usr/bin/env python3

import yat.model as model

def test_scope():
    f = model.Function([], [model.Number(0)])
    ft = model.Number(42)
    t = model.Number(10)
    parent = model.Scope()
    parent["foo"] = f
    parent["bar"] = t
    assert parent["bar"] is t
    assert parent["foo"] is f
    scope = model.Scope(parent)
    assert scope["bar"] is t
    scope["bar"] = ft
    assert scope["bar"] is ft
    assert parent["bar"] is t

def test_number():
    scope = model.Scope()
    n = model.Number(42)
    assert n.evaluate(scope) is n

def test_function():
    n = model.Number(0)
    f = model.Function([], [n])
    assert f.evaluate(model.Scope()) is n

def test_function_definition():
    name = "foo"
    scope = model.Scope()
    n = model.Number(10)
    f = model.Function([], [n])
    d = model.FunctionDefinition(name, f)
    d.evaluate(scope)
    assert scope[name] is f

def test_conditional():
    scope = model.Scope()
    true = model.Number(1)
    false = model.Number(0)
    f = model.Function([], [true])
    cond = model.Conditional(true, None, None)
    cond.evaluate(scope)
    cond = model.Conditional(false, None, None)
    cond.evaluate(scope)
    cond = model.Conditional(true, [], None)
    cond.evaluate(scope)
    cond = model.Conditional(true, None, [])
    cond.evaluate(scope)
    cond = model.Conditional(false, [], None)
    cond.evaluate(scope)
    cond = model.Conditional(false, None, [])
    cond.evaluate(scope)
    cond = model.Conditional(true, [], [])
    cond.evaluate(scope)
    cond = model.Conditional(true, [], [])
    cond.evaluate(scope)
    cond = model.Conditional(true, [true], None)
    assert cond.evaluate(scope) is true
    cond = model.Conditional(false, None, [false])
    assert cond.evaluate(scope) is false
    cond = model.Conditional(true, [f], None)
    assert cond.evaluate(scope) is true
    cond = model.Conditional(false, None, [f])
    assert cond.evaluate(scope) is true
    # If one of the following assertions fail, it means that Conditional has
    # evaluated wrong branch.
    cond = model.Conditional(false, [true], None)
    assert cond.evaluate(scope) is not true
    cond = model.Conditional(false, [true], [])
    assert cond.evaluate(scope) is not true
    cond = model.Conditional(true, None, [false])
    assert cond.evaluate(scope) is not false
    cond = model.Conditional(true, [], [false])
    assert cond.evaluate(scope) is not false

def test_function_call():
    arg_name = "arg"
    f = model.Function([arg_name], [model.Reference(arg_name)])
    scope = model.Scope()
    f_name = "foo"
    f_r = model.Reference(f_name)
    scope[f_name] = f
    n = model.Number(10)
    call = model.FunctionCall(f_r, [n])
    assert call.evaluate(scope) is n

def test_reference():
    name = "foo"
    value = model.Number(10)
    ref = model.Reference(name)
    scope = model.Scope()
    scope[name] = value
    assert ref.evaluate(scope) is value

def test_binary_operation():
    a = model.Number(10)
    b = model.Number(20)
    for op in ["+", "-", "*", "/", "%", "==", "!=", "<", ">", "<=", ">=", "&&", "||"]:
        model.BinaryOperation(a, op, b).evaluate(model.Scope())

def test_unary_operation():
    a = model.Number(10)
    for op in ["-", "!"]:
        model.UnaryOperation(op, a).evaluate(model.Scope())

if __name__ == "__main__":
    import traceback

    smoke_tests = [
        test_scope, test_number, test_function, test_function_definition,
        test_conditional, test_function_call, test_reference,
        test_binary_operation, test_unary_operation
    ]

    for test in smoke_tests:
        try:
            test()
        except Exception as err:
            print("test {} failed with error: {}".format(test.__name__, err))
            traceback.print_exc()
