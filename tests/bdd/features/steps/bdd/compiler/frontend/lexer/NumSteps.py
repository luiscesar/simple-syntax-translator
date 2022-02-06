from behave import *
from compiler.frontend.lexer.Num import Num
from compiler.frontend.lexer.Tag import *

@given('Num creation - Case1')
def step_impl(context):
    context.token = Num(0)

@when('Num value 0 - Case1')
def step_impl(context):
    context.num = Num(0)

@then('Num is created - Case1')
def step_impl(context):
    assert((context.num.tag == Tag.NUM) and
           (context.num.value == 0))


if __name__ == '__main__':
    pass
