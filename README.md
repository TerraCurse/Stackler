# Stackler - A simple, stack-based language.
Stackler is a simple, stack-based language, with insanely simple syntax.
## Opcodes
`(any number, negatives are supported)` : Pushes the number to the stack.</br>
`+` : Pops the top two numbers on the stack and adds them together, then pushes the result to the stack.</br>
`-` : Pops the top two numbers on the stack and subtracts the first one from the second one (reverse polish notation), then pushes the result to the stack (reverse polish notation).</br>
`*` : Pops the top two numbers on the stack and multiplies the first one by the second one, then pushes the result to the stack.</br>
`/` : Pops the top two numbers on the stack and divides the second one by the first one (reverse polish notation), then pushes the result to the stack.</br>
`%` : Pops the top two numbers on the stack, performs a modulo operation (n2%n1) and pushes the result to the stack.</br>
`**` : Pops the top number from the stack, squares it, then pushes the result to the stack.</br>
`//` : Pops the top number from the stack, gets the square root of it and rounds it, then pushes the result to the stack.</br>
`."(text)"` : Prints the text to the console.</br>
`,` : Pops the top number from the stack and prints it to the console.</br>
`_` : Pops the top number from the stack, negates it, and pushes it to the stack.</br>
`:` : Pops the top number from the stack and pushes it twice to the stack, thus duplicating it.</br>
`\\` : Pops the top 2 numbers from the stack, and pushes the first one then second one, thus swapping them.</br>
`^` : Pops the top 2 numbers from the stack, performs an exponential operation on the second number based off the first number (n2**n1 (python)), and pushes the result to the stack.</br>
`!` : Pops the top number from the stack, performs a factorial operation on it, and pushes the result to the stack.</br>
`⊻` : Pops the top 2 numbers from the stack, performs an XOR operation on the second number based off the first number (n2^n1 (still python)), and pushes the result to the stack.</br>
`V` : Pops the top 2 numbers from the stack, performs an OR operation on the second number based off the first number (n2|n1 (stillll python)), and pushes the result to the stack.</br>
`∧` : Pops the top 2 numbers from the stack, performs an AND operation on the second number based off the first number (n2&n1 (stilllllll python)), and pushes the result to the stack.</br>
`<` : Pops the top 2 numbers from the stack, bitshifts the second number (first number) times left, pushes the result to the stack.</br>
`>` : Pops the top 2 numbers from the stack, bitshifts the second number (first number) times right, pushes the result to the stack.</br>
`;` : Gets number input from the user, and pushes it to the stack. (will ask again if the input isnt a number)
