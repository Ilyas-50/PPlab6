def n_lower_chars(string):
    return sum(map(str.islower, string))

def n_upper_chars(string):
    return sum(map(str.isupper, string))

a = "hjJJKKasALdlalsdlfa"
print(n_lower_chars(a), n_upper_chars(a))