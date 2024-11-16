# import nltk
from os import getcwd
import pandas as pd
# from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import numpy as np

# A = np.array([[2,2],  [2,2]])
# print(A.shape)

# A_squared = np.square(A)
# print(A_squared)

# A_Frobenious = np.sqrt(np.sum(A_squared))
# print(A_Frobenious)
#create a hash table with 5 buckets
n_buckets = 5
hash_table = {i:[] for i in range(n_buckets)}
print('hash_table: ',hash_table)
# define a simple hash function that takes an integer key and returns a bucket index
def hash_func(key):
    return key % n_buckets

# insert some items into the hash table
hash_table[hash_func(4)].append("apple")
hash_table[hash_func(7)].append("banana")
hash_table[hash_func(2)].append("orange")
hash_table[hash_func(1)].append("grape")

# retrieve an item from the hash table
bucket_index = hash_func(2)
if "orange" in hash_table[bucket_index]:
    print("Found 'orange' in bucket", bucket_index)
else:
    print("Did not find 'orange' in bucket", bucket_index)

print(hash_table)

p =  np.array([1,1])
v1 = np.array([1,1])
v2 = np.array([2,2])
v3 = np.array([-1,-1])

print(np.dot(p,v1.T))
print(np.dot(p,v2.T))
print(np.dot(p,v3.T))

def side_of_plane(p,v):
    dotproduct = np.dot(p,v.T)
    sign_of_dot_product = np.sign(dotproduct)
    sign_of_dot_product_scalar= np.asscalar(sign_of_dot_product)
    print('sign: ', sign_of_dot_product)
    print('sing_scaler: ', sign_of_dot_product_scalar)
    return sign_of_dot_product_scalar

for i in [v1,v2,v3]:
    side_of_plane(p, i)