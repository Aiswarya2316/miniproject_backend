              #  find the reverse of a string in the list


strings_list = ['hello', 'world', 'python', 'heloooo','hello','example']
print(strings_list)
for string in strings_list:
    reversed_string = "  "
    for i in string:
        reversed_string =i+reversed_string
    print(reversed_string)
