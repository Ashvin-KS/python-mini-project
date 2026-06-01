"""
🔍 Interactive Search System for Python Mini Projects
=====================================================
Search, filter, and explore all projects by keyword,
category, or difficulty level.
"""

import os
import subprocess
import sys

# ─────────────────────────────────────────────
#  Project Registry
# ─────────────────────────────────────────────
PROJECTS = [
    {
        "name": "Rock Paper Scissors",
        "emoji": "🪨",
        "category": "games",
        "difficulty": "beginner",
        "description": "Battle against the computer in this classic hand game.",
        "keywords": ["rock", "paper", "scissors", "game", "battle", "computer"],
        "path": "games/Rock-Paper-Scissor/Rock-Paper-Scissor.py",
    },
    {
        "name": "Dice Rolling",
        "emoji": "🎲",
        "category": "games",
        "difficulty": "beginner",
        "description": "Roll two dice and calculate your fortune with emoji dice!",
        "keywords": ["dice", "roll", "random", "luck", "board"],
        "path": "games/Roling-Dice/Roling-Dice.py",
    },
    {
        "name": "Coin Flip",
        "emoji": "🪙",
        "category": "games",
        "difficulty": "beginner",
        "description": "Predict heads or tails — a quick decision maker.",
        "keywords": ["coin", "flip", "heads", "tails", "random"],
        "path": "games/Flipping-toss/Flipping-toss.py",
    },
    {
        "name": "Number Guessing Game",
        "emoji": "🎯",
        "category": "games",
        "difficulty": "beginner",
        "description": "Guess the computer's secret number with smart hints.",
        "keywords": ["guess", "number", "hints", "game", "interactive"],
        "path": "games/Number-Guessing-Game/Number-Guessing-Game.py",
    },
    {
        "name": "Hangman Game",
        "emoji": "🎮",
        "category": "games",
        "difficulty": "intermediate",
        "description": "Classic word-guessing game with 6 attempts.",
        "keywords": ["hangman", "word", "guess", "letters", "classic"],
        "path": "games/Hangman-Game/Hangman-Game.py",
    },
    {
        "name": "FLAMES Game",
        "emoji": "💖",
        "category": "games",
        "difficulty": "beginner",
        "description": "Discover your relationship status with two names!",
        "keywords": ["flames", "love", "relationship", "names", "fun"],
        "path": "games/FLAMES-Game/FLAMES-Game.py",
    },
    {
        "name": "Fibonacci Series",
        "emoji": "✨",
        "category": "math",
        "difficulty": "beginner",
        "description": "Generate beautiful Fibonacci sequences visually.",
        "keywords": ["fibonacci", "series", "sequence", "math", "pattern"],
        "path": "math/Fibonacci-Series/Fibonacci-Series.py",
    },
    {
        "name": "Pascal's Triangle",
        "emoji": "🔺",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Explore mathematical beauty in Pascal's triangle.",
        "keywords": ["pascal", "triangle", "pattern", "math", "rows"],
        "path": "math/Pascal-Triangle/Pascal-Triangle.py",
    },
    {
        "name": "Armstrong Number Checker",
        "emoji": "💎",
        "category": "math",
        "difficulty": "beginner",
        "description": "Check if a number is an Armstrong number with breakdown.",
        "keywords": ["armstrong", "number", "checker", "narcissistic", "math"],
        "path": "math/Armstrong-Number/Armstrong-Number.py",
    },
    {
        "name": "Simple Calculator",
        "emoji": "🧮",
        "category": "math",
        "difficulty": "beginner",
        "description": "All basic math operations plus power and modulus.",
        "keywords": ["calculator", "math", "arithmetic", "add", "subtract"],
        "path": "math/Simple-Calculator/Simple-Calculator.py",
    },
    {
        "name": "Prime Number Analyzer",
        "emoji": "🔱",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Check, generate, and factorize prime numbers.",
        "keywords": ["prime", "factor", "analyze", "sieve", "number theory"],
        "path": "math/Prime-Number-Analyzer/Prime-Number-Analyzer.py",
    },
    {
        "name": "Collatz Conjecture",
        "emoji": "🔢",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Explore the famous 3n+1 sequence until it reaches 1.",
        "keywords": ["collatz", "conjecture", "sequence", "3n+1", "math"],
        "path": "math/Collatz-Conjecture/Collatz-Conjecture.py",
    },
    {
        "name": "Projectile Motion Game",
        "emoji": "🚀",
        "category": "math",
        "difficulty": "advanced",
        "description": "Launch projectiles and visualize trajectory stats with matplotlib.",
        "keywords": ["projectile", "physics", "simulation", "trajectory", "matplotlib"],
        "path": "math/Projectile-Motion-Game/Projectile-Motion-Game.py",
    },
    {
        "name": "Derivative Calculator",
        "emoji": "∂",
        "category": "math",
        "difficulty": "advanced",
        "description": "Compute first and nth polynomial derivatives at any point.",
        "keywords": ["derivative", "calculus", "polynomial", "math", "algebra"],
        "path": "math/Derivative-Calculator/Derivative-Calculator.py",
    },
    {
        "name": "Coordinate to Polar Transformation",
        "emoji": "🧭",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Convert Cartesian (x,y) coordinates to polar form.",
        "keywords": ["polar", "cartesian", "coordinate", "geometry", "angle"],
        "path": "math/Coordinate-to-Polar-Transformation/Coordinate-to-Polar-Transformation.py",
    },
    {
        "name": "AP/GP/AGP/HP Recognizer",
        "emoji": "📐",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Identify progression types from any number sequence.",
        "keywords": ["progression", "arithmetic", "geometric", "harmonic", "sequence"],
        "path": "math/AP-GP-AGP-HP-Recognizer/AP-GP-AGP-HP-Recognizer.py",
    },
    {
        "name": "Morse Code Translator",
        "emoji": "📻",
        "category": "utilities",
        "difficulty": "beginner",
        "description": "Translate text to Morse code and back — bidirectional.",
        "keywords": ["morse", "code", "translate", "encrypt", "dots", "dashes"],
        "path": "utilities/Text-to-Morse/Text-to-Morse.py",
    },
    {
        "name": "Tower of Hanoi",
        "emoji": "🗼",
        "category": "utilities",
        "difficulty": "intermediate",
        "description": "Solve the classic Tower of Hanoi puzzle step by step.",
        "keywords": ["tower", "hanoi", "puzzle", "recursion", "algorithm"],
        "path": "utilities/Tower-of-Hanoi/Tower-of-Hanoi.py",
    },
]

