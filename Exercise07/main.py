from typing import Any, Tuple, List


def parentheses(n: int) -> List[str]:
    """This function gets an integer and returns all possible brackets sequences in a list,
    only if they are a valid mathematical expression. for example: 2 -> [()(), (())]
    it helped by parentheses_helper function"""
    lst: List[str] = []
    parentheses_helper(n, 0, 0, "", lst)
    return lst


def check_balance_of_brackets(collector: str) -> bool:
    """This function gets a string which contains a certain number of brackets
    it returns True if it is a valid mathematical expression, false otherwise"""
    opener = ['(']
    closer = [')']
    stack = []
    for char in collector:
        if char in opener:
            stack.append(char)
        elif char in closer:
            pos = closer.index(char)
            if len(stack) > 0 and stack[-1] == opener[pos]:
                stack.pop()
            else:
                return False
    return True if not stack else False


def parentheses_helper(n: int, n_open: int, n_close: int, collector: str, lst: List[str]) -> None:
    """This function help parentheses function above.
    it helped by check_balance_of_brackets this way:
    parentheses_helper send every possible brackets expression.
    if it is a valid mathematical expression, the function will append it to the list (lst)"""
    if n_open == n and n_close == n:
        if check_balance_of_brackets(collector):
            lst.append(collector)
            return
    if n_open < n:
        parentheses_helper(n, n_open + 1, n_close, collector + "(", lst)
    if n_close < n:
        parentheses_helper(n, n_open, n_close + 1, collector + ")", lst)


if __name__ == '__main__':
    print(parentheses(13))