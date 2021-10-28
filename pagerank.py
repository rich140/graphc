# Example 1: A points to B, B points to A

# Graph as adjacency list
#adj = [[1],[0]]
#pr = [40,40]

adj = [[1,2], [2], [0], [2]]
pr = [1,1,1,1]

for i in range(30):
    print("Iteration: " + str(i))
    tmp = []
    for j in range(len(adj)):
        new_pr = 1-0.85 
        for k in range(len(adj)):
            if j in adj[k] and j != k:
                new_pr += 0.85*(pr[k]/len(adj[k]))
        tmp.append(new_pr)
    for l in range(len(pr)):
        pr[l] = tmp[l]
        print(l, pr[l])
