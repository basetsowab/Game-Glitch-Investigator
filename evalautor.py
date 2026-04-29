from glitch_analyzer import analyze_glitch

TESTS = [
    ("falling through the floor platform", "collision"),
    ("character stuck in t pose animation broken", "animation"),
    ("music cuts out no sound effects", "audio"),
    ("health bar disappears in pause menu", "ui"),
    ("game crashes loading next level", "crash"),
    ("game broken", "unknown")
]


def run_evaluation():
    print("\n--- Running Evaluation ---")

    passed = 0

    for i, (inp, expected) in enumerate(TESTS, 1):
        result = analyze_glitch(inp)
        actual = result["glitch_type"]

        status = "PASS" if actual == expected else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"\nTest {i}: {status}")
        print(f"Input: {inp}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print(f"Confidence: {result['confidence']}")

    total = len(TESTS)
    accuracy = round((passed / total) * 100, 2)

    print("\n--- SUMMARY ---")
    print(f"{passed}/{total} passed")
    print(f"Accuracy: {accuracy}%")
