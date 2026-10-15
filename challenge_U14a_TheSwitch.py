# -*- coding: utf-8 -*-
"""
🍦 THE ICE-CREAM CHALLENGE — U14a · The Switch
==================================================

The mark scheme's three sentences for a star topology are:

    the sending device sends the packets to the switch
    the switch checks the destination address
    ... and sends them only to the intended receiver

How does the switch KNOW which port the receiver is on? Nobody tells it. It
learns — from the frames that pass through it. You write that switch.

THE SET-UP (provided)

    A switch with PORTS numbered 1..5. A frame is (port, src, dst): it arrived on
    `port`, from the device with MAC address `src`, addressed to `dst`.
    Six frames arrive in order (FRAMES). The devices: A, B, C, D, E (their MAC
    addresses are the strings "A".."E" here — a real one is 48 bits).

╔══════════════════════════════════════════════════════════════════════════╗
║  PART 1 — WITH A PEN, BEFORE YOU WRITE A LINE OF CODE                    ║
║                                                                          ║
║  Fill the switch's table by hand for the six frames in FRAMES, one row   ║
║  per frame: after each frame, (i) what the table now holds (MAC → port), ║
║  (ii) which port(s) the frame went OUT of. The rule:                     ║
║    · LEARN: write the frame's src next to the port it arrived on         ║
║    · KNOWN destination → out of that one port only                       ║
║      (if that port is the one it arrived on, send nowhere)               ║
║    · UNKNOWN destination → out of every port except the one it came in  ║
║  Which frames flooded, and why did the flooding stop?                    ║
║                                                                          ║
║  Check yourself:  python3 challenge_U14a_TheSwitch.py trace              ║
╚══════════════════════════════════════════════════════════════════════════╝

PART 2 — THE CODE. A class with one method:

    class Switch:
        def __init__(self, ports):      # ports: how many ports, numbered 1..ports
            self.table = {}             # MAC address -> port number
        def receive(self, port, src, dst) -> list
            Learn src on `port`. Return the list of ports the frame goes out of:
            [p] if dst is known on port p (and p != port), [] if dst is known on
            the same port it came in on, every other port if dst is unknown.

Run this file to face the judge:   python3 challenge_U14a_TheSwitch.py

🍨 THE SECOND SCOOP — python3 challenge_U14a_TheSwitch.py bus
   The same six frames on a BUS: there is no switch, one cable, every frame
   reaches every device and only the addressed one keeps it — and when two
   frames are sent in the same moment, they collide. The scoop prints who
   heard what, and counts the collisions the star never had.
"""
import random
import sys

PORTS = 5
# (arrived on port, from, to) — the six frames, in order
FRAMES = [
    (1, "A", "B"),     # A speaks first: nobody is known yet
    (2, "B", "A"),     # B replies: A is known now
    (3, "C", "A"),
    (1, "A", "C"),
    (4, "D", "E"),     # E has never spoken
    (5, "E", "D"),
]


# ═══════════════════════ YOUR SWITCH ═══════════════════════

class Switch:
    def __init__(self, ports):
        self.ports = ports
        self.table = {}               # MAC address -> port number

    def receive(self, port, src, dst):
        """Learn where src lives; return the list of ports this frame goes out of."""
        out = []
        # YOUR CODE HERE
        return out


# ═══════════════════════════════ THE JUDGE ═══════════════════════════════

def _check(name, cond, why):
    print(("  ✅ " if cond else "  ❌ ") + name + ("" if cond else "\n       " + why))
    return bool(cond)


def _safe(fn, *a):
    try:
        return fn(*a), None
    except Exception as e:  # noqa: BLE001
        return None, repr(e)


class _RefSwitch:
    def __init__(self, ports):
        self.ports = ports; self.table = {}

    def receive(self, port, src, dst):
        self.table[src] = port
        if dst in self.table:
            return [] if self.table[dst] == port else [self.table[dst]]
        return [p for p in range(1, self.ports + 1) if p != port]


