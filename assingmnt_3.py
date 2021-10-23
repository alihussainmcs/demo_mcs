# 1
import collections
string = 'karnataka'
results = collections.Counter(string)
print(results)

# 2
for i in string:

    print("%s" % i, string.count(i))
