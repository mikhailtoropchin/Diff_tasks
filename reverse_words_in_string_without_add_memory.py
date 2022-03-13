# Развернуть слова в строке без использования доп. помяти (напр. исп. функции .split())


def reverse(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_words(s: str):
    start = 0 # начало слова
    s = list(s)
    for cur in range(len(s) - 1):
        if s[cur] == " ":
            reverse(s, start, cur - 1)
            start = cur + 1
    reverse(s, start, len(s) - 1)
    return "".join(s)

print(reverse_words("My name is Mikhail"))

