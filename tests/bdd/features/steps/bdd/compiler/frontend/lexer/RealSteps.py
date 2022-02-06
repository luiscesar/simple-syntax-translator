from behave import *
from compiler.frontend.lexer.Real import Real
from compiler.frontend.lexer.Tag import *

@given('Real creation - Case1')
def step_impl(context):
    context.real = Real(0)

@when('Real value 0 - Case1')
def step_impl(context):
    pass

@then('Real is created - Case1')
def step_impl(context):
    assert((context.real.tag == Tag.REAL) and (context.real.value == 0))


if __name__ == '__main__':
    pass
