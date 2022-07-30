languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)
nom="nicodem"
# convert enumerate object to list
print(list(enumerate_prime))
print(list(enumerate(nom)))
import string
b=string.ascii_lowercase



print(tuple(enumerate(b,1)))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]