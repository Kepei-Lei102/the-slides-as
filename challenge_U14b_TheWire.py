# -*- coding: utf-8 -*-
"""
🍦 THE ICE-CREAM CHALLENGE — U14b · The Wire
==================================================

Ethernet's rule for a shared wire — Carrier Sense Multiple Access with Collision Detection:

    the STATION listens to the wire and sends only when it is quiet;
    two can still start in the same instant — a collision;
    each detects it, aborts, sends a jamming signal,
    waits a random number of slots (0 … 2^k − 1, k = how many times it has collided),
    and tries again.

A protocol cannot do anything. The stations do. You write the station.

THE SET-UP (provided)

    Time runs in SLOTS. A frame takes FRAME_SLOTS (4) slots to send. Each slot, the wire tells
    every station whether it was BUSY in the previous slot. A station is given frames to send
    (station.queue counts them). The judge drives eight stations for 2000 slots.

╔══════════════════════════════════════════════════════════════════════════╗
║  PART 1 — WITH A PEN, BEFORE YOU WRITE A LINE OF CODE                    ║
║                                                                          ║
║  Three stations A, B, C on one wire. A frame takes 4 slots. A and B both ║
║  get a frame in slot 1; C gets one in slot 10. When stations collide,     ║
║  their random draws are given: A draws 1, B draws 0 (k = 1: 0 or 1).     ║
║  Draw a slot-by-slot table (slots 1 … 16): for each station write         ║
║  listen / send / COLLIDE / jam / wait / done. In which slot does each     ║
║  frame finish, and how many collisions happened in all?                  ║
║                                                                          ║
║  Check yourself:  python3 challenge_U14b_TheWire.py trace                ║
╚══════════════════════════════════════════════════════════════════════════╝

PART 2 — THE CODE. A class with one method:

    class Station:
        queue      how many frames it still has to send (the judge adds to it)
        def tick(self, wire_busy, collided) -> "send" | "idle"
            Called once per slot. wire_busy: was another station transmitting last slot?
            collided: did MY transmission collide last slot (the wire tells me)?
            Return "send" if I put a signal on the wire this slot, else "idle".
            Keep your own state: slots left in the current frame, back-off slots left,
            collision count k. When a frame's 4 slots complete, queue -= 1.
            On a collision: abort the frame (it must be sent again from the start),
            k += 1, wait random.randrange(2 ** k) slots, then listen again.

Run this file to face the judge:   python3 challenge_U14b_TheWire.py

🍨 THE SCOOPS — python3 challenge_U14b_TheWire.py switch · hidden
   switch: the same stations, each on its own cable to a switch — count the collisions.
   hidden: two stations that cannot HEAR each other (Wi-Fi's problem) — watch what CD cannot do.
"""
import random
import sys

FRAME_SLOTS = 4


# ═══════════════════════ YOUR STATION ═══════════════════════

class Station:
    def __init__(self, name):
        self.name = name
        self.queue = 0            # frames waiting to be sent
        # YOUR STATE HERE (slots left in the frame, back-off slots left, collisions so far)

    def tick(self, wire_busy, collided):
        """Return "send" if this station transmits this slot, otherwise "idle"."""
        # YOUR CODE HERE
        return "idle"


# ═══════════════════════════════ THE JUDGE ═══════════════════════════════

def _run(stations, slots, p, seed=1, switch=False, deaf=None, log=None):
    """Drive the stations. Returns (delivered, collisions, mean wait, offered)."""
    random.seed(seed); busy = False; collided = {s: False for s in stations}
    collisions = delivered = offered = 0; waits = []; ready = {s: None for s in stations}
    for t in range(slots):
        for s in stations:
            if random.random() < p:
                s.queue += 1; offered += 1
                if ready[s] is None: ready[s] = t
        before = {s: s.queue for s in stations}
        acts = {s: s.tick(False if switch else (busy and not (deaf and s in deaf and busy == 'far')), collided[s]) for s in stations}
        sending = [s for s in stations if acts[s] == "send"]
        for s in stations: collided[s] = False
        if not switch and len(sending) > 1:
            collisions += 1
            for s in sending: collided[s] = True
            if log is not None: log.append((t, "COLLISION " + "+".join(s.name for s in sending)))
        else:
            for s in sending:
                if s.queue < before[s]:
                    delivered += 1; waits.append(t - (FRAME_SLOTS - 1) - (ready[s] if ready[s] is not None else t))
                    ready[s] = t if s.queue else None
                    if log is not None: log.append((t, s.name + " delivered"))
        busy = bool(sending)
    return delivered, collisions, (sum(waits) / len(waits) if waits else 0.0), offered


