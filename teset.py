# -*- coding:GBK -*-
import xml.etree.ElementTree as ET
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from  collections import namedtuple
import numpy as npET
from xml.etree import ElementTree
# a=[[100,10],[2,14],[52,56],[4,72],[5,27],[6,32]]
# b=np.array(a)
# def get_max(a):
# 	b=[]
# 	for i in a:
# 		b.append(i[1])
tree= ET.parse('2017.xml')
root = tree.getroot()
tag1 = root.getchildren()[0]    #get document
tag2 = tag1.getchildren()[1]
tag3 = tag2.getchildren()
print(len(tag3))
# 	return	max(b)
# d=get_max(a)
#
# g=np.where(b==d)
# # print(g[0][0])
# a=9
# while a<20:
# 	a+=1
#
# print(a)
#
# tree = ElementTree.parse('test.xml')  # ����ָ���ļ�
# root = tree.getroot()  # ��ø��ڵ�
# sub1=root.getchildren()[0]
#
# # �����ڵ�
# Placemark = ElementTree.Element('Placemark')  # Element(tag, attrib={}, **extra)
# name = ElementTree.SubElement(Placemark, 'name')  # SubElement(parent, tag, attrib={}, **extra)
# Style = ElementTree.SubElement(Placemark, 'Style')
# LineStyle = ElementTree.SubElement(Style, 'LineStyle')
# color = ElementTree.SubElement(LineStyle, 'color')
# color.text='7fffff80'
# width = ElementTree.SubElement(LineStyle, 'width')
# width.text='4'
# IconStyle = ElementTree.SubElement(Style, 'IconStyle')
# Icon= ElementTree.SubElement(IconStyle, 'Icon')
# MultiGeometry = ElementTree.SubElement(Placemark, 'MultiGeometry')
# Point = ElementTree.SubElement(MultiGeometry, 'Point')
# coordinates = ElementTree.SubElement(Point, 'coordinates')
# coordinates.text='112.32037530,23.25538530,0'
# LineString= ElementTree.SubElement(MultiGeometry, 'LineString')
# coordinates = ElementTree.SubElement(LineString, 'coordinates')
# coordinates.text='112.32037530,23.25538530,0 112.32037530,23.25538530,0 112.31950730,23.25570050,0'
#
# root.append(Placemark)

# write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml")
# tree.write('updated.xml', encoding='utf-8')






# import xml.dom.minidom as xdm
# domtree = xdm.parse("2017.xml")
# root = domtree.documentElement
# tag1=root.childNodes
# tag2=tag1[1].getElementsByTagName('Folder')
# tar_tag=tag2[3].childNodes[1]
# print(tar_tag.childNodes[0].nodeValue)
# tag2=tag1.childNodes[1]
# tag3=tag2.childNodes[1]
# print(tag3.childNodes[0].nodeValue)

# print(tag2.childNodes[0].nodeValue)
# impl = xml.dom.minidom.getDOMImplementation()
# # ���ø����emps
# dom = impl.createDocument(None, 'emps', None)
# root = dom.documentElement
# Placemark = dom.createElement('Placemark ')
#
# # ��������
# employee.setAttribute("empno", "1111")
# root.appendChild(employee)
#
# # �����ӽ��
# # ename
# nameE = dom.createElement('ename')
# nameT = dom.createTextNode('�ܿ�')
# nameE.appendChild(nameT)
# # �ӽڵ��������
# nameE.setAttribute("lastname", "ke")
#
# employee.appendChild(nameE)
# # age
# nameE = dom.createElement('age')
# nameT = dom.createTextNode('33')
# nameE.appendChild(nameT)
#
# employee.appendChild(nameE)
#
# f = open('emplist.xml', 'w')  # w�滻Ϊa��׷��
# dom.writexml(f, addindent=' ', newl='\n')
# f.close()