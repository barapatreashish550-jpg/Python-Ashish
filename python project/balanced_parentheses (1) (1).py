# ============================================================
#  Stack-Based Balanced Parenthesis / Bracket / Brace Checker
#          Enhanced Edition with Visual CLI
# ============================================================

import time
import sys
import os
from typing import Tuple, List, Dict

# ------------------------------------------------------------------
# ANSI Color Codes for Beautiful CLI Output
# ------------------------------------------------------------------

class Colors:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    # Bright colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"


def colorize(text: str, color: str) -> str:
    """Apply color to text."""
    return f"{color}{text}{Colors.RESET}"


def bold(text: str) -> str:
    """Make text bold."""
    return f"{Colors.BOLD}{text}{Colors.RESET}"


# ------------------------------------------------------------------
# ASCII Art Banner
# ------------------------------------------------------------------

BANNER = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██████╗ ║
║   ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗║
║      ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██████╔╝║
║      ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██╔══██╗║
║      ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║██║  ██║║
║      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝║
║                                                                   ║
║         ██████╗ ███████╗███████╗████████╗                       ║
║         ██╔══██╗██╔════╝██╔════╝╚══██╔══╝                       ║
║         ██║  ██║█████╗  ███████╗   ██║                          ║
║         ██║  ██║██╔══╝  ╚════██║   ██║                          ║
║         ██████╔╝███████╗███████║   ██║                          ║
║         ╚═════╝ ╚══════╝╚══════╝   ╚═╝                          ║
║                                                                   ║
║              ███████╗ ██████╗ ██████╗ ███████╗                   ║
║              ██╔════╝██╔═══██╗██╔══██╗██╔════╝                   ║
║              ███████╗██║   ██║██████╔╝█████╗                     ║
║              ╚════██║██║   ██║██╔══██╗██╔══╝                     ║
║              ███████║╚██████╔╝██║  ██║███████╗                   ║
║              ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝                   ║
║                                                                   ║
{Colors.RESET}{Colors.DIM}                    🔍 Balanced Parenthesis Checker 🔍{Colors.RESET}
{Colors.CYAN}╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""


# ------------------------------------------------------------------
# Stack Implementation with Visualization
# ------------------------------------------------------------------

class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at an empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"

    def copy(self):
        """Create a copy of the stack."""
        new_stack = Stack()
        new_stack._data = self._data.copy()
        return new_stack


# ------------------------------------------------------------------
# Core Algorithm with Step Tracking
# ------------------------------------------------------------------

OPENING = set("([{")
CLOSING = set(")]}")
MATCH = {')': '(', ']': '[', '}': '{'}
PAIR_NAMES = {'(': 'parentheses', '[': 'square brackets', '{': 'curly braces'}


def is_balanced(expression: str, track_steps: bool = False) -> Tuple[bool, str, List[Dict]]:
    """
    Check whether an expression has balanced parentheses, brackets,
    and braces using a stack.

    Returns
    -------
    (True,  "Balanced", steps)           – expression is balanced
    (False, reason_string, steps)       – expression is not balanced
    
    If track_steps is True, returns a list of steps showing the process.
    """
    stack = Stack()
    steps = []
    
    # Initial state
    if track_steps:
        steps.append({
            'index': -1,
            'char': '',
            'action': 'START',
            'stack': stack.copy(),
            'message': 'Initializing empty stack'
        })

    for index, char in enumerate(expression):
        if char in OPENING:
            stack.push((char, index))
            if track_steps:
                steps.append({
                    'index': index,
                    'char': char,
                    'action': 'PUSH',
                    'stack': stack.copy(),
                    'message': f"Pushing opening '{char}' at position {index}"
                })

        elif char in CLOSING:
            if stack.is_empty():
                reason = (
                    f"Unmatched closing '{char}' at position {index} "
                    f"– no corresponding opening symbol."
                )
                if track_steps:
                    steps.append({
                        'index': index,
                        'char': char,
                        'action': 'ERROR',
                        'stack': stack.copy(),
                        'message': reason
                    })
                return False, reason, steps
            
            top_char, top_index = stack.pop()
            if top_char != MATCH[char]:
                reason = (
                    f"Mismatch at position {index}: "
                    f"closing '{char}' does not match opening "
                    f"'{top_char}' at position {top_index}."
                )
                if track_steps:
                    steps.append({
                        'index': index,
                        'char': char,
                        'action': 'MISMATCH',
                        'stack': stack.copy(),
                        'message': reason,
                        'expected': MATCH[char],
                        'got': top_char
                    })
                return False, reason, steps
            
            if track_steps:
                steps.append({
                    'index': index,
                    'char': char,
                    'action': 'POP',
                    'stack': stack.copy(),
                    'message': f"Matching '{char}' at {index} with '{top_char}' at {top_index}"
                })

    if not stack.is_empty():
        unclosed = ", ".join(
            f"'{sym}' at position {pos}" for sym, pos in stack._data
        )
        reason = f"Unclosed opening symbol(s): {unclosed}."
        if track_steps:
            steps.append({
                'index': -1,
                'char': '',
                'action': 'UNCLOSED',
                'stack': stack.copy(),
                'message': reason
            })
        return False, reason, steps

    if track_steps:
        steps.append({
            'index': -1,
            'char': '',
            'action': 'SUCCESS',
            'stack': stack.copy(),
            'message': 'All symbols balanced successfully!'
        })
    
    return True, "Balanced", steps if track_steps else []


# ------------------------------------------------------------------
# Visual Display Helpers
# ------------------------------------------------------------------

def print_box(text: str, width: int = 60, color: str = Colors.CYAN) -> None:
    """Print text inside a box."""
    print(color + "╔" + "═" * (width - 2) + "╗" + Colors.RESET)
    lines = text.split('\n')
    for line in lines:
        print(color + "║" + Colors.RESET + f" {line:<{width-3}}" + color + "║" + Colors.RESET)
    print(color + "╚" + "═" * (width - 2) + "╝" + Colors.RESET)


def print_divider(char: str = "─", length: int = 60, color: str = Colors.DIM) -> None:
    """Print a divider line."""
    print(color + char * length + Colors.RESET)


def print_stack_visual(stack: Stack, highlight_index: int = -1) -> None:
    """Print a visual representation of the stack."""
    if stack.is_empty():
        print(f"  {Colors.DIM}Stack: [ ]{Colors.RESET}  (empty)")
        return
    
    stack_str = "Stack: ["
    items = []
    for i, (char, pos) in enumerate(stack._data):
        if i == len(stack._data) - 1 and i == highlight_index:
            items.append(colorize(f"{char}@{pos}", Colors.BRIGHT_CYAN + Colors.BOLD))
        else:
            items.append(f"{char}@{pos}")
    stack_str += " → ".join(items) + "]"
    print(f"  {stack_str}")


def animate_loading(duration: float = 1.0, message: str = "Processing") -> None:
    """Show an animated loading indicator."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Colors.CYAN}{frames[i % len(frames)]}{Colors.RESET} {message}...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
    sys.stdout.flush()


def print_progress_bar(iteration: int, total: int, prefix: str = '', 
                       suffix: str = '', length: int = 40, 
                       fill: str = '█', color: str = Colors.CYAN) -> None:
    """Print a progress bar."""
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{color}{prefix} |{bar}| {percent}% {suffix}{Colors.RESET}')
    sys.stdout.flush()
    if iteration == total:
        print()


# ------------------------------------------------------------------
# Check and Display with Visualization
# ------------------------------------------------------------------

def check_and_display(expression: str, visualize: bool = True) -> None:
    """Check and display the result with optional visualization."""
    print()
    print_divider(color=Colors.YELLOW)
    print(f"\n  {Colors.BOLD}Expression:{Colors.RESET} {colorize(expression, Colors.WHITE)}")
    
    # Show character positions
    if expression:
        positions = "  Positions:  "
        for i, c in enumerate(expression):
            if c in OPENING or c in CLOSING:
                positions += colorize(f"{c}@{i}", Colors.BRIGHT_CYAN) + " "
        print(positions)
    
    print()
    
    if visualize and expression:
        animate_loading(0.5, "Analyzing")
    
    balanced, message, steps = is_balanced(expression, track_steps=True)
    
    if visualize and steps:
        print(f"\n  {Colors.BOLD}Step-by-Step Analysis:{Colors.RESET}")
        print_divider(color=Colors.DIM)
        
        for i, step in enumerate(steps):
            action = step['action']
            msg = step['message']
            
            if action == 'START':
                print(f"\n  {colorize('▶', Colors.CYAN)} {colorize('START', Colors.BOLD + Colors.CYAN)}: {msg}")
                print_stack_visual(step['stack'])
                
            elif action == 'PUSH':
                char = step['char']
                color_code = Colors.BRIGHT_GREEN
                print(f"\n  {colorize('▶', Colors.BRIGHT_GREEN)} {colorize('PUSH', color_code + Colors.BOLD)}: {msg}")
                print_stack_visual(step['stack'])
                
            elif action == 'POP':
                print(f"\n  {colorize('▶', Colors.BRIGHT_YELLOW)} {colorize('POP', Colors.BRIGHT_YELLOW + Colors.BOLD)}: {msg}")
                print_stack_visual(step['stack'])
                
            elif action == 'ERROR':
                print(f"\n  {colorize('▶', Colors.BRIGHT_RED)} {colorize('ERROR', Colors.BRIGHT_RED + Colors.BOLD)}: {msg}")
                print_stack_visual(step['stack'])
                break
                
            elif action == 'MISMATCH':
                print(f"\n  {colorize('▶', Colors.BRIGHT_RED)} {colorize('MISMATCH', Colors.BRIGHT_RED + Colors.BOLD)}: {msg}")
                print(f"       {colorize('Expected:', Colors.YELLOW)} {step.get('expected', '?')} {colorize('but got:', Colors.YELLOW)} {step.get('got', '?')}")
                print_stack_visual(step['stack'])
                break
                
            elif action == 'UNCLOSED':
                print(f"\n  {colorize('▶', Colors.BRIGHT_RED)} {colorize('UNCLOSED', Colors.BRIGHT_RED + Colors.BOLD)}: {msg}")
                print_stack_visual(step['stack'])
                
            elif action == 'SUCCESS':
                print(f"\n  {colorize('✓', Colors.BRIGHT_GREEN)} {colorize('SUCCESS', Colors.BRIGHT_GREEN + Colors.BOLD)}: {msg}")
                print_stack_visual(step['stack'])
    
    print()
    print_divider(color=Colors.YELLOW)
    
    # Final result
    if balanced:
        print(f"\n  {colorize('✓', Colors.BRIGHT_GREEN)} {colorize('BALANCED', Colors.BRIGHT_GREEN + Colors.BOLD)}")
        print(f"  {Colors.DIM}All parentheses, brackets, and braces are properly matched!{Colors.RESET}")
    else:
        print(f"\n  {colorize('✗', Colors.BRIGHT_RED)} {colorize('NOT BALANCED', Colors.BRIGHT_RED + Colors.BOLD)}")
        print(f"  {colorize('Reason:', Colors.YELLOW)} {message}")
    
    print()


def show_statistics(expressions: List[Tuple[str, bool]]) -> None:
    """Show statistics about checked expressions."""
    total = len(expressions)
    balanced_count = sum(1 for _, b in expressions if b)
    unbalanced_count = total - balanced_count
    
    print_box(f"📊 Statistics\nTotal checked: {total}\nBalanced: {balanced_count}\nUnbalanced: {unbalanced_count}", width=50, color=Colors.MAGENTA)


# ------------------------------------------------------------------
# Interactive Menu
# ------------------------------------------------------------------

def show_menu() -> None:
    """Display the main menu."""
    print(BANNER)
    print(f"\n  {Colors.BOLD}Main Menu:{Colors.RESET}")
    print_divider(color=Colors.CYAN)
    print(f"  {colorize('1.', Colors.BRIGHT_CYAN)}  Check a custom expression")
    print(f"  {colorize('2.', Colors.BRIGHT_CYAN)}  Run built-in test cases")
    print(f"  {colorize('3.', Colors.BRIGHT_CYAN)}  Show check history")
    print(f"  {colorize('4.', Colors.BRIGHT_CYAN)}  Interactive demo")
    print(f"  {colorize('5.', Colors.BRIGHT_CYAN)}  Clear history")
    print(f"  {colorize('Q.', Colors.BRIGHT_RED)}  Quit")
    print_divider(color=Colors.CYAN)


def run_test_cases() -> None:
    """Run built-in test cases with beautiful formatting."""
    test_cases = [
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("({[]})", True),
        ("{[()]}", True),
        ("([{}])", True),
        ("a + (b * c) - [d / {e}]", True),
        ("if (x > 0) { return [x]; }", True),
        ("", True),
        ("(", False),
        (")", False),
        ("({)", False),
        ("({[}])", False),
        ("(((", False),
        (")))", False),
        ("{[}]", False),
    ]

    print(f"\n{Colors.BOLD}╔══════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BOLD}║{Colors.RESET}              🧪 Running Built-in Test Cases              {Colors.BOLD}║{Colors.RESET}")
    print(f"{Colors.BOLD}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}\n")

    passed = 0
    failed = 0
    
    # Test result table header
    print(f"  {Colors.BOLD}{'Test':<35} {'Expected':<15} {'Result':<10}{Colors.RESET}")
    print_divider(color=Colors.DIM, length=65)
    
    for i, (expr, expected) in enumerate(test_cases):
        result, _, _ = is_balanced(expr)
        is_pass = result == expected
        
        if is_pass:
            passed += 1
            icon = colorize("✓", Colors.BRIGHT_GREEN)
            status = colorize("PASS", Colors.BRIGHT_GREEN)
        else:
            failed += 1
            icon = colorize("✗", Colors.BRIGHT_RED)
            status = colorize("FAIL", Colors.BRIGHT_RED)
        
        expected_str = colorize("Balanced", Colors.BRIGHT_GREEN) if expected else colorize("Not Balanced", Colors.BRIGHT_RED)
        result_str = colorize("Balanced", Colors.BRIGHT_GREEN) if result else colorize("Not Balanced", Colors.BRIGHT_RED)
        
        # Show progress bar
        print_progress_bar(i + 1, len(test_cases), prefix="  ", suffix="", length=25)
        
        print(f"  {icon} {expr:<33} {expected_str:<15} {result_str}")
    
    print_divider(color=Colors.DIM, length=65)
    
    # Summary
    total = len(test_cases)
    percentage = (passed / total) * 100
    
    if percentage == 100:
        summary_color = Colors.BRIGHT_GREEN
        summary_icon = "🎉"
    elif percentage >= 75:
        summary_color = Colors.BRIGHT_YELLOW
        summary_icon = "👍"
    else:
        summary_color = Colors.BRIGHT_RED
        summary_icon = "💪"
    
    print(f"\n  {summary_icon} {colorize('Results:', Colors.BOLD)} {passed}/{total} tests passed ({percentage:.1f}%)")
    
    if passed == total:
        print(f"  {colorize('⭐ All tests passed! Great job!', summary_color)}")
    
    print()


def show_history(history: List[Tuple[str, bool]]) -> None:
    """Show the history of checked expressions."""
    if not history:
        print(f"\n  {Colors.DIM}No expressions checked yet.{Colors.RESET}\n")
        return
    
    print(f"\n{Colors.BOLD}📜 Check History:{Colors.RESET}")
    print_divider(color=Colors.MAGENTA)
    
    for i, (expr, balanced) in enumerate(history, 1):
        status = colorize("✓ Balanced", Colors.BRIGHT_GREEN) if balanced else colorize("✗ Not Balanced", Colors.BRIGHT_RED)
        # Truncate long expressions
        display_expr = expr if len(expr) <= 40 else expr[:37] + "..."
        print(f"  {i:2d}. {display_expr:<42} {status}")
    
    print_divider(color=Colors.MAGENTA)
    show_statistics(history)


def interactive_demo() -> None:
    """Run an interactive demonstration with visualization."""
    print(f"\n{Colors.BOLD}🎯 Interactive Demo{Colors.RESET}")
    print(f"{Colors.DIM}Watch how the stack works in real-time!{Colors.RESET}\n")
    
    demo_expressions = [
        "({[]})",
        "({[}])",
        "a + (b * c)",
    ]
    
    for i, expr in enumerate(demo_expressions, 1):
        print(f"\n{Colors.BOLD}Example {i}:{Colors.RESET} {colorize(expr, Colors.WHITE)}")
        print_divider(color=Colors.DIM)
        check_and_display(expr, visualize=True)
        
        if i < len(demo_expressions):
            input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")


def clear_history(history: List) -> None:
    """Clear the check history."""
    history.clear()
    print(f"\n  {colorize('✓', Colors.BRIGHT_GREEN)} History cleared successfully!\n")


# ------------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------------

def main() -> None:
    """Main entry point for the application."""
    history: List[Tuple[str, bool]] = []
    
    while True:
        show_menu()
        choice = input(f"  {Colors.BOLD}Enter your choice:{Colors.RESET} ").strip().upper()

        if choice == '1':
            expr = input("\n  Enter expression to check: ")
            balanced, _, _ = is_balanced(expr)
            check_and_display(expr, visualize=True)
            history.append((expr, balanced))
            
        elif choice == '2':
            run_test_cases()
            
        elif choice == '3':
            show_history(history)
            
        elif choice == '4':
            interactive_demo()
            
        elif choice == '5':
            clear_history(history)
            
        elif choice == 'Q':
            print(f"\n  {colorize('👋 Goodbye!', Colors.BRIGHT_CYAN)}")
            print(f"  {colorize('Thanks for using Balanced Parenthesis Checker!', Colors.DIM)}\n")
            break
            
        else:
            print(f"\n  {colorize('⚠ Invalid choice. Please try again.', Colors.BRIGHT_YELLOW)}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {colorize('👋 Interrupted. Goodbye!', Colors.BRIGHT_CYAN)}\n")
        sys.exit(0)
