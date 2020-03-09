class ParseObj:
    def __init__(self, equation):
        self.equation = equation

    def parse_to_list(self):
        ints = '1234567890'
        intbuffer = []
        return_result = []
        for character in self.equation:
            if character in ints:
                intbuffer.extend(character)
            else:
                if intbuffer:
                    return_result.append(float(''.join(intbuffer)))
                    intbuffer = []
                return_result.append(character)
        if intbuffer:
            return_result.append(float(''.join(intbuffer)))
        return return_result

    def parse_equation(self):
        return_list = self.parse_to_list()
        return return_list