import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import math

class point2D:
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.polar=0

class pointsList:
    def __init__(self):
        super().__init__()
        self.hull=[]
    def add(self,a):
        self.hull.append(a)
    def delete(self):
        return self.hull.pop()
    def peek(self):
        return self.hull[-1]
    def print(self):
        for obj in self.hull:
            print("x:",obj.x," y:",obj.y," angle:",obj.polar)

    def get(self):
        x=[]
        y=[]
        polar=[]
        for obj in self.hull:
            x.append(obj.x)
            y.append(obj.y)
            polar.append(obj.polar)
        return x,y,polar
        
    def exch(self,a,b):
        swap=self.hull[a]
        self.hull[a]=self.hull[b]
        self.hull[b]=swap

    def partitionY(self,start,end):
        pivot=self.hull[(start+end)//2]
        i=start-1
        j=end+1
        while True:
            i+=1
            while ((self.hull[i].y<pivot.y) or   
                (self.hull[i].y==pivot.y and self.hull[i].x<pivot.x) ): # se garantiza escoger el menor o mas izquierdo en caso de empate
                i+=1
            j-=1
            while (self.hull[j].y>pivot.y or 
                (self.hull[j].y==pivot.y and self.hull[j].x>pivot.x) ):
                j-=1
            if (i>=j): return j
            self.exch(i,j)
        
    def sort(self,by):
        random.shuffle(self.hull)
        if by=="Y":
            self.qsY(0,len(self.hull)-1)
        elif by=="POLAR":
            self.hull[0].polar=0
            self.qsPolar(1,len(self.hull)-1)

    def qsY(self,start,end):
        if(start<end):
            pidx=self.partitionY(start,end)
            self.qsY(start,pidx)
            self.qsY(pidx+1,end)

    def calcularPolar(self):
        self.hull[0].polar=0
        for i in range(1,len(self.hull)):
            origin=point2D(self.hull[i].x-self.hull[0].x,
                self.hull[i].y-self.hull[0].y)
            # print("origin:",origin.x, origin.y)
            self.hull[i].polar=math.degrees(math.atan2(origin.y,origin.x))
    
    def ccw(self,a,b,c):
        #producto cruz trasladado al origen (restando p[0])
        return ((b.x - a.x) * (c.y - a.y) -
              (c.x - a.x) * (b.y - a.y))
    
    def distance(self,p1,p2):
        return math.sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))

    def less(self,p1,p2):
        ori=self.ccw(self.hull[0],p1,p2)
        if(ori==0):    # colinear toca resolver por distancia a p[0]
            d1=self.distance(self.hull[0],p1)
            d2=self.distance(self.hull[0],p2)
            # print(ori,d1,d2)
            return True if (d1 <= d2) else False
        # forma compacta de if dentro de un return
        return True if (ori<0) else False
    
    def greater(self,p1,p2):
        ori=self.ccw(self.hull[0],p1,p2)
        if(ori==0):    # colinear toca resolver por distancia a p[0]
            d1=self.distance(self.hull[0],p1)
            d2=self.distance(self.hull[0],p2)
            # print(ori,d1,d2)
            return True if (d1 >= d2) else False
        # forma compacta de if dentro de un return
        return True if (ori>0) else False

    def partitionAngle(self,start,end):
        pivot=self.hull[(start+end)//2]
        i=start-1
        j=end+1
        while True:
            i+=1
            # while (self.less(self.hull[i],pivot)):
            while (self.hull[i].polar<pivot.polar):
                i+=1
            j-=1
            # while (self.greater(self.hull[j],pivot)):
            while (self.hull[j].polar>pivot.polar):
                j-=1
            if(i>=j): return j
            self.exch(i,j)

    def qsPolar(self,start,end):
        if(start<end):
            pang=self.partitionAngle(start,end)
            self.qsPolar(start,pang)
            self.qsPolar(pang+1,end)
    
    def convexHull(self):
        self.sort("Y")
        self.calcularPolar()
        self.qsPolar(1,len(self.hull)-1)
        finalHull=pointsList()

        finalHull.add(point2D(self.hull[0].x,self.hull[0].y))
        finalHull.add(point2D(self.hull[1].x,self.hull[1].y))
        for i in range(2,len(self.hull)):
            top=finalHull.delete()
            while (self.ccw(finalHull.peek(),top,self.hull[i])<=0):
                top=finalHull.delete()

            finalHull.add(point2D(top.x,top.y))
            finalHull.add(point2D(self.hull[i].x,self.hull[i].y))
        
        #agrego el primero nuevamente para cerrar el poligono
        finalHull.add(point2D(self.hull[0].x,self.hull[0].y))
        return finalHull

    def jitter(self):
        numberList=[-1,1]
        upLimit=0.03
        for i in range(0,len(self.hull)):
            factor=random.uniform(0,upLimit)
            print(factor)
            sign=random.choice(numberList)
            self.hull[i].x+=self.hull[i].x*factor*sign
            factor=random.uniform(0,upLimit)
            sign=random.choice(numberList)
            self.hull[i].y+=self.hull[i].y*factor*sign
        




N=10
xvert=list(np.random.randint(-50,50,N).flatten())
yvert=list(np.random.randint(0,50,N).flatten())
prg=pointsList()
for i in range(0,N):
    prg.add(point2D(xvert[i],yvert[i]))

print("unordered by Y")
prg.print()
# print("shuffle")
# prg.sort1()
# prg.print()
# print("sorted by Y")
# prg.sort("Y")
# prg.print()

# prg.calcularPolar()
# print("unordered by angle")
# prg.print()
# print("sorted by Angle")
# prg.qsPolar(1,len(prg.hull)-1)
# prg.print()

fig = plt.figure()
ax1 = plt.axes(xlim=(-75, 75), ylim=(-15,65))
plt.xlabel('x')
plt.ylabel('y')
lines=[]
sc,=ax1.plot([], [], "bs",ls="")
lines.append(sc)  # set linestyle to none
sc1,=ax1.plot([], [], "red")
lines.append(sc1)       # set linestyle to none
# call the animator.  blit=True means only re-draw the parts that have changed.
img=plt.imread("1.jpg")
ax1.imshow(img, extent=[-75, 75, -15, 65])

# for line in lines:
#     print(line)
#     line.set_data([],[])


lnum,line=enumerate(lines)
print(lnum,line)

for i in range(500):
    fl=prg.convexHull()
    # fl.print()
    x,y,polar=prg.get()
    x1,y1,polar2=fl.get()
    # X = np.c_[x, y]
    # sc.set_offsets(X)
    # xlist = [x, x1]
    # ylist = [y, y1]
    # #for index in range(0,1):
    # for lnum,line in enumerate(lines):
    #     line.set_data(xlist[lnum], ylist[lnum])
    sc.set_data(x,y)
    sc1.set_data(x1,y1)
    fig.canvas.draw_idle()
    plt.pause(0.1)
    prg.jitter()

plt.show()

# plt.scatter(x, y)
# plt.plot(x1,y1,'red')
# hacerla con pocos puntos y ponerle messi a uno de ellos