DIFFICULTY_ORDER = {"beginner": 1, "intermediate": 2, "advanced": 3}

DIFFICULTY_BADGE = {
    "beginner":     "🟢 Beginner",
    "intermediate": "🟡 Intermediate",
    "advanced":     "🔴 Advanced",
}

CATEGORY_BADGE = {
    "games":     "🎮 Games",
    "math":      "🔢 Math",
    "utilities": "🔧 Utilities",
}


def banner():
    print("\n" + "═" * 56)
    print("   🔍  Python Mini Projects — Interactive Search")
    print("═" * 56)


def divider():
    print("─" * 56)


def display_project(idx, p, show_path=False):
    print(f"\n  [{idx}] {p['emoji']}  {p['name']}")
    print(f"       {CATEGORY_BADGE[p['category']]}   {DIFFICULTY_BADGE[p['difficulty']]}")
    print(f"       {p['description']}")
    if show_path:
        print(f"       📂 {p['path']}")


def display_results(results, show_path=False):
    if not results:
        print("\n  ⚠️  No projects found. Try a different search term.")
        return
    print(f"\n  ✅  Found {len(results)} project(s):\n")
    for idx, p in enumerate(results, start=1):
        display_project(idx, p, show_path)
        divider()


def search_by_keyword(query):
    q = query.lower().strip()
    return [
        p for p in PROJECTS
        if q in p["name"].lower()
        or q in p["description"].lower()
        or any(q in kw for kw in p["keywords"])
    ]


def filter_by_category(category):
    return [p for p in PROJECTS if p["category"] == category.lower().strip()]


def filter_by_difficulty(level):
    return [p for p in PROJECTS if p["difficulty"] == level.lower().strip()]


