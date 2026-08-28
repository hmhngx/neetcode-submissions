class TimeMap:

    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        
        arr = self.key_store[key]
        left, right = 0, len(arr) - 1

        res = ""

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
