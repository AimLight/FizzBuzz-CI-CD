"""Function to solve the fizzbuzz problem."""


def fizz_buzz(num: int) -> str:
    """This is my great and neat function to solve the famous
    Fizz Buzz problem.
    :param num: That's the number which we want the answer for

    :return: fizz, buzz, fizzbuzz or the number itself
    """
    if num % 15 == 0:
        return "fizzbuzz"
    if num % 5 == 0:
        return "buzz"
    if num % 3 == 0:
        return "fizz"
    return str(num)
