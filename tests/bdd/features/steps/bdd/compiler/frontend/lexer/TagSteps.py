from behave import *
from compiler.frontend.lexer.Tag import *


@given('Tag with AND defined - case 1')
def step_impl(context):
    context.tag = Tag()
    context.result = ""

@when('AND is tested')
def step_impl(context):
    context.result = context.tag.AND

@then('AND works')
def step_impl(context):
    assert(context.result == 256)


if __name__ == '__main__':
    pass
