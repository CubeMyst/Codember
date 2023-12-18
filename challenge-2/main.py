def mini_compiler(input_str: str) -> str:
    numeric_value = 0
    output = []

    for symbol in input_str:
        if symbol == "#":
            numeric_value += 1
        elif symbol == "@":
            numeric_value -= 1
        elif symbol == "*":
            numeric_value *= numeric_value
        elif symbol == "&":
            output.append(str(numeric_value))

    return ''.join(output)

input_str = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"
output_str = mini_compiler(input_str)
print(output_str)