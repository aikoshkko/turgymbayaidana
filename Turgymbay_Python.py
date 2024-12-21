def check_number(number):
    if number > 7:
        print("Hello")


def check_name(name):
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def print_multiples_of_three(array):
    multiples = [x for x in array if x % 3 == 0]
    print("Multiples of 3:", multiples)


def main():
    number = int(input("Enter a number: "))
    check_number(number)

    name = input("Enter a name: ")
    check_name(name)

    # Input for numeric array
    array = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    print_multiples_of_three(array)


if __name__ == "__main__":
    main()