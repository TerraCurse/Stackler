## module system
def HRT(stack, registers, args):
    try:
        amount = int(args[0])
    except:
        amount = 1
    for _ in range(amount):
        print("<3")
    return 1

opcodes = {
    "HRT" : HRT
}