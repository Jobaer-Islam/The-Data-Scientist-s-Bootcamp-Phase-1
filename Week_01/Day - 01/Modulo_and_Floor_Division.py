total_seconds = 130

# // (Floor Division) finds how many WHOLE minutes are in 130
minutes = total_seconds // 60 

# % (Modulo) finds the REMAINDER (the leftover seconds)
seconds = total_seconds % 60

print(f"Time: {minutes} minutes and {seconds} seconds") # 2 minutes and 10 seconds

Why it works: Floor division discards the fraction to give you a solid count,
while modulo gives you whatever couldn't fit into a whole group.
