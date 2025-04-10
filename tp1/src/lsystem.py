
from mathsutils import *
from drawing.line import Line
from lsystems.lsystem2d import *
from lsystems.lsystem3d import *
import random

def derivation(axiom, rules):
    """
    axiom : string
    rules : dictionary
    return the result of the derivation
    """
    res = "" 
    for c in axiom:
        if c in rules:
            res += rules.get(c)
        else:
            res += c 
    return res


def generation(axiom, rules, n):
    """
    axiom : string
    rules : dictionary
    n : integer
    return the result of n successive derivations
    """
    for i in range (n):
        axiom = derivation(axiom, rules)
    return axiom
    
def axiomtoline2d(gen : str, p : tuple[float, float], lsys : LSystem2d) -> list[Line]:
    pass

def axiomtoline3d(gen : str, p : tuple[float, float, float], lsys : LSystem3d) -> list[tuple[Line, int]]:
    pass
    
def axiomtoline3drand(gen : str, p : tuple[float, float, float], lsys : LSystem3d, randmax : float) -> list[tuple[Line, int]]:
    pass
