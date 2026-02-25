## MORE MATH
## Adds more math ops
import math
description = "Simple math module that adds more math opcodes."
def msin(stk, regs, args):
    v = stk.pop()
    stk.push(round(math.sin(math.radians(v*1000))))
    return 1
def mcos(stk, regs, args):
    v = stk.pop()
    stk.push(round(math.cos(math.radians(v*1000))))
    return 1
def mtan(stk, regs, args):
    v = stk.pop()
    stk.push(round(math.tan(math.radians(v*1000))))
    return 1
def mcube(stk, regs, args):
    v = stk.pop()
    stk.push(v**3)
    return 1
def mcbrt(stk, regs, args):
    v = stk.pop()
    stk.push(round((v*(1/3))*1000))
    return 1
def msign(stk, regs, args):
    v = stk.pop()
    stk.push(int(math.copysign(1,v)))
    return 1
def mabs(stk, regs, args):
    v = stk.pop()
    stk.push(abs(v))
    return 1
def mpi(stk,regs,args):
    stk.push(round(math.pi*1000))
def me(stk,regs,args):
    stk.push(round(math.e*1000))

## info sect
### SIN
msin.usage = "SIN"
msin.description = "SIN trigonometry function. Pops a value, *1000 and convert to radians, and apply the SIN func. (round(math.sin(math.radians(v*1000))))"
### COS
mcos.usage = "COS"
mcos.description = "COS trigonometry function. Pops a value, *1000 and convert to radians, and apply the COS func. (round(math.cos(math.radians(v*1000))))"
### TAN
mtan.usage = "TAN"
mtan.description = "TAN trigonometry function. Pops a value, *1000 and convert to radians, and apply the TAN func. (round(math.tan(math.radians(v*1000))))"
### CUBE
mcube.usage = "***"
mcube.description = "Pops a value and cubes it. (v*v*v)/(v**3)"
### CBRT
mcbrt.usage = "\\\\"
mcbrt.description = "Pops a value and gets the cube root of it. (round(v*(1/3)*1000))"
## SIGN
msign.usage = "SGN"
msign.description = "Pops a value and applies the SIGN algebraic function. (int(math.copysign(1,v)))"
## ABS
mabs.usage = "ABS"
mabs.description = "Pops a value and applies the ABS algebraic function. (abs(v))"
## PI
mpi.usage = "PI"
mpi.description = "Returns 4 digits of PI, outside of floats. (round(math.pi*1000))"
## E
me.usage = "M:E"
me.description = "Returns 4 digits of E, outside of floats. (round(math.e*1000))"

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