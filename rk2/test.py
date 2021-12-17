import unittest
import sys, os
sys.path.append(os.getcwd())
from main import *

class TddTest(unittest.TestCase):
    def test_first_task(self):
        one_to_many = [(op.op_name, op.memory, ln.name)
                for ln in lngs
                for op in ops
                if op.ln_id == ln.id]
        self.assertEqual(first_task(one_to_many), [('Java', 'Сравнение'), ('Java', 'Вызов функции')])
    def test_2(self):
        one_to_many = [(op.op_name, op.memory, ln.name)
                    for ln in lngs
                    for op in ops
                    if op.ln_id == ln.id]
        self.assertEqual(second_task(one_to_many), [('Java', 2), ('Python', 4), ('С', 4)])
    def test_3(self):
     many_to_many_temp = [(ln.name, lop.ln_id, lop.op_id)
                          for ln in lngs
                          for lop in ln_op
                          if ln.id == lop.ln_id]
     many_to_many = [(op.op_name, op.memory, language)
                     for language, ln_id, op_id in many_to_many_temp
                     for op in ops if op.id == op_id]
     self.assertEqual(third_task(many_to_many), [('Вызов функции', 'Python'), ('Вызов функции', 'Python'), ('Вызов функции', 'Java'), ('Вызов функции', 'C++'), ('Сложение', 'Python'), ('Сложение', 'С'), ('Сложение', 'Java'), ('Сравнение', 'С'), ('Сравнение', 'Java'), ('Умножение', 'Python'), ('Умножение', 'С'), ('Умножение', 'Java')])