# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext


# The directory dir contains an empty sub-directory subdir1 and a sub-directory 
# subdir2 containing a file file.ext.

# The string 
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
# represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext


# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 
# contains a file file1.extand an empty second-level sub-directory subsubdir1. 
# subdir2 contains a second-level sub-directorysubsubdir2 containing a file 
# file2.ext.

# We are interested in finding the longest (number of characters) absolute path to
# a file within our file system. For example, in the second example above, the
# longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is
# 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the
# length of the longest absolute path to a file in the abstracted file system. If
# there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.
def lengthLongestPath(s):
        dividedPath = s.split('\n')
        start = dividedPath[0]
        
        if len(start.split('.')) > 1:
            longest = len(start)
        else:
            longest = 0
        startLength = len(start)
        
        def helper(index):
                current = dividedPath[index]
                isFile = len(current.split('.')) == 2
                if isFile:
                        return len(current.split('\t')[-1])
                
                current = current.split('\t')
                current_longest = 0
                current_length = len(current[-1])
                for i in range(index + 1, len(dividedPath)):
                        if len(dividedPath[i].split('\t')) > len(current):
                                result = helper(i)
                                if result:
                                    current_longest = max(current_longest, 1 + current_length + result)
                                
                        
                        else:
                                break
                
                return current_longest
        
        
        for i in range(1, len(dividedPath)):
                current = dividedPath[i].split('\t')
                if len(current) == 2:
                        result = helper(i)
                        if result:
                                longest = max(longest, 1 + startLength + helper(i))
                
                elif len(current) > 2:
                        continue
                
                else:
                        # new directory
                        current = dividedPath[i]
                        startLength = len(current)
                        longest = max(longest, startLength)
                        
        
        return longest         
                

assert lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
assert lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
assert lengthLongestPath("a\n\tb\n\t\tc") == 0
assert lengthLongestPath("a\n\tb.txt\na2\n\tb2.txt") == 9