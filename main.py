import sys


DEGREES_TYPES_LIST = {
    "f": "Fahrenheit",
    "c": "Celsius",
}
ROUND = 0
LIMIT = 3
LIMIT_MSG = "The limit of attempts is exceeded"


def fahrenheit_converter(num: int) -> int:
    result = (num - 32) * 5 / 9
    return result


def celsius_converter(num: int) -> int:
    result = 9 / 5 * num + 32
    return result


def converter(degrees_type: str, degrees: int, round_result: int = ROUND) -> int:
    if degrees_type == "c":
        result = celsius_converter(degrees)
    elif degrees_type == "f":
        result = fahrenheit_converter(degrees)
    else:
        raise Exception(f"Converter error: unexpected degrees type: {degrees_type}")

    if round_result == 0:
        result = int(round(result, round_result))
    else:
        result = round(result, round_result)
    return result


def get_degrees() -> int:
    degrees = input("How many degrees are there?\n ")
    count = 0
    while not degrees.isdigit():
        count += 1
        if degrees == "q":
            print("Try again later!")
            sys.exit()

        if count == LIMIT:
            print(LIMIT_MSG)
            sys.exit()

        degrees = input('Please, use integer or "q" to quit.\n')

    return int(degrees)


def get_degrees_type() -> str:
    degrees_type = input(
        """
            Sometimes the weather can be frustrating.
            Especially if you got lost in degrees.
            But this converter should help you!

            Enter 'f' if you want to convert Fahrenheit to Celsius
            Enter 'c' if you want to convert Celsius to Fahrenheit.\n
        """
    )
    count = 0
    while degrees_type not in DEGREES_TYPES_LIST.keys():
        count += 1
        if degrees_type == "q":
            print("Try again later")
            sys.exit()

        if count == LIMIT_MSG:
            print(LIMIT_MSG)
            sys.exit()

        degrees_type = input('Please use letters "c" or "f". Or "q" to quit.\n')
    return degrees_type


def main():
    degrees_type = get_degrees_type()
    degrees = get_degrees()

    result = converter(degrees_type, degrees)

    convert_to = DEGREES_TYPES_LIST.keys() - degrees_type
    convert_to = DEGREES_TYPES_LIST.get(convert_to.pop())

    degrees_type = DEGREES_TYPES_LIST.get(degrees_type)

    print(f"{degrees} degrees in {degrees_type} is " f"{result} in {convert_to}")


if __name__ == "__main__":
    main()
