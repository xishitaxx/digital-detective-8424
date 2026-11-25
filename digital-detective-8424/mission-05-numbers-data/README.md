# Mission 5 - Numbers and data

## 1. Task / objective
Convert decimal, binary, and hexadecimal numbers by hand, verify conversions in Python, build number_converter.py, and explain text encoding.

## 2. Work completed
Completed manual conversions across decimal, binary, and hexadecimal, verified them in the Python interactive shell, wrote and tested number_converter.py, and answered text-encoding questions.

## 3. Commands / tools used
* **python3:** Used to run the interactive Python shell and execute number_converter.py.
* **bin() and hex():** Built-in Python functions that convert integers into binary and hexadecimal strings prefixed with 0b and 0x.
* **int() and input():** Built-in Python functions used to read user text input and convert it into an integer.
* **VS Code / Git:** Used to edit files and commit/push Mission 5 work.

## 4. My understanding
Bits hold 0 or 1, and 8 bits make a byte. Positional place values depend on the base (base 2 for binary, base 10 for decimal, base 16 for hexadecimal with A=10 through F=15). Character encoding maps text characters to numbers so computers can store and exchange text; ASCII covers basic characters (A is 65, a is 97), while UTF-8 supports a much broader set of characters such as accented letters or emojis.

### Task 5.1: Manual conversions
| Question | Your working and answer |
| :--- | :--- |
| Convert decimal 13 to binary | 13 = 8 + 4 + 1 = (1*8) + (1*4) + (0*2) + (1*1) -> `1101` |
| Convert decimal 25 to binary | 25 = 16 + 8 + 1 = (1*16) + (1*8) + (0*4) + (0*2) + (1*1) -> `11001` |
| Convert binary 1010 to decimal | (1*8) + (0*4) + (1*2) + (0*1) = 8 + 2 -> `10` |
| Convert binary 1101 to decimal | (1*8) + (1*4) + (0*2) + (1*1) = 8 + 4 + 1 -> `13` |
| Convert hexadecimal A to decimal | A in hex = `10` |
| Convert hexadecimal 1F to decimal | (1*16) + (15*1) = 16 + 15 -> `31` |
| Convert binary 1111 to hexadecimal | 1111 in binary = 8 + 4 + 2 + 1 = 15 in decimal -> `F` |

### Task 5.2: Python verification
Tested `bin(13)` -> `'0b1101'`, `bin(25)` -> `'0b11001'`, `int('1010', 2)` -> `10`, `int('1101', 2)` -> `13`, `int('A', 16)` -> `10`, `int('1F', 16)` -> `31`, and `hex(int('1111', 2))` -> `'0xf'`. All results matched the manual calculations.

### Task 5.3: Converter test results
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| 13 | 0b1101 | 0xd |
| 25 | 0b11001 | 0x19 |
| 255 | 0b11111111 | 0xff |

### Task 5.4: Text encoding notes
* **ASCII codes:** Uppercase `A` is `65`; lowercase `a` is `97`.
* **Why encoding standards are needed:** Computers store data as binary numbers, so an encoding standard is required to map characters consistently to numeric codes across systems.
* **Non-ASCII character example:** `é` or `🚀`.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* mission-05-numbers-data/number_converter.py
* mission-05-numbers-data/README.md

## 8. Commit details
Committed with the message: "Build number converter and practise data representation" and pushed to GitHub.
