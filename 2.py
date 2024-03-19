def count_char_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def print_char_frequency(frequency):
    print("Character frequency:")
    for char, freq in frequency.items():
        print(f"{char}: {freq}")

input_string = input("Enter a string: ")
char_frequency = count_char_frequency(input_string)
print_char_frequency(char_frequency)