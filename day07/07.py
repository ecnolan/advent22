class Node:
    def __init__(self, name, value=0, type = None):
        self.name = name
        self.value = value
        self.children = []
        self.parent = None
        self.type = type

    def insertchild(self, node):
        self.children.append(node)
        node.parent = self

    def setparent(self, parent):
        self.parent = parent

    def settype(self, type):
        self.type = type

    def setvalue(self, value):
        self.value = value

    def depthprint(self, depth=0):
        print("  " * depth + '-', self.name, (self.type, self.value))
        for child in self.children:
            child.depthprint(depth + 1)
        return

    def isleaf(self):
        if self.children == []:
            return True
        return False

    def print(self):
        self.depthprint(0)

# ==============================================================================
def enter(name, current):
    newnode = Node(name)
    if current == None:
        return newnode

    current.insertchild(newnode)
    return newnode


def exit(currnode):
    return currnode.parent


def getvalue(line):
    value = line[:line.find(' ')]
    return int(value)


def fillnode(currnode, lines):
    for line in lines:
        if '$' not in line:
            if 'dir' not in line:
                name = line[line.find(' ')+1:-1]
                currnode.insertchild(Node(name, type = 'file', value = getvalue(line)))
        else:
            return
    return


def update_values(node_list):
    for node in node_list:
        if not node.isleaf():
            update_values(node.children)
            for child in node.children:
                node.setvalue(node.value + child.value)

    return


def generate_tree(lines):
    dirname = None
    currnode = None
    root = None
    lineindex = 0
    for line in lines:

        if '$ cd' in line:
            dirname = line[5:-1]
            if dirname == '..':
                currnode = exit(currnode)
            else:
                currnode = enter(dirname, currnode)
                currnode.settype('dir')
                if root == None:
                    root = currnode
        if '$ ls' in line:
            fillnode(currnode, lines[lineindex+1:])
        lineindex += 1

    update_values([root])
    return root


def dir_list(root):
    """ returns list of directory nodes beneath root """
    list = []
    if root.type == 'dir':
        list.append(root)
    for child in root.children:
        if child.type == 'dir':
            list = list + dir_list(child)
    return list


def part2(dir_list, totalspace):
    remaining = (70000000 - totalspace)
    need = 30000000 - remaining

    small_enough = []
    for dir in dir_list:
        if dir.value >= need:
            small_enough.append(dir.value)

    return min(small_enough)


def main():
    with open('07input.txt') as f:
        lines = f.readlines()

    tree = generate_tree(lines)
    directories = dir_list(tree)
    sum = 0
    for dir in directories:
        if dir.value <= 100000:
            sum += dir.value

    print(sum)
    print(part2(directories, tree.value))

if __name__ == '__main__':
    main()
