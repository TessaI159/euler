import subprocess
import sys
from os import walk, chdir, getcwd
from os.path import exists
from importlib import import_module

if __name__ == '__main__':
    check_list = []
    if len(sys.argv) < 2:
        print(f'Usage: script.py <answersToCheck>')
        sys.exit()
    else:
        
        for x, arg in enumerate(sys.argv):
            if x == 0:
                continue
            try:
                check_list.append(int(arg))
            except ValueError as e:
                print('You can only enter characters that can be interpreted as integers.')
    
    python_modules = [f'euler{i}.py' for i in check_list]
    cpp_modules = [f'euler{i}.cpp' for i in check_list]
    
    for pmod, cmod in zip(python_modules[:], cpp_modules[:]):
        if not exists(f'python/{pmod}') or not exists(f'cpp/{cmod}'):
            print(f'Could not find euler{pmod[5:-3]}')
            python_modules.remove(pmod)
            cpp_modules.remove(cmod)

    outfile = open('temp_compare_results.txt', 'w')
    begindir = getcwd()
    
    chdir("/Users/tessaisola/Code/euler/python")
    for index, pmod in enumerate(python_modules):
        print(f'Running {pmod}')
        subprocess.run(['python3', f'{pmod}'], stdout=outfile)

    
    chdir("/Users/tessaisola/Code/euler/cpp")
    for index, cmod in enumerate(cpp_modules):
        print(f'Recompiling {cmod}...')
        subprocess.run(['zsh', 'compile.sh', f'{cmod[5:-4]}'])
        
        print(f'Running {cmod[:-4]}.run')
        subprocess.run([f'./{cmod[:-4]}.run'], stdout=outfile)
        
    chdir(begindir)
    print('Parsing output into compare_results.txt')
    
    subprocess.run(['python3', 'parse.py'])
    outfile.close()
    subprocess.run(['rm', 'temp_compare_results.txt'])
    subprocess.run(['open', 'compare_results.txt'])
    
        