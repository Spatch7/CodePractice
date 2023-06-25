# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.



def characterReplacement(s, k):
    largest = 0
    left = 0
    count = {}
    maxFreq = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxFreq = max(maxFreq, count[s[right]])

        if (right - left + 1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1

        window = right - left
        largest = max(largest, window + 1)

    return largest












if __name__ == '__main__':
    s = "ABAB"
    k = 2
    print(characterReplacement(s, k))