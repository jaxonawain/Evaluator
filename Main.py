import Validator, Parser, Evaluator


def validate(equation):
    '''Creates a validation object and runs it through the validate function to validate grammar'''
    validationObj = Validator.ValidationObj(equation)
    return_result = validationObj.validate_equation()
    if return_result:
        return return_result


def parse(equation):
    '''Creates a parser object to parse a validated equation into a list'''
    parserObj = Parser.ParseObj(equation)
    return_result = parserObj.parse_equation()
    if return_result:
        return return_result

def evaluate(equation):
    '''Creates an evaluation object to evaluate a parsed and validated object'''

if __name__ == '__main__':
    '''Set two lists to use in main decision loop'''
    acceptable_acceptance = ['Y','y','yes','Yes','YES','YEs','yES','yeS','yea','yeboeyy']
    acceptable_decline = ['N','n','No','NO','Exit','hells naw', 'no', 'nO']


    '''Main program to achieve evaluation'''
    def start_evaluation():
        equation = input("Enter an Eequation: ")
        valid_equation = validate(equation)
        parsed_equation = parse(valid_equation)
    #    final_result = evaluate(parsed_equation)
        print(parsed_equation)

    '''Main loop to decide to quit or keep evaluating'''
    def start_main_loop():
        main_loop_start = input('Would you like to solve an equation?')
        while main_loop_start not in acceptable_decline:
            if main_loop_start in acceptable_acceptance:
                start_evaluation()
                start_main_loop()
            else:
                print('Unacceptable Input, please try again')
                start_main_loop()
        if main_loop_start in acceptable_decline:
            print("Got it. Exiting")
            exit()

    start_main_loop()