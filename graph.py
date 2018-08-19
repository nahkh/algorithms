class Node:
    def __init__(self, name):
        self.edges = []
        self.name = name

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)

    def __repr__(self):
        return self.name

class Edge:
    def __init__(self, start, end, weight=1):
        self.weight = weight
        self.start = start
        self.end = end
        start.add_edge(self)

    def __repr__(self):
        return '%s %.2f %s' %(self.start, self.weight, self.end);

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_edge(self, start, end, weight=1):
        if start not in self.nodes:
            self.nodes[start] = Node(start)
        if end not in self.nodes:
            self.nodes[end] = Node(end)
        self.edges[(start, end)] = Edge(self.nodes[start], self.nodes[end], weight)
        
    def debug(self):
        for name in self.nodes:
            print(name)
            print(' -> %s' % (', '.join(map(lambda x: '%s (%.2f)' %(x.end.name, x.weight), self.nodes[name].edges))))

    def min_spanning_tree_kruskal(self):
        active_edges = set()
        edge_queue = list(self.edges.values())
        edge_queue.sort(key=lambda x: x.weight)
        regions = {}
        region_count = 0
        for node in self.nodes:
            regions[node] = region_count
            region_count += 1

        def activate_edge(edge):
            active_edges.add((edge.start.name, edge.end.name))
            active_edges.add((edge.end.name, edge.start.name))

        def is_edge_active(edge):
            return (edge.start.name, edge.end.name) in active_edges

        def mark_region(original, new, node):
            frontier = [node]
            while len(frontier) > 0:
                current = frontier.pop()
                regions[current.name] = new
                for current_edge in current.edges:
                    if is_edge_active(current_edge) and regions[current_edge.end.name] == original:
                        frontier.append(current_edge.end)
        i = 0
        while i < len(edge_queue) and region_count > 1:
            edge = edge_queue[i]
            if regions[edge.start.name] != regions[edge.end.name]:
                activate_edge(edge)
                mark_region(regions[edge.end.name], regions[edge.start.name], edge.end)
                region_count -= 1
            i += 1
        new_graph = Graph()
        for edge in self.edges.values():
            if is_edge_active(edge):
                new_graph.add_edge(edge.start.name, edge.end.name, edge.weight)
            else:
                print('Discarding edge %s' % edge)
        return new_graph

def read_graph(filename):
    g = Graph()
    directed = False
    with open(filename) as f:
        for line in iter(f.readline, ''):
            if line == 'directed\n':
                directed = True
                continue
            ends = line.split(' ')
            start = ends[0].strip().upper()
            end = ends[1].strip().upper()
            weight = 1 if len(ends) <= 2 else float(ends[2])
                
            g.add_edge(start, end, weight=weight)
            if not directed:
                g.add_edge(end, start, weight=weight)
            
            
    return g


if __name__=='__main__':
    g = read_graph('graph.txt')
    g.debug()
    print('-'*50)
    g.min_spanning_tree_kruskal().debug()


