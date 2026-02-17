class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dict = OrderedDict()
        

    def get(self, key: int) -> int:
        val = self.dict.get(key, -1) 
        if val == -1 : 
            return -1 
        self.dict.move_to_end(key) 
        return val
    

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        self.dict.move_to_end(key) 
        if len(self.dict) > self.capacity : 
            self.dict.popitem(last= False)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)