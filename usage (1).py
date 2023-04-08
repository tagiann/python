import python_module
import keyword
import primes


a = 5
b = 10
c = python_module.add(a, b)  #custom python module
print(c)

print(keyword.iskeyword("abcc"))  #built-in python module



result = primes.find_primes(1, 100)  #custom cpp module
print(result)
