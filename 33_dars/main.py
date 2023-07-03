with open('pi.txt') as file:
    pi = file.read()

pi = pi.rstrip()
pi = pi.replace('/n', '')
pi = pi.replace(' ', '')
bdate = '26092007'
#print(bdate in pi)

pi = float(pi)
print(pi)
