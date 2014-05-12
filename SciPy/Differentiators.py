
import numpy as np

def twoPtForwardDiff(x,y):
    """function takes the dy/dx of element ahead of current point
    Function takes the backwards difference at the last poin"""
    
    dydx = np.zeros(len(x))
    
    dydx[0:-1] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    return dydx

def twoPtCenteredDiff(x,y):
    """function takes the slope of the line between the two
    points above and below it. the first and last points
    are calculated using the regular forwards and backward
    derivatives though"""
    
    dydx = np.zeros(len(x))
    
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])

    return dydx

def fourPtCenteredDiff(x,y):
    
    """function computes the derivative at a point by using
    a formula involving the two terms above and below it
    and the taylor expansion"""
    
    difference = max(np.diff(x))
    
    dydx = np.zeros(len(x))
    
    dydx[1] = (y[2] - y[0])/(x[2] - x[0])
    
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    dydx[-2] = (y[-1] - y[-3])/(x[-1] - x[-3])
    
    dydx[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1]
                  - y[4:])/(12*difference)
    
    return dydx