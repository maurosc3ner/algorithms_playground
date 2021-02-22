import sys


class ex_1_1_21:
    def main(self):
        pipe=sys.stdin.readlines()
        for linea in pipe:
            llave=(linea.split(" "))
            prom=round(float(llave[1])/float(llave[2]),3)
            print(llave[0]+" promedio de bateo="+str(prom))



programa=ex_1_1_21()
programa.main()