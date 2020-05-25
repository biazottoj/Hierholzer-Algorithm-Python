from Graph import createCircuit

#========== Main ============
edgesNumber = ['1 2', '3 1', '1 5', '1 6', '2 3','2 6', '2 5', '3 6', '3 4','4 5', '5 6']
edgesChar = ['A B', 'C A', 'A E', 'A F', 'B C','B F', 'B E', 'C F', 'C D','D E', 'E F']

edges2 = ['1 2', '1 3', '2 3', '2 4']

print(createCircuit(edges2, '1'))