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

    def add_node(self, node : Node):
        self._nodes.append(node)

    def add_arc(self, from_node: Node, to_node: Node, distance: int):
        self._arcs.append(Arc(from_node, to_node, distance))

    def incoming_arcs(self, v : Node):
        inacrs = []
        for a in self._arcs:
            if a.get_to_node() == v:
                inacrs.append(a)
        return inacrs
    
    def SP(self, s : Node, v : Node) -> int:
        min = None
        for a in self.incoming_arcs(v):
            length = a.get_distance() + self.SP(s, a.get_from_node())
            if min is None or length <= min:
                min = length
        
        return 0 if min is None else min
    
d  = DAG()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

d.add_node(n1)
d.add_node(n2)
d.add_node(n2)

d.add_arc(n1, n2, 3)
d.add_arc(n1, n3, 10)
d.add_arc(n2, n3, 5)

print(d.SP(n1,n3))