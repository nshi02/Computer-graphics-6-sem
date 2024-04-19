import math
import numpy as np
# cmyk
def rgb_to_cmyk(rgb):
    rgb=[i/255 for i in rgb]
    k=1-max(rgb)
    c=(1-rgb[0]-k)/(1-k)
    m=(1-rgb[1]-k)/(1-k)
    y=(1-rgb[2]-k)/(1-k)
    return [c,m,y,k]
def cmyk_to_rgb(cmyk):
    r=255*(1-cmyk[0])*(1-cmyk[3])
    g=255*(1-cmyk[1])*(1-cmyk[3])
    b=255*(1-cmyk[2])*(1-cmyk[3])
    return [r,g,b]
# hsv
def rgb_to_hsv(rgb):
    rgb=[i/255 for i in rgb]
    cmax=max(rgb)
    cmin=min(rgb)
    d=cmax-cmin
    if d==0:
        h=0
    elif cmax==rgb[0]:
        h=(60 * ((rgb[1]-rgb[2])/d) + 360) % 360
    elif cmax == rgb[1]:
        h = (60 * ((rgb[2]-rgb[0])/d) + 120) % 360
    elif cmax == rgb[2]:
        h = (60 * ((rgb[0]-rgb[1])/d) + 240) % 360
    if cmax==0:
        s=0
    else:
        s=d/cmax
    v=cmax
    return ([h,s,v])
def hsv_to_rgb(hsv):
    c=hsv[2]*hsv[1]
    x=c*(1-abs((hsv[0]/60)%2- 1))
    m=hsv[2]-c
    if 0<=hsv[0] and hsv[0]<60:
        r=c
        g=x
        b=0
    elif 60<=hsv[0] and hsv[0]<120:
        r=x
        g=c
        b=0
    elif 120<=hsv[0] and hsv[0]<180:
        r=0
        g=c
        b=x
    elif 180<=hsv[0] and hsv[0]<240:
        r=0
        g=x
        b=c
    elif 240<=hsv[0] and hsv[0]<300:
        r=x
        g=0
        b=c
    else:
        r=c
        g=0
        b=x
    return [(r+m)*255,(g+m)*255,(b+m)*255]
# hsl
def rgb_to_hsl(rgb):
    rgb=[i/255 for i in rgb]
    cmax=max(rgb)
    cmin=min(rgb)
    d=cmax-cmin
    if d==0:
        h=0
    elif cmax==rgb[0]:
        h=(60 * ((rgb[1]-rgb[2])/d)%6) % 360
    elif cmax == rgb[1]:
        h = (60 * ((rgb[2]-rgb[0])/d) + 120) % 360
    elif cmax == rgb[2]:
        h = (60 * ((rgb[0]-rgb[1])/d) + 240) % 360
    l=(cmax+cmin)/2
    if cmax==0:
        s=0
    else:
        s=d/(1-abs(2*l-1))
    l=(cmax+cmin)/2

    return ([h,s,l])
def hsl_to_rgb(hsl):
    c=(1-abs(2*hsl[2]-1))*hsl[1]
    x=c*(1-abs((hsl[0]/60)%2- 1))
    m=hsl[2]-c/2
    if 0<=hsl[0] and hsl[0]<60:
        r=c
        g=x
        b=0
    elif 60<=hsl[0] and hsl[0]<120:
        r=x
        g=c
        b=0
    elif 120<=hsl[0] and hsl[0]<180:
        r=0
        g=c
        b=x
    elif 180<=hsl[0] and hsl[0]<240:
        r=0
        g=x
        b=c
    elif 240<=hsl[0] and hsl[0]<300:
        r=x
        g=0
        b=c
    else:
        r=c
        g=0
        b=x
    return [((r+m)*255),(g+m)*255,(b+m)*255]
print(hsl_to_rgb(rgb_to_hsl([128,128,128])))
# xyz
def rgb_to_xyz(rgb):
    rgb=[i/255 for i in rgb]
    X = rgb[0] * 0.4124 + rgb[1] * 0.3576 + rgb[2] * 0.1805
    Y = rgb[0] * 0.2126 + rgb[1] * 0.7152 + rgb[2] * 0.0722
    Z = rgb[0] * 0.0193 + rgb[1] * 0.1192 + rgb[2] * 0.9505
    return [X,Y,Z]
def xyz_to_rgb(xyz):

    r = xyz[0] *  3.2406 + xyz[1] * (-1.5372) + xyz[2] * (-0.4986)
    g = xyz[0] * (-0.9689) + xyz[1] *  1.8758 + xyz[2] *  0.0415
    b = xyz[0] *  0.0557 + xyz[1] * (-0.2040) + xyz[2] *  1.0570
    return [r*255,g*255,b*255]

# lab
def xyz_to_lab(xyz):
    xn=96.4212
    yn=100
    zn=82.5188
    def f(t):
        delta=6/29
        if t>delta**3:
            return t**(1/3)
        else:
            return 1/3*t*delta**(-2)+4/29
    L=116*f(xyz[1]/yn)-16
    a=500*(f(xyz[0]/xn)-f(xyz[1]/yn))
    b=200*(f(xyz[1]/yn)-f(xyz[2]/zn))
    return [L,a,b]
def lab_to_xyz(lab):
    xn=96.4212
    yn=100
    zn=82.5188
    def f(t):
        delta=6/29
        if t>delta:
            return t**(3)
        else:
            return 3*(t-4/29)*delta**(2)
    x=xn*f((lab[0]+16)/116+lab[1]/500)
    y=yn*f((lab[0]+16)/116)
    z=zn*f((lab[0]+16)/116-lab[2]/200)
    return [x,y,z]
print(xyz_to_lab(rgb_to_xyz([125,0,0])))
print((rgb_to_xyz([125,0,0])))
print(hsv_to_rgb([120,1,1]))
print(rgb_to_hsv([0,225,0]))