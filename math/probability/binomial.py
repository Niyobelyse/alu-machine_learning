#!/usr/bin/env python3
"""Initialize Binomial, normal distribution"""


class Binomial:
    """Class that represents a binomial distribution"""
    e = 2.7182818285
    π = 3.1415926536

    def __init__(self, data=None, n=1, p=0.5):
        """Class constructor

        data: is a list of the data to be used to estimate the distribution
        n: is the number of Bernoulli trials
        p: is the probability of a success
        """
        self.n = int(n)
        self.p = float(p)

        if data is None:
            if n < 1:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            dev = sum(((x - mean) ** 2) for x in data) / len(data)
            self.p = 1 - (dev / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n

    def pmf(self, k):
        """Function that calculates the value of the PMF for a given number
        of successes

        k: is the number of successes

        Return: the PMF value for k"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        firstPart = self.factorial(self.n) / (
            self.factorial(k) * self.factorial(self.n - k))
        secondPart = (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return firstPart * secondPart

    def cdf(self, k):
        """Function that calculates the value of the CDF for a given number
        of successes

        k: is the number of successes

        return the CDF value for k"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))

    def factorial(self, x):
        """Function that calculates the factorial of x"""
        result = 1
        for n in range(1, x + 1):
            result *= n
        return result
