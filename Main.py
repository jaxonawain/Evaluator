import Validator


def validate(equation):
    validationObj = Validator.ValidationObj(equation)
    validationObj.validate_equation()

validate('(1+1)(1)')