# Stacklers easy-to-use module system
Stackler has a very simple easy-to-use module system which allows you to make your own opcodes, this guide will show you how to make a module.
# Making the actual module
Stackler assumes that the module is located in the modules folder, so make sure you put your module.py file in the Modules folder.
### Folder structure:
```
Stackler/
├─ interpreter.py
└─ Modules/
   └─ mymodule.py
```
***note: Your stackler files can be anywhere, just make sure your module is in the modules folder.***
</br>
Once your done, its time to write some functions!
Why functions? Well the system works by searching for custom opcodes in a custom opcodes dictionary, if it finds the custom opcode it will run the function behind it.
Lets for example make a hello world opcode,
First we need the function so copy the following:
```python
def HelloWorld(stack, registers, arguments):
    pass
```
Now we need to add actual functionality to the function, so lets make it print "Hello, World!"
```python
def HelloWorld(stack, registers, arguments):
    print("Hello, World!")
```
Nice! Now we need to put its opcode/alias into an opcodes dictionary, so lets do that!
```python
def HelloWorld(stack, registers, arguments):
    print("Hello, World!")
# the opcodes dictionary, defines all opcodes in this module
opcodes = {
    "HW": HelloWorld # Tells the interpreter that the "HW" opcode refers to the HelloWorld function, and executes it.
}
```
Now we have succesfully made a module!</br>
You can add as many opcodes as you want to a module, just make sure to put its opcode/alias in the opcodes dictionary.
# Using stack functions
`stack.pop()` : Pops the top value from the stack and returns it.</br>
Example use:
```python
print(str(stack.pop()))
```
`stack.push()` : Pushes a value to the stack.</br>
Example use:
```python
stack.push(10)
```
`stack.top()` : Returns the number at the top of the stack without popping it.</br>
Example use:
```python
value = stack.top()
if value > 5:
    print("yes")
else:
    print("no")
```
`stack.clear` : Clears the stack ; Sets all values to zero and the stack pointer back to where it started.</br>
Example use:
```python
stack.clear()
stack.push(10)
print(str(stack.pop()))
```
# Using Registers
Stackler has 5 available registers which you can modify </br>
These registers are:</br>
* R1
* R2
* R3
* R4
* R5</br>
### Getting a registers value and modifying registers
To get a registers value, you'll have to do the following:
```python
registers["R1"] # or any other register, this returns register 1s value
```
To modify a registers value, you'll have to do the following:
```python
registers["R1"] = 5 # or any other register, this modifies the registers value
```
NOTE: Please only put number values into registers.

# Using arguments
Arguments can be used for alot of things, the interpreter automatically supplies a list of arguments based off of space splitting.</br>
You can use arguments for for example, how many times you print "<3"</br>
Theres alot of uses to say the least.</br>
You can look in the example module file in the modules folder to see how its used there.</br>
# Using your module
Using your module in a stackler file is relatively easy</br>
You basically import it using the `USE` opcode.</br>
Code snippet:
```
USE module.py
HRT
```