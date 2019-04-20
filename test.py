import pandas
import json
import rdflib

# f = pandas.read_csv('id.json');
# f = json.loads('id.json')

# f = open('id.json')
# str = f.read()
# print(str)
# f = str.split(",")
# # print(f[0])
# # print(f[1])
# print(f)
# j = 0
#
# for i in f:
#     print(i.strip().strip('\ufeff').strip('"'));
#     j = j+1
# print(j)

g = rdflib.Graph()
g.parse("graph.rdf")

select = 'select ?id where { ?id ns1:isReporter "dsirnapalli" .}'

querystring = "PREFIX ns1:<http://www.bugzilla.com/>"+ "PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>"+select;


x = g.query(querystring)
t = list(x)

print(len(t))
for i in t:
    print(i)


# print(eval(f[0]));
# print(eval(f[1]));
# print(eval(f[2]));
# print(f[2].strip('"'));
# print(f[3].strip('"'));