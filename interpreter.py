import math as m
from tkinter.constants import NONE

import colorama as c


class Stack:
    def __init__(self, stack_size):
        self.bf = [0 for _ in range(stack_size)]
        self.sp = -1

    def push(self, num):
        self.sp += 1
        self.bf[self.sp] = num

    def pop(self):
        number = self.bf[self.sp]
        if self.sp < 0:
            print(
                c.Fore.RED
                + "Stack underflow error! Stopping interpreter."
                + c.Fore.RESET
            )
            exit()
        self.sp -= 1
        return number

    def top(self):
        return self.bf[self.sp]


def evaluate(code: str):
    stk = Stack(256)
    for line in code.splitlines():
        parts = line.split(" ")
        opcode = parts[0]
        if not line.strip():
            continue
        try:
            stk.push(int(opcode))
            continue
        except ValueError:
            pass
        if opcode == "+":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1 + n2)
        elif opcode == "-":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 - n1)
        elif opcode == "*":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1 * n2)
        elif opcode == "/":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 // n1)
        elif opcode == "%":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 % n1)
        elif opcode == "**":
            n1 = stk.pop()
            stk.push(n1 * n1)
        elif opcode == "//":
            n1 = stk.pop()
            stk.push(m.isqrt(n1))
        elif line.startswith('."') and line.endswith('"'):
            print(line[2:-1])
        elif opcode == ",":
            n = stk.pop()
            print(str(n))
        elif opcode == "_":
            n = stk.pop()
            stk.push(n * -1)
        elif opcode == ":":
            n = stk.pop()
            stk.push(n)
            stk.push(n)
        elif opcode == "\\":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1)
            stk.push(n2)
        elif opcode == "^":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2**n1)
        elif opcode == "!":
            n1 = stk.pop()
            stk.push(m.factorial(n1))
        elif opcode == "⊻":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 ^ n1)
        elif opcode == "∨":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 | n1)
        elif opcode == "∧":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 & n1)
        elif opcode == "<":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 << n1)
        elif opcode == ">":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 >> n1)


evaluate("""5
5
>
,""")
