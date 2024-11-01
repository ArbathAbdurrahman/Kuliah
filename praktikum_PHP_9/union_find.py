parent=[]
rank=[]

def union_find(length):
    parent.clear()
    rank.clear()
    for i in range(length):
        parent.append(i)
        rank.append(0)

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]
def set_union(u,v):
    root_u = find(u)
    root_v = find(v)
    if (root_u != root_v):
        if rank[root_u] < rank[root_v]:
            parent[root_u]=root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v]=root_u
        else:
            parent[root_v]=root_u
            rank[root_u] += 1


