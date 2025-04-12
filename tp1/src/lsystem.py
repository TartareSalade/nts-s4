
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
    gen : string, where the turtle moves
    p : tuple[float, float] start position of the turtle
    """
    stack = []
    lines = []
    position = p 
    angle = lsys.l_angle

    for deplacement in gen:
        if deplacement == 'F' or deplacement == 'G':
            rotation_matrix = r2d(lsys.l_angle)
            new_position = move2d(position[0], position[1], rotation_matrix , lsys.d)
            line = Line(position, new_position)
            lines.append(line)
            position = new_position
        elif deplacement == '+':
            angle += lsys.l_angle
        elif deplacement == '-':
            angle += lsys.r_angle
        elif deplacement == '[':
            stack.append((position, angle))
        elif deplacement == ']':
            if stack:
                position, angle = stack.pop()

    return lines

def axiomtoline3d(gen : str, p : tuple[float, float, float], lsys : LSystem3d) -> list[tuple[Line, int]]:
    pass
    
def axiomtoline3drand(gen : str, p : tuple[float, float, float], lsys : LSystem3d, randmax : float) -> list[tuple[Line, int]]:
    pass
