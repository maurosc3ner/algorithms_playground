import numpy as np

class ex_1_1_33:
    def productoPunto(self,x,y):
        res=0
        # print(len(x))
        if (len(x)!=len(y)): return -1
        for i in range(0,len(x)):
            print(x[i]*y[i],i)
            res+=x[i]*y[i]
        print(res)

    def productoMatricial(self,m1,m2):
        # comprobacion m1.col==m2.row
        if (m1.shape[1]!=m2.shape[0]): return -1
        inner=m1.shape[1]
        # creo la matriz resultante
        res=np.zeros([m1.shape[0],m2.shape[1]])
        print(res)
        for row in range(0,res.shape[0]):
            for col in range(0,res.shape[1]):
                for k in range(0,inner):
                    res[row,col]+=m1[row,k]*m2[k,col]
        print(res)

    def traspuesta(self,m1):
        mtraspuesta=np.zeros([m1.shape[1], m1.shape[0]])
        print(mtraspuesta,m1.shape)
        for i in range(0,m1.shape[0]):
            for j in range(0,m1.shape[1]):
                mtraspuesta[j,i]=m1[i,j]
        print(mtraspuesta)
        # return mtranspose

    def productoMxV(self,m1,m2):
        if(len(m2.shape)==1):
            if (m1.shape[1]!=m2.shape[0]): return -1
            # creo la matriz resultante
            res=np.zeros([m1.shape[0],1])
            inner=m1.shape[1]
            print(res,res.shape)
            for row in range(0,res.shape[0]):
                # for col in range(0,res.shape[1]):
                for k in range(0,inner):
                    res[row,0]+=m1[row,k]*m2[k]
            print(res)
        elif(len(m1.shape)==1):
            if (m1.shape[0]!=m2.shape[0]): return -1
            # creo la matriz resultante
            res=np.zeros([1,m2.shape[1]])
            print(res)
            inner=m2.shape[0]
            for col in range(0,res.shape[1]):
                for k in range(0,inner):
                    res[0,col]+=m1[k]*m2[k,col]
            print(res)


        # print(m1.shape,m2.shape,len(m2),len(m2.shape))
        # comprobacion m1.col==m2.row
        # if (m1.shape[1]!=m2.shape[0]): return -1
        # inner=m1.shape[1]
        # # creo la matriz resultante
        # res=np.zeros([m1.shape[0],m2.shape[1]])
        # print(res)
        # for row in range(0,res.shape[0]):
        #     for col in range(0,res.shape[1]):
        #         for k in range(0,inner):
        #             res[row,col]+=m1[row,k]*m2[k,col]
        # print(res)


    def main(self):
        # arr=np.array([[1,2,3],[4,5,6]])
        # self.traspuesta(arr)
        # producto punto
        # x=np.array([1, 0.5,3])
        # y=np.array([4,-4,1])
        # self.productoPunto(x,y)
        # producto matricial
        # x=np.array([[1, 2],[4,5],[7,8]])
        # y=np.array([[1,2,3],[0,5,2]])
        # self.productoMatricial(x,y)
        # producto MxN.Mx1
        x=np.array([[1, 2,3],[4,5,6],[7,8,9]])
        y=np.array([2,1,3])
        self.productoMxV(x,y)
        
        self.productoMxV(y,x)

programa=ex_1_1_33()
programa.main()