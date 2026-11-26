# Mission 5 — Numbers and data

## 1. Task / objective
Convert decimal, binary, and hexadecimal values manually and with Python, build a decimal number converter, and explain text encoding.

## 2. Work completed

### Manual conversions
| Question | Working and answer |
|---|---|
| Decimal 13 to binary | 13 ÷ 2: 1 remainder repeatedly; reverse remainders: `1101₂`. |
| Decimal 25 to binary | 25 = 16 + 8 + 1 = `11001₂`. |
| Binary `1010` to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 10. |
| Binary `1101` to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 13. |
| Hexadecimal `A` to decimal | A = 10. |
| Hexadecimal `1F` to decimal | 1×16 + 15×1 = 31. |
| Binary `1111` to hexadecimal | 1111₂ = 15₁₀ = F₁₆. |

The binary values were verified using Python:

| Expression | Result | Manual match |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `hex(10)` | `0xa` | Yes (`A`) |
| `hex(31)` | `0x1f` | Yes (`1F`) |

### Number converter
Created `number_converter.py`. It asks for an integer and prints the binary and hexadecimal forms. The program accepts positive and negative integers but was tested with positive values.

### Text encoding
- ASCII decimal code for `A`: 65.
- ASCII decimal code for `a`: 97.
- An encoding standard is needed so software agrees about how bytes represent characters and can preserve or share text consistently.
- An example of a character outside basic 7-bit ASCII is `é`.

## 3. Commands / tools used
- `python3`: launched Python 3 for interactive checks and the converter program.
- `bin(number)`: converts an integer to a binary string with a `0b` prefix.
- `hex(number)`: converts an integer to a hexadecimal string with a `0x` prefix.
- `int(text, 2)`: interprets text as a binary integer.
- `int(text, 16)`: interprets text as a hexadecimal integer.
- `input()`: obtains text entered by the user.
- `int()`: converts input text to an integer.

## 4. My understanding
A number's base changes how digits are grouped and weighted. Binary uses powers of two, decimal uses powers of ten, and hexadecimal uses powers of sixteen. Hexadecimal is convenient for grouping binary digits because each hex digit represents four binary digits. `bin()` and `hex()` add prefixes; `int(..., base)` interprets an encoded string. ASCII covers basic English characters, while UTF-8 can encode much larger character sets.

## 5. Difficulties faced
The converter should show clear output when input is not an integer. Invalid text could otherwise produce a Python `ValueError`.

## 6. How I resolved them
The converter uses a `try`/`except` block and prints an explanation when the user does not enter a valid integer.

## 7. Evidence / files
- `number_converter.py` — working decimal-to-binary/hexadecimal converter.
- Manual conversions and Python verification in this README.
- Encoding answers in this README.

## 8. Commit details
Commit: `Build number converter and practise data representation`. Pushed to `main`.
