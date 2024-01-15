def num_to_words_digit_group(N):
    const_hundred = " Hundred"
    const_one = " One"
    const_two = " Two"
    const_three = " Three"
    const_four = " Four"
    const_five = " Five"
    const_six = " Six"
    const_seven = " Seven"
    const_eight = " Eight"
    const_nine = " Nine"

    buf = ""
    flag = False

    if N // 100 != 0:
        case = N // 100
        if case == 0:
            buf = ""
            flag = False
        else:
            buf = {
                1: const_one,
                2: const_two,
                3: const_three,
                4: const_four,
                5: const_five,
                6: const_six,
                7: const_seven,
                8: const_eight,
                9: const_nine,
            }[case] + const_hundred
            flag = True

    if flag is not False:
        N = N % 100

    if N > 0:
        if flag is not False:
            buf += " "
    else:
        return buf

    if N // 10 != 0:
        case = N // 10
        if case in [0, 1]:
            flag = False
        else:
            buf += {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety",
            }[case]
            flag = True

    if flag is not False:
        N = N % 10

    if N > 0:
        if flag is not False:
            buf += " "

    else:
        return buf

    buf += {
        0: "",
        1: const_one,
        2: const_two,
        3: const_three,
        4: const_four,
        5: const_five,
        6: const_six,
        7: const_seven,
        8: const_eight,
        9: const_nine,
        10: " Ten",
        11: " Eleven",
        12: " Twelve",
        13: " Thirteen",
        14: " Fourteen",
        15: " Fifteen",
        16: " Sixteen",
        17: " Seventeen",
        18: " Eighteen",
        19: " Nineteen",
    }[N]

    return buf

def convert_to_indian_numbering_system(number):
    ten = 10
    hundred = ten * ten
    thousand = ten * hundred
    lakh = thousand * hundred
    crore = lakh * hundred

    if number == 0:
        return "Rupees Zero Only"

    result = "Rupees "
    if number < 0:
        result = "Negative Rupees "
        number = abs(number)

    crore_part = int(number / crore)
    if crore_part > 0:
        result += num_to_words_digit_group(crore_part) + " Crore "
        number %= crore

    lakh_part = int(number / lakh)
    if lakh_part > 0:
        result += num_to_words_digit_group(lakh_part) + " Lakh "
        number %= lakh

    thousand_part = int(number / thousand)
    if thousand_part > 0:
        result += num_to_words_digit_group(thousand_part) + " Thousand "
        number %= thousand

    hundred_part = int(number / hundred)
    if hundred_part > 0:
        result += num_to_words_digit_group(hundred_part) + " Hundred "
        number %= hundred

    if number > 0:
        result += num_to_words_digit_group(number)

    return ' '.join(result.split()).strip() + " Only"

def main():
    while True:
        try:
            number = float(input("Enter a number (or any non-numeric value to end): "))
        except ValueError:
            print("Exiting the program. Thank you!")
            break

        result = convert_to_indian_numbering_system(number)
        print(result)

if __name__ == "__main__":
    main()
