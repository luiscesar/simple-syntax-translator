from behave import *
from compiler.frontend.lexer.Token import Token


@given('Token creation - Case1')
def step_impl(context):
    context.token = Token(0)

@when('Token value 0 - Case1')
def step_impl(context):
    pass

@then('Token is created - Case1')
def step_impl(context):
    assert(context.token.tag == 0)


if __name__ == '__main__':
    pass
