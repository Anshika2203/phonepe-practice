class CacheLevel:
    def __init__(self, capacity):
        self.capacity=capacity
        self.data={}
        self.order=[]
    
    def read(self, key):
        if key in self.data:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.data[key]
        return None
    
    def write(self, key, value):
        evicted=None
        if key in self.data:
            self.order.remove(key)
        elif len(self.data) >= self.capacity:
            evicted=self.order.pop(-1)
            del self.data[evicted]
        self.order.insert(0, key)
        self.data[key] = value
        return evicted, self.data[key]
    
    def delete(self, key):
        if key in self.data:
            self.order.remove(key)
            del self.data[key]

class MultiLevelCache:
    def __init__(self, capacities):
        self.levels=[CacheLevel(i) for i in capacities]

    def read(self, key):
        value=None
        for i, level in enumerate(self.levels):
            value=level.read(key)
            if value is not None:
                for j in range(i):
                    self.write(key, value)
                break
        return value
    
    def delete(self, key):
        for level in self.levels:
            level.delete(key)
    
    def write(self, key, value):
        evicted_pair= (key, value)
        for level in self.levels:
            evicted=level.write(evicted_pair[0], evicted_pair[1])
            if evicted[0] is None:
                return
            evicted_pair=evicted
        self.levels.append(CacheLevel(self.levels[-1]).capacity)
        self.levels[-1].write(evicted_pair[0], evicted_pair[1])

    def display(self):
        for i, level in enumerate(self.levels):
            print(f"Level {i+1}: {level.data}")

if __name__=="__main__":
    capacities=[2, 1, 3]
    cache=MultiLevelCache(capacities)
    cache.write("k1", "v1")
    cache.write("k2", "v2")
    cache.write("k3", "v3")
    cache.write("k4", "v4")
    cache.write("k5", "v5")

    print("After writes: ")
    cache.display()

    print("Reading k3")
    cache.read("k3")

    print("after reading k3")
    cache.display()

    cache.delete("k3")
    print("k3 deleted")
    cache.display()