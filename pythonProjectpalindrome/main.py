def palindrome_check(word):
    letter_check = len(word) / 2
    x = 0
    y = -1
    while True:
        if word[x] == word[y]:
            x = x + 1
            y = y - 1
            if x > letter_check:
                return True
        else:
            return False


def get_word():
    while True:
        try:
            x = input("Please enter a word to test: ").strip()
            assert x != ""
            return x.lower()
        except AssertionError:
            print("Invalid entry")


guess_count = 0
done = False
failed = True
print("You will have three tries to guess a palindrome!")
while not done and guess_count < 3:
    word = get_word()
    if palindrome_check(word):
        print("Yes,that is a palindrome. You win")
        done = True
        failed = False
    else:
        print("Incorrect. Not a palindrome")
        guess_count += 1
if failed:
    print("Sorry you lose.")




