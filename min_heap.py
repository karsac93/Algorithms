class Node:
    def __init__(self, data, listNo):
        self.data = data
        self.listNo = listNo

class MergeArrays:
    def __init__(self):
        self.heap = []
        self.pos = 0
        self.result = []

    def merge(self, kList):
        k = len(kList)
        list_size = len(kList[0])
        n = k* list_size
        self.heap = [None] * k
        list_counter = []
        for i in range(0, k):
            list_counter.append(0)
        for i in range(0, k):
            if list_counter[i] < list_size:
                self.insert(kList[i][list_counter[i]], i)
            else:
                self.insert(sys.maxsize, i)
        count = 0
        while count < n:
            tempResut = self.extractRoot()
            self.result.append(tempResut.data)
            list_counter[tempResut.listNo] = list_counter[tempResut.listNo] + 1
            if list_counter[tempResut.listNo] < list_size:
                self.insert(kList[tempResut.listNo][list_counter[tempResut.listNo]], tempResut.listNo)
            count = count + 1
        return self.result

    def insert(self, data, listNo):
        if self.pos == 0:
            self.heap[self.pos] = Node(data, listNo)
            self.pos = self.pos + 1
        else:
            self.heap[self.pos] = Node(data, listNo)
            self.pos = self.pos + 1
            self.checkHeapCon()

    def checkHeapCon(self):
        currentPos = self.pos - 1
        while currentPos > 0 and self.heap[currentPos//2].data > self.heap[currentPos].data:
            temp = self.heap[currentPos]
            self.heap[currentPos] = self.heap[currentPos//2]
            self.heap[currentPos // 2] = temp
            currentPos = currentPos//2

    def extractRoot(self):
        root = self.heap[0]
        self.heap[0] = self.heap[self.pos-1]
        self.heap[self.pos-1] = None
        self.pos = self.pos-1
        self.CheckTree(0)
        return root

    def CheckTree(self, k):
        smallest = k
        if 2*k < self.pos and self.heap[smallest].data > self.heap[2*k].data:
            smallest = 2*k
        if 2*k+1 < self.pos and self.heap[smallest].data > self.heap[2*k+1].data:
            smallest = 2*k+1
        if smallest != k:
            node = self.heap[k]
            self.heap[k] = self.heap[smallest]
            self.heap[smallest] = node
            self.CheckTree(smallest)


mergeArrays = MergeArrays()
k = [[1, 2, 3, 4], [7, 8, 9, 10], [5, 6, 11, 12]]
print(mergeArrays.merge(k))
