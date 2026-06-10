"""
🔨 Whack-a-Mole
Type the number of the mole before it disappears!
"""

import random
import time
import os
import sys

# Add root directory to sys.path to import utils package
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils import save_score, get_top_scores

# Windows only for non-blocking input
try:
    import msvcrt
    has_msvcrt = True
except ImportError:
    has_msvcrt = False

GRID_SIZE  = 9        # 3×3 grid
MOLE       = "🐭"
HOLE       = "🕳️ "
HAMMER     = "🔨"

LEVELS = {
    "1": {"name": "Easy",   "window": 2.5, "rounds": 10, "moles": 1},
    "2": {"name": "Medium", "window": 1.5, "rounds": 15, "moles": 2},
    "3": {"name": "Hard",   "window": 0.8, "rounds": 20, "moles": 3},
}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("╔══════════════════════════════╗")
    print("║   🔨  WHACK-A-MOLE  🐭       ║")
    print("╚══════════════════════════════╝\n")
    print("  Difficulty:")
    for k, v in LEVELS.items():
        print(f"  {k} → {v['name']:8s}  ({v['window']}s window, {v['moles']} mole(s), {v['rounds']} rounds)")
    print()

    while True:
        level_choice = input("  Enter 1 / 2 / 3: ").strip()
        if level_choice in LEVELS:
            break
        print("  ⚠️  Enter 1, 2, or 3.")

    level = LEVELS[level_choice]
    window = level["window"]
    rounds = level["rounds"]
    n_moles = level["moles"]

    score = 0
    misses = 0
    reaction_times = []

    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n  🐭 {level['name']} mode — {rounds} rounds — {window}s per mole")
    print("  Type the number(s) and press Enter fast!\n")
    time.sleep(2)

    rnd = 1
    while rnd <= rounds:
        active = set(random.sample(range(GRID_SIZE), n_moles))
        hit = set()

        os.system("cls" if os.name == "nt" else "clear")
        print(f"  Round {rnd}/{rounds}  |  Score: {score}  |  Misses: {misses}\n")
        
        # Draw grid
        print()
        for row in range(3):
            line = "  "
            for col in range(3):
                idx = row * 3 + col
                if idx in hit:
                    line += f" {HAMMER}[{idx+1}] "
                elif idx in active:
                    line += f" {MOLE}[{idx+1}] "
                else:
                    line += f" {HOLE}[{idx+1}] "
            print(line)
        print()

        print("  Whack! Enter number(s) e.g. '2' or '1 3': ", end="", flush=True)

        user_input_str = ""
        start_ts = time.time()
        elapsed = 0
        timed_out = False

        if has_msvcrt:
            while True:
                elapsed = time.time() - start_ts
                if elapsed > window:
                    timed_out = True
                    break
                if msvcrt.kbhit():
                    char = msvcrt.getwche()
                    if char in ('\r', '\n'):
                        print() # New line
                        break
                    elif char == '\b': # Backspace
                        user_input_str = user_input_str[:-1]
                        print(" \b", end="", flush=True) # visual backspace hack
                    else:
                        user_input_str += char
                else:
                    time.sleep(0.01)
        else:
            # Fallback if not Windows (though prompt says user is on Windows)
            # Cannot do non-blocking easily without defs/threads or select.
            # Just do blocking input and check time.
            user_input_str = input()
            elapsed = time.time() - start_ts
            if elapsed > window:
                timed_out = True

        if not timed_out and user_input_str.strip():
            try:
                chosen = set(int(x) - 1 for x in user_input_str.split())
            except ValueError:
                chosen = set()

            valid_hits = chosen & active
            wrong_hits = chosen - active

            hit = valid_hits
            round_score = len(valid_hits) * 10
            round_miss = len(active - valid_hits) + len(wrong_hits)

            reaction_times.append(elapsed)

            score += round_score
            misses += round_miss

            os.system("cls" if os.name == "nt" else "clear")
            print(f"  Round {rnd}/{rounds}  |  Score: {score}  |  Misses: {misses}\n")
            
            # Draw grid
            print()
            for row in range(3):
                line = "  "
                for col in range(3):
                    idx = row * 3 + col
                    if idx in hit:
                        line += f" {HAMMER}[{idx+1}] "
                    elif idx in active:
                        line += f" {MOLE}[{idx+1}] "
                    else:
                        line += f" {HOLE}[{idx+1}] "
                print(line)
            print()

            if valid_hits == active and not wrong_hits:
                print(f"  ✅ Perfect hit! +{round_score}  ⚡ {elapsed:.2f}s")
            elif valid_hits:
                print(f"  ⚠️  Partial hit! +{round_score}  Missed: {len(active - valid_hits)}")
            else:
                print("  ❌ Missed!")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"  Round {rnd}/{rounds}  |  Score: {score}  |  Misses: {misses}\n")
            # Draw grid
            print()
            for row in range(3):
                line = "  "
                for col in range(3):
                    idx = row * 3 + col
                    if idx in hit:
                        line += f" {HAMMER}[{idx+1}] "
                    elif idx in active:
                        line += f" {MOLE}[{idx+1}] "
                    else:
                        line += f" {HOLE}[{idx+1}] "
                print(line)
            print()
            print("  ⏰ Too slow!")
            misses += n_moles

        time.sleep(0.9)
        gap = random.uniform(0.4, 1.0)
        time.sleep(gap)
        rnd += 1

    os.system("cls" if os.name == "nt" else "clear")
    print("\n╔══════════════════════════════════════╗")
    print("║         🏁  GAME OVER!               ║")
    print("╚══════════════════════════════════════╝\n")
    print(f"  🎯 Final Score : {score}")
    print(f"  ❌ Total Misses: {misses}")
    max_score = rounds * n_moles * 10
    accuracy = round((score / max_score) * 100) if max_score else 0
    print(f"  📊 Accuracy    : {accuracy}%")

    if reaction_times:
        avg_rt = sum(reaction_times) / len(reaction_times)
        print(f"  ⚡ Avg Reaction: {avg_rt:.2f}s")

    # Save and display high scores
    name = input("\n  Enter your name for the high scores board: ").strip()
    if name:
        save_score("Whack-a-Mole", name, score)
    
    print("\n🏆 ===== HIGH SCORES BOARD =====")
    top_scores = get_top_scores("Whack-a-Mole", 5)
    if top_scores:
        for idx, (p_name, p_score, p_time) in enumerate(top_scores):
            print(f"  {idx+1}. {p_name:15s} : {p_score:4d}  ({p_time})")
    else:
        print("  No high scores yet!")
    print("================================")

    while True:
        replay = input("\n  Play again? (y / n): ").strip().lower()
        if replay in ['y', 'yes', 'n', 'no']:
            break
        print("  ⚠️ Enter 'y' or 'n'.")
    if replay in ['n', 'no']:
        print("\n  Thanks for playing! 🔨\n")
        break