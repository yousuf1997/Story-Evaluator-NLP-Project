
'''
    This class contains method to calculate the outlier and other utills
    https://articles.outlier.org/calculate-outlier-formula#section-what-is-the-outlier-formula
'''
import math


class OutlierUtill:
    def __init__(self):
        print("hello")

    def calculateOutlier(self, data: list):
        if len(data) == 0:
            return []

        ## sort the list
        data.sort()

        ## calculate Q1 : first quartile and up to next full int
        L = math.ceil((0.25) * len(data)) - 1
        Q1 = data[L]

        ## calculate Q3 : third quartile and up to next full int
        L2 = math.ceil((0.75) * len(data))
        Q3 = data[L2 - 1]

        ## Find the interquartile range, IQR.
        IQR = Q3 - Q1

        ## find upper boundary
        upperBound = Q3 + (1.5) * IQR

        ## find lower boundary
        lowerBound = Q1 - ((1.5) * IQR)

        return {"lowerBound": lowerBound, "upperBound" : upperBound}

