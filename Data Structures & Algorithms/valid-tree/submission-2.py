class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree has no cyles, so check for cycles

        # build linked list / hash map

        tree = defaultdict(list)

        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        # use dfs to find loop

        if len(edges) == 0: # stupid edge case
            return True

        visited = set()

        def dfs(node, parent):

            if node not in tree:
                return True
            if node in visited and node != parent:
                return False
            
            visited.add(node)

            total = True
            for i in range(len(tree[node])):
                if tree[node][i] == parent:
                    continue
                total = total and dfs(tree[node][i], node)
            
            return total
        
        return True if (dfs(edges[0][0], None) and len(visited) == n) else False


