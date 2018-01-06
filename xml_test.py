# -*- coding:GBK -*-
import xml.etree.ElementTree as ET
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from  collections import namedtuple
import xml.dom.minidom as xdm


#####################################       寻找变电站下的文件夹标签
def tag_get(tag):
	global tag_target
	next_name=tag.getchildren()[0]
	next_folder = tag.getchildren()[1]
	print(next_name.text)
	bdz=bdz_re.match(next_name.text)
	if bdz :
		# tag_target=next_folder.getchildren()[1]
		tag_target=tag
		return
	else:
		tag_get(next_folder)



######################################		求两点距离
def get_dist_max(point1,point2):     #		求最大距离
	dist =float(np.square(point1.jd -point2.jd) + np.square(point1.wd- point2.wd))
	return dist
def get_dist_min(point1,point2):     #		求最小距离
	dist = np.square(point1.jd -point2.jd) + np.square(point1.wd- point2.wd)
	if dist==0:
		return 100
	else:
		return dist



######################################       对线路各点排序
def order_list(maxdist_p,line_f):
	list1_order=[]
	line_tmp=line_f[:]
	list1_order.append(maxdist_p[1])
	
	for i in range(len(line_tmp)):
		if len(list1_order)==len(line_tmp):
			break
		else:
			# print(list1_order)
			# print('first::line_tmp:', line_tmp)
			mindist_p=get_mindist(list1_order[i],line_tmp)
			# print(mindist_p)
			while mindist_p in list1_order:
			# if mindist_p in list1_order:
				line_tmp[mindist_p]=line_tmp[mindist_p]._replace(jd=float(10000),wd=float(0))
				# print('line_tmp:',line_tmp)
				mindist_p = get_mindist(list1_order[i], line_tmp)
				# print(mindist_p)
				# list1_order.append(mindist_p)
			# else:
			list1_order.append(mindist_p)
			line_tmp = line_f[:]
	return list1_order




######################################      求最大距离点的位置
def get_maxdist(list_vec_f,line):
	list=[]
	for i in list_vec_f:
		# print(line[i.max_p],line[i.root_p])
		list.append(get_dist_max(line[i.max_p],line[i.root_p]))
	# print(list)
	np_list = np.array(list)
	max_p = np.where(np_list == np.max(np_list))[0][0]
	# print(line[max_p],line[list_vec[max_p].root_p])
	# max_dist=get_dist_max(line[max_p],line[list_vec[max_p].max_p])
	# print(max_dist)
	max_p2=list_vec_f[max_p].max_p
	return [max_p,max_p2]


######################################      求点的最小距离的位置
def get_mindist(poi,line_f):
	list_min=[]                       ##存放某点与其它点的最小距离
	for i in range(len(line_f)):
		list_min.append(get_dist_min(line_f[poi],line_f[i]))
	np_list2=np.array(list_min)
	min_p = np.where(np_list2 == np.min(np_list2))[0][0]  #求最小值位置
	return min_p



######################################      求最某点最大距离的位置
def get_pointplc(poi,line_f):
	list_max=[]                       ##存放某点与其它点的最大距离
	for i in range(len(line_f)):
		list_max.append(get_dist_max(line_f[poi],line_f[i]))
	np_list1=np.array(list_max)
	max_p = np.where(np_list1==np.max(np_list1))   #求最大值位置
	return max_p[0][0]



######################################      按order画出图
def draw(list,line_f):
	jd_list1=[]
	wd_list1=[]
	for i in list:
		# print(i)
		jd_list1.append(line_f[i].jd)
		wd_list1.append(line_f[i].wd)
	plt.figure(2)
	# print(jd_list1)
	# print(wd_list1)
	plt.plot(jd_list1,wd_list1)


######################################      按list_order整理好line,返回字符串数组
def orderlist_line(order,line_f):
	line_use=line_f[:]
	line_result=[]
	for i in order:
		line_result.append(str(line_use[i].jd)+','+str(line_use[i].wd)+','+'0')
	return  line_result


	
def get_jwd(tag_target_f):
	jd_list = []  # 存放经度
	wd_list = []  # 存放纬度
	line = []  # 存放各点经纬度
	place = []
	Point = namedtuple('point', ['id', 'jd', 'wd'])  # 定义点（经度，纬度）
	point_mesg = namedtuple('vec', ['root_p', 'max_p'])  # 定义存放点（原点，最大值）
	fen = re.compile(',')
	for i in tag_target_f.iter("coordinates"):
		place.append(i.text)
	for i in place:  # 存放经纬度
		total = fen.split(i)
		line.append(Point(id=place.index(i), jd=float(total[0]), wd=float(total[1])))
		
	list_vec = []  # 存放各点的最大、最小距离
	for i in range(len(line)):
		list_vec.append(point_mesg(root_p=i, max_p=get_pointplc(i, line)))
	
	max_dist_point = get_maxdist(list_vec,line)
	print(max_dist_point)
	print(line)
	list_r_order = order_list(max_dist_point, line)
	right_list = orderlist_line(list_r_order, line)
	str_right_list = ' '.join(right_list)
	
	return [str_right_list,right_list]
	
	
	
# for i in tag_target.iter("coordinates"):
# 	place.append(i.text)


