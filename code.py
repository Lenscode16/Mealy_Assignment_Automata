
# Mealy Machine for C-style Comments
# A valid comment starts with /* and ends with */
# By Earl Lenser B. Bolansoy

def mealy_machine(input_string):
    state = "q0"
    output = ""

    transitions = {
        "q0": {
            "/": ("q1", "0"),
            "a": ("qd", "0"),
            "*": ("qd", "0")
        },
        "q1": {
            "*": ("q2", "0"),
            "/": ("qd", "0"),
            "a": ("qd", "0")
        },
        "q2": {
            "a": ("q2", "0"),
            "/": ("q2", "0"),
            "*": ("q3", "0")
        },
        "q3": {
            "a": ("q2", "0"),
            "*": ("q3", "0"),
            "/": ("q4", "1")
        },
        "q4": {
            "a": ("qd", "0"),
            "/": ("qd", "0"),
            "*": ("qd", "0")
        },
        "qd": {
            "a": ("qd", "0"),
            "/": ("qd", "0"),
            "*": ("qd", "0")
        }
    }

    for symbol in input_string:
        # Treat any character other than * and / as a
        if symbol not in ["*", "/"]:
            symbol = "a"

        state, result = transitions[state][symbol]
        output += result

    print("Input:", input_string)
    print("Output:", output)

    if state == "q4":
        print("Result: Valid C-style comment")
    else:
        print("Result: Invalid C-style comment")


# Test the Mealy Machine
mealy_machine("/*a*/")
mealy_machine("/**/")
mealy_machine("/*hello world*/")
mealy_machine("/*hello")
mealy_machine("hello")
