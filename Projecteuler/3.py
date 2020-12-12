""" The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? """


def primeFactors(number):
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


print(primeFactors(600851475143))


