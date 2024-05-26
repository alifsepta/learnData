def interpret(command):
    # Replace '()' with 'o' and '(al)' with 'al'
    interpreted = command.replace("()", "o").replace("(al)", "al")
    return interpreted

# Test cases
command1 = "G()(al)"
print(interpret(command1))  # Output: "Goal"

command2 = "G()()()()(al)"
print(interpret(command2))  # Output: "Gooooal"

command3 = "(al)G(al)()()G"
print(interpret(command3))  # Output: "alGalooG"
