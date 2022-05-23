def converter():
    input_degree = input("""
            Sometimes the weather can be frustrating.
            Especially if you got lost in degrees.
            But this converter should help you!

            Enter 'f' if you want to convert Fahrenheit to Celsius
            Enter 'c' if you want to convert Celsius to Fahrenheit. \n """)
    if input_degree == 'f':
        input_degree_c = int(input('How many degrees are there? \n '))
        count_c = (input_degree_c - 32) * 5/9
        print(input_degree_c, 'degrees in Fahrenheit is ',
              round(count_c), 'in Celsius')
    elif input_degree == 'c':
        input_degree_f = int(input('How many degrees are there? \n '))
        count_f = 9/5 * input_degree_f + 32
        print(input_degree_f, 'degrees in Celsius is ',
              round(count_f), 'in Fahrenheit')
    else:
        print('Please use letters "c" or "f" \n ')
        converter()


def main():
    converter()


if __name__ == "__main__":
    main()
