#Escape sequence
print("Hello\nWorld")  # Hello and World will be printed in different lines
print("Hello\tWorld")  # Hello and World will be separated by a tab space
print("Hello\\World")  # Hello\World will be printed with a single backslash
print("She said, \"Hello!\"")  # She said, "Hello!" will be printed with double quotes
print('It\'s a nice day!')  # It's a nice day! will be
# printed with a single quote
print("This is a backslash: \\")  # This is a backslash: \ will be printed with a single backslash
print("First Line\rSecond Line")  # Second Line will overwrite First Line
print("Column1\bColumn2")  # Column2 will overwrite Column1 at the back
print("This is a form feed\fNew Page")  # New Page will be printed on a new page (form feed)
print("This is a vertical tab\vNew Line")  # New Line will be printed on a new line (vertical tab)
print("This is a carriage return\rNew Line")  # New Line will overwrite the beginning of the line
print("This is a backspace\bNew Line")  # New Line will overwrite the last character of the line

# print("This is a raw string: r\"Hello\\nWorld\"")  # This is a raw string: r"Hello\nWorld" will be printed without interpreting escape sequences

print("Hello\n\tWorld")  # Hello and World will be printed in different lines