def _judge():
    print("🍦 The Switch — the judge\n")
    score, total = 0, 6

    sw, err = _safe(Switch, PORTS)
    got, err2 = _safe(sw.receive, 1, "A", "B") if err is None else (None, err)
    ok = err2 is None and isinstance(sw.table, dict) and sw.table.get("A") == 1
    score += _check("learn: after A's first frame arrives on port 1, the table says A → 1",
                    ok, ("error: %s" % (err or err2)) if (err or err2) else "table is %r — write the frame's source next to the port it came in on" % (getattr(sw, 'table', None),))

    ok = err2 is None and sorted(got or []) == [2, 3, 4, 5]
    score += _check("flood: B is unknown, so the frame goes out of every port except the one it came in on — [2, 3, 4, 5]",
                    ok, ("error: %s" % err2) if err2 else "got %r — an unknown destination is sent everywhere except back where it came from" % (got,))

    sw = Switch(PORTS); sw.receive(1, "A", "B")
    got, err = _safe(sw.receive, 2, "B", "A")
    ok = err is None and got == [1]
    score += _check("forward: B replies to A, and A is known on port 1 — the frame goes out of port 1 only",
                    ok, ("error: %s" % err) if err else "got %r — a known destination goes out of exactly one port, the one in the table" % (got,))

    sw = Switch(PORTS); sw.receive(1, "A", "B"); sw.receive(1, "X", "A")
    got, err = _safe(sw.receive, 1, "A", "X")      # X and A share port 1 (a hub hangs off it)
    ok = err is None and got == [] and sw.table.get("X") == 1
    score += _check("same port: a destination known on the port the frame arrived on is sent nowhere — []",
                    ok, ("error: %s" % err) if err else "got %r — the receiver already heard it; forwarding it back would duplicate it" % (got,))

    sw = Switch(PORTS); ref = _RefSwitch(PORTS); floods = []; ok = True; bad = None
    for port, src, dst in FRAMES:
        g, err = _safe(sw.receive, port, src, dst)
        r = ref.receive(port, src, dst)
        floods.append(len(r) > 1)
        if err or sorted(g or []) != sorted(r):
            ok = False; bad = (port, src, dst, g if not err else err, r); break
    ok = ok and floods == [True, False, False, False, True, False]
    score += _check("the six frames: floods on frames 1 and 5 only — the flooding stops as the table fills",
                    ok, "on frame (%r, %r, %r) got %r, the reference says %r" % bad if bad else "flood pattern was %r, expected [True, False, False, False, True, False]" % (floods,))

    sw = Switch(PORTS); sw.receive(1, "A", "B"); sw.receive(2, "B", "A"); sw.receive(3, "A", "B")   # A has moved to port 3
    got, err = _safe(sw.receive, 2, "B", "A")
    ok = err is None and got == [3] and sw.table.get("A") == 3
    score += _check("re-learn: A unplugs and reappears on port 3 — the next frame for A goes to port 3, not 1",
                    ok, ("error: %s" % err) if err else "got %r with table %r — learning overwrites: the newest port wins" % (got, getattr(sw, 'table', None)))

    print("\n" + ("🟢" if score == total else "🟡") + " %d / %d" % (score, total))
    if score == total:
        print("   That is the scheme's sentence, built: the switch checks the destination address and sends only to the intended receiver —")
        print("   and the one thing the scheme leaves out: it learnt the addresses from the frames themselves. Nobody configured it.")
        print("   🍨 second scoop:  python3 challenge_U14a_TheSwitch.py bus")


def _trace_mode():
    print("Part 1 — the judge's own trace of the six frames\n")
    ref = _RefSwitch(PORTS)
    for i, (port, src, dst) in enumerate(FRAMES, start=1):
        out = ref.receive(port, src, dst)
        how = "FLOOD (unknown)" if len(out) > 1 else ("nowhere (same port)" if not out else "port %d only (known)" % out[0])
        print("  frame %d: %s → %s in on port %d | table now %s | out: %s" % (i, src, dst, port, " ".join("%s→%d" % kv for kv in ref.table.items()), how))
    print("\n  Two floods: frame 1 (nobody known) and frame 5 (E has never spoken). Every other frame went to one port.")
    print("  The switch was never configured — it learnt every address from the frames it carried.")


def _bus():
    print("🍨 bus — the same six frames, one shared cable, no switch\n")
    devices = ["A", "B", "C", "D", "E"]
    # on a bus every frame reaches every device; the sender chooses a random moment to transmit
    random.seed(11)
    moments = [random.randrange(8) for _ in FRAMES]      # each frame picks one of eight moments
    collisions = 0
    for i, ((port, src, dst), t) in enumerate(zip(FRAMES, moments), start=1):
        others = [d for d in devices if d != src]
        clash = [j + 1 for j, m in enumerate(moments) if m == t and j != i - 1]
        if clash:
            collisions += 1
        print("  frame %d at moment %d: %s → %s — heard by %s; kept by %s%s" % (i, t, src, dst, ", ".join(others), dst, "  ✖ COLLIDES with frame %s" % ", ".join(map(str, clash)) if clash else ""))
    print("\n  Every frame reached four devices to be kept by one — that is the posting board. %d of 6 frames collided and would be resent." % collisions)
    print("  On the star, each frame went down one cable to the switch and one cable out; zero collisions, and nobody else heard it.")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "trace":
        _trace_mode()
    elif arg == "bus":
        _bus()
    else:
        _judge()
