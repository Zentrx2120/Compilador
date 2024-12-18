import p_base

while True:
	text = input('p_base > ')
	if text.strip() == "": continue
	result, error = p_base.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
