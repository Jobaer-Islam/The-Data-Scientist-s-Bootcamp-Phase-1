for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    print(i)


continue skips the current iteration and moves to the next one.
It’s essential for filtering. If you are reading through a massive data file, continue lets you quickly skip
over all the bad, missing, or irrelevant data so you can focus only on the items you need to process.
