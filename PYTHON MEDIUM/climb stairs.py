def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Use dynamic programming to calculate the number of ways
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Test cases
def test():
    test_cases = [2, 3, 4, 1, 5]
    for n in test_cases:
        print(f"Input: n = {n}\nOutput: {climb_stairs(n)}\n")

# Get input from the user
def main():
    n = int(input("Enter the number of steps: "))
    print(f"Number of distinct ways to climb to the top: {climb_stairs(n)}")

# Uncomment the next line to run the program
# main()

test()
