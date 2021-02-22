<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1605594999105" ID="ID_1655193547" MODIFIED="1607579527454" TEXT="Graphs">
<font BOLD="true" NAME="SansSerif" SIZE="12"/>
<node CREATED="1605595017038" ID="ID_1364270821" MODIFIED="1606964372038" POSITION="right" TEXT="Undirected graphs">
<node CREATED="1605595065028" ID="ID_1796938635" MODIFIED="1605595341287">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Conjunto de nodos y una
    </p>
    <p>
      coleccion de links que
    </p>
    <p>
      conecta un par de nodos
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1605595223956" ID="ID_328355499" MODIFIED="1605595271567" TEXT="Tiene multiples formas de dibjujado"/>
<node CREATED="1605595272869" ID="ID_1243306314" MODIFIED="1605595279442" TEXT="Anomalias">
<node CREATED="1605595280531" ID="ID_1857036740" MODIFIED="1605595325859" TEXT="Un link hacia si mismo"/>
<node CREATED="1605595297124" ID="ID_1824439491" MODIFIED="1605595320947">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      dos o mas links que conectan
    </p>
    <p>
      el mismo par de nodos
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1605595372898" ID="ID_1191105788" MODIFIED="1605595380078" TEXT="Tambien llamados multigrafos"/>
</node>
<node CREATED="1605597628137" ID="ID_1549429790" MODIFIED="1605597630590" TEXT="Glosario">
<node CREATED="1605597632347" ID="ID_1426620939" MODIFIED="1605597680345" TEXT="nodo adjacente=cuando hay un link entre dos nodos"/>
<node CREATED="1605597682464" ID="ID_30130699" MODIFIED="1605597712868" TEXT="link incidente=el link que conecta nodos v y w"/>
<node CREATED="1605597714713" ID="ID_819044157" MODIFIED="1605597747506" TEXT="grado de un nodo v=numero de links incidentes con v"/>
<node CREATED="1605597750168" ID="ID_1574558256" MODIFIED="1605597789478" TEXT="subgrafo=subconjunto de links y nodos que constituyen un grafo"/>
<node CREATED="1605597791592" ID="ID_237263192" MODIFIED="1605597820301" TEXT="path=secuencia de nodos conectados por links"/>
<node CREATED="1605597823573" ID="ID_1135751332" MODIFIED="1605597840197" TEXT="simple path=secuencia con nodos no repetidos"/>
<node CREATED="1605597842974" ID="ID_186716641" MODIFIED="1605597943967" TEXT="ciclo=path con un al menos un link entre el primero y ultimo nodo"/>
<node CREATED="1605597946107" ID="ID_1651444604" MODIFIED="1605597975185" TEXT="ciclo simple=ciclo sin links o nodos repetidos excepto el primero y ultimo"/>
<node CREATED="1605597977573" ID="ID_201793471" MODIFIED="1605597992141" TEXT="length=numero de links"/>
<node CREATED="1605598008877" ID="ID_708198524" MODIFIED="1605598059559" TEXT="conectado=si hay al menos un path entre cada nodo a cada otro nodo en el grafo"/>
<node CREATED="1605598061407" ID="ID_379059373" MODIFIED="1605598099429" TEXT="no conectado=conjunto de grafos conectados"/>
<node CREATED="1605598112649" ID="ID_480184594" MODIFIED="1605598126673" TEXT="grafo aciclico=grafo sin ciclos"/>
<node CREATED="1605598131018" ID="ID_780236712" MODIFIED="1605598167935" TEXT="tree= es un grafo aciclico &quot;conectado&quot;"/>
<node COLOR="#338800" CREATED="1605598170306" ID="ID_763102212" MODIFIED="1605598201366" TEXT="forest=conjunto desunido de tree"/>
<node CREATED="1605598205356" ID="ID_1674230560" MODIFIED="1605598695767" TEXT="spanning tree=es un grafo compuesto de todos los nodos y casi todos los links de un grafo conectado"/>
<node CREATED="1605598701542" ID="ID_1481970602" MODIFIED="1605598717436" TEXT="spanning forest=union de spanning trees"/>
<node CREATED="1605598366990" ID="ID_1605666358" MODIFIED="1605598388549" TEXT="densidad de un grafo=proportion de pares posibles de ndos conectados por links"/>
<node CREATED="1605598390765" ID="ID_1512021316" MODIFIED="1605598435473" TEXT="sparse=links es igual a un factor pequenho de la cant de nodos"/>
<node CREATED="1605598437697" ID="ID_1378646816" MODIFIED="1605598459491" TEXT="dense=lo contrario a sparse"/>
<node CREATED="1605598472090" ID="ID_555594108" MODIFIED="1605598521901" TEXT="grafo bipartito=es un grafo que divido en dos podemos conectar el 1er conjunto de vertices con el 2do conjunto"/>
</node>
<node CREATED="1605598746719" ID="ID_1932677237" MODIFIED="1605598749505" TEXT="representaciones">
<node CREATED="1605598751116" ID="ID_1233094910" MODIFIED="1605598759967" TEXT="matriz de adjacencia V^2"/>
<node CREATED="1605598763040" ID="ID_1175964050" MODIFIED="1605598833934" TEXT="lista de links (dificil de implementar el conteo de nodos porque tocaria examinarlos todos para evitar repetidos)"/>
<node CREATED="1605598836248" ID="ID_66991724" MODIFIED="1605598868872" TEXT="lista de adjacencia (mas comun), usa un bag de linked list por vertice"/>
</node>
<node CREATED="1605851221467" ID="ID_1796782704" MODIFIED="1605851223741" TEXT="DFS">
<node CREATED="1605851369765" ID="ID_514046013" MODIFIED="1605851394344" TEXT="es el metodo mas simple dentro de la familia de algoritmos de procesamiento de grafos">
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1605851429482" ID="ID_216886166" MODIFIED="1605851440371" TEXT="problema historico del laberinto y el hilo rojo"/>
<node CREATED="1605854877542" ID="ID_544239625" MODIFIED="1605854884576" TEXT="Implementacion">
<node CREATED="1605854886975" ID="ID_1398096483" MODIFIED="1605854892526" TEXT="mejor desacoplado"/>
<node CREATED="1605854894199" ID="ID_1317112989" MODIFIED="1605854923334">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      la estructura como una lista
    </p>
    <p>
      de v-1 nodos y cada posicion un Bag
    </p>
  </body>
