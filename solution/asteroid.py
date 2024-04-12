from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    result = []
    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while len(stack) > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if len(stack) == 0:
                result.append(asteroid)
            else:
                if stack[-1] == abs(asteroid):
                    stack.pop()
    result += stack
    return result