def launch_project(projects):
    if not projects:
        return
    divider()
    choice = input("  ▶  Enter project number to launch (or press Enter to skip): ").strip()
    if not choice:
        return
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(projects):
            path = projects[idx]["path"]
            if os.path.exists(path):
                print(f"\n  🚀  Launching: {path}\n")
                subprocess.run([sys.executable, path])
            else:
                print(f"\n  ⚠️  File not found: {path}")
                print("     Make sure you're running this from the repo root.")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")


def main():
    banner()

    while True:
        print("""
  📌  What would you like to do?

  1  🔍  Search by keyword
  2  📂  Browse by category  (games / math / utilities)
  3  📊  Filter by difficulty (beginner / intermediate / advanced)
  4  📋  List all projects
  5  ❌  Exit
""")
        choice = input("  Enter choice (1-5): ").strip()

        if choice == "1":
            divider()
            query = input("  🔍  Search Project: ").strip()
            if query:
                results = search_by_keyword(query)
                display_results(results, show_path=True)
                launch_project(results)
            else:
                print("  ⚠️  Please enter a search term.")

        elif choice == "2":
            divider()
            print("  Categories: games  |  math  |  utilities")
            cat = input("  📂  Enter category: ").strip()
            if cat in ("games", "math", "utilities"):
                results = filter_by_category(cat)
                display_results(results, show_path=True)
                launch_project(results)
            else:
                print("  ⚠️  Unknown category. Use: games, math, or utilities.")

        elif choice == "3":
            divider()
            print("  Levels: beginner  |  intermediate  |  advanced")
            level = input("  📊  Enter difficulty: ").strip()
            if level in ("beginner", "intermediate", "advanced"):
                results = filter_by_difficulty(level)
                results = sorted(results, key=lambda p: p["name"])
                display_results(results, show_path=True)
                launch_project(results)
            else:
                print("  ⚠️  Unknown level. Use: beginner, intermediate, or advanced.")

        elif choice == "4":
            all_sorted = sorted(
                PROJECTS,
                key=lambda p: (p["category"], DIFFICULTY_ORDER[p["difficulty"]])
            )
            display_results(all_sorted, show_path=False)
            launch_project(all_sorted)

        elif choice == "5":
            print("\n  👋  Happy coding! See you next time.\n")
            break

        else:
            print("  ⚠️  Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
EOFcat > search_projects.py << 'EOF'
"""
🔍 Interactive Search System for Python Mini Projects
=====================================================
Search, filter, and explore all projects by keyword,
category, or difficulty level.
"""

import os
import subprocess
import sys

# ─────────────────────────────────────────────
#  Project Registry
# ─────────────────────────────────────────────
PROJECTS = [
    {
        "name": "Rock Paper Scissors",
        "emoji": "🪨",
        "category": "games",
        "difficulty": "beginner",
        "description": "Battle against the computer in this classic hand game.",
        "keywords": ["rock", "paper", "scissors", "game", "battle", "computer"],
        "path": "games/Rock-Paper-Scissor/Rock-Paper-Scissor.py",
    },
    {
        "name": "Dice Rolling",
        "emoji": "🎲",
        "category": "games",
        "difficulty": "beginner",
        "description": "Roll two dice and calculate your fortune with emoji dice!",
        "keywords": ["dice", "roll", "random", "luck", "board"],
        "path": "games/Roling-Dice/Roling-Dice.py",
    },
    {
        "name": "Coin Flip",
        "emoji": "🪙",
        "category": "games",
        "difficulty": "beginner",
        "description": "Predict heads or tails — a quick decision maker.",
        "keywords": ["coin", "flip", "heads", "tails", "random"],
        "path": "games/Flipping-toss/Flipping-toss.py",
    },
    {
        "name": "Number Guessing Game",
        "emoji": "🎯",
        "category": "games",
        "difficulty": "beginner",
        "description": "Guess the computer's secret number with smart hints.",
        "keywords": ["guess", "number", "hints", "game", "interactive"],
        "path": "games/Number-Guessing-Game/Number-Guessing-Game.py",
    },
    {
        "name": "Hangman Game",
        "emoji": "🎮",
        "category": "games",
        "difficulty": "intermediate",
        "description": "Classic word-guessing game with 6 attempts.",
        "keywords": ["hangman", "word", "guess", "letters", "classic"],
        "path": "games/Hangman-Game/Hangman-Game.py",
    },
    {
        "name": "FLAMES Game",
        "emoji": "💖",
        "category": "games",
        "difficulty": "beginner",
        "description": "Discover your relationship status with two names!",
        "keywords": ["flames", "love", "relationship", "names", "fun"],
        "path": "games/FLAMES-Game/FLAMES-Game.py",
    },
    {
        "name": "Fibonacci Series",
        "emoji": "✨",
        "category": "math",
        "difficulty": "beginner",
        "description": "Generate beautiful Fibonacci sequences visually.",
        "keywords": ["fibonacci", "series", "sequence", "math", "pattern"],
        "path": "math/Fibonacci-Series/Fibonacci-Series.py",
    },
    {
        "name": "Pascal's Triangle",
        "emoji": "🔺",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Explore mathematical beauty in Pascal's triangle.",
        "keywords": ["pascal", "triangle", "pattern", "math", "rows"],
        "path": "math/Pascal-Triangle/Pascal-Triangle.py",
    },
    {
        "name": "Armstrong Number Checker",
        "emoji": "💎",
        "category": "math",
        "difficulty": "beginner",
        "description": "Check if a number is an Armstrong number with breakdown.",
        "keywords": ["armstrong", "number", "checker", "narcissistic", "math"],
        "path": "math/Armstrong-Number/Armstrong-Number.py",
    },
    {
        "name": "Simple Calculator",
        "emoji": "🧮",
        "category": "math",
        "difficulty": "beginner",
        "description": "All basic math operations plus power and modulus.",
        "keywords": ["calculator", "math", "arithmetic", "add", "subtract"],
        "path": "math/Simple-Calculator/Simple-Calculator.py",
    },
    {
        "name": "Prime Number Analyzer",
        "emoji": "🔱",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Check, generate, and factorize prime numbers.",
        "keywords": ["prime", "factor", "analyze", "sieve", "number theory"],
        "path": "math/Prime-Number-Analyzer/Prime-Number-Analyzer.py",
    },
    {
        "name": "Collatz Conjecture",
        "emoji": "🔢",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Explore the famous 3n+1 sequence until it reaches 1.",
        "keywords": ["collatz", "conjecture", "sequence", "3n+1", "math"],
        "path": "math/Collatz-Conjecture/Collatz-Conjecture.py",
    },
    {
        "name": "Projectile Motion Game",
        "emoji": "🚀",
        "category": "math",
        "difficulty": "advanced",
        "description": "Launch projectiles and visualize trajectory stats with matplotlib.",
        "keywords": ["projectile", "physics", "simulation", "trajectory", "matplotlib"],
        "path": "math/Projectile-Motion-Game/Projectile-Motion-Game.py",
    },
    {
        "name": "Derivative Calculator",
        "emoji": "∂",
        "category": "math",
        "difficulty": "advanced",
        "description": "Compute first and nth polynomial derivatives at any point.",
        "keywords": ["derivative", "calculus", "polynomial", "math", "algebra"],
        "path": "math/Derivative-Calculator/Derivative-Calculator.py",
    },
    {
        "name": "Coordinate to Polar Transformation",
        "emoji": "🧭",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Convert Cartesian (x,y) coordinates to polar form.",
        "keywords": ["polar", "cartesian", "coordinate", "geometry", "angle"],
        "path": "math/Coordinate-to-Polar-Transformation/Coordinate-to-Polar-Transformation.py",
    },
    {
        "name": "AP/GP/AGP/HP Recognizer",
        "emoji": "📐",
        "category": "math",
        "difficulty": "intermediate",
        "description": "Identify progression types from any number sequence.",
        "keywords": ["progression", "arithmetic", "geometric", "harmonic", "sequence"],
        "path": "math/AP-GP-AGP-HP-Recognizer/AP-GP-AGP-HP-Recognizer.py",
    },
    {
        "name": "Morse Code Translator",
        "emoji": "📻",
        "category": "utilities",
        "difficulty": "beginner",
        "description": "Translate text to Morse code and back — bidirectional.",
        "keywords": ["morse", "code", "translate", "encrypt", "dots", "dashes"],
        "path": "utilities/Text-to-Morse/Text-to-Morse.py",
    },
    {
        "name": "Tower of Hanoi",
        "emoji": "🗼",
        "category": "utilities",
        "difficulty": "intermediate",
        "description": "Solve the classic Tower of Hanoi puzzle step by step.",
        "keywords": ["tower", "hanoi", "puzzle", "recursion", "algorithm"],
        "path": "utilities/Tower-of-Hanoi/Tower-of-Hanoi.py",
    },
]

DIFFICULTY_ORDER = {"beginner": 1, "intermediate": 2, "advanced": 3}

DIFFICULTY_BADGE = {
    "beginner":     "🟢 Beginner",
    "intermediate": "🟡 Intermediate",
    "advanced":     "🔴 Advanced",
}

CATEGORY_BADGE = {
    "games":     "🎮 Games",
    "math":      "🔢 Math",
    "utilities": "🔧 Utilities",
}


def banner():
    print("\n" + "═" * 56)
    print("   🔍  Python Mini Projects — Interactive Search")
    print("═" * 56)


def divider():
    print("─" * 56)


def display_project(idx, p, show_path=False):
    print(f"\n  [{idx}] {p['emoji']}  {p['name']}")
    print(f"       {CATEGORY_BADGE[p['category']]}   {DIFFICULTY_BADGE[p['difficulty']]}")
    print(f"       {p['description']}")
    if show_path:
        print(f"       📂 {p['path']}")


def display_results(results, show_path=False):
    if not results:
        print("\n  ⚠️  No projects found. Try a different search term.")
        return
    print(f"\n  ✅  Found {len(results)} project(s):\n")
    for idx, p in enumerate(results, start=1):
        display_project(idx, p, show_path)
        divider()


def search_by_keyword(query):
    q = query.lower().strip()
    return [
        p for p in PROJECTS
        if q in p["name"].lower()
        or q in p["description"].lower()
        or any(q in kw for kw in p["keywords"])
    ]


def filter_by_category(category):
    return [p for p in PROJECTS if p["category"] == category.lower().strip()]


def filter_by_difficulty(level):
    return [p for p in PROJECTS if p["difficulty"] == level.lower().strip()]


def launch_project(projects):
    if not projects:
        return
    divider()
    choice = input("  ▶  Enter project number to launch (or press Enter to skip): ").strip()
    if not choice:
        return
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(projects):
            path = projects[idx]["path"]
            if os.path.exists(path):
                print(f"\n  🚀  Launching: {path}\n")
                subprocess.run([sys.executable, path])
            else:
                print(f"\n  ⚠️  File not found: {path}")
                print("     Make sure you're running this from the repo root.")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")


def main():
    banner()

    while True:
        print("""
  📌  What would you like to do?

  1  🔍  Search by keyword
  2  📂  Browse by category  (games / math / utilities)
  3  📊  Filter by difficulty (beginner / intermediate / advanced)
  4  📋  List all projects
  5  ❌  Exit
""")
        choice = input("  Enter choice (1-5): ").strip()

        if choice == "1":
            divider()
            query = input("  🔍  Search Project: ").strip()
            if query:
                results = search_by_keyword(query)
                display_results(results, show_path=True)
                launch_project(results)
            else:
                print("  ⚠️  Please enter a search term.")

        elif choice == "2":
            divider()
            print("  Categories: games  |  math  |  utilities")
            cat = input("  📂  Enter category: ").strip()
            if cat in ("games", "math", "utilities"):
                results = filter_by_category(cat)
                display_results(results, show_path=True)
                launch_project(results)
            else:
                print("  ⚠️  Unknown category. Use: games, math, or utilities.")

        elif choice == "3":
            divider()
            print("  Levels: beginner  |  intermediate  |  advanced")
            level = input("  📊  Enter difficulty: ").strip()
            if level in ("beginner", "intermediate", "advanced"):
                results = filter_by_difficulty(level)
                results = sorted(results, key=lambda p: p["name"])
                display_results(results, show_path=True)
                launch_project(results)
            else:
                print("  ⚠️  Unknown level. Use: beginner, intermediate, or advanced.")

        elif choice == "4":
            all_sorted = sorted(
                PROJECTS,
                key=lambda p: (p["category"], DIFFICULTY_ORDER[p["difficulty"]])
            )
            display_results(all_sorted, show_path=False)
            launch_project(all_sorted)

        elif choice == "5":
            print("\n  👋  Happy coding! See you next time.\n")
            break

        else:
            print("  ⚠️  Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
