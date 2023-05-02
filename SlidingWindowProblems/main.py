def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    max_length = 0
    i = 0
    j = 0
    while (j < len(s)):
        if s[j] not in char_set:
            char_set.add(s[j])
            j += 1
            max_length = max(max_length, j - i)
        else:
            char_set.remove(s[i])
            i += 1
    return max_length
print(lengthOfLongestSubstring("abcabcbb"))
