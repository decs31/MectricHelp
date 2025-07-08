---
title: "MecScript Language Reference"
weight: 1
---

MecScript uses the same general syntax as the C/C++ languages.

 - `Types` are declared before variable names.
 - `Expressions` must be termiated with a semicolon `;`.
 - `Blocks` that encapsulate local scopes are surrounded with `{` and `}`.

---

## Built-in Types
MecScript is a statically typed language. This means that any variable must be declared as an explicit type.

| Name       | Description                  | Min            | Max           |
| ---------- | ---------------------------- | -------------- | ------------- |
| **char**   | 8 bit singed integer         | 0              | 255           |
| **byte**   | 8 bit unsinged integer       | -128           | 127           |
| **short**  | 16 bit singed integer        | -32678         | 32767         |
| **ushort** | 16 bit unsinged integer      | 0              | 65535         |
| **int**    | 32 bit singed integer        | -2,147,483,648 | 2,147,483,647 |
| **uint**   | 32 bit unsinged integer      | 0              | 4,294,967,295 |
| **float**  | 32 bit floating point number | ~1.175E-38     | ~3.4E+38      |

### Examples
``` c++
// Declaring integer types
short shortVar;
int x = 123;

// Declaring a floating point type
float f = 123.4;
```

---

## Operators
MecScript supports a full range of mathematical and logical operations.

### Mathematical
| Operator | Description |
| -------- | ----------- |
| **+**    | Add         |
| **-**    | Subtract    |
| **\***   | Multiply    |
| **/**    | Divide      |

### Assignment
| Operator | Description             |
| -------- | ----------------------- |
| **=**    | Assign                  |
| **+=**   | Add then assign         |
| **-=**   | subtract then assign    |
| ***=**   | Multiply then assign    |
| **/=**   | Divide then assign      |

### Logical
| Operator | Description              |
| -------- | ------------------------ |
| **==**   | Equal to                 |
| **!=**   | Not equal to             |
| **>**    | Greater than             |
| **<**    | Less than                |
| **>=**   | Greater than or equal to |
| **<=**   | Less than or equal to    |
| **&&**   | Logical And              |
| **\|\|** | Logical Or               |
| **!**    | Logical Not              |
| **?**    | Ternary                  |

### Bitwise
| Operator | Description              |
| -------- | ------------------------ |
| **&**    | Bitwise And              |
| **\|**   | Bitwise Or               |
| **^**    | Bitwise XOr              |
| **~**    | Bitwise Not              |
| **<<**   | Shift left               |
| **>>**   | Shift right              |

---

## Literals
Literals are numbers represented explicitly. They can be used anywhere in expressions. Literals can be expressed in a range of formats...

### Integer
Integer literals are represented as a typed number without a decimal place.

``` c++
123 // Integer literal
```

### Float
Floating point numbers are represented as a typed number with a decimal place.

``` c++
123.4 // Floating point literal
```

### Hexadecimal
Hex values are represented by prefixing the value with `0x`.
``` c++
0x7B // Hexadecimal literal
```

### Binary
Binary values are represented by prefixing the value with `0b`.
``` c++
0b01111011 // Binary literal
```

---

## Variables
Variables are declared first by the type, then the name. Optionally, you can specify an initial value. The initial value can be a literal or an expression. 
> **Tip:** If no initial value is given, it will be assigned to 0 by default.

``` c++
int myInt; // No initial value
short myShort = 1234; // Literal initialiser
short anotherShort = myShort * 2; // Expression initialiser
```

### Const
The `const` keyword specifies that a variable cannot be changed after it is set. Const values can be read and used in expressions freely. Attempting to write a `const` variable after initialisation will cause a compile error.

``` c++
const int immutableValue = foo; // Declare a cost value.
int mutableValue = immutableValue + bar; // It can be read.
immutableValue += 2; // This will cause an error. It cannot be written.
```

---

## Control Flow
### If Statements
Conditional program flow can be expressed with `if` / `else if` / `else` statements.

``` c++
if (something == comparison) {
    // Do something
} else if (somethingElse) {
    // Do a different thing
} else {
    // Do this instead
}
```

The body of the `if` statement can either be a single expression or a block.

``` c++
if (a == b) c = UpdateC(); // Single expression.

if (c > 10) { // Blocks can contain any number of expressions.
    b = 100;
    a = b & 0x0F;
}
```

### Ternary Statements
Ternary statements are essentially a shorthand version of an if/else block.

``` c++
// Ternary statement
int a = b > c ? 1 : 2;

// Is equivalent to:
int a;
if (b > c) a = 1;
else a = 2;
```

The condition before the `?` is evaluated. If true, the expression on the LHS of the `:` is used, else the expression on the RHS is used.

### Switch Statements
Switch statements allow a single integer value to direct the program flow. 
Switch statements are fast as they do not have to check each condition, they simple jump program execution to the matching position. The trade-off is that they can increase the size of the compiled script.

``` c++
switch (a) {
    case 0:
        // Do something when a == 0.
        break;
    case 1: 
        // Do something when a == 1.
        break;
    case 10:
        // Do something when a == 10.
        break;
    default:
        // Do this when a is not any of the above values.
        break;
}
``` 
---

## Loops

### While

### For
