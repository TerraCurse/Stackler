# Stackler - A simple, stack-based language.
Stackler is a simple, stack-based language, with insanely simple syntax.
It allows only one opcode per line.
Turing complete!
## Opcodes (i'm not that great at explaining)
### Labels, Numbers
`[(labelname)` : Defines a label.</br>
`(any number, negatives are supported)` : Pushes the number to the stack.</br>
`RN (min) (max)` : Pushes a random number between the specified range to the stack.</br>
### Extra
`COM (comment)` : The entire line with this opcode gets ignored by the interpreter, like a comment. Inline comments are supported, any text following a valid opcode and its required arguments counts as an inline comment.
### Arithmetic
`+` : Pops the top two numbers on the stack and adds them together, then pushes the result to the stack.</br>
`-` : Pops the top two numbers on the stack and subtracts the first one from the second one (reverse polish notation), then pushes the result to the stack (reverse polish notation).</br>
`*` : Pops the top two numbers on the stack and multiplies the first one by the second one, then pushes the result to the stack.</br>
`/` : Pops the top two numbers on the stack and divides the second one by the first one (reverse polish notation), then pushes the result to the stack.</br>
`%` : Pops the top two numbers on the stack, performs a modulo operation (n2%n1) and pushes the result to the stack.</br>
`**` : Pops the top number from the stack, squares it, then pushes the result to the stack.</br>
`//` : Pops the top number from the stack, gets the square root of it and rounds it, then pushes the result to the stack.</br>
`I` : Pops the top value from the stack, increments it by 1 and pushes it back onto the stack.
`D` : Pops the top value from the stack, decrements it by 1 and pushes it back onto the stack.
### Output
`."(text)"` : Prints the text to the console.</br>
`,` : Pops the top number from the stack and prints it to the console.</br>
`C,` : Pops the top number from the stack and converts it to an ascii character.</br>
### Stack Manipulation
`_` : Pops the top number from the stack, negates it, and pushes it to the stack.</br>
`:` : Pops the top number from the stack and pushes it twice to the stack, thus duplicating it.</br>
`\\` : Pops the top 2 numbers from the stack, and pushes the first one then second one, thus swapping them.</br>
`RS` : Resets the stack. (sets everything back to zero and sets the pointer back to where it started)</br>
### Advanced Math
`^` : Pops the top 2 numbers from the stack, performs an exponential operation on the second number based off the first number (n2**n1 (python)), and pushes the result to the stack.</br>
`!` : Pops the top number from the stack, performs a factorial operation on it, and pushes the result to the stack.</br>
### Bitwise Operations
`⊻` : Pops the top 2 numbers from the stack, performs an XOR operation on the second number based off the first number (n2^n1 (still python)), and pushes the result to the stack.</br>
`V` : Pops the top 2 numbers from the stack, performs an OR operation on the second number based off the first number (n2|n1 (stillll python)), and pushes the result to the stack.</br>
`∧` : Pops the top 2 numbers from the stack, performs an AND operation on the second number based off the first number (n2&n1 (stilllllll python)), and pushes the result to the stack.</br>
`<` : Pops the top 2 numbers from the stack, bitshifts the second number (first number) times left (n2 << n1), pushes the result to the stack.</br>
`>` : Pops the top 2 numbers from the stack, bitshifts the second number (first number) times right (n2 >> n1), pushes the result to the stack.</br>
`~` : Pops the top number from the stack, performs a bitwise NOT operation on it (~n1) and pushes it back to the stack.</br>
### Input
`;` : Gets number input from the user, and pushes it to the stack. (will ask again if the input isnt a number)</br>
`C;` : Gets one character input from the user, and pushes its ascii value to the stack.</br>
### Control
`E` : Halts the program.</br>
`X` : Pops a value from the stack. (basically just deletes it).</br>
`J (label)` : Jumps to the specified label.</br>
### Register-related
`SR (register number)` : Pops the top value from the stack and saves it to the specified register. (Available registers: R1, R2, R3, R4, R5 | you have to refer to them as 1, 2, 3, 4, 5 in register related opcodes, else they're in the same form.)</br>
`LR (register number)` : Pushes the value of the specified register into the stack.</br>
`RR (register number)` : Resets the specified register (sets its value to zero).</br>
### Comparisons
`GT (value)` : Compares the top stack value to the specified value, you can also specify a register. (stacktop > value) (example: GT R1)</br>
`LT (value)` : Compares the top stack value to the specified value, you can also specify a register. (stacktop < value) (example: LT R1)</br>
`GE (value)` : Compares the top stack value to the specified value, you can also specify a register. (stacktop >= value) (example: GE R1)</br>
`LE (value)` : Compares the top stack value to the specified value, you can also specify a register. (stacktop <= value) (example: LE R1)</br>
`EQ (value)` : Compares the top stack value to the specified value, you can also specify a register. (stacktop == value) (example: EQ R1)</br>
`NE (value)` : Compares the top stack value to the specified value, you can also specify a register. (stacktop != value) (example: NE R1)</br>
# Example Programs
### Truth Machine
```
;
EQ 1
J loop
."0"
E
[loop
."1"
J loop
```
Explanation: Asks the user for number input (`;`), if the top stack value (the users input) is equal to 1 (`EQ 1`), it jumps to the loop label (`J loop`), otherwise it prints 0 (`."0"`) and ends the program (`E`), in the loop label (`[loop`), it prints 1 (`."1"`) then repeats (`J loop`).
### Input squarer
```
;
**
,
```
Explanation: Asks the user for number input (`;`), squares the number inputted (`**`), pops it from the stack and prints it (`,`).
### Countdown
```
10
[loop
:
,
D
GT 0
J loop
E
```
Explanation: Pushes 10 to the stack (`10`), declares a label (`[loop`), duplicates the top stack value which is 10 (`:`), prints it out (`,`), decrements the current top value {which is 10} by 1 (`D`), if the top stack value {which is now 9} is greater than 0 (`GT 0`), then it jumps back to the loop label (`J loop`) which makes it loop until the countdown is at 0, else it ends the program (`E`).
### Square Countdown
```
10
[loop
:
**
,
D
GT 0
J loop
E
```
Explanation: Pushes 10 to the stack (`10`), declares a label (`[loop`), duplicates the top stack value which is 10 (`:`), squares it (`**`), prints it out (`,`), decrements the current top value {which is 10} by 1 (`D`), if the top stack value {which is now 9} is greater than 0 (`GT 0`), then it jumps back to the loop label (`J loop`) which makes it loop until the countdown is at 0, else it ends the program (`E`).