# Point=namedtuple('point',['id','jd','wd']) # 定义点（经度，纬度）
# point_mesg=namedtuple('vec',['root_p','max_p'])   #定义存放点（原点，最大值）
# jd_list = []  # 存放经度
# wd_list = []  # 存放纬度
# line = []   #存放各点经纬度
# place=[]
# fen = re.compile(',')
# for i in place:     #存放经纬度
# 	total = fen.split(i)
# 	line.append(Point(id=place.index(i),jd=float(total[0]),wd=float(total[1])))
# 	jd_list.append(float(total[0]))
# 	wd_list.append(float(total[1]))
#
# # for i in range(len(line)):  ##画出各点
# # 	plt.figure(1)
# # 	plt.plot(line[i].jd,line[i].wd, 'bs')
#
# list_vec=[]   #存放各点的最大、最小距离
#
# for i in range(len(line)):
# 	list_vec.append(point_mesg(root_p=i,max_p=get_pointplc(i,line)))
#
# print(list_vec)
# max_dist_point=get_maxdist(list_vec)
# print(max_dist_point)
# print(line)
# list_r_order=order_list(max_dist_point,line)
# # plt.figure(3)
# # plt.plot(jd_list,wd_list)    ##画出各点连线
# # draw(list_r_order,line)
# print(list_r_order)
# right_list=orderlist_line(list_r_order,line)
# print(right_list)
# str_right_list=' '.join(right_list)
# print (str_right_list)
# plt.show()

########################################################################################################    加入xml节点
#  1、使用etree 添加xml
def xml_write(tag_target_f,right_list,str_right_list):
	Placemark1 = ET.Element('Placemark')  # Element(tag, attrib={}, **extra)
	name1 = ET.SubElement(Placemark1, 'name')  # SubElement(parent, tag, attrib={}, **extra)
	name1.text = tag_target_f.getchildren()[0].text
	Style1 = ET.SubElement(Placemark1, 'Style')
	LineStyle1 = ET.SubElement(Style1, 'LineStyle')
	color1 = ET.SubElement(LineStyle1, 'color')
	color1.text = '7f400040'
	width1 = ET.SubElement(LineStyle1, 'width')
	width1.text = '8'
	IconStyle1 = ET.SubElement(Style1, 'IconStyle')
	Icon1 = ET.SubElement(IconStyle1, 'Icon')
	MultiGeometry1 = ET.SubElement(Placemark1, 'MultiGeometry')
	Point1 = ET.SubElement(MultiGeometry1, 'Point')
	coordinates1 = ET.SubElement(Point1, 'coordinates')
	coordinates1.text = right_list[0]
	LineString1 = ET.SubElement(MultiGeometry1, 'LineString')
	coordinates1 = ET.SubElement(LineString1, 'coordinates')
	coordinates1.text = str_right_list
	# tag_target_f.append(Placemark1)
	# tree.write('2017_updated.xml', encoding='utf-8')
	return  Placemark1
	
# Placemark1 = ET.Element('Placemark')  # Element(tag, attrib={}, **extra)
# name1 = ET.SubElement(Placemark1,'name')  # SubElement(parent, tag, attrib={}, **extra)
# name1.text = tag_target.getchildren()[0].text
# Style1 = ET.SubElement(Placemark1,'Style')
# LineStyle1 = ET.SubElement(Style1,'LineStyle')
# color1 = ET.SubElement(LineStyle1,'color')
# color1.text = '7fffff80'
# width1 = ET.SubElement(LineStyle1,'width')
# width1.text = '4'
# IconStyle1 = ET.SubElement(Style1,'IconStyle')
# Icon1 = ET.SubElement(IconStyle1,'Icon')
# MultiGeometry1 = ET.SubElement(Placemark1,'MultiGeometry')
# Point1 = ET.SubElement(MultiGeometry1,'Point')
# coordinates1 = ET.SubElement(Point1,'coordinates')
# coordinates1.text=right_list[0]
# LineString1 = ET.SubElement(MultiGeometry1,'LineString')
# coordinates1 = ET.SubElement(LineString1,'coordinates')
# coordinates1.text = str_right_list
#
# tag_target.append(Placemark1)
#
# # write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml")
# tree.write('2017_updated.xml', encoding='utf-8')
# # print(order_list(line))


#   2、采用dom进行解析
# domtree = xdm.parse("2017.xml")
# root = domtree.documentElement
# tag1=root.childNodes
# tag2=tag1[1].getElementsByTagName('Folder')
# tar_tag=tag2[3].childNodes[1]
# print(tar_tag.childNodes[0].nodeValue)
# def dom_tag_get(tag):
# 	global dom_tag_target
# 	next_name=tag.getchildren()[0]
# 	next_folder = tag.getchildren()[1]
# 	print(next_name.text)
# 	bdz=bdz_re.match(next_name.text)
# 	if bdz :
# 		tag_target=next_folder.getchildren()[1]
# 		return
# 	else:
# 		tag_get(next_folder)
#
#

######################################                        主程序

tag_target=None                     #######        解析xml
tree= ET.parse('2017.xml')
root = tree.getroot()
tag1 = root.getchildren()[0]    #get document
tag2 = tag1.getchildren()[1]  #get  first_folder
tag3 = tag2.getchildren()[1:]

# bdz_re=re.compile(r".*站\b")
# tag_get(tag2)
# bdz_line_tag=tag_target.getchildren()[1:]
# print(bdz_line_tag)
for bdz_tag in tag3:
	bdz_line_tag=bdz_tag.getchildren()[1:]
	for line_tag in bdz_line_tag:
		line_tag_list = line_tag.getchildren()[1:]
		for base_line in line_tag_list:
			result_list = get_jwd(base_line)
			place_mark = xml_write(base_line, result_list[1], result_list[0])
			base_line.append(place_mark)


# for line_tag in bdz_line_tag:
# 	line_tag_list=line_tag.getchildren()[1:]
# 	for base_line in line_tag_list:
# 		result_list=get_jwd(base_line)
# 		place_mark=xml_write(base_line,result_list[1],result_list[0])
# 		base_line.append(place_mark)
tree.write('2017_updated.xml', encoding='utf-8')







	


	


