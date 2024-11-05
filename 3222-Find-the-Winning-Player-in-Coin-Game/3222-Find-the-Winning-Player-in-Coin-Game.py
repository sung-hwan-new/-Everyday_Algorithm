class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        needed_75 = 1
        needed_10 = 4
        turns = min(x // needed_75, y // needed_10)
        if turns % 2 == 0:
            return "Bob"
        else:
            return "Alice"