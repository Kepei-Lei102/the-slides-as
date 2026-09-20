"""U04 optional Ice-Cream Challenge — Hex Translator (0 extra marks).

Do the paper-first box first: IG Q6 / AS Q10. Those six marks are on paper.
Then implement BOTH functions below, without int(), hex() or bin().

Contract:
* binary_to_hex accepts a nonempty string containing only 0 and 1.
  Pad on the LEFT to a multiple of four. Return one uppercase hex digit per
  padded nibble, preserving leading zero nibbles: '00000001' -> '01'.
* hex_to_binary accepts a nonempty string of 0-9 / A-F / a-f, without 0x.
  Return exactly FOUR bits per supplied hex digit, including leading zeroes.
* Both functions raise ValueError for empty or invalid strings. Inputs are str.
* No whitespace or prefixes in accepted inputs. Do not silently strip them.

Run this file for local checks. Passing examples is useful evidence, not a
proof for every input. Explain your method and demonstrate both directions.
"""

def binary_to_hex(bits):
    # TODO: validate, pad, group, translate; use a nibble lookup table.
    raise NotImplementedError('Write binary_to_hex after your paper plan.')


def hex_to_binary(digits):
    # TODO: validate, normalise case, translate each digit to four bits.
    raise NotImplementedError('Write hex_to_binary after your paper plan.')


def run_checks():
    tests = [
        (binary_to_hex, '1', '1'),
        (binary_to_hex, '00000001', '01'),
        (binary_to_hex, '101011', '2B'),
        (binary_to_hex, '111100001', '1E1'),
        (hex_to_binary, '00', '00000000'),
        (hex_to_binary, 'a7', '10100111'),
        (hex_to_binary, '4D', '01001101'),
    ]
    passed = 0
    for fn, value, expected in tests:
        try:
            actual = fn(value)
            ok = actual == expected
            print(('PASS' if ok else 'FAIL'), fn.__name__, repr(value),
                  'got', repr(actual), 'expected', repr(expected))
            passed += ok
        except Exception as exc:
            print('FAIL', fn.__name__, repr(value), type(exc).__name__, str(exc))
    for fn, value in [(binary_to_hex, ''), (binary_to_hex, '102'),
                      (binary_to_hex, ' 10'), (hex_to_binary, ''),
                      (hex_to_binary, 'G1'), (hex_to_binary, '0x10')]:
        try:
            fn(value)
            print('FAIL', fn.__name__, repr(value), 'expected ValueError')
        except ValueError:
            print('PASS', fn.__name__, repr(value), 'rejected')
            passed += 1
        except Exception as exc:
            print('FAIL', fn.__name__, repr(value), type(exc).__name__)
    print(str(passed) + '/13 local checks passed. Built-in ban: human code review.')
    return passed


if __name__ == '__main__':
    run_checks()
