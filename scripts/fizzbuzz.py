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


class FizzBuzz:

    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def convert_range_to_fizzbuzz(self):
        return [calculate_fizzbuzz(i) for i in range(1, self.upper_limit + 1)]


if __name__ == "__main__":
    print(FizzBuzz(20).convert_range_to_fizzbuzz())
