# 0. Basic dictionary
A class BasicCache that inherits from BaseCaching and is a caching system
This class has two methods:
* put: adds an item to a dictionary
* get: gets an item from a dictionary using the item's key

# 1. FIFO caching
A class FIFOCache that inherits from BaseCaching and is a caching system
This class's put method has an added functionality that implements the FIFO caching
algorithm by discarding the first item on the cache.
