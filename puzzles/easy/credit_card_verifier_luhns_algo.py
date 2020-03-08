""" Verify credit card number using Luhn's algorithm:
1.Double every second digit from right to left. If this “doubling” results in a two-digit number, subtract 9 from it get a single digit.
2.Now add all single digit numbers from step 1.
3.Add all digits in the odd places from right to left in the credit card number.
4.Sum the results from steps 2 & 3.
5.If the result from step 4 is divisible by 10, the card number is valid; otherwise, it is invalid.


"""

n = int(input())
for i in range(n):
    card = [int(x) for x in (input().replace(' ', ''))]
    print('YES' if (sum([x if x < 10 else x - 9 for x in [2*x for x in card[-2::-2]]]) + sum([x for x in card[-1::-2]])) % 10 == 0 else 'NO')