# hard-level

def string_compress(s):
    chars = list(s)
    n = len(chars)
    new_index = 0
    i = 0

    while i < n:
        count = 1
        # count consecutive characters
        while i + 1 < n and chars[i] == chars[i + 1]:
            count += 1
            i += 1
        chars[new_index] = chars[i]
        new_index += 1
        if count > 1:
            for c in str(count):  # handle multi-digit counts
                chars[new_index] = c
                new_index += 1
        i += 1

    return "".join(chars[:new_index])

string = input("Enter String for compression: ")
print(string_compress(string))
