#!/usr/bin/env python3
"""U09d · The RLE engine · IG and AS practice Q9.

PEN FIRST: write your encoder plan and prediction on the practice sheet.
Then complete encode and decode below. Run this file to check the 3 code marks.
The plan (2) and prediction (1) are human marked: total task = 6 marks.

Contract
  * Input symbols: printable ASCII except digits; spaces/punctuation included.
  * Case matters. Counts are positive decimal integers, including multi-digit.
  * Format: count then one symbol, e.g. '3P2q' represents 'PPPqq'.
  * Canonical: one maximal run per count/symbol pair; no leading count zeroes.
  * Empty data encodes to ''; empty code decodes to ''.
  * Decoder inputs are valid canonical encodings. No invalid-input handling.
  * Functions work independently, using their argument, without shared caches.
Use loops; do not import a compression/grouping library. Tests are evidence,
not universal proof; a teacher also reviews the method. Change only your three
functions. The optional smart_encode task carries no marks.
"""


def encode(data):
    """Return the canonical count-before-symbol encoding of data."""
    # TODO: your loop-based encoder
    return ""


def decode(code):
    """Return the original string from a valid canonical code."""
    # TODO: your loop-based decoder
    return ""


def smart_encode(data):
    """Optional: (True, RLE) if strictly shorter; else (False, original data).

    The bool is the mode flag. If serialised, assume one extra flag byte
    whichever representation you choose. Compare payload lengths to choose;
    account for the flag separately when explaining total stored size.
    """
    # TODO: optional extension
    return False, data


# ---- Checks: leave these intact. They compare with independent expectations. ----
ENCODE_CASES = (
    ("", ""), ("X", "1X"), ("HHHHH", "5H"), ("xyxy", "1x1y1x1y"),
    ("aAAa", "1a2A1a"), ("  !! ", "2 2!1 "), ("R" * 12, "12R"),
    ("_" * 101 + "?" * 3, "101_3?"), ("C" * 17 + "d" * 2 + "C", "17C2d1C"),
)
DECODE_CASES = (
    ("", ""), ("1Q", "Q"), ("2b1A3b", "bbAbbb"),
    ("11m2N", "m" * 11 + "NN"), ("3 2!1 ", "   !! "),
    ("100Z1z", "Z" * 100 + "z"), ("1/1:1;", "/:;"),
)


def judge(verbose=True):
    """Return three separate code results, marks 0..3, and an unmarked result."""
    failures = {"encoding": [], "decoding": [], "independence": [], "optional": []}

    def check(group, label, action, expected):
        try:
            got = action()
            if type(got) is not type(expected) or got != expected:
                failures[group].append(f"{label}: expected {expected!r}, got {got!r}")
        except Exception as exc:
            failures[group].append(f"{label}: {type(exc).__name__}: {exc}")

    # Decode first, so success cannot depend on an earlier encoding call.
    for code, expected in DECODE_CASES:
        check("decoding", repr(code), lambda c=code: decode(c), expected)
    for data, expected in ENCODE_CASES:
        check("encoding", repr(data), lambda d=data: encode(d), expected)

    # Store several results before decoding any of them. Changed cases include
    # transitions, spaces, letter case, and count lengths of one/two/three digits.
    pending = []
    for symbol, other in [("V", "v"), (" ", "!"), ("@", "#")]:
        for n in [1, 2, 9, 10, 13, 99, 100]:
            data = symbol * n + other * 3 + symbol * 2
            expected = f"{n}{symbol}3{other}2{symbol}"
            check("independence", "changed encoding " + repr(data), lambda d=data: encode(d), expected)
            try:
                pending.append((data, encode(data)))
            except Exception as exc:
                failures["independence"].append(f"round trip encoding: {type(exc).__name__}")
    for data, encoded in reversed(pending):
        check("independence", "earlier input " + repr(data), lambda c=encoded: decode(c), data)
    for code, expected in reversed(DECODE_CASES):
        check("independence", "standalone decoding " + repr(code), lambda c=code: decode(c), expected)

    for data, expected in [
        ("", (False, "")), ("AA", (False, "AA")), ("AB", (False, "AB")),
        ("YYY", (True, "3Y")), ("a" * 14, (True, "14a")),
        ("!" * 3 + " " * 4, (True, "3!4 ")),
    ]:
        def attempt(d=data):
            result = smart_encode(d)
            if not isinstance(result, tuple) or len(result) != 2 or type(result[0]) is not bool or type(result[1]) is not str:
                raise TypeError("return exactly (bool, string)")
            return result
        check("optional", repr(data), attempt, expected)
    passed = {name: not errors for name, errors in failures.items()}
    marks = sum(passed[name] for name in ["encoding", "decoding", "independence"])
    result = {"passed": passed, "code_marks": marks, "failures": failures}
    if verbose:
        for name in ["encoding", "decoding", "independence"]:
            print(f"{name}: {int(passed[name])}/1")
            for message in failures[name][:2]:
                print("  " + message)
        print(f"Code: {marks}/3. Add the teacher-marked plan /2 and prediction /1.")
        print("Optional extension: " + ("all cases passed" if passed["optional"] else "not yet passed") + " (unmarked)")
        for message in failures["optional"][:1]:
            print("  " + message)
    return result


if __name__ == "__main__":
    judge()
