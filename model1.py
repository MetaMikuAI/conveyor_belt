import math
import os

#恒量
g=9.8;#重力加速度
dt=0.001;#最小时间间隔
L=100;#带长
u=0.3;#传送带动摩擦因数
w=4;#带速
theta=math.pi/6;#倾角pi/6
m=1;#质量(暂时无实义)
N=4;#数值输出时保留位数
#变量
global t;
global a;
global v;
global x;
t=0;
a=0;
v=0;
x=0;

#推量
afmax=u*g*math.cos(theta);#最大静摩擦加速度
a0=g*math.sin(theta);

def sgn(inputx):
    if inputx  < 0:
        return -1;
    elif inputx==0:
        return 0;
    else:
        return 1;

def middle(inputa,inputb,inputc):
    if ((inputa>=inputb) & (inputb>=inputc)) | ((inputc>=inputb) & (inputb>=inputa)):
        return inputb;
    if ((inputb>=inputa) & (inputa>=inputc)) | ((inputc>=inputa) & (inputa>=inputb)):
        return inputa;
    if ((inputa>=inputc) & (inputc>=inputb)) | ((inputb>=inputc) & (inputc>=inputa)):
        return inputc;

while x<=L:
    t+=dt;
    a=(a0+middle(-afmax,(w-v)/dt-a0,afmax));
    v+=dt*a;
    x+=dt*v;
    print('t='+str(round(t,N))+' a='+str(round(a,N))+' v='+str(round(v,N))+' x='+str(round(x,N)));
    
os.system('pause');