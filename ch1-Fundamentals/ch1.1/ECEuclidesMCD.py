import sys
#  ex_1_1_24
#  python ECEuclidesMCD.py 1111111 1234567

class euclidesMCD:

    def euclides(self,p,q,depth):
        depth=depth+1
        if q==0: return p
        # si q es mayor que P el residuo voltea ambos
        # ya que el cosciente seria 0 y el residuo de la division
        # seria P
        residuo=p%q
        print(depth*" "+"p:"+str(p)+", q:"+str(q)+" r:"+str(residuo))
        return self.euclides(q,residuo,depth)

    def main(self):
        p=int(sys.argv[1])
        q=int(sys.argv[2])
        print(self.euclides(p,q,0))

programa=euclidesMCD()
programa.main()