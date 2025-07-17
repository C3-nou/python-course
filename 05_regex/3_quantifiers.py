import re

# * -> cero o más ocurrencias

text = "aaaabbba"
pattern = "a*"
result = re.findall(pattern, text)
print(result)

# + -> una o más ocurrencias

text = "aaaab"
pattern = "a+"
result = re.findall(pattern, text)
print(result)

# ? -> cero o una ocurrencia

text = "aaaab"
pattern = "a?"
result = re.findall(pattern, text)
print(result)

# {n} -> exactamente n ocurrencias

text = "aaaab"
pattern = "a{2}"
result = re.findall(pattern, text)
print(result)