</html></richcontent>
<node CREATED="1605855027185" ID="ID_1021537662" MODIFIED="1605855088254" TEXT="numero de vertices int"/>
<node CREATED="1605855035156" ID="ID_103531819" MODIFIED="1605855334881" TEXT="Un numero de Edges"/>
<node CREATED="1605855337340" ID="ID_1217346281" MODIFIED="1605855346928" TEXT="Una lista de adjacencia"/>
<node CREATED="1605855384666" ID="ID_1234494732" MODIFIED="1605855406591" TEXT="addEdge(v,w) lo hace tanto en v como en w"/>
</node>
<node CREATED="1605854927579" ID="ID_1184758083" MODIFIED="1605854963803">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Los algoritmos de procesamiento a
    </p>
    <p>
      parte como otra clase ejm DFS o BFS
    </p>
  </body>
</html></richcontent>
<node CREATED="1605854976717" ID="ID_289985703" MODIFIED="1605854994957" TEXT="Tienen un arreglo booleano marked[v-1]"/>
<node CREATED="1605854997213" ID="ID_1561434248" MODIFIED="1605855008735" TEXT="tienen un backtrace edgeTo entero"/>
<node CREATED="1605855015687" ID="ID_339570849" MODIFIED="1605855023452" TEXT="tiene s como source o nodo origen"/>
</node>
</node>
</node>
<node CREATED="1605856732359" ID="ID_1795155258" MODIFIED="1605856735120" TEXT="BFS">
<node CREATED="1605856749215" ID="ID_215907679" MODIFIED="1605856764868" TEXT="Visita tmb todos los nodos pero usa un esquema de cola para ello"/>
<node CREATED="1605856766937" ID="ID_792058879" MODIFIED="1606287604714">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Permite contestar cual es la ruta
    </p>
    <p>
      mas corta al nodo sabido debido
    </p>
    <p>
      a su modo de expansion de adentro
    </p>
    <p>
      hacia fuera
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1606286405952" ID="ID_1147043134" MODIFIED="1606286411147" TEXT="implementacion">
<node CREATED="1606286412301" ID="ID_1382604778" MODIFIED="1606286420495" TEXT="no es recursivo como el DFS"/>
<node CREATED="1606287625330" ID="ID_657749983" MODIFIED="1606287628531" TEXT="marked"/>
<node CREATED="1606287630808" ID="ID_1822980491" MODIFIED="1606287646069" TEXT="edgeTo igual que DFS para el backtrace"/>
<node CREATED="1606287647807" ID="ID_816792492" MODIFIED="1606287683415">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      dist[source]=0
    </p>
    <p>
      distTo=dist[cur]+1
    </p>
  </body>
