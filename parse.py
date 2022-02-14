# This still needs to be edited to work for MiniScript

if __name__ == '__main__':
    inputfile = open('temp_compare_results.txt', 'r')
    

    input_data = inputfile.readlines()
    inputfile.close()

    input_data = [x.strip() for x in input_data]
    input_data = [x for x in input_data if x]
    num_solutions = len(input_data) // 5

    python_solutions = []
    python_runtimes = []
    
    for index in range(num_solutions * 3):
        if index % 3 == 0:
            python_solutions.append(int(input_data[index][input_data[index].index(':')+2:]))
        if (index+1) % 3 == 0:
            python_runtimes.append(float(input_data[index][-8:]) * 1000)
    

    cpp_solutions = []
    cpp_runtimes = []
    for index in range(num_solutions * 3, (num_solutions * 3) + (num_solutions * 2)):
        if not 'ms' in input_data[index]:
            cpp_solutions.append(int(input_data[index]))
        else:
            cpp_runtimes.append(int(input_data[index][:-10]))
        
    with open('compare_results.txt', 'w') as outputfile:
        for index, (csol, psol) in enumerate(zip(cpp_solutions, python_solutions)):
            if csol == psol:
                outputfile.write(f'euler{index+1}: Both programs got {psol} as an answer\n')
            else:
                outputfile.write(f'euler{index+1}: cpp got {csol} but python got {psol}. Woops.\n')

            outputfile.write(f'cpp took {cpp_runtimes[index]:.6f} ms\n')
            outputfile.write(f'python took {python_runtimes[index]:.6f} ms\n')
            
            if cpp_runtimes[index] <= 0:
                outputfile.write(f'cpp ran too fast to compare to python\n')
            else:
                multiplier = python_runtimes[index] / cpp_runtimes[index]
                outputfile.write(f'cpp ran {multiplier:.6f} times faster than python\n')
                
            outputfile.write('\n')
