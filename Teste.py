from Graph import createCircuit

#========== Main ============
edgesNumber = ['1 2', '3 1', '1 5', '1 6', '2 3','2 6', '2 5', '3 6', '3 4','4 5', '5 6']
edgesChar = ['A B', 'C A', 'A E',
             'A F', 'B C','B F',
             'B E', 'C F', 'C D','D E', 'E F']

edgesGrafo01 = ['0 1',
                '0 2',
                '0 3',
                '0 4',
                '1 4',
                '2 1',
                '2 3',
                '3 2',
                '3 4',
                '4 1']



print(createCircuit(edgesGrafo01, '1'))