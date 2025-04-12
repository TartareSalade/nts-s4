
from mathsutils import *
from drawing.line import Line
from lsystems.lsystem2d import *
from lsystems.lsystem3d import *
import random
from turtle import *

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

    """
    gen : string, where the turtle moove
    p : tuple[float, float] start position of the turtle

    """

    stack = []
    position = tuple

    for deplacement in gen:
        if deplacement == 'F' or deplacement == 'G':
            rotation_matrice = r2d(lsys.init_angle)
            new_position = move2d(tuple[0], tuple[1], rotation_matrice, lsys.d)
            new_line = Line(tuple, new_position)
            forward(lsys.d)
            stack.append(new_line)
            position = new_position

            #Move forward
        elif deplacement == '+':
            right(90)
            #Turn right
        elif deplacement == '-':
            #Turn left
            left(90)
        elif deplacement == '[':
            #Save the position on the stack
            stack.append((lsys.x0, lsys.y0))
        elif deplacement == ']':



    return stack


def axiomtoline3d(gen : str, p : tuple[float, float, float], lsys : LSystem3d) -> list[tuple[Line, int]]:
    pass
    
def axiomtoline3drand(gen : str, p : tuple[float, float, float], lsys : LSystem3d, randmax : float) -> list[tuple[Line, int]]:
    pass
