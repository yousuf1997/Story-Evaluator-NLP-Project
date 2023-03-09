import math

'''
    This class represents utils methods for vectors
'''

class VectorUtill:

    def __init__(self):
        pass


    # this method computes the consine simalarity
    def computeCosineSimilarity(self, vector1: list, vector2: list):
        vec1len = len(vector1)
        vec2len = len(vector2)
        ## make sure both of the vectors are same size
        ## otherwise append zeros if they are not same
        if vec1len != vec2len:
            if vec1len > vec2len:
                for i in range(vec1len - vec2len):
                    vector2.append(0)
            else:
                for i in range(vec2len - vec1len):
                    vector1.append(0)
        ## compute the cross product
        ## bottom portion (length)
        vec1Squared = 0
        vec2Squared = 0
        crossProduct = 0
        squareRootAndMultiplied = 0
        for index in range(len(vector1)):
            crossProduct = crossProduct + vector1[index] * vector2[index]
            vec1Squared = vec1Squared + math.pow(vector1[index], 2)
            vec2Squared = vec2Squared + math.pow(vector2[index], 2)
        ## cosine simularity
        return crossProduct / (math.sqrt(vec1Squared) * math.sqrt(vec2Squared))

    ## this method gets list of vectors, and computes average vector
    def computeAverageVector(self, vectors: list):
        if len(vectors) == 0:
            return 0.0

        xIndex = 0
        xLength = len(vectors[0])
        yLength = len(vectors)
        averageVector = []

        while xIndex < xLength:
            yIndex = 0
            sum = 0.0
            while yIndex < yLength:
                sum = sum + vectors[yIndex][xIndex]
                yIndex = yIndex + 1
            average = float(sum / yIndex)
            ## add the sum to the average vector
            averageVector.append(average)
            xIndex = xIndex + 1
        return averageVector

    '''The following method adds two equal size vector'''
    def addVectorOfEqualSize(self,vector1, vector2):
        if len(vector1) == 0 and len(vector2) == 0:
            return []
        if len(vector1) == 0 and len(vector2) != 0:
            return vector2
        if len(vector1) != 0 and len(vector2) == 0:
            return vector1
        length = len(vector2)
        rVector = []
        for i in range(length):
            rVector.append(float(vector1[i] + vector2[i]))
        return rVector

        ## helper method to perform vector arithmetic
    def performVectorArthimetic(self,vector1, vector2, operation):
        if len(vector1) == 0 and len(vector2) == 0:
            return []
        if len(vector1) == 0 and len(vector2) != 0:
            return vector2
        if len(vector1) != 0 and len(vector2) == 0:
            return vector1

        vecIndex1 = 0
        vecIndex2 = 0
        result = []

        while vecIndex1 < len(vector1) and vecIndex2 < len(vector2):
            result.append(self._operation(vector1[vecIndex1], vector2[vecIndex2], operation))
            vecIndex1 = vecIndex1 + 1
            vecIndex2 = vecIndex2 + 1

        return result

    def _operation(self, num1, num2, operation):
        if operation == "ADD":
            return num1 + num2
        if operation == "SUB":
            return num1 - num2
