#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
eve_nums = []
calc = 0
while int(calc) < 15:
    eve_nums.append(calc)
    calc = int(calc) + 2
print(eve_nums)
