from behave import *
from compiler.frontend.lexer.Tag import *
from compiler.frontend.lexer.Word import *

@given('Word AND creation - Case1')
def step_impl(context):
    context.word = Word.AND

@when('Word value AND - Case1')
def step_impl(context):
    pass

@then('Word AND is created - Case1')
def step_impl(context):
    assert((context.word.tag == Tag.AND) and (context.word.lexeme == "&&"))


if __name__ == '__main__':
    pass
