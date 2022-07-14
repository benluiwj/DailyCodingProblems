# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that
# contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct
# characters is "bcb".
def longest_substring_with_k_distinct(s, k):
        if k == 0:
                return ""
        
        longest_start = 0
        longest_end = 0
        start = 0
        end = 0
        n = len(s)
        curr = set()
        while end < n:
                curr.add(s[end])

                
                while len(curr) > k:
                        if s[start] in curr:
                                curr.remove(s[start])
                        start += 1
                
                if len(curr) == k and end - start > longest_end - longest_start:
                        longest_start = start
                        longest_end = end
                
                end += 1
        
        return s[longest_start:longest_end+1]

print(longest_substring_with_k_distinct("cababac" , 2))
                