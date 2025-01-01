class CacheEntry:
    def __init__(self, value: str):
        self.value = value
        self.frequency = 1

class MultiLevelCache:
    def __init__(self, max_levels: int, level_capacities: list[int]):
        self.max_levels = max_levels
        self.capacities = level_capacities
        self.levels = [{}] 

    def read(self, key: str) -> str:
        for level_idx, level in enumerate(self.levels):
            if key in level:
                value = level[key].value
                level[key].frequency += 1
                
                if level_idx > 0:
                    self._write_to_level(0, key, value)
                    del level[key]
                
                return value
        return None
    
    def write(self, key: str, value: str) -> None:
        self._write_to_level(0, key, value)
    
    def _write_to_level(self, level_idx: int, key: str, value: str) -> None:
        while level_idx >= len(self.levels) and len(self.levels) < self.max_levels:
            self.levels.append({})
            
        if level_idx >= len(self.levels):
            return 
            
        current_level = self.levels[level_idx]
        
        if key in current_level:
            current_level[key].value = value
            current_level[key].frequency += 1
            return
            
        if len(current_level) >= self.capacities[level_idx]:
            lfu_key = min(current_level.items(), 
                         key=lambda x: x[1].frequency)[0]
            evicted_value = current_level[lfu_key].value
            del current_level[lfu_key]
            
            self._write_to_level(level_idx + 1, lfu_key, evicted_value)
            
        current_level[key] = CacheEntry(value)
    
    def delete(self, key: str) -> None:
        for level in self.levels:
            if key in level:
                del level[key]

    def display(self, operation: str = "") -> None:
        print(f"\n=== After {operation} ===")
        for i, level in enumerate(self.levels):
            print(f"L{i+1}: ", end="")
            if not level:
                print("Empty")
            else:
                entries = [f"{k}:[v={v.value},f={v.frequency}]" for k, v in level.items()]
                print(", ".join(entries))
        print("=" * 30)
        

if __name__ == "__main__":
    cache = MultiLevelCache(3, [2, 3, 4])
    cache.write("k1", "v1")
    cache.write("k2", "v2")
    cache.write("k3", "v3")
    print(cache.read("k1"))
    cache.delete("k2")
    print(cache.read("k2"))
    cache.display()