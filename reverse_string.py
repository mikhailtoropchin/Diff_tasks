def reverse_string(s: list) -> None:
    print(f"{s} - input")
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(f"{s} - result")


reverse_string(['d', 's', 'f'])