# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from py2neo import Graph,Node,Relationship
import rdflib
from tools import Bug_name_list,Product_list,Component_list,Reported_time,Modified_time,Assignee_list,Reporter_list,TriageOwner_list,Description_list,g
class BugzillaPipeline(object):


    def __init__(self):
        product_list = []

    def process_item(self, item, spider):
        graph = Graph('http://localhost:7474', username='neo4j', password='KING1218')

        #创建Neo4j中的节点
        # Bug_id = Node('Bug_id', name=item['Bug_id'])
        # Bug_name = Node('Bug_name', name=item['Bug_name'])
        # Product = Node('Product', name=item['Product'])
        # Component = Node('Component', name=item['Component'])
        # Reported = Node('Reported', name=item['Reported'])
        # Modified = Node('Modified', name=item['Modified'])
        # Assignee = Node('Assignee', name=item['Assignee'])
        # Reporter = Node('Reporter', name=item['Reporter'])
        # TriageOwner = Node('TriageOwner', name=item['TriageOwner'])
        # Description = Node('Description', name=item['Description'])


        #g.open('graph.rdf',create = True)

        Bug_id = rdflib.URIRef('http://www.bugzilla.com/'+item['Bug_id'])
        Bug_name = rdflib.URIRef('http://www.bugzilla.com/'+item['Bug_name'])
        Product = rdflib.URIRef('http://www.bugzilla.com/'+item['Product'])
        Component = rdflib.URIRef('http://www.bugzilla.com/'+item['Component'])
        Reported = rdflib.URIRef('http://www.bugzilla.com/'+item['Reported'])
        Modified = rdflib.URIRef('http://www.bugzilla.com/'+item['Modified'])
        Assignee = rdflib.URIRef('http://www.bugzilla.com/'+item['Assignee'])
        Reporter = rdflib.URIRef('http://www.bugzilla.com/'+item['Reporter'])
        TriageOwner = rdflib.URIRef('http://www.bugzilla.com/'+item['TriageOwner'])
        Description = rdflib.URIRef('http://www.bugzilla.com/'+item['Description'])

        Bug_name_list.append(item['Bug_name'].strip())
        Product_list.append(item['Product'].strip())
        Reported_time.append(item['Reported'].strip())
        Modified_time.append(item['Modified'].strip())
        Component_list.append(item['Component'].strip())
        Assignee_list.append(item['Assignee'].strip())
        Reporter_list.append(item['Reporter'].strip())
        TriageOwner_list.append(item['TriageOwner'].strip())
        Description_list.append(item['Description'].strip())

        r1 = rdflib.URIRef('http://www.bugzilla.com/isBugname')
        r2 = rdflib.URIRef('http://www.bugzilla.com/isProduct')
        r3 = rdflib.URIRef('http://www.bugzilla.com/isComponent')
        r4 = rdflib.URIRef('http://www.bugzilla.com/ReportedTime')
        r5 = rdflib.URIRef('http://www.bugzilla.com/ModifiedTime')
        r6 = rdflib.URIRef('http://www.bugzilla.com/isAssignee')
        r7 = rdflib.URIRef('http://www.bugzilla.com/isReporter')
        r8 = rdflib.URIRef('http://www.bugzilla.com/isTriageOwner')
        r9 = rdflib.URIRef('http://www.bugzilla.com/isDescription')

        g.add((Bug_id,r1,Bug_name))
        g.add((Bug_id,r2,Product))
        g.add((Bug_id,r3,Component))
        g.add((Bug_id,r4,Reported))
        g.add((Bug_id,r5,Modified))
        g.add((Bug_id,r6,Assignee))
        g.add((Bug_id,r7,Reporter))
        g.add((Bug_id,r8,TriageOwner))
        g.add((Bug_id,r9,Description))


        #g.close()
        #创建图中的节点与关系
        # graph.create(Bug_id)
        # graph.create(Bug_name)
        # graph.create(Product)
        # graph.create(Component)
        # graph.create(Reported )
        # graph.create(Modified)
        # graph.create(Assignee)
        # graph.create(Reporter)
        # graph.create(TriageOwner)
        # graph.create(Description)
        #
        # relation1 = Relationship(Bug_id, 'isBugName', Bug_name)
        # relation2 = Relationship(Bug_id, 'isProduct', Product)
        # relation3 = Relationship(Bug_id, 'isComponent', Component)
        # relation4 = Relationship(Bug_id, 'ReportedTime', Reported)
        # relation5 = Relationship(Bug_id, 'ModifiedTime', Modified)
        # relation6 = Relationship(Bug_id, 'isAssignee', Assignee)
        # relation7 = Relationship(Bug_id, 'isReporter', Reporter)
        # relation8 = Relationship(Bug_id, 'isTriageOwner', TriageOwner)
        # relation9 = Relationship(Bug_id, 'isDescription', Description)

        # graph.create(relation1)
        # graph.create(relation2)
        # graph.create(relation3)
        # graph.create(relation4)
        # graph.create(relation5)
        # graph.create(relation6)
        # graph.create(relation7)
        # graph.create(relation8)
        # graph.create(relation9)

        #试图合并图中重复节点,未果
        # graph = Graph()
        # tx = graph.begin()
        # tx.merge(Bug_id, "Bug_id", "name")
        # tx.merge(Bug_name, "Bug_name", "name")
        # tx.merge(Product, "Product", "name")
        # tx.merge(Component, "Component", "name")
        # tx.merge(Reported, "Reported", "name")
        # tx.merge(Modified, "Modified", "name")
        # tx.merge(Assignee, "Assignee", "name")
        # tx.merge(Reporter, "Reporter", "name")
        # tx.merge(TriageOwner, "TriageOwner", "name")
        # tx.merge(Description, "Description", "name")
        # tx.commit()

        return item
    def close_spider(self,spider):
        g.serialize('graph.rdf')

        file = open('Bug_name_list', 'w')
        file.write(str(Bug_name_list))
        file.close()

        file=open('product_list','w')
        file.write(str(Product_list))
        file.close()

        file = open('Component_list', 'w')
        file.write(str(Component_list))
        file.close()

        file = open('Reported_time', 'w')
        file.write(str(Reported_time))
        file.close()

        file = open('Modified_time', 'w')
        file.write(str(Modified_time))
        file.close()

        file = open('Assignee_list', 'w')
        file.write(str(Assignee_list))
        file.close()

        file = open('Reporter_list', 'w')
        file.write(str(Reporter_list))
        file.close()

        file = open('TriageOwner_list', 'w')
        file.write(str(TriageOwner_list))
        file.close()

        file = open('Description_list', 'w')
        file.write(str(Description_list))
        file.close()