</html></richcontent>
</node>
</node>
</node>
</node>
<node CREATED="1606796060244" ID="ID_153102571" MODIFIED="1606796067804" POSITION="left" TEXT="directed graphs">
<node CREATED="1606796113846" ID="ID_1332691755" MODIFIED="1606796131407" TEXT="Todo UG es un Digraph"/>
<node CREATED="1606796083219" ID="ID_1125705841" MODIFIED="1606796651939" TEXT="implementacion">
<node CREATED="1606796088908" ID="ID_872768920" MODIFIED="1606796092171" TEXT="DFS">
<node CREATED="1606796105783" ID="ID_38989070" MODIFIED="1606796151811" TEXT="Identico que undirected"/>
</node>
<node CREATED="1606796094170" ID="ID_396656383" MODIFIED="1606796096131" TEXT="BFS">
<node CREATED="1606796136340" ID="ID_1275180879" MODIFIED="1606796147909" TEXT="Identico que en undirected"/>
</node>
<node CREATED="1606796097968" ID="ID_1927964640" MODIFIED="1606796102597" TEXT="Strong connectivity"/>
</node>
<node CREATED="1606796702666" ID="ID_1515759745" MODIFIED="1606796704384" TEXT="ejemplos">
<node CREATED="1606796719702" ID="ID_1691886303" MODIFIED="1606796728720" TEXT="academia-paper-citacion"/>
<node CREATED="1606796731771" ID="ID_660312885" MODIFIED="1606796750607" TEXT="internet-page-hyperlink"/>
</node>
<node CREATED="1606964390389" ID="ID_1030965842" MODIFIED="1606964415145" TEXT="topological sort">
<node CREATED="1606964418381" ID="ID_444624230" MODIFIED="1606964456951" TEXT="precedence-constrained scheduling"/>
<node CREATED="1606964459944" ID="ID_1104498130" MODIFIED="1606964459944" TEXT=""/>
</node>
</node>
<node CREATED="1607317355572" ID="ID_55154465" MODIFIED="1607317365062" POSITION="right" TEXT="Minimum spanning trees">
<node CREATED="1607317367927" ID="ID_1087634566" MODIFIED="1607317412501">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      objetivo: tocar todos los vertices con el menor peso posible
    </p>
    <p>
      osea los edges (links) con el menor peso)
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1607317721306" ID="ID_1115975228" MODIFIED="1607317723372" TEXT="Kruskal">
<node CREATED="1607317724994" ID="ID_407787237" MODIFIED="1607317742829" TEXT="evalue los edges por peso de menor a mayor"/>
<node CREATED="1607317744569" ID="ID_468801156" MODIFIED="1607317765846" TEXT="agregue al tree SINO crea un ciclo "/>
<node CREATED="1607318312042" ID="ID_1160970520" MODIFIED="1607318338440" TEXT="usa una priority queue (queue ordenada)"/>
<node CREATED="1607318341252" ID="ID_771859357" MODIFIED="1607318377453" TEXT="y usa un union-find para ver si hay ciclo antes de agregar el edge"/>
</node>
<node CREATED="1607320335779" ID="ID_1345910968" MODIFIED="1607320385007" TEXT="Prim">
<node CREATED="1607320347809" ID="ID_910281794" MODIFIED="1607320492903" TEXT="0. arranca desde cero"/>
<node CREATED="1607320353115" ID="ID_1919461305" MODIFIED="1607320591972">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      1. Evalua los edges conectados y
    </p>
    <p>
      ordenados al vertex inicial
    </p>
  </body>
</html></richcontent>
<node CREATED="1607320604633" ID="ID_1883663973" MODIFIED="1607323457811">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      se decarta el edge si es obsoleto&#160;
    </p>
    <p>
      osea union-find.connected
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1607320386639" ID="ID_769988467" MODIFIED="1607320503971" TEXT="2. agrega el edge de minWeight"/>
<node CREATED="1607320425962" ID="ID_626865224" MODIFIED="1607320509298" TEXT="3. agrega a la cola ordenada los edges del vertice agregado"/>
<node CREATED="1607320451732" ID="ID_215605238" MODIFIED="1607320514763" TEXT="4. repite paso 1"/>
<node CREATED="1607320519937" ID="ID_1750530047" MODIFIED="1607320519937" TEXT=""/>
</node>
</node>
<node CREATED="1607578473821" ID="ID_1272536443" MODIFIED="1607578479632" POSITION="left" TEXT="Shortest Paths">
<node CREATED="1607578481875" ID="ID_461787147" MODIFIED="1607578494038" TEXT="se aplica sobre edgeWeightedDigraph"/>
<node CREATED="1607578496238" ID="ID_232315304" MODIFIED="1607578497481" TEXT="API">
<node CREATED="1607578499614" ID="ID_1144421558" MODIFIED="1607578504250" TEXT="DirectedEdge">
<node CREATED="1607578506845" ID="ID_1856072859" MODIFIED="1607578522204" TEXT="v, w, weight"/>
<node CREATED="1607578523704" ID="ID_294349899" MODIFIED="1607578528262" TEXT="getWeight"/>
<node CREATED="1607578529790" ID="ID_1242507723" MODIFIED="1607578547139" TEXT="from() return v (reemplaza either)"/>
<node CREATED="1607578548779" ID="ID_350803864" MODIFIED="1607578561475" TEXT="to(): return w (reemplaza other)"/>
</node>
<node CREATED="1607578567157" ID="ID_549580119" MODIFIED="1607578577231" TEXT="EdgeWeightedDigraph">
<node CREATED="1607578579229" ID="ID_736888621" MODIFIED="1607578624903" TEXT="misma API que minimum spanning tree"/>
<node CREATED="1607578627078" ID="ID_1400718125" MODIFIED="1607579116997" TEXT="addEdge es solo en V por ser directed como en los Digraph"/>
</node>
<node CREATED="1607579145213" ID="ID_12680099" MODIFIED="1607579149945" TEXT="SP">
<node CREATED="1607579181993" ID="ID_1674492234" MODIFIED="1607579238321" TEXT="SP(graph G, vertex source)"/>
<node CREATED="1607579190170" ID="ID_1455302298" MODIFIED="1607579203552" TEXT="int distTo(vertex v)"/>
<node CREATED="1607579205379" ID="ID_1643827150" MODIFIED="1607579226890" TEXT="iterable pathTo(vertex v)"/>
</node>
</node>
<node CREATED="1607579287223" ID="ID_818884824" MODIFIED="1607579289555" TEXT="tipos">
<node CREATED="1607579290480" ID="ID_1670373604" MODIFIED="1607579312997" TEXT="single-source: camino mas corto desde source a todos los demas vertices"/>
<node CREATED="1607579317437" ID="ID_1812643339" MODIFIED="1607579335382" TEXT="all-pairs: caminos mas cortos desde cada vertice hacia los demas"/>
</node>
<node CREATED="1607579611389" ID="ID_1654702026" MODIFIED="1607579616285" TEXT="edge relaxation"/>
<node CREATED="1607579831163" ID="ID_1288131786" MODIFIED="1607579836880" TEXT="optimality">
<node CREATED="1607580102591" ID="ID_1762798617" MODIFIED="1607580151787" TEXT="la distancia[w]&lt;= dist[w-1]+e[w]_weight"/>
</node>
</node>
</node>
</map>
