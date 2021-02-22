


class ex_1_1_6:
    def main(self):
        f=0
        g=0

        for i in range(0,16):
            # print(i,end="\n")
            print(f,end="\n")
            f=f+g
            g=f-g
            

programa=ex_1_1_6()

programa.main()

# imprime cero por 15 veces facil de comprobar por prueba de escritorio