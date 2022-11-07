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


if __name__ == "__main__":
    print(calculate_fizzbuzz(30))
