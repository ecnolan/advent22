class Node:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.children = []
        self.parent = None

    def insertchild(self, node):
        self.children.append(node)
        node.parent = self

    def setparent(self):
        self.parent = parent

    def depthprint(self, depth=0):
        print("  " * depth + '-', self.name)
        for child in self.children:
            child.depthprint(depth + 1)
        return

    def print(self):
        self.depthprint(0)

# ==============================================================================

def generate_tree(lines):
    dirname = None
    currnode = None
    for line in lines:
        if '$ cd' in line:
            dirname = line[5:-1]
            print([dirname])
            if dirname == '..':
                currnode = currnode.parent
            else:
                currnode.insertchild(Node(dirname))



    p = Node('/')
    p.insertchild(Node('a'))
    # children = p.children()
    print(p.children)
    p.insertchild(Node('b'))
    print(p.children)

    print(p)
    print(p.children[1].parent)

    # print(p)
    # p.insertchild(Node('c'))
    # Node('a').depthprint(0)
    p.print()


def main():
    # with open('05test.txt') as f:
    with open('07input.txt') as f:
        lines = f.readlines()

    generate_tree(lines)

if __name__ == '__main__':
    main()
