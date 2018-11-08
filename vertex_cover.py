class Node:
    def __init__(self, value, edges=None):
        self.value = value
        self.edges = edges or []
        self.visited = 0

class Edges:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

class FreeTree:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.start_value = 0

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, from_node, to_node):
        edge = Edges(from_node, to_node)
        from_node_index = self.nodes.index(from_node)
        self.nodes[from_node_index].edges.append(edge)
        to_node_index = self.nodes.index(to_node)
        self.nodes[to_node_index].edges.append(edge)
        self.edges.append(edge)

    def dfs(self, start_node, start_value, enter_node):
        result = []
        if len(start_node.edges) is 1 and start_node is not enter_node:
            return [start_node]
        elif len(start_node.edges) is 0:
            return [start_node]
        else:
            if start_node.visited == start_value:
                start_node.visited = start_value + 1
                for item in start_node.edges:
                    if start_node is not item.from_node:
                        result = result + self.dfs(item.from_node, start_value, enter_node)
                    else:
                        result = result + self.dfs(item.to_node, start_value, enter_node)
        return result

    #Method to print 
    def printOVC(self, start_node, vc):
        if len(start_node.edges) is 0:
            return vc
        else:
            leaves = self.dfs(start_node, self.start_value, start_node)
            self.start_value = self.start_value + 1
            s = set(vc)
            for item in leaves:
                for item_edges in item.edges:
                    if item is item_edges.from_node:
                        s.add(item_edges.to_node.value)
                        start_node = self.remove_edges(item, item_edges.to_node, start_node)
                    elif item is item_edges.to_node:
                        s.add(item_edges.from_node.value)
                        start_node = self.remove_edges(item, item_edges.from_node, start_node)
        return self.printOVC(start_node, list(s))

    def remove_edges(self, original_node, node, start_node):

        for edges in node.edges:
            if original_node is edges.to_node or original_node is edges.from_node:
                node.edges.remove(edges)

        for item in node.edges:
            if node is item.from_node:
                if node is start_node:
                    start_node = item.to_node
                self.remove_nextlevel_edges(node, item.to_node)
            elif node is item.to_node:
                if node is start_node:
                    start_node = item.from_node
                self.remove_nextlevel_edges(node, item.from_node)
        node.edges[:] = []
        return start_node

    def remove_nextlevel_edges(self, node, parent_node):
        parent_node_edges = parent_node.edges[:]
        for edges in parent_node_edges:
            if node is edges.to_node:
                parent_node.edges.remove(edges)
            elif node is edges.from_node:
                parent_node.edges.remove(edges)


#Test Data
freeTree = FreeTree()
zero = freeTree.insert_node(0)
one = freeTree.insert_node(1)
two = freeTree.insert_node(2)


freeTree.insert_edge(zero, one)
freeTree.insert_edge(one, two)

#Please change the input by change the number in freeTree.nodes["Enter number between zero to fifteen"]

print('Entry node:' + str(4))
print(freeTree.printOVC(freeTree.nodes[2], []))
