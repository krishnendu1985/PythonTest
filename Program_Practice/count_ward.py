#!/usr/bin/python
# from collections import Counter
# words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']
# print(Counter(words))



words = ['apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear','apple', 'apple', 'banana', 'banana', 'banana', 'pear', 'banana', 'pear', 'pear', 'pear', 'pear', 'pear']

d={x:words.count(x) for x in words}
print(d)