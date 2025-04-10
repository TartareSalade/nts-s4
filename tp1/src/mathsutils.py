from math import pi, cos, sin
from random import randint


def degreetorad(theta):
    """
    theta : float
    return the conversion in radian
    """
    return (theta * pi)/180

"""
def multmatvector(M: list[list[float]], X: list[float]):
    M : matrix of size n * m
    X : vector of size m
    return the product of M and X
    final = []
    for i in range (len(M)):
        res = []
        items = 0
        for j in range (len(X)):
            items += M[i][j] * X[j]
            res.append(items)
        final.append(res)
    return final

"""

def multmatvector(M: list[list[float]], X: list[float]):
    """
    M : matrix of size n * m
    X : vector of size m
    return the product of M and X (vector of size n)
    """
    results = []
    for i in range(len(M)):  
        total = 0
        for j in range(len(X)):  
            total += M[i][j] * X[j]
        results.append(total)
    return results



def __mat_init(l, c, val):
    M = []
    for i in range (l):
        M.append([])
        for j in range (c):
            M[i].append(val)
    return M


def multmat(M1: list[list[float]], M2: list[list[float]]):
    """
    M1 : matrix of size n * m
    M2 : matrix of size m * p
    return the product of M1 and M2
    
    Special case: If M2 has only one row, it handles a custom multiplication
    where the first row of result is element-wise product of M1[0] and M2[0],
    and subsequent rows are copies of M2.
    """
    m = len(M1)       # Number of rows in M1
    n = len(M1[0])    # Number of columns in M1
    p = len(M2[0])  
    M = __mat_init(m, p, 0)
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                M[i][j] = M[i][j] + M1[i][k] * M2[k][j]
    
    return M



def r2d(theta):
    """
    theta : angle in degrees
    return the 2d rotation matrix of angle theta
    """
    pass

def move2d(x, y, r, d):
    """
    x, y : initial position
    r : rotation matrix representing the current direction
    d : distance
    return the new coordinates
    """
    pass
    
def ru3d(theta):
    """
    theta : angle in degrees
    return the 3d rotation matrix of angle theta along the axis ru
    """
    pass
    
def rl3d(theta):
    """
    theta : angle in degrees
    return the 3d rotation matrix of angle theta along the axis rl
    """
    pass
    
def rh3d(theta):
    """
    theta : angle in degrees
    return the 3d rotation matrix of angle theta along the axis rh
    """
    pass

def move3d(x, y, z, r, d):
    """
    x, y, z : initial position
    r : rotation matrix representing the current direction
    d : distance
    return the new coordinates
    """
    pass
