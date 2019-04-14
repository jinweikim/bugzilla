from py2neo import Graph,Node,Relationship

graph = Graph('http://localhost:7474', username='neo4j', password='KING1218')

testnode1 =  Node('BugId',name='1288988')
testnode2 =  Node('Product',name='Thunderbird')
testnode3 =  Node('Reporter',name='Bernie')

#node = Node("Test_Class",name='姚明董事长',id='0001',age=65,location='上海')
#graph.create(node)
# graph.create(testnode1)
# graph.create(testnode2)
# graph.create(testnode3)

relation1 = Relationship(testnode1,'isProduct',testnode2)
relation2 = Relationship(testnode1,'isReporter',testnode3)

s1 = testnode1 | relation1 | testnode2
s2 = testnode1 | relation2 | testnode3

graph.create(s1)
graph.create(s2)

print(graph)


