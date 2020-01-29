# Okay, remember, a hash table has two parts:
#  {
#   array: [None, None, None],
#   hashFunction: ()
# }

# Our hash table needs to return an index in the array

# Let's make some toy functions!

length_of_array = 8

def myHash1(key):
  # modulo shit is a trick to stay within the bounds
  # of the array
  return len(key) % length_of_array

# Given dog, this returns the hash 3

# Pro:
# - deterministic
# - non-invertible, one-way function (if you know it gave back 3, do you know what key that belongs to?)

# Con:
# - output not unique! dog, dad, Tim

# We want the hash function to make hashes that are deterministic
# but LOOK random!

# Okay let's make it better
import time
def myHash2(key):
  output_index = len(key) + time.time()
  
  return output_index % length_of_array
# Pro:
# - non-invertible
# - pretty unique!

# Con:
# - not deterministic!! The time will always be different! acck!
# 
# print(myHash2('bob'))

def myHash3(key, salt):
  output_index = (len(key) * salt) % length_of_array

  return output_index % length_of_array
# Pro:
# - deterministic
# - non-invertible
# - pretty unique!

# Con:
# - Gotta store the salt somewhere for this to be deterministic

salty = 5241

# this shit not coming out that unique
# dog, dad, Tim
# need to check how it was done in lecture
print(myHash3('dog', salty))
print(myHash3('bob', salty))
print(myHash3('tim', salty))

# Okay, I also typed out djb2 during class, but it's a stretch goal!
# So I have removed it. However it's quite simple
# Rememer to use ord(char) inside your for-loop when you add the sale

# djb2 is actually used, also check out:
# - sha256
# - bcrypt