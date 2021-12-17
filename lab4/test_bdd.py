from behave import *
from main import *


@given("Coefs")
def get_coef(context):
    context.c1 = 1
    context.c2 = -1
    context.c3 = 0

@when("Solved")
def solution(context):
    context.result = get_roots(context.c1, context.c2, context.c3)

@then("Check result")
def expect_result(context):
    assert context.result == [-1, 0, 1]