def _check(name, cond, why):
    print(("  ✅ " if cond else "  ❌ ") + name + ("" if cond else "\n       " + why))
    return bool(cond)


def _judge():
    print("🍦 The Wire — the judge\n")
    score, total = 0, 6
    random.seed(1)

    # 1 a lone station with one frame sends it in 4 consecutive slots
    s = Station("A"); s.queue = 1; acts = [s.tick(False, False) for _ in range(8)]
    ok = acts[:4] == ["send"] * 4 and acts[4:] == ["idle"] * 4 and s.queue == 0
    score += _check("a lone station sends its frame in four consecutive slots, then goes quiet, queue 0",
                    ok, "got %r, queue %r — a frame is FRAME_SLOTS slots of 'send', and queue drops by 1 when it completes" % (acts, s.queue))

    # 2 it listens: with the wire busy it does not start
    s = Station("A"); s.queue = 1; acts = [s.tick(True, False) for _ in range(3)] + [s.tick(False, False)]
    ok = acts[:3] == ["idle"] * 3 and acts[3] == "send"
    score += _check("carrier sense: while the wire is busy it stays idle; the first quiet slot, it starts",
                    ok, "got %r — check wire_busy before starting a frame" % (acts,))

    # 3 a collision aborts the frame, and the frame is resent from the start
    s = Station("A"); s.queue = 1; a1 = s.tick(False, False); a2 = s.tick(False, True)    # collided in slot 1
    ok = a1 == "send" and a2 == "idle" and s.queue == 1
    later = []
    for _ in range(40):
        later.append(s.tick(False, False))
    ok = ok and later.count("send") == FRAME_SLOTS and s.queue == 0
    score += _check("collision detection: told 'collided', it aborts (idle, frame still queued) and later resends all four slots",
                    ok, "after the collision: %r then %d sends, queue %r — abort means the whole frame goes again" % (a2, later.count('send'), s.queue))

    # 4 binary exponential back-off: the wait after k collisions is drawn from 0..2^k-1
    draws = {1: set(), 2: set(), 3: set()}
    for trial in range(300):
        random.seed(trial); s = Station("A"); s.queue = 1
        started = s.tick(False, False) == "send"              # the first slot of the frame
        for k in (1, 2, 3):
            s.tick(False, True)                                # collided on the slot just sent
            wait = 0
            while wait < 5000 and s.tick(False, False) == "idle": wait += 1     # ends on the retry's first 'send'
            draws[k].add(wait)
    ok = started and all(draws[k] and draws[k] <= set(range(2 ** k)) and max(draws[k]) == 2 ** k - 1 and 0 in draws[k] for k in (1, 2, 3))
    score += _check("binary back-off: after 1, 2, 3 collisions the wait is drawn from 0…1, 0…3, 0…7 — the range doubles each time",
                    ok, "waits seen: %s — use random.randrange(2 ** k) with k counting this frame's collisions, and reset k when the frame gets through" % ({k: sorted(v) for k, v in draws.items()},))

    # 5 the shared wire: everything eventually arrives; with more stations the mean wait grows
    res = {}
    for n in (2, 8):
        st = [Station("S%d" % i) for i in range(n)]
        res[n] = _run(st, 2000, 0.02, seed=3)
    ok = all(res[n][0] >= 0.9 * res[n][3] - 2 for n in (2,)) and res[8][0] > 0 and res[8][2] > res[2][2] and res[8][1] > 0
    score += _check("eight stations, 2000 slots: %d of %d frames delivered after %d collisions; the mean wait %.1f slots against %.1f with two" % (res[8][0], res[8][3], res[8][1], res[8][2], res[2][2]),
                    ok, "eight stations should still deliver, with collisions, and wait longer than two — check that a collision does not lose the frame")

    # 6 the sting: one station that never listens and talks a lot — what it does to the seven that keep the rule
    class _Deaf(Station):
        def tick(self, wire_busy, collided): return super().tick(False, collided)      # never hears the wire
    def polite_delivered(stations, ps, seed):
        random.seed(seed); busy = False; coll = {s: False for s in stations}; got = 0
        for t in range(2000):
            for s, pp in zip(stations, ps):
                if random.random() < pp: s.queue += 1
            before = {s: s.queue for s in stations}
            acts = {s: s.tick(busy, coll[s]) for s in stations}
            sending = [s for s in stations if acts[s] == "send"]
            for s in stations: coll[s] = False
            if len(sending) > 1:
                for s in sending: coll[s] = True
            else:
                for s in sending:
                    if s.queue < before[s] and s.name.startswith("S"): got += 1
            busy = bool(sending)
        return got
    g1 = polite_delivered([Station("S%d" % i) for i in range(7)] + [Station("X")], [0.02] * 7 + [0.1], 5)
    g2 = polite_delivered([Station("S%d" % i) for i in range(7)] + [_Deaf("ALOHA")], [0.02] * 7 + [0.1], 5)
    ok = g1 > 0 and g2 < 0.75 * g1
    score += _check("the sting: a talkative eighth station that keeps the rule leaves the seven %d frames; one that never listens leaves them %d" % (g1, g2),
                    ok, "the seven polite stations should lose more than a quarter of their deliveries — the deaf one starts whenever it likes, and they hear it busy and wait")

    print("\n" + ("🟢" if score == total else "🟡") + " %d / %d" % (score, total))
    if score == total:
        print("   That is the scheme's four lines, built: listen · send when quiet · detect, abort, jam · wait a random, doubling time.")
        print("   And the report's sentence: the protocol did nothing — your Station did all of it.")
        print("   🍨 scoops:  python3 challenge_U14b_TheWire.py switch   ·   hidden")


