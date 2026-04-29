from glitch_analyzer import analyze_glitch
from evaluator import run_evaluation

def main():
    print(" Game Glitch Investigator (Applied AI System)\n")

    while True:
        print("\nMenu:")
        print("1. Analyze a glitch")
        print("2. Run reliability tests")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            report = input("\nDescribe the game glitch:\n> ")

            result = analyze_glitch(report)

            print("\n--- AI RESULT ---")
            print(f"Glitch Type: {result['glitch_type']}")
            print(f"Confidence: {result['confidence']}")

            print("\nLikely Causes:")
            for cause in result["likely_causes"]:
                print(f"- {cause}")

            print("\nSuggested Fixes:")
            for fix in result["suggested_fixes"]:
                print(f"- {fix}")

            print(f"\nGuardrail: {result['guardrail']}")

        elif choice == "2":
            run_evaluation()

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
