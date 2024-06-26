              #  find the reverse of a string in the list


strings_list = ['hello', 'world', 'python', 'heloooo','hello','example']
print(strings_list)
for string in strings_list:
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    print(reversed_string)
