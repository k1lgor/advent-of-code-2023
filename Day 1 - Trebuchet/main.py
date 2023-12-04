def extract_digits(input_lines):
    digits = []
    for line in input_lines:
        digits_only = [char for char in line if char.isdigit()]
        if digits_only:
            first_digit = int(digits_only[0])
            last_digit = int(digits_only[-1])
            calibration_value = first_digit * 10 + last_digit
            digits.append(calibration_value)

    return digits


def main():
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line)

    return sum(extract_digits(input_lines))


if __name__ == "__main__":
    print(main())
