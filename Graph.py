from collections import defaultdict

#Cria um dicionário onde cada chave é uma aresta
#E o valor é um boolean (True ou False) que indica de a aresta foi visitada
def edgesVisiting(edges: list):
 visited = {}
 for edge in edges:
  visited[edge] = False
 return visited

#Função que percorre as arestas procurando se para o vértice vertex há alguma aresta não visitada
def hasNext(vertex: str, edgesVisited: defaultdict):
    next = None
    for e in edgesVisited.keys():
        if vertex in e and edgesVisited[e] == False:
            next = e
            break

    return next

#Função que cria o circuito percorrendo as arestas ligadas ao grafo
def createCircuit(edges: dict, startingVertex: str):
    #Cria a lista de visitas às arestas
    visitedEdges = edgesVisiting(edges)

    #Recebe o vertice inicial por parâmetro
    currentVertex = startingVertex

    #Cria uma pilha onde serão inseridos os vértices percorridos
    stack = []

    #Cria um circuito onde os vértices serão inseridos
    circuit = []

    #Encontra uma aresta ligada ao vertice que ainda não foi percorrida
    next = hasNext(currentVertex, visitedEdges)

    # Coloca o vértice inicial na pulha
    stack += [currentVertex]

    #Percorre os vértices buscando arestas não percorridas enquanto houverem vértices na pilha
    while len(stack) > 0:
        #Idem ao trecho anterior
        next = hasNext(currentVertex, visitedEdges)
        stack += [currentVertex]

        #Executa enquando o retorno da função hasNext() for diferente de None
        #Se a função hasNext() retorna None quer dizer que o vertice
        #Que foi passada como parâmetro não possui nenhum aresta sem visita
        while next != None:

            #Indica que aresta foi visitada
            visitedEdges[next] = True

            #Coloca atribui o destino da aresta como currentVertice
            #Com esse código, a aresta pode ser fornecida com: u,v ou v,u
            if next[0] == currentVertex:
                currentVertex = next[2]
            else:
                currentVertex = next[0]

            #Insere o currentVertice na Pilha
            stack += [currentVertex]

            #Busca o próiximo destino
            next = hasNext(currentVertex, visitedEdges)

        #Remove o útlimo elemento da pilha
        stack.pop()

        #Adiciona o vértice removido ao circuito
        circuit += [currentVertex]

        #Atribui a currentVertice o próximo elemento da pilha
        currentVertex = stack[len(stack) - 1]

        #Remove o elemento inserido na Pilha
        stack.pop()

    #Retorna o circuito
    return circuit






