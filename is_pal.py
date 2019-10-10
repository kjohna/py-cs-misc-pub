def is_pal(s):
    # helper, takes string and returns True if it is a palandrome
    for i in range(len(s) // 2 + 1):
        j = len(s) - 1 - i
        if i >= j:
            return True
        if not s[i] == s[j]:
            return False

    return False


print(is_pal('abeba'))
print(is_pal('tacocat'))
print(is_pal('a'))
