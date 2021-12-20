from behave import *
import telebot
token = '5048990230:AAH2MovxsbqssKT6kMMdbNf01R6S_B0idRc'
bot = telebot.TeleBot(token)


@given("Entered data")
def DataEnt(context):
    context.a = bot()

@when("Fix name")
def Fix(context):
    context.a.test_1()

@when("Fix winx")
def Fix2(context):
    context.a.test_2()

@then("Completed")
def check_result(context):
    pass
