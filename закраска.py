"""Алгоритмы закраски
С построчным сканированием
со списком реберных точек, 
со списком активных ребер
С затравкой
С прстрочной затравкой"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
def str_scan(coords,image,new_color):
    n=len(coords)
    Y=[coords[i][1] for i in range (n)]
    y_min, y_max = 0, image.height - 1
    y_min=min(y_min,min(Y))
    y_max=max(y_max,max(Y))
    for y in range(y_min, y_max+1):
        intersections = []
        for i in range(n):
            p1 = coords[i]
            p2 = coords[(i+1) % n]
            if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
                intersections.append(p1[0] + (y - p1[1]) / (p2[1] - p1[1]) * (p2[0] - p1[0]))
        
        intersections.sort()
        for i in range(0, len(intersections), 2):
            for x in range(int(intersections[i]), int(intersections[i+1])+1):
                image.putpixel((x,y),new_color)



def edge_point(coords,image,new_color):
    edges=[]
    for i in range(len(coords)-1):
        if coords[i][1]<=coords[i+1][1]:
            edges.append([(coords[i][0],coords[i][1]),(coords[i+1][0],coords[i+1][1])]) 
        else:
            edges.append([(coords[i+1][0],coords[i+1][1]),(coords[i][0],coords[i][1])])
    if coords[0][1]<=coords[-1][1]:
        edges.append([(coords[0][0],coords[0][1]),(coords[-1][0],coords[-1][1])]) 
    else:
        edges.append([(coords[-1][0],coords[-1][1]),(coords[0][0],coords[0][1])])
    edges.append([(coords[-1][0],coords[-1][1]),(coords[0][0],coords[0][1])])
    coords.sort(key=lambda coords:coords[1])
    pixel_lists={}
    for edge in edges:
        x1, y1 = edge[0]
        x2, y2 = edge[1]
        y = round(y1)
        dx = (x2 - x1) / (y2 - y1)
        x = x1 + dx * (y - y1)
   
        while y<=y2:
            if y not in pixel_lists.keys():
                pixel_lists[y] = []
            pixel_lists[y].append(x)
            y+=1    
            x+=dx
    for y in pixel_lists:
        pixel_lists[y].sort()
    for y in range(min(pixel_lists.keys()), max(pixel_lists.keys()) + 1):
        if y in pixel_lists:
            draw.line(((pixel_lists[y][0],y),(pixel_lists[y][-1],y)),new_color)


def active_edge(coords,image,new_color):
    edges=[]
    for i in range(len(coords)-1):
        if coords[i][1]<=coords[i+1][1]:
            edges.append([(coords[i][0],coords[i][1]),(coords[i+1][0],coords[i+1][1])]) 
        else:
            edges.append([(coords[i+1][0],coords[i+1][1]),(coords[i][0],coords[i][1])])
    if coords[0][1]<=coords[-1][1]:
        edges.append([(coords[0][0],coords[0][1]),(coords[-1][0],coords[-1][1])]) 
    else:
        edges.append([(coords[-1][0],coords[-1][1]),(coords[0][0],coords[0][1])])
    edges.append([(coords[-1][0],coords[-1][1]),(coords[0][0],coords[0][1])])
    y_list=[]
    for edge in edges:
        x1, y1 = edge[0]
        x2, y2 = edge[1]
        y = round(y1)
        dx = (x2 - x1) / (y2 - y1)
        x = x1 + dx * (y - y1)
        y_list.append({'y':y,'y2':y2,'dx':dx,'x':x})
    y_list.sort(key=lambda y_list:y_list['y'])
    cap=[]
    y=y_list[0]['y']
    print(y)
    while True:
        for itm in y_list:
            if itm['y'] <= y:
                cap.append(itm)
                y_list.remove(itm)
        cap.sort(key=lambda cap:cap['x'])
        for i in range(0, len(cap)-1,2):
            x1 = cap[i]['x']
            x2 = cap[i+1]['x']
            draw.line(((int(x1),int(y)),(int(x2),int(y))),new_color,width=2)
        y+=1 
        i=0
        while i<len(cap):
            if y>=cap[i]['y2']:
                cap.pop(i)
            else:
                cap[i]['x']+=cap[i]['dx']
                while i>0 and cap[i-1]['x']>cap[i]['x']:
                    cap[i-1],cap[i]= cap[i],cap[i-1]
                    i-=1
                i+=1

        if  (len(cap)<=0):
            break

def zatr(boundary_color, new_color, x, y, img):
    stack = [(x,y)]
    while stack:
        cur_x, cur_y = stack.pop()
        if img.getpixel((cur_x,cur_y)) != boundary_color and img.getpixel((cur_x,cur_y)) != new_color:
            img.putpixel((cur_x,cur_y), new_color)
            if cur_x > 0:
                stack.append((cur_x - 1, cur_y))
            if cur_x < img.width - 1:
                stack.append((cur_x + 1, cur_y))
            if cur_y > 0:
                stack.append((cur_x, cur_y - 1))
            if cur_y < img.height - 1:
                stack.append((cur_x, cur_y + 1))

def str_zatr(boundary_color, new_color, start_x, start_y, img):
    stack = [(start_x,start_y)]
    while stack:
        x, y = stack.pop()
        x_min=x
        while x_min > 0 and img.getpixel((x_min-1,y))!=boundary_color:
            x_min-=1
        x_max=x
        while x_max < img.width - 1 and img.getpixel((x_max+1,y))!=boundary_color:
            x_max+=1
        draw.line(((x_max,y),(x_min,y)),new_color)
        flag=1
        for i in range(x_min,x_max+1):
            if img.getpixel((i,y-1))!=boundary_color and img.getpixel((i,y-1))!=new_color:
                if flag==1:
                    stack.append((i,y-1))
                    flag=0
                else:
                    flag=1
        flag1=1
        for i in range(x_min,x_max+1):
            if img.getpixel((i,y+1))!=boundary_color and img.getpixel((i,y+1))!=new_color:
                if flag1==1:
                    stack.append((i,y+1))
                    flag1=0
                else:
                    flag1=1

    
    

"""Алгоритмы закраски
С построчным сканированием
со списком реберных точек, 
со списком активных ребер
С затравкой
С прстрочной затравкой"""

x=250 #центр полигона (x)
y=250 #центр полигона (y)
n=7  #число сторон полигона
r=200  #радиус окружности в которую вписываем полигон
#получаем координаты вершин
coords=[(x + r * np.cos(2 * np.pi * i / n), y + r * np.sin(2 * np.pi * i / n)) for i in range(1, n+1)]
s=sorted(coords,key=lambda coords:coords[1])
x,y=s[0][0],s[0][1]
img = Image.new("RGB",(500,500), (255,255,255))
draw = ImageDraw.Draw(img)
draw.polygon((coords),outline =(255,0,0))
how=str(input())
if how=='str':
    str_scan(coords,img,(0,0,0))
elif how=='edge point':
    edge_point(coords,img,(0,0,0))
elif how=='active edge':
    active_edge(coords,img,(0,0,0))
elif how=='zatr':
    zatr((255,0,0), (0,0,0), int(x) , int(y)+1, img)
elif how=='str zatr':
    str_zatr((255,0,0), (0,0,0), 250 , 250, img)

img.show()

