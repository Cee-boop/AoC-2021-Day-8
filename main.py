with open(file='data.txt') as file:
    data = file.read().split("\n")

total_value = 0
unique_digits = 0

for entry in data:
    decode = entry.split(" | ")
    digits, output = sorted(decode[0].split(" "), key=len), decode[1].split(" ")
    number_map = {
        "0": None,
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
        "6": None,
        "7": None,
        "8": None,
        "9": None
    }

    # find unique numbers:
    for digit in digits:
        for letter in digit:
            if len(digit) == 2:
                number_map["1"] = digit
            elif len(digit) == 3:
                number_map["7"] = digit
            elif len(digit) == 4:
                number_map["4"] = digit
            elif len(digit) == 7:
                number_map["8"] = digit

    # FIND 3:
    three_count = 0
    for digit in digits:
        if len(digit) == 5:

            for letter in digit:
                if letter in number_map["7"]:
                    three_count += 1
                    if three_count == 3:
                        number_map["3"] = digit
                        digits.remove(digit)

            if three_count < 3:
                three_count = 0

    # FIND 9:
    nine_count = 0
    for digit in digits:
        if len(digit) == 6:

            for letter in number_map["3"]:
                if letter in digit:
                    nine_count += 1
                    if nine_count == 5:
                        number_map["9"] = digit
                        digits.remove(digit)

            if nine_count < 5:
                nine_count = 0

    # FIND 0:
    zero_count = 0
    for digit in digits:
        if len(digit) == 6:

            for letter in digit:
                if letter in number_map["7"]:
                    zero_count += 1
                    if zero_count == 3:
                        number_map["0"] = digit
                        digits.remove(digit)

            if zero_count < 3:
                zero_count = 0

    # FIND 6:
    six_count = 0
    for digit in digits:
        if len(digit) == 6:

            for letter in digit:
                if letter in number_map["8"]:
                    six_count += 1
                    if six_count == 6:
                        number_map["6"] = digit
                        digits.remove(digit)

            if six_count < 6:
                six_count = 0

    # FIND 5:
    five_count = 0
    for digit in digits:
        if len(digit) == 5:

            for letter in digit:
                if letter in number_map["6"]:
                    five_count += 1
                    if five_count == 5:
                        number_map["5"] = digit
                        digits.remove(digit)

            if five_count < 5:
                five_count = 0

    # FIND 2:
    for digit in digits:
        if len(digit) == 5:
            number_map["2"] = digit

    output_value = ""
    for number in output:
        if len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7:
            unique_digits += 1

        for k, v in number_map.items():
            if sorted(number_map[k]) == sorted(number):
                output_value += k

    total_value += int(output_value)

# part one:
print(unique_digits)
# part two:
print(total_value)
