import unittest
from os.path import exists
from parameterized import parameterized

modules = []

fptr = open('data/answers', 'r')
unformatted = fptr.readlines()
fptr.close()

answers = [int(answer.strip()) for answer in unformatted]
del(unformatted)


for x in range(1,11):
    if exists(f'euler{x}.py'):
        modules.append(__import__(f'euler{x}'))
    else:
        try:
            answers.pop(answers.index(answers[x-1]))
        except:
            pass

times = []
class CheckSolutions(unittest.TestCase):
    @parameterized.expand([[f'euler{a}', b, c] for a, (b, c) in enumerate(zip(answers, modules))])
    def test_all_tests(self, name, answer, module):
        found_answer, mem, time = module.find_answer()
        self.assertEqual(answer, found_answer)

        times.append(time)

    def test_times(self):
        print('')
        for i, module in enumerate(modules):
            print(f'{module.__name__} {times[i]}')
        
            



if __name__ == '__main__':
    unittest.main()
