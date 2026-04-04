class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        curr_guess = init
        for i in range(iterations):
            d = 2*curr_guess
            curr_guess = curr_guess-learning_rate*d
        return curr_guess