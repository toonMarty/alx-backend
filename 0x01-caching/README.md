# 0. Basic dictionary
A class BasicCache that inherits from BaseCaching and is a caching system
This class has two methods:
* put: adds an item to a dictionary
* get: gets an item from a dictionary using the item's key

# 1. FIFO caching
A class FIFOCache that inherits from BaseCaching and is a caching system
This class's put method has an added functionality that implements the FIFO caching
algorithm by discarding the first item on the cache.

# 2. LIFO caching
A class LIFOCache that inherits from BaseCaching and is a caching system
This class's put method has an added functionality that implements the LIFO caching
algorithm by discarding the first item on the cache.

# 3. LRU Caching
A class LRUCache that inherits from BaseCaching and is a caching system
This class's put method has an added functionality that implements the LRU caching
algorithm by discarding the Least Recently Used item on the cache

# 4. MRU Caching
A class MRUCache that inherits from BaseCaching and is a caching system
This class's put method has an added functionality that implements the MRU caching
algorithm by discarding the Most Recently Used item on the cache
