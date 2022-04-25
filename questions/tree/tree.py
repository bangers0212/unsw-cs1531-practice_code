
def width(node):
    label, children = node
    w = sum(width(child) for child in children)
    return max(w, 2 + len(label))


def height(node):
    label, children = node
    return 1 + max((height(child) for child in children), default=0)


def _draw(grid, node, x=0, y=0):
    label, children = node
    w = width(node)
    grid[y][x:x+w] = '[' + label + '_'*(w - len(label) - 2) + ']'
    new_x = x
    for child in children:
        new_x = _draw(grid, child, new_x, y + 1)
    return max(x + w, new_x)


def draw(tree):
    w, h = width(tree), height(tree)
    grid = [['.']*w for _ in range(h)]
    _draw(grid, tree)
    return '\n'.join(''.join(row) for row in grid)
