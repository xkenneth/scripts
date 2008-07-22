import math

DELIM = '\t'

t = []
columns = ['depth','gammaray','inclination','azimuth','resistivity']
for i in range (100):
    s = []
    s.append(-1.0*float(i)*7.5)
    for j in range(4):
        s.append(math.sin((float(j+1)/10.0*math.pi*float(i))))
    t.append(s)

f = file('log.xls','w')
my_string = ''

for c in columns:
    my_string += c + DELIM
my_string += '\n'
    
for i in t:
    line = ''
    for j in i:
        line += str(j) + DELIM
    line += '\n'
    my_string += line
    
f.write(my_string)
f.close()
