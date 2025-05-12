
class Node:
    def __init__(self, code: str) -> None:
        self._code = code
    
    def get_code(self):
        return self._code
        
class Arc:
    def __init__(self, from_node: Node, to_node: Node, distance: int) -> None:
        self._from_node = from_node
        self._to_node = to_node
        self._distance = distance

    def get_from_node(self):
        return self._from_node
    
    def get_to_node(self):
        return self._to_node
    
    def get_distance(self):
        return self._distance


class DAG:
    def __init__(self) -> None:
         self._nodes = []
         self._arcs = []

    def add_node(self, node : Node ):
        self._nodes.append(node)

    def add_arc(self, from_node : Node, to_node : Node, distance : int):
        self._arcs.append(Arc(from_node, to_node, distance))

    def incomming_arcs(self, v: Node):
        # Discuss performance

        inarcs = []
        for a in self._arcs:
            if (a.get_to_node() == v):
                inarcs.append(a)
        return inarcs

    def SP(self, s : Node, v: Node) -> int:
        # Discuss performance

        min = None
        for a in self.incomming_arcs(v):
            length = a.get_distance() + self.SP(s, a.get_from_node())
            if (min is None or length < min):
                min = length

        if (min is None):
            return 0

        return min
    

d = DAG()

n1 = Node(1)
n2 = Node(2)         
n3 = Node(3)

d.add_node(n1)
d.add_node(n2)
d.add_node(n3)

d.add_arc(n1,n2,3)
d.add_arc(n1,n3,10)
d.add_arc(n2,n3,5)

print (d.SP(n1,n3))