# Fixed demonstration fixtures; no Station implementation is shipped here.
def _trace():
    print('Part 1 — fixed trace fixture: A and B get a frame in slot 1, C in slot 10; on the collision A draws 1, B draws 0\n\n  slot   A               B               C\n     1   COLLIDE         COLLIDE         —              \n     2   jam, draw 1     jam, draw 0     —              \n     3   wait 1          send            —              \n     4   listen          send            —              \n     5   listen          send            —              \n     6   listen          send → DONE     —              \n     7   listen          —               —              \n     8   send            —               —              \n     9   send            —               —              \n    10   send            —               listen         \n    11   send → DONE     —               listen         \n    12   —               —               listen         \n    13   —               —               send           \n    14   —               —               send           \n    15   —               —               send           \n    16   —               —               send → DONE    \n\n  One collision (slot 1). B sends in slots 3–6; A sends in slots 8–11; C sends in slots 13–16.\n  read the table for the order the three frames finished. Nobody told the stations the order: the rule and the draws did.\n')


def _switch():
    print("Recorded example with a completed station (not your current code):")
    print('🍨 switch — the same eight stations, each on its own cable to a switch\n\n  delivered 342 of 344, collisions 0, mean wait 0.0 slots — a cable joins two devices, so nobody can collide with anybody.\n  on one wire: delivered 249 of 330, collisions 174, mean wait 22.4 slots.\n')


def _hidden():
    print("Two wireless clients may each hear an access point but not each other.")
    print("Their carrier-sense readings can both be idle while the other is sending.")
    print("A sender cannot reliably detect the resulting collision at the receiver.")
    print("Wi-Fi therefore uses avoidance and acknowledgements rather than Ethernet CD.")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "trace": _trace()
    elif arg == "switch": _switch()
    elif arg == "hidden": _hidden()
    else: _judge()
