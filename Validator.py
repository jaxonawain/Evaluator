class ValidationObj:
    global finalresult
    valid_characters = {'valid_chars': '()-+*/&^1234567890',
                        'start_chars': '-(1234567890',
                        'end_chars': ')1234567890',
                        'operators': '+-*^/'}


    def __init__(self, equation):
        self.equation = equation


    def validate_characters(self):
        for character in self.equation:
            if character not in self.valid_characters['valid_chars']:
                print('Invalid Character Detected.')
                return 'Error'
        return True


    def validate_paren_count(self):
        if str(self.equation).count('(') != str(self.equation).count(')'):
            print('Unbalanced Parenthesis Detected.')
            return 'Error'
        return True


    def validate_operator(self):
        i = 0
        for character in self.equation:
            if character in self.valid_characters['operators']:
                if self.equation[i + 1] in self.valid_characters['operators']:
                    print('No double operators')
                    return 'Error'
            i += 1
        return True


    def validate_paren_filled(self):
        i = 0
        for character in self.equation:
            if character == '(' and self.equation[i+1] == ')':
                print('cannot have empty parenthesis clauses.')
                return 'Error'
            i += 1
        return True


    def validate_paren_b2b(self):
        i = 0
        for character in self.equation:
            if character == ')' and self.equation[i+1] == '(':
                print('No back to back parenthesis.')
                return 'Error'
            i += 1
        return True


    def validate_first_char(self):
        if self.equation[0] not in self.valid_characters['start_chars']:
            print('Cannot have anything other than: number, -, or ( for the starting characters.')
            return 'Error'
        return True


    def validate_equation(self):
        self.validate_characters()
        self.validate_paren_count()
        self.validate_operator()
        self.validate_first_char()
        self.validate_paren_filled()
        self.validate_paren_b2b()