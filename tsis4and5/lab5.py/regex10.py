import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
    return snake_case_string