# Valid Parentheses (Stack Algorithm)
#
# This program determines whether a string of parentheses is valid.
# A string is considered valid if:
# 1. Every closing bracket matches the most recent opening bracket.
# 2. Brackets are closed in the correct order.
# 3. No opening brackets remain unmatched at the end.
#
# The algorithm uses a stack to track opening brackets that still need
# to be matched. When an opening bracket is encountered, it is pushed
# onto the stack. When a closing bracket is encountered, the most recent
# opening bracket is popped from the stack and checked for a match.
#
# Two important validity checks:
# • If a closing bracket appears when the stack is empty, there is no
#   opening bracket available to match it → invalid.
# • If the stack is not empty after processing the entire string,
#   there are unmatched opening brackets → invalid.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        # If we encounter an opening bracket, push it onto the stack.
        # The stack represents opening brackets that still need to be matched.
        if char in ('(', '{', '['):
            stack.append(char)
            continue

        # If we encounter a closing bracket, we must check if it correctly
        # matches the most recent opening bracket.
        if char in (')', '}', ']'):

            # First check if the stack is empty.
            # If it is empty, this means we encountered a closing bracket
            # before seeing a matching opening bracket.
            # Example: "]" or "())"
            if stack:

                # Pop the most recent opening bracket from the stack.
                # This should match the current closing bracket.
                # If it does not match, the parentheses are invalid.
                if pairs[char] != stack.pop():
                    return False
            else:
                # Stack is empty but we found a closing bracket.
                # This means there was nothing to match it with.
                return False

    # After processing the entire string, the stack should be empty.
    # If it is not empty, it means there were opening brackets that
    # were never closed.
    # Example: "(" or "[("
    if stack:
        return False
    
    return True


s = "[]"
print(is_valid(s), '\n')

s = "{"
print(is_valid(s), '\n')

s = "]"
print(is_valid(s), '\n')

s = "()}"
print(is_valid(s), '\n')

s = "[{()}]"
print(is_valid(s), '\n')
