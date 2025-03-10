def count_letters_and_digits(string_of_bob):
    number_of_letter_digits = 0
    notis_letter_digits = [
        '.', ',', ';', ':', '/', '?', '|', '\\', '!', '@', '#', '$',
        '%', '¨', '&', '*', '(', ')', '-', '_', '+', '=', '§', '[', ']',
        '{', '}', 'ª', 'º', '°', '´', '`', '~', '^'
    ]
    for letter in string_of_bob:
        if letter not in notis_letter_digits:
            number_of_letter_digits += 1
            print('is letter/digit')
        else:
            print('is not letter/digit')
            continue
    
    return number_of_letter_digits

string = 'eklsja lahskfda **j'
str_length = len(string)
number = count_letters_and_digits(string)
print(f'string: {string}\n string length: {str_length}\n number of letter/digits: {number}')
        