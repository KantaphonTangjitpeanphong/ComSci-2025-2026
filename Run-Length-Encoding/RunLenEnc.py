uncompressed = input("input phrase to compress:")
letters = [[],
           []]
if len(uncompressed) > 0:
    current_char = uncompressed[0]
    count = 1

    for i in range(1, len(uncompressed)):
        if uncompressed[i] == current_char:
            count += 1
        else:
            letters[0].append(current_char)
            letters[1].append(count)
            current_char = uncompressed[i]
            count = 1
    # Append the last run
    letters[0].append(current_char)
    letters[1].append(count)

print(uncompressed)
print(letters)
