with open('sentences.txt','r') as f:
    lines = f.readlines()

ff = open('words.txt','w')

for line in lines:
    line = line.strip()
    line = line.split(' ')
    for a in line:
        ff.write(a)
        ff.write(' ')
f.close()
ff.close()
