import math as m
import sys as s
import colorama as c
import random as r
labels = {}
registers = {"R1":0,"R2":0,"R3":0,"R4":0,"R5":0}
def definelabels(code:str):
    count = 0
    for line in code.splitlines():
        if line.startswith("["):
            labels[line[1:].strip()] = count
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

def getcharinp(inptext, charcount):
    return input(inptext)[:charcount]

class Stack:
    def __init__(self, stack_size):
        self.bf = [0 for _ in range(stack_size)]
        self.sp = -1
        self.size = stack_size

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

    def clear(self):
        self.bf = [0 for _ in range(self.size)]
        self.sp = -1

    def top(self):
        return self.bf[self.sp]


def evaluate(tcode: str):
    stk = Stack(256)
    definelabels(tcode)
    l = 0
    custom_opcodes = {}
    split = tcode.splitlines()
    while l < len(split):
        parts = split[l].split(" ")
        opcode = parts[0]
        if not split[l].strip():
            """Skip empty line"""
            l += 1
            continue
        try:
            """Attempt to push a number"""
            stk.push(int(opcode))
            l += 1
            continue
        except ValueError:
            pass
        if opcode in custom_opcodes:
            custom_opcodes[opcode](stk,registers)
            l += 1
        elif opcode == "E":
            """End"""
            break
        elif opcode == "+":
            """Add"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1 + n2)
            l += 1
        elif opcode == "-":
            """Subtract"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 - n1)
            l += 1
        elif opcode == "*":
            """Multiply"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1 * n2)
            l += 1
        elif opcode == "/":
            """Divide"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 // n1)
            l += 1
        elif opcode == "%":
            """Modulo"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 % n1)
            l += 1
        elif opcode == "**":
            """Square"""
            n1 = stk.pop()
            stk.push(n1 * n1)
            l += 1
        elif opcode == "//":
            """Integer square root"""
            n1 = stk.pop()
            stk.push(m.isqrt(n1))
            l += 1
        elif split[l].startswith('."') and split[l].endswith('"'):
            """Print"""
            print(split[l][2:-1])
            l += 1
        elif opcode == ",":
            """Print top stack value"""
            n = stk.pop()
            print(str(n))
            l += 1
        elif opcode == "_":
            """Negate"""
            n = stk.pop()
            stk.push(n * -1)
            l += 1
        elif opcode == ":":
            """Duplicate"""
            n = stk.pop()
            stk.push(n)
            stk.push(n)
            l += 1
        elif opcode == "\\":
            """Swap"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n1)
            stk.push(n2)
            l += 1
        elif opcode == "^":
            """Power"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2**n1)
            l += 1
        elif opcode == "!":
            """Factorial"""
            n1 = stk.pop()
            stk.push(m.factorial(n1))
            l += 1
        elif opcode == "⊻":
            """Bitwise XOR"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 ^ n1)
            l += 1
        elif opcode == "V":
            """Bitwise OR"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 | n1)
            l += 1
        elif opcode == "∧":
            """Bitwise AND"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 & n1)
            l += 1
        elif opcode == "<":
            """Bitwise shift left"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 << n1)
            l += 1
        elif opcode == ">":
            """Bitwise shift right"""
            n1 = stk.pop()
            n2 = stk.pop()
            stk.push(n2 >> n1)
            l += 1
        elif opcode == ";":
            """Get number input"""
            stk.push(getnuminp(";"))
            l += 1
        elif opcode == "X":
            """Pop"""
            stk.pop()
            l += 1
        elif opcode == "J":
            """Jump"""
            if len(parts) < 2:
                print(c.Fore.RED + f"J ; Missing label to jump to!" + c.Fore.RESET)
                exit()
            label = parts[1]
            if label in labels:
                l = labels[label]
            else:
                print(c.Fore.RED + f"J ; Invalid label!" + c.Fore.RESET)
                exit()
        elif opcode == "GT":
            """If Greater Than"""
            if len(parts) < 2:
                print(c.Fore.RED + f"GT ; Missing number to compare to!" + c.Fore.RESET)
                exit()
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if n2 in registers:
                    n2 = str(registers[n2])
                else:
                    print(c.Fore.RED + f"GT ; Invalid register number: {n2}!" + c.Fore.RESET)
                    exit()
            if n1 > int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "LT":
            """If Less Than"""
            if len(parts) < 2:
                print(c.Fore.RED + f"LT ; Missing number to compare to!" + c.Fore.RESET)
                exit()
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if n2 in registers:
                    n2 = str(registers[n2])
                else:
                    print(c.Fore.RED + f"LT ; Invalid register number: {n2}!" + c.Fore.RESET)
                    exit()
            if n1 < int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "GE":
            """If Greater of Equal"""
            if len(parts) < 2:
                print(c.Fore.RED + f"GE ; Missing number to compare to!" + c.Fore.RESET)
                exit()
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if n2 in registers:
                    n2 = str(registers[n2])
                else:
                    print(c.Fore.RED + f"GE ; Invalid register number: {n2}!" + c.Fore.RESET)
                    exit()
            if n1 >= int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "LE":
            """If Less or Equal"""
            if len(parts) < 2:
                print(c.Fore.RED + f"LE ; Missing number to compare to!" + c.Fore.RESET)
                exit()
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if n2 in registers:
                    n2 = str(registers[n2])
                else:
                    print(c.Fore.RED + f"LE ; Invalid register number: {n2}!" + c.Fore.RESET)
                    exit()
            if n1 <= int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "EQ":
            """If Equal"""
            if len(parts) < 2:
                print(c.Fore.RED + f"EQ ; Missing number to compare to!" + c.Fore.RESET)
                exit()
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if n2 in registers:
                    n2 = str(registers[n2])
                else:
                    print(c.Fore.RED + f"EQ ; Invalid register number: {n2}!" + c.Fore.RESET)
                    exit()
            if n1 == int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "NE":
            """If Not Equal"""
            if len(parts) < 2:
                print(c.Fore.RED + f"NE ; Missing number to compare to!" + c.Fore.RESET)
                exit()
            n1 = stk.top()
            n2 = parts[1]
            if n2.startswith("R"):
                if n2 in registers:
                    n2 = str(registers[n2])
                else:
                    print(c.Fore.RED + f"NE ; Invalid register number: {n2}!" + c.Fore.RESET)
                    exit()
            if n1 != int(n2):
                l += 1
            else:
                l += 2
        elif opcode == "SR":
            """Pop from the stack and save the value to the specified register"""
            if len(parts) < 2:
                print(c.Fore.RED + f"SR ; Missing register number!" + c.Fore.RESET)
                exit()
            v = stk.pop()
            regnum = parts[1]
            if f"R{regnum}" not in registers:
                print(c.Fore.RED + f"SR ; Invalid register: R{regnum}!" + c.Fore.RESET)
                exit()
            registers[f"R{regnum}"] = v
            l += 1
        elif opcode == "LR":
            """Load value from specified register and push it"""
            if len(parts) < 2:
                print(c.Fore.RED + f"SR ; Missing register number!" + c.Fore.RESET)
                exit()
            regnum = parts[1]
            if f"R{regnum}" not in registers:
                print(c.Fore.RED + f"SR ; Invalid register: R{regnum}!" + c.Fore.RESET)
                exit()
            stk.push(registers[f"R{regnum}"])
            l += 1
        elif opcode == "I":
            """Increment"""
            val = stk.pop()
            stk.push(val + 1)
            l += 1
        elif opcode == "D":
            """Decrement"""
            val = stk.pop()
            stk.push(val - 1)
            l += 1
        elif opcode == "~":
            """Bitwise NOT"""
            val = stk.pop()
            stk.push(~val)
            l += 1
        elif opcode == "RS":
            """Reset the stack"""
            stk.clear()
            l += 1
        elif opcode == "RR":
            """Reset specified register"""
            if len(parts) < 2:
                print(c.Fore.RED + f"SR ; Missing register number!" + c.Fore.RESET)
                exit()
            registernum = parts[1]
            if f"R{registernum}" not in registers:
                print(c.Fore.RED + f"SR ; Invalid register: R{regnum}!" + c.Fore.RESET)
                exit()
            registers[f"R{registernum}"] = 0
            l += 1
        elif opcode == "C;":
            """Get one character input"""
            char = getcharinp("C;", 1)
            stk.push(ord(char))
            l += 1
        elif opcode == "C,":
            """Output top stack value as ascii character"""
            val = stk.pop()
            print(chr(val % 256), end="")
            l += 1
        elif opcode == "RN":
            """Random"""
            if len(parts) < 3:
                if len(parts) == 2:
                    print(c.Fore.RED + f"RN ; Missing MAX argument! (RN min max)" + c.Fore.RESET)
                    exit()
                else:
                    print(c.Fore.RED + f"RN ; Missing MIN and MAX argument! (RN min max)" + c.Fore.RESET)
                    exit()
            minimum = int(parts[1])
            maximum = int(parts[2])
            stk.push(r.randint(minimum,maximum))
            l += 1
        elif opcode == "COM":
            """Comment"""
            l += 1
        elif opcode == "USE":
            """import basically"""
            if len(parts) < 2:
                print(c.Fore.RED + f"USE ; Missing module filename!" + c.Fore.RESET)
                exit()
            filename = parts[1]
            try:
                module = {}
                exec(open(f"./Modules/{filename}").read(), {}, module)
                if "opcodes" in module:
                    custom_opcodes.update(module["opcodes"])
                else:
                    print(c.Fore.YELLOW + f"USE ; Specified module has no opcodes dict. Please check {filename} and add it in. Check examples to see how to use it." + c.Fore.RESET)
            except OSError as e:
                print(c.Fore.RED + f"USE ; OS Error: {e}" + c.Fore.RESET)
                exit()
            l += 1
        else:
            print(c.Fore.RED + f"INTERPRETER ; Invalid opcode: '{split[l]}'! Line: {l+1}" + c.Fore.RESET)
            exit()
if len(s.argv) > 1:
    try:
        f = open(" ".join(s.argv[1:]))
        evaluate(f.read())
        input("Press enter to exit.")
        exit()
    except OSError as e:
        print(c.Fore.RED + f"Interpreter ; OS Error: {e}" + c.Fore.RESET)
else:
    print("No file specified for interpretation.")
    input("Press enter to exit.")
    exit()