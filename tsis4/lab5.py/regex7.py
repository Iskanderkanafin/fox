def snake_to_camel(snake_case_string):
    parts = snake_case_string.split('_')
    camel_case_string = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    return camel_case_string