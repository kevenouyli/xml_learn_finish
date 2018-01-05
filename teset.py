import numpy as npET
from xml.etree import ElementTree
# a=[[100,10],[2,14],[52,56],[4,72],[5,27],[6,32]]
# b=np.array(a)
# def get_max(a):
# 	b=[]
# 	for i in a:
# 		b.append(i[1])
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

tree = ElementTree.parse('test.xml')  # 加载指定文件
root = tree.getroot()  # 获得根节点
sub1=root.getchildren()[0]

# 创建节点
Placemark = ElementTree.Element('Placemark')  # Element(tag, attrib={}, **extra)
name = ElementTree.SubElement(Placemark, 'name')  # SubElement(parent, tag, attrib={}, **extra)
Style = ElementTree.SubElement(Placemark, 'Style')
LineStyle = ElementTree.SubElement(Style, 'LineStyle')
color = ElementTree.SubElement(LineStyle, 'color')
color.text='7fffff80'
width = ElementTree.SubElement(LineStyle, 'width')
width.text='4'
IconStyle = ElementTree.SubElement(Style, 'IconStyle')
Icon= ElementTree.SubElement(IconStyle, 'Icon')
MultiGeometry = ElementTree.SubElement(Placemark, 'MultiGeometry')
Point = ElementTree.SubElement(MultiGeometry, 'Point')
coordinates = ElementTree.SubElement(Point, 'coordinates')
coordinates.text='112.32037530,23.25538530,0'
LineString= ElementTree.SubElement(MultiGeometry, 'LineString')
coordinates = ElementTree.SubElement(LineString, 'coordinates')
coordinates.text='112.32037530,23.25538530,0 112.32037530,23.25538530,0 112.31950730,23.25570050,0'

root.append(Placemark)

# write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml")
tree.write('updated.xml', encoding='utf-8')
