class Node:
    def __init__(self):
        self.value = None
        self.parent = None
        self.left = None
        self.right = None
        self.descendents = 0

    def shift_up(self):
        value_to_return = self.value
        if self.descendents == 1:
            self.value = None
            self.left = None
            self.right = None
            self.descendents = 0
            ancestor = self.parent
            while ancestor != None:
                ancestor.descendents -= 1
                ancestor = ancestor.parent
        else:
            if self.left_is_smaller():
                self.value = self.left.value
                self.left.shift_up()
            else:
                self.value = self.right.value
                self.right.shift_up()
            
        return value_to_return

    def left_is_smaller(self):
        if self.right.value == None:
            return True
        if self.left.value == None:
            return False
        return self.left.value < self.right.value

    def shift_down(self, value):
        if self.value == None:
            self.value = value
            self.descendents = 1
            self.left = Node()
            self.left.parent = self
            self.right = Node()
            self.right.parent = self
            
            ancestor = self.parent
            while ancestor != None:
                ancestor.descendents += 1
                ancestor = ancestor.parent
            return
        if self.value > value:
            self.value, value = value, self.value

        if self.left.descendents < self.right.descendents:
            self.left.shift_down(value)
        else:
            self.right.shift_down(value)

    def debug(self, depth=0):
        if self.value == None:
            return
        current = self
        line = []
        branches = []
        branch_depth = depth
        while current.value != None:
             line.append('%s(%i)' % (str(current.value), current.descendents))
             if current.left.value != None:
                 branches.append({
                     'node': current.left,
                     'depth': branch_depth,
                 })
             branch_depth += 1
             current = current.right
        print('\t'*depth + ' ->\t'.join(line))
        for branch in reversed(branches):
            print('\t'*branch['depth'] + '|')
            print('\t'*branch['depth'] + 'V')
            branch['node'].debug(branch['depth'])

class MinHeap:
    def __init__(self):
        self.root = Node()

    def push(self, value):
        self.root.shift_down(value)

    def pop(self):
        return self.root.shift_up()

    def debug(self):
        self.root.debug()
        

def heapsort(arr, in_place=False):
    heap = MinHeap()
    for value in arr:
        heap.push(value)
    if in_place:
        for i in range(len(arr)):
            arr[i] = heap.pop()
        return arr
    else:
        result = []
        for i in range(len(arr)):
            result.append(heap.pop())
        return result


if __name__=='__main__':
    print(heap_sort('HEAPSORT'))
