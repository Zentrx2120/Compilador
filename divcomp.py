import p_base

def compile_code(code):
    if code.strip() == "":
        return None, None

    result, error = p_base.run('<stdin>', code)

    return result, error

def display_result(result, error):
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))

while True:
    text = input('p_base > ')
    result, error = compile_code(text)
    display_result(result, error)
