# Learning C

## Summary

- [Courses & Good Links](#courses-&-good-links)
- [Compilation phase](#compilation-phase)
- [Comments](#comments)
- [Variables](#variables)
  - [Declaration](#declaration-samples)
  - [Types](#variables-types)
- [Reserved words](#rerserved-words)

## Courses & Good Links

### Courses:
- https://www.udemy.com/course/apprendre-la-programmation-en-c-cours-complet

### Good Links:
- https://devdocs.io/c/
- https://www.tablesgenerator.com/markdown_tables

## ------------------

### Main program

```c
#include <stdio.h>

int main() {
    return 0;
}
```

### Compilation phase
```sh
# Compile the file
$ clang main.c

# Run the program
$ ./a.out
```

### Comments
```c
// one line comment

/*
multiple lines 
of comments
*/
```

### Variables
`type name_variable = value ;`

#### Declaration samples:

```c
int number = 0;  
char character = "A";
unsigned short 
```

#### Variables types:

|Type|Size|Min|Max|Display|
|---|:---:|:---:|:---:|---|
|`unsigned short`   | 2     | 0                                     | 65535                             |`%d`|
|`short`            | 2     | -32768                                | 32767                             |`%d`|
|`unsigned long`    | 4/8   | 0/0                                   | 4294967295 / 18446744073709551615 |`%ld`|
|`long`             | 4/8   | -2147483648 / -9223372036854775808    | 2147483647 / 23372036854775807    |`%ld`|
|`unsigned int`     | 2/4   | 0/0                                   | 65535/ 4294967295                 |`%d`|
|`int`              | 2/4   | -32768 / -2147483648                  | 32767 / 2147483647                |`%d`|
|`unsigned char`    | 1     | 0                                     | 255                               |`%c`|
|`signed char`      | 1     | -128                                  | 127                               |`%c`|
|`char`             | 1     | -128 / 0                              | 127 / 255                         |`%c`|
|`float`            | 4     | -3.4^38                               | 3.4^38                            |`%f`|
|`double`           | 8     | -1.7^308                              | 1.7^308                           |`%f`|

### Rerserved words

| `auto` | `break` | `case` | `char` | `const` | `default` | `do` | `double` |
|---|---|---|---|---|---|---|---|
| `else` | `enum` | `extern` | `float` | `for` | `goto` | `if` | `int` |
| `long`  | `register`  | `return`  | `short`  | `signed`  | `sizeof` | `static` | `struct` |
| `switch` | `typedef` | `union` | `unsigned` | `void` | `volatile` | `while` |

### Links:

## Divers
`alias gcc="clang -Werror -Wextra -Wall"`