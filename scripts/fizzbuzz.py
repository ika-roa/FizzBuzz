def calculate_fizzbuzz(i):
    output = ""

    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"

    if output:
        return output
    else:
        return i


def convert_range_to_fizzbuzz(upper_limit):
    return [calculate_fizzbuzz(i) for i in range(1, upper_limit+1)]


if __name__ == "__main__":
    print(convert_range_to_fizzbuzz(30))
