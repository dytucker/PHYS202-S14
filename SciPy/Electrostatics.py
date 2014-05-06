
import numpy as np

def pointPotential(x,y,q,Xc,Yc):
    """
    Return the electric potential for a 
    point charge q at (Xc,Yc)
    
    Units returned are [Volts] if input 
    units are [meters] and [Coulombs]                                   
    """
    
    k = 8.987551787997912e9 #(Nm^2/C^2) 
    
    Vxy = k*q/np.sqrt(((x-Xc)**2 + (y-Yc)**2))
    return Vxy

def dipolePotential(x,y,q,d):
    Vxy=pointPotential(x,y,q,-d/2.,0.) + pointPotential(x,y,-q,+d/2.,0.)
    return Vxy