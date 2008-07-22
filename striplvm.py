import sys
import pdb

f = file(sys.argv[1],'r')

s = f.read()

lines = s.split('\n')
print lines[0]
data = []

for line in lines:
    d = line.split('\t')
    d.pop(0)
    try:
        
        float(d[0])
        for count in range(len(d)):
            d[count] = float(d[count])
        data.append(d)
            
    except ValueError:
        pass
    
    except IndexError:
        pass

pdb.set_trace()

my_string = ''
for d in data:
    for e in d:
        my_string += str(e) + '\t'
    my_string += '\n'

f2 = file(sys.argv[1]+'.stripped','w')
f2.write(my_string)
f2.close()
    
    
    
