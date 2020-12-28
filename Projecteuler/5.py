""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """


def primeFactors(number):
    if number == 1:
        return 1
    array = []
    while number % 2 == 0:
        array.append(2)
        number = number/2

    for i in range(2, int(number**0.5)+1):
        while number % i == 0:
            array.append(i)
            number = number/i

    if number > 2:
        array.append(int(number))

    return array


number = 1
primefactors = []
for i in range(1, 21):
    primefactors.append(primeFactors(i))
print(primefactors)
