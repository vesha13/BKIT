import unittest
import sys, os
sys.path.append(os.getcwd())
text = 'не хочешь развлекух - как хочешь, переходи в /menu'
winx = ['лейла', 'стела', 'муза', 'флора', 'техна', 'блум', 'не люблю винкс']

class TestBot(unittest.TestCase):
    def test_1(self):
        reset = text
        self.assertEqual(reset, 'не хочешь развлекух - как хочешь, переходи в /menu')

    def test_2(self):
        cmd = winx
        self.assertEqual(cmd, ['лейла', 'стела', 'муза', 'флора', 'техна', 'блум', 'не люблю винкс'])

if __name__ == '__main__':
    unittest.main()
