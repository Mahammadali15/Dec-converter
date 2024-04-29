# Decimal Conversion Functions
def decimal_to_binary(num):
    # Split into integer and fractional parts
    integer_part = int(num) # takes just the integer part of the number
    fractional_part = num - integer_part # subtracts off the integer just leaving the decimal

    # Convert integer part using the built-in bin function
    binary_integer = bin(integer_part)[2:]

    # Convert fractional part
    binary_fraction = '.'
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        if bit == 1:
            fractional_part -= bit
        binary_fraction += str(bit)

        # Limiting the length of the fractional part to avoid infinite loop
        if len(binary_fraction) > 10:
            break

    return binary_integer + binary_fraction

def decimal_to_octal(num):
    integer_part = int(num)
    fractional_part = num - integer_part

    # Convert integer part using the built-in oct function
    octal_integer = oct(integer_part)[2:]

    # Convert fractional part
    octal_fraction = '.'
    while fractional_part:
        fractional_part *= 8
        digit = int(fractional_part)
        fractional_part -= digit
        octal_fraction += str(digit)

        # Limiting the length of the fractional part
        if len(octal_fraction) > 10:
            break

    return octal_integer + octal_fraction

def decimal_to_hex(num):
    integer_part = int(num)
    fractional_part = num - integer_part

    # Convert integer part using the built-in hex function
    hex_integer = hex(integer_part)[2:].upper()

    # Convert fractional part
    hex_fraction = '.'
    while fractional_part:
        fractional_part *= 16
        digit = int(fractional_part)
        fractional_part -= digit
        hex_digit = hex(digit)[2:].upper()
        hex_fraction += hex_digit

        # Limiting the length of the fractional part
        if len(hex_fraction) > 10:
            break

    return hex_integer + hex_fraction

# Binary Conversion Functions
def binary_to_decimal(binary_str):
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
    else:
        integer_part, fractional_part = binary_str, '0'

    decimal_integer = int(integer_part, 2)
    decimal_fraction = sum(int(bit) * 2 ** -(index + 1) for index, bit in enumerate(fractional_part))

    return decimal_integer + decimal_fraction

# Octal Conversion Functions
def octal_to_decimal(octal_str):
    if '.' in octal_str:
        integer_part, fractional_part = octal_str.split('.')
    else:
        integer_part, fractional_part = octal_str, '0'

    decimal_integer = int(integer_part, 8)
    decimal_fraction = sum(int(digit) * 8 ** -(index + 1) for index, digit in enumerate(fractional_part))

    return decimal_integer + decimal_fraction


# Hex Conversion Functions
def hex_to_decimal(hex_str):
    if '.' in hex_str:
        integer_part, fractional_part = hex_str.split('.')
    else:
        integer_part, fractional_part = hex_str, '0'

    decimal_integer = int(integer_part, 16)
    decimal_fraction = sum(int(digit, 16) * 16 ** -(index + 1) for index, digit in enumerate(fractional_part))

    return decimal_integer + decimal_fraction
