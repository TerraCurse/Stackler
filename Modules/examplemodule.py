## module system
description = "Example module for module developers."
def HRT(stack, registers, args):
    try:
        amount = int(args[0])
    except:
        amount = 1
    for _ in range(amount):
        print("<3")
    return 1

## info sect
### HRT
HRT.usage = "HRT (Amount)"
HRT.description = "Prints a heart (Amount) times, if not specified, just once."

opcodes = {
    "HRT" : HRT
}