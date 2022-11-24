import igraph as ig
g = ig.load("rabbit.net")
CBs = g.cohesive_blocks()
#problematic node see https://raw.githubusercontent.com/mok33/igraph-issue/main/Cohesive_Blocks.PNG :
print(CBs.membership[1059])
#it's not in the same C.B as it neighbor 1044 (left top neighbor): 
print(CBs.membership[1044])

#neighbor check : 
print(g.neighbors(1059))
print(g.neighbors(1044))
