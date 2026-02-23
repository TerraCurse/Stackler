import math as m
import sys as s
import colorama as c
labels = {}
registers = {"R1":0,"R2":0,"R3":0,"R4":0,"R5":0}

def definelabels(code:str):
    count = 0
    for line in code.splitlines():
        if line.startswith("["):
            labels[line[1:]] = count
            count += 1
            continue
        count += 1

def getnuminp(inptext):
    accepted = 0
    global numinp
    numinp = ""
    while accepted == 0:
        try:
            numinp = int(input(inptext))
            accepted = 1
        except ValueError as ve:
            print("Invalid input: Numbers only.")
    return numinp

class Stack:
    def __init__(self, stack_size):
        self.bf = [0 for _ in range(stack_size)]
        self.sp = -1

    def push(self, num):
        try:
            self.sp += 1
            self.bf[self.sp] = num
        except IndexError:
            print(c.Fore.RED + "ERROR: Attempted to push a number when stack was full." + c.Fore.RESET)
            input("Press enter to exit.")
            exit()

    def pop(self):
        if self.sp < 0:
            print(
                c.Fore.RED
                + "Stack underflow error! Stopping interpreter."
                + c.Fore.RESET
            )
            input("Press enter to exit.")
            exit()
        number = self.bf[self.sp]
        self.sp -= 1
        return number

    def top(self):
        return self.bf[self.sp]


def evaluate(tcode: str):
    stk = Stack(256)
    definelabels(tcode)
    l = 0
    split = tcode.splitlines()
    while l < len(split):
        parts = split[l].split(" ")
        opcode = parts[0]
        if not split[l].strip():
            l += 1
            continue
        try:
            stk.push(int(opcode))
            l += 1
            continue
        except ValueError:
            pass
        if opcode == "E":
            break
        elif opcode == "+":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1 + n2)
            l += 1
        elif opcode == "-":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 - n1)
            l += 1
        elif opcode == "*":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1 * n2)
            l += 1
        elif opcode == "/":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 // n1)
            l += 1
        elif opcode == "%":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 % n1)
            l += 1
        elif opcode == "**":
            n1 = stk.pop()
            stk.push(n1 * n1)
            l += 1
        elif opcode == "//":
            n1 = stk.pop()
            stk.push(m.isqrt(n1))
            l += 1
        elif split[l].startswith('."') and split[l].endswith('"'):
            print(split[l][2:-1])
            l += 1
        elif opcode == ",":
            n = stk.pop()
            print(str(n))
            l += 1
        elif opcode == "_":
            n = stk.pop()
            stk.push(n * -1)
            l += 1
        elif opcode == ":":
            n = stk.pop()
            stk.push(n)
            stk.push(n)
            l += 1
        elif opcode == "\\":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1)
            stk.push(n2)
            l += 1
        elif opcode == "^":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2**n1)
            l += 1
        elif opcode == "!":
            n1 = stk.pop()
            stk.push(m.factorial(n1))
            l += 1
        elif opcode == "⊻":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 ^ n1)
            l += 1
        elif opcode == "V":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 | n1)
            l += 1
        elif opcode == "∧":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 & n1)
            l += 1
        elif opcode == "<":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 << n1)
            l += 1
        elif opcode == ">":
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 >> n1)
            l += 1
        elif opcode == ";":
            stk.push(getnuminp(";"))
            l += 1
        elif opcode == "X":
            stk.pop()
            l += 1
        elif opcode == "J":
            label = parts[1]
            l = labels[label]
        elif opcode == "GT":
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if int(n2[1:]) <= 5 and int(n2[1:]) >= 1:
                    n2 = str(registers[n2])
            if n1 > int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "LT":
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if int(n2[1:]) <= 5 and int(n2[1:]) >= 1:
                    n2 = str(registers[n2])
            if n1 < int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "GE":
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if int(n2[1:]) <= 5 and int(n2[1:]) >= 1:
                    n2 = str(registers[n2])
            if n1 >= int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "LE":
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if int(n2[1:]) <= 5 and int(n2[1:]) >= 1:
                    n2 = str(registers[n2])
            if n1 <= int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "EQ":
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if int(n2[1:]) <= 5 and int(n2[1:]) >= 1:
                    n2 = str(registers[n2])
            if n1 == int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "NE":
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if int(n2[1:]) <= 5 and int(n2[1:]) >= 1:
                    n2 = str(registers[n2])
            if n1 != int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "SR":
            v = stk.pop()
            regnum = parts[1]
            if int(regnum) > 5 or int(regnum) < 1:
                print(c.Fore.RED + f"Invalid register: R{regnum}!" + c.Fore.RESET)
                input("Press enter to exit.")
                exit()
            registers[f"R{regnum}"] = v
            l += 1
        elif opcode == "LR":
            regnum = parts[1]
            if int(regnum) > 5 or int(regnum) < 1:
                print(c.Fore.RED + f"Invalid register: R{regnum}!" + c.Fore.RESET)
                input("Press enter to exit.")
                exit()
            stk.push(registers[f"R{regnum}"])
            l += 1
        else:
            l += 1
    print(stk.bf)
if len(s.argv) > 1:
    f = open(s.argv[1])
    evaluate(f.read())
    input("Press enter to exit.")
    print(registers)
    exit()
else:
    print("No file specified for interpretation.")
    input("Press enter to exit.")

    exit()
