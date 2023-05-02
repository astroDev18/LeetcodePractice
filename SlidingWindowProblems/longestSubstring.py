def lengthOfLongestSubstring(s: str) -> int:
    # dictionary
    seen = set()
    # left, right values
    left, right, max_length = 0, 0, 0
    # while right is less than len(s)
    while right < len(s):
    # check if char is in set, add to set otherwised
        if s[right] in seen:
            seen.remove(s[left])
            left += 1
        else:
            seen.add(s[right])
            right += 1
            max_length = max(max_length, right - left)

    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
# answer = abc