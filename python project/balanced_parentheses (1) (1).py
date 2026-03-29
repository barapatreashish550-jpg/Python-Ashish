def is_balanced(expr):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != match[ch]:
                return False
    return len(stack) == 0


def run_tests():
    tests = ["()", "({[]})", "({[}])", "(((", "a+(b*c)"]
    print("\nTest Cases:")
    for t in tests:
        print(f"{t:10} -> {'Balanced' if is_balanced(t) else 'Not Balanced'}")


def show_history(history):
    if not history:
        print("No history yet!")
        return
    print("\nHistory:")
    for i, (expr, res) in enumerate(history, 1):
        print(f"{i}. {expr} -> {'Balanced' if res else 'Not Balanced'}")


def main():
    history = []

    while True:
        print("\n--- MENU ---")
        print("1. Check Expression")
        print("2. Run Test Cases")
        print("3. Show History")
        print("4. Clear History")
        print("Q. Quit")

        choice = input("Enter choice: ").upper()

        if choice == '1':
            expr = input("Enter expression: ")
            result = is_balanced(expr)
            print("Balanced ✅" if result else "Not Balanced ❌")
            history.append((expr, result))

        elif choice == '2':
            run_tests()

        elif choice == '3':
            show_history(history)

        elif choice == '4':
            history.clear()
            print("History cleared!")

        elif choice == 'Q':
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
