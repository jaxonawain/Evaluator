equation = [1.0, '-', 1.0, '*', 5.0, '+', 9.0]

def emdas(equation):
    def concatenate(result, equation, index):
        equation.insert(index-1, result)
        del equation[index:index+3]
        while len(equation) != 1:
            exp(equation)
        fin(equation)


    def exp(equation):
        index = 0
        for character in equation:
            if character == '^':
                result = equation[index-1] ** equation[index+1]
                concatenate(result, equation, index)
            index += 1
        multidiv(equation)


    def multidiv(equation):
        index = 0
        for item in equation:
            if item == '*' or item == '/':
                if item == '*':
                    result = equation[index - 1] * equation[index + 1]
                    concatenate(result, equation, index)
                if item == '/':
                    result = equation[index - 1] / equation[index + 1]
                    concatenate(result, equation, index)
            index += 1
        addtract(equation)


    def addtract(equation):
        index = 0
        for item in equation:
            if item == '+' or item == '-':
                if item == '+':
                    result = equation[index - 1] + equation[index + 1]
                    concatenate(result, equation, index)
                if item == '-':
                    result = equation[index - 1] - equation[index + 1]
                    concatenate(result, equation, index)
            index += 1


    def fin(equation):
        global part_result
        part_result = equation


    exp(equation)
    return part_result


def parens(equation):
    i = -1
    end_paren = equation.index(')')








#print(emdas(equation))