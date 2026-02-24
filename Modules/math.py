import math
## MATH MODULE
## Adds extra math opcodes
def mcube(stk, regs, args):
    v = stk.pop()
    stk.push(v**3)
    return 1
def mcbrt(stk, regs, args):
    v = stk.pop()
    stk.push(round(v ** (1/3)))
    return 1
def msin(stk, regs, args):
    v = stk.pop()
    stk.push(round(math.sin(math.radians(v))*1000))
    return 1
def mcos(stk, regs, args):
    v = stk.pop()
    stk.push(round(math.cos(math.radians(v))*1000))
    return 1
def mtan(stk, regs, args):
    v = stk.pop()
    stk.push(round(math.tan(math.radians(v))*1000))
    return 1
def mabs(stk, regs, args):
    v = stk.pop()
    stk.push(abs(v))
    return 1
def mpi(stk, regs, args):
    stk.push(round(math.pi*1000))
    return 1
def me(stk, regs, args):
    stk.push(round(math.e*1000))
    return 1
def msign(stk, regs, args):
    v = stk.pop()
    stk.push(int(math.copysign(1, v)))
    return 1
opcodes = {
    "***": mcube,
    "\\\\": mcbrt,
    "SIN": msin,
    "COS": mcos,
    "TAN": mtan,
    "ABS": mabs,
    "PI": mpi,
    "M:E": me,
    "SGN": msign,
}