class ValidationObj:
    global finalresult
    '''Set Valid Characters dictionary to refer to during function calls'''
    valid_characters = {'valid_chars': '()-+*/&^1234567890',
                        'start_chars': '-(1234567890',
                        'end_chars': ')1234567890',
                        'operators': '+-*^/'}


    def __init__(self, equation):
        self.equation = equation


    def validate_characters(self):
        '''Verify that there is no invalid characters'''
        for character in self.equation:
            if character not in self.valid_characters['valid_chars']:
                print('Invalid Character Detected.')
                exit()
        return True


    def validate_paren_count(self):
        '''Validate that there are not more open parenthesis than close parenthesis, or vice versa'''
        if str(self.equation).count('(') != str(self.equation).count(')'):
            print('Unbalanced Parenthesis Count Detected.')
            exit()
        print(f"There are {str(self.equation).count('(')} open parenthesis, and {str(self.equation).count(')')} closed parenthesis")
        return True


    def validate_operator(self):
        '''Validate that there are no double operators.'''
        i = 0
        for character in self.equation:
            if character in self.valid_characters['operators']:
                    if self.equation[i + 1] in self.valid_characters['operators']:
                        print('No double operators')
                        exit()
            i += 1
        return True


    def validate_paren_content_exist(self):
        '''Verify that there are no empty parenthesis'''
        i = 0
        for character in self.equation:
            if character == '(' and self.equation[i+1] == ')':
                print('cannot have empty parenthesis clauses.')
                exit()
            i += 1
        return True


    def validate_paren_b2b(self):
        '''Validate that there are no back to back parenthesis ")(" Generally, these are used to indicate multiplication. However fuck that.'''
        i = 0
        for character in self.equation[:len(self.equation) - 1]:
            if character == ')' and self.equation[i+1] == '(':
                print('No back to back parenthesis.')
                exit()
            i += 1
        return True


    def validate_last_char(self):
        '''Validate the last character in the equation is legal'''
        if self.equation[-1] not in self.valid_characters['end_chars']:
            print('Invalid Last Character')
            exit()
        return True

    def validate_first_char(self):
        '''Validate that the first character is legal'''
        if self.equation[0] not in self.valid_characters['start_chars']:
            print('Cannot have anything other than: number, -, or ( for the starting characters.')
            exit()
        return True


    def validate_equation(self):
        self.validate_characters()
        self.validate_paren_count()
        self.validate_last_char()
        self.validate_operator()
        self.validate_first_char()
        self.validate_paren_content_exist()
        self.validate_paren_b2b()
        return self.equation
