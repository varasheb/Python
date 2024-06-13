# 9. Write a Python program to display formatted text (width=50) as output.
def format_text(s, width):
    formatted_text = ""
    line = ""
    for word in s.split():
        if len(line) + len(word) + 1 <= width:
            line += word + " "
        else:
            formatted_text += line.rstrip() + "\n"
            line = word + " "
    if line:
        formatted_text += line.rstrip()
    return formatted_text

def main():
    input_string = "This is an example of a very long string that needs to be formatted with a width of fifty characters."
    print(format_text(input_string, 50))
main()