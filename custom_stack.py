def is_valid_parentheses(s: str) -> bool:
    # 1. Map open characters to their respective closing characters
    bracket_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    stack = []
    
    # 2. Loop through each character in the target string
    for char in s:
        if char in bracket_map:
            # If it's an opening bracket, push its expected closing bracket onto the stack
            stack.append(bracket_map[char])
        else:
            # If it's a closing bracket, check for matching pairs
            if not stack or stack.pop() != char:
                return False
                
    # 3. If the stack is empty, all braces were matched perfectly
    return len(stack) == 0
