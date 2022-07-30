# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic
# idea is to represent repeated successive characters as a single count and
# character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

def encode(s):
        result = ""
        current = ""
        count = 0 
        
        for char in s:
                if char != current and count:
                        to_add = str(count) + current
                        result += to_add
                        count = 0
                        current = ""
                
                current = char
                count += 1
        
        if count:
                to_add = str(count) + current
                result += to_add
        
        return result


"""

Handle case where there can be multiple digits

"""

def decode(s):
        result = ""
        count = 0
        
        for char in s:
                if char.isdigit():
                        count = count * 10 + int(char)
                
                else:
                        result += char * count
                        count = 0
        
        return result

print(encode("AAAABBBCCDAA"))
print(decode("4A3B2C1D2A"))