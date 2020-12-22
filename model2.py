import math
import os
import matplotlib.pyplot as plt

#恒量
g=10;#重力加速度
dt=0.001;#最小时间间隔
L=4;#带长
u=0.86602540378444;#传送带动摩擦因数
w=2;#带速
theta=math.pi/6;#倾角pi/6
m=1;#质量(暂时无实义)
N=4;#数值输出时保留位数

#(全局)变量
global t;
global a;
global v;
global x;
t=0;#时间
a=0;#加速度
v=0;#速度
x=0;#位移

#推量
afmax=u*g*math.cos(theta);#最大静摩擦加速度
a0=g*math.sin(theta);#重力加速度斜向分量

#记录
ArrayT=[];#时间数组
ArrayA=[];#加速度数组
ArrayV=[];#速度数组
ArrayX=[];#位移数组

def sgn(inputx):#符号函数
    if inputx  < 0:
        return -1;
    elif inputx==0:
        return 0;
    else:
        return 1;

def middle(inputa,inputb,inputc):#(三路输入)中位数函数
    if ((inputa>=inputb) & (inputb>=inputc)) | ((inputc>=inputb) & (inputb>=inputa)):
        return inputb;
    if ((inputb>=inputa) & (inputa>=inputc)) | ((inputc>=inputa) & (inputa>=inputb)):
        return inputa;
    if ((inputa>=inputc) & (inputc>=inputb)) | ((inputb>=inputc) & (inputc>=inputa)):
        return inputc;

while x<=L:
    t+=dt;
    a=a0+middle(-afmax,(w-v)/dt-a0,afmax);
    v+=dt*a;
    x+=dt*v;
    ArrayT.append(t);#时间数组
    ArrayA.append(a);#加速度数组
    ArrayV.append(v);#速度数组
    ArrayX.append(x);#位移数组
    print('t='+str(round(t,N))+' a='+str(round(a,N))+' v='+str(round(v,N))+' x='+str(round(x,N)));#实时输出

plt.plot(ArrayT,ArrayA);#加速度图像
plt.plot(ArrayT,ArrayV);#速度图像
#plt.plot(ArrayT,ArrayX);
plt.show();#图像显示
os.system('pause');#暂停
