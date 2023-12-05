for i in range(100):
    if i <= 9:
        print( f"0{i}, ", end= " ")
    elif i == 99:
        print(i)
    else:
        print(f"{i}, ", end= " ")


character = input("Please enter the pattern to be printed: ")
count = 0
for j in character:
    count += 1
for i in [1, 3, 5, 7, 9]:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        print("Vowels are not allowed in the input")
        break
    elif count > 1:
        print("The length of the character should be 1")
        break
    else:
        print(character * i)


palindrome = input("Please enter the word to check it palindrome or not: ")
palindrome_split = []
for i in palindrome:
    palindrome_split.append(i)
palindrome_split.reverse()
palindrome_string = ""
for i in palindrome_split:
    palindrome_string += i
if palindrome == palindrome_string:
    print(f"The word {palindrome} is a palindrome.")
else:
    print(f"The word {palindrome} is not a palindrome because {palindrome_string} is not equal to {palindrome}")


number_dictionary = {
    6: "Three",
    10: "Five",
    12: "Three",
    18: "Three",
    20: "Five",
    24: "Three",
    30: "Three and Five",
    36: "Three",
    40: "Five",
    42: "Three",
    48: "Three",
    50: "Five"
}
total_sum = 0
count_three_or_five = 0
for i in range(51):
    number = i % 2
    if number == 0:
        if i == 6 or i == 10 or i == 12 or i == 18 or i == 20 or i == 24 or i == 30 or i == 36 or i == 40 or i == 42 or i == 48:
            count_three_or_five += 1
            print(f"{number_dictionary[i]} + ", end= " ")
        elif i == 50:
            count_three_or_five += 1
            print(f"{number_dictionary[i]} = ")
        else:
            print(f"{i} + ", end= " ")
        total_sum += i

print(f"Total sum: {total_sum}")
print(f"The number of the multiple of 3 or 5 is: {count_three_or_five}")


