def fizzbuzz(i):
    output = ""

    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"

    if output:
        return output
    else:
        return i
