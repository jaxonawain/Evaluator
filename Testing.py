equation_with_paren = ['(', 1.0, '+', '(', 1.0, '-', 1.0, ')', ')']
equation_with_paren = ['(', 1.0, '+', 1, '(', 1.0, '-', 1.0, ')', ')']
equation1 = [1.0, '*', 3.0, '^', 2.0]

def get_inner_indices(equation):
    return_result = []
    end_paren_index = equation.index(')')
    start_paren_index = max(i for i, character in enumerate(equation) if character == '(')
    return_result.append(start_paren_index)
    return_result.append(end_paren_index)
    return return_result

def get_inner_equation(equation, indices):
    start = indices[0] + 1
    stop = indices[1]
    return equation[start:stop]

def restruction(equation, result, indices):
    start = indices[0]
    stop = indices[1] + 2
    equation.insert(start, result)
    del equation[start:stop]
    return equation


print(restruction(equation_with_paren, 1, get_inner_indices(equation_with_paren)))