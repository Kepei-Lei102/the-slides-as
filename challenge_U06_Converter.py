"""U06 - The Signed Converter

PEN FIRST: complete practice Q10 on paper. It assesses the decoding plan,
Python statements and a test value, not function syntax.

SUPPLIED WRAPPERS: def introduces a named operation; return sends its result
back to the caller. Keep both supplied headers and return lines. Indent your
statements where indicated. You are not asked to design these wrappers.

Q10: binary_to_denary(bits)
  Input: a valid 8-character STRING of 0s and 1s.
  Output: an INT in -128..127, stored in total.

OPTIONAL reverse direction: denary_to_binary(n)
  Input: an INT in -128..127.
  Output: exactly 8 characters of 0s and 1s, stored in pattern.

Use loops, selection and arithmetic. Do not use bin(), int(bits, 2), format()
or a binary format specifier in an f-string. This judge checks outputs;
your teacher checks the method. No score or written marks are awarded here.
Run the unfinished file to see RED; then complete the decoder first.
GREEN requires both directions independently correct for all 256 values.
The reference data below is a lookup table, not a worked conversion algorithm.
"""


def binary_to_denary(bits):
    # Q10(b): replace this placeholder with your statements calculating total.
    total = None
    return total


def denary_to_binary(n):
    # Optional extension: replace this with statements calculating pattern.
    pattern = None
    return pattern


# Supplied local checks. Leave this section unchanged.
# Entries are the expected bytes for denary -128, -127, ... , 127 in order.
_EXPECTED = (
    '10000000 10000001 10000010 10000011 10000100 10000101 10000110 10000111 '
    '10001000 10001001 10001010 10001011 10001100 10001101 10001110 10001111 '
    '10010000 10010001 10010010 10010011 10010100 10010101 10010110 10010111 '
    '10011000 10011001 10011010 10011011 10011100 10011101 10011110 10011111 '
    '10100000 10100001 10100010 10100011 10100100 10100101 10100110 10100111 '
    '10101000 10101001 10101010 10101011 10101100 10101101 10101110 10101111 '
    '10110000 10110001 10110010 10110011 10110100 10110101 10110110 10110111 '
    '10111000 10111001 10111010 10111011 10111100 10111101 10111110 10111111 '
    '11000000 11000001 11000010 11000011 11000100 11000101 11000110 11000111 '
    '11001000 11001001 11001010 11001011 11001100 11001101 11001110 11001111 '
    '11010000 11010001 11010010 11010011 11010100 11010101 11010110 11010111 '
    '11011000 11011001 11011010 11011011 11011100 11011101 11011110 11011111 '
    '11100000 11100001 11100010 11100011 11100100 11100101 11100110 11100111 '
    '11101000 11101001 11101010 11101011 11101100 11101101 11101110 11101111 '
    '11110000 11110001 11110010 11110011 11110100 11110101 11110110 11110111 '
    '11111000 11111001 11111010 11111011 11111100 11111101 11111110 11111111 '
    '00000000 00000001 00000010 00000011 00000100 00000101 00000110 00000111 '
    '00001000 00001001 00001010 00001011 00001100 00001101 00001110 00001111 '
    '00010000 00010001 00010010 00010011 00010100 00010101 00010110 00010111 '
    '00011000 00011001 00011010 00011011 00011100 00011101 00011110 00011111 '
    '00100000 00100001 00100010 00100011 00100100 00100101 00100110 00100111 '
    '00101000 00101001 00101010 00101011 00101100 00101101 00101110 00101111 '
    '00110000 00110001 00110010 00110011 00110100 00110101 00110110 00110111 '
    '00111000 00111001 00111010 00111011 00111100 00111101 00111110 00111111 '
    '01000000 01000001 01000010 01000011 01000100 01000101 01000110 01000111 '
    '01001000 01001001 01001010 01001011 01001100 01001101 01001110 01001111 '
    '01010000 01010001 01010010 01010011 01010100 01010101 01010110 01010111 '
    '01011000 01011001 01011010 01011011 01011100 01011101 01011110 01011111 '
    '01100000 01100001 01100010 01100011 01100100 01100101 01100110 01100111 '
    '01101000 01101001 01101010 01101011 01101100 01101101 01101110 01101111 '
    '01110000 01110001 01110010 01110011 01110100 01110101 01110110 01110111 '
    '01111000 01111001 01111010 01111011 01111100 01111101 01111110 01111111 '
 ).split()


def _check_decode(bits, expected):
    try:
        got = binary_to_denary(bits)
    except Exception as error:
        return "RED decoder: %s for %r: %s" % (type(error).__name__, bits, error)
    if type(got) is not int:
        return "RED decoder: %r must return an INT; got %r (%s)." % (bits, got, type(got).__name__)
    if got != expected:
        return "RED decoder: %r expected %d, got %d. Check the -128 column and column weights." % (bits, expected, got)
    return None


def _check_encode(n, expected):
    try:
        got = denary_to_binary(n)
    except Exception as error:
        return "RED encoder: %s for %r: %s" % (type(error).__name__, n, error)
    if type(got) is not str:
        return "RED encoder: %d must return a STRING; got %r (%s)." % (n, got, type(got).__name__)
    if len(got) != 8 or any(ch not in "01" for ch in got):
        return "RED encoder: expected exactly 8 binary characters for %d; got %r." % (n, got)
    if got != expected:
        return "RED encoder: %d expected %s, got %s. Keep eight bits and check negative values." % (n, expected, got)
    return None


def _judge():
    print("U06 SIGNED CONVERTER - local output checks, no marks")
    assert len(_EXPECTED) == 256
    decoder_ok = True
    for n, bits in zip(range(-128, 128), _EXPECTED):
        error = _check_decode(bits, n)
        if error:
            print(error)
            decoder_ok = False
            break
    if decoder_ok:
        print("Decoder PASS: all 256 patterns independently checked.")
    encoder_ok = True
    for n, bits in zip(range(-128, 128), _EXPECTED):
        error = _check_encode(n, bits)
        if error:
            print(error)
            encoder_ok = False
            break
    if encoder_ok:
        print("Encoder PASS: all 256 values independently checked.")
    if decoder_ok and encoder_ok:
        print("GREEN: both directions pass 512 independent checks.")
        print("Explain your algorithm on paper; these checks do not award method marks.")
    elif decoder_ok:
        print("Q10 decoder output checks pass. Reverse conversion is the optional extension.")
    else:
        print("Fix the decoder, then run again. Complete the paper reasoning separately.")
    return decoder_ok and encoder_ok


if __name__ == "__main__":
    _judge()
