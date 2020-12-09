def int_func():
    for word in input("Enter words with a space(lower latin script):\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - only small English letters!")


int_func()