import unittest
from os.path import exists
from parameterized import parameterized
from importlib import import_module
import sys

time_limit = 10.0
mem_limit = 25.0
custom = False


if len(sys.argv) > 1:
    args = []
    for x in range(1, len(sys.argv)):
        args.append(sys.argv.pop())
    custom = True
    args.reverse()

modules = []
if not custom:
    for x in range(1,771):
        if exists(f'euler{x}.py'):
            modules.append(import_module(f'euler{x}'))
else:
    for x in args:
        if exists(f'euler{x}.py'):
            modules.append(import_module(f'euler{x}'))


with open('data/answers') as fptr:
    answers = fptr.readlines()

answers = [answer.strip() for answer in answers]
needed_answers = []

for module in modules:
    print(module.__name__)
    needed_answers.append(int(answers[int(module.__name__[5:]) - 1]))

answers = needed_answers.copy()
del(needed_answers)
answers = [int(answer) for answer in answers]

class TestAnswers(unittest.TestCase):
    @parameterized.expand([f'{module.__name__}', b, c] for module, b, c in zip(modules, modules, answers))
    def test_all_tests(self, name, module, answer):
        derived_answer, mem, time = module.find_answer()
        self.assertEqual(int(derived_answer), int(answer), f'{name} should have gotten {answer} but got {derived_answer}')
        self.assertEqual(True, float(time[28:]) < time_limit, f'{name} took {time} seconds, but had a limit of {time_limit} seconds')
        self.assertEqual(True, float(mem[17:-3]) < mem_limit, f'{name} used {mem} MB of memory, but had a limit of {mem_limit} MB')
    


if __name__ == '__main__':
    print(f'Running {len(answers)} test(s). Please be patient.\n')
    unittest.main()
