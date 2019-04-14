import pandas
import json
# f = pandas.read_csv('id.json');
# f = json.loads('id.json')
f = open('id.json')
str = f.read()
print(str)
f = str.split(",")
# print(f[0])
# print(f[1])
print(f)
j = 0

for i in f:
    print(i.strip().strip('\ufeff').strip('"'));
    j = j+1
print(j)



# print(eval(f[0]));
# print(eval(f[1]));
# print(eval(f[2]));
# print(f[2].strip('"'));
# print(f[3].strip('"'));