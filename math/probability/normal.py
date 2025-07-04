#!/usr/bin/env python3
"""Normal distribution"""


class Normal:
    """Normal class that represents a normal distribution"""
    e = 2.7182818285
    π = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Class constructor

        data: is a list of the data to be used to estimate the distribution
        mean: is the mean of the distribution
        stddev: is the standard deviation of the distribution
        """
        self.mean = float(mean)
        self.stddev = float(stddev)
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            leng = len(data)
            self.mean = sum(data) / leng
            variance = sum((x - self.mean) ** 2 for x in data) / leng
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """Calculating the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculating the x-value of a given z-score"""
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """Calculating the value of the PDF for a given x-value"""
        stdd = self.stddev
        first_part = 1 / (stdd * ((self.π * 2) ** 0.5))
        second_part = self.e ** (self.z_score(x) ** 2 * -0.5)
        return first_part * second_part

    def erf(self, x):
        """Function that calculates the erf of x"""
        first_part = 2 / (self.π ** 0.5)
        second_part = (x - (x ** 3 / 3) + (x ** 5 / 10)
                       - (x ** 7 / 42) + (x ** 9 / 216))
        return first_part * second_part

    def cdf(self, x):
        """Function that calculates the value of the CDF for a given x-value"""
        z_score_modified = (x - self.mean) / (self.stddev * (2 ** 0.5))
        return 0.5 * (1 + self.erf(z_score_modified))
