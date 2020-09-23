from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    s = {}

    for parent, child in ancestors:
        if child not in s:
            s[child] = [parent]
        else:
            s[child].append(parent)
    
    if starting_node not in s:
        return -1

    return g.dfs(starting_node, s)


