# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Write a function to flatten a nested dictionary. Namespace the keys with a
# period.

# For example, given the following dictionary:

# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }


# it should become:

# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }


# You can assume keys do not contain dots in them, i.e. no clobbering will occur.
from typing import * 

def flatten(dictionary: dict):
        result = dict()
        frontier = dictionary
        while frontier:
                new_frontier = {}
                for key, val in frontier.items():
                        if isinstance(val, dict):
                                for subkey, value in val.items():
                                        new_frontier[key+"."+subkey] = value
                        else:
                                result[key] = val
                
                frontier = new_frontier
        return result
        
        

directory = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

print(flatten(directory))
        
