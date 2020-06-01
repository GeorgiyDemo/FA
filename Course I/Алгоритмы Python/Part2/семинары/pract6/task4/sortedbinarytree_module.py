
def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    """Красивое дерево"""
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
    else:
        node_repr = str(root.value)

    new_root_width = gap_size = len(node_repr)

    
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left_child, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right_child, 2 * curr_index + 2, index, delimiter)


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

class SortedTreeNode:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_root_val(self, obj):
        """Выставление значения"""
        self.value = obj

    def get_root_val(self):
        """Получение значения"""
        return self.value

    def get_right_child(self):
        """Получение подэлемента справа"""
        return self.right_child

    def get_left_child(self):
        """Получение подэлемента слева"""
        return self.left_child

    def compare(self, new_value):
        """Сравнение значений"""
       
        if new_value >= self.value:
            if self.right_child:
                self.right_child.compare(new_value)
            else:
                
                self.right_child = SortedTreeNode(new_value)

        if new_value < self.value:
           
            if self.left_child:
                self.left_child.compare(new_value)
            else:
              
                self.left_child = SortedTreeNode(new_value)

    def sort(self):
        """Сортировка данных"""
        if self.left_child:
            self.left_child = self.left_child.sort()
        else:
          
            self.left_child = []

     
        if self.right_child:
            self.right_child = self.right_child.sort()
        else:

            self.right_child = []


        return self.left_child + [self.value] + self.right_child

    def __str__(self):
        """Вывод структуры на экран"""
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))


    
class SortedTree:

    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root:
            self.root.compare(value)
        else:
            self.root = SortedTreeNode(value)

    def merge(self):
        return self.root.sort()

    def __str__(self):
        return self.root.__str__()