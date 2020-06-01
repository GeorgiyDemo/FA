
class BinaryTree:
    """Класс бинарного дерева"""

    def __init__(self, root=None, parent=None):
        self.key = root
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node=None):
        """Вставка элемента слева"""

        if self.left_child == None:
            self.left_child = BinaryTree(new_node, self)
        else:
            t = BinaryTree(new_node, self)
            t.left_child = self.left_child
            self.left_child = t

        return self.left_child

    def insert_right(self, new_node=None):
        """Вставка элемента справа"""

        if self.right_child == None:
            self.right_child = BinaryTree(new_node, self)
        else:
            t = BinaryTree(new_node, self)
            t.right_child = self.right_child
            self.right_child = t

        return self.right_child

    def get_parent(self):
        """Получение узла-родителя"""

        return self.parent

    def get_right_child(self):
        """Получение подэлемента справа"""

        return self.right_child

    def get_left_child(self):
        """Получение подэлемента слева"""

        return self.left_child

    def set_root_val(self, obj):
        """Выставление значения"""

        self.key = obj

    def get_root_val(self):
        """Получение значения"""

        return self.key

    def tree_string(self, root, curr_index, index=False, delimiter='-'):
        """Красивое дерево"""

        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.key)
        else:
            node_repr = str(root.key)

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = \
            self.tree_string(root.left_child, 2 *
                             curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            self.tree_string(root.right_child, 2 *
                             curr_index + 2, index, delimiter)

        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end

    def __str__(self):
        """Вывод структуры на экран"""

        lines = self.tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))
