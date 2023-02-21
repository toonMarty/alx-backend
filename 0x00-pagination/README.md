# 0. Simple helper function
A function named index_range that takes two integer arguments page and page_size.
The function returns a tuple of size two containing a start index and an end
index corresponding to the range of indexes to return in a list for those particular pagination parameters.

# 1. Simple pagination
A method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

# 2. Hypermedia pagination
A get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

* page_size: the length of the returned dataset page
* page: the current page number
* data: the dataset page (equivalent to return from previous task)
* next_page: number of the next page, None if no next page
* prev_page: number of the previous page, None if no previous page
* total_pages: the total number of pages in the dataset as an integer

# 3. Deletion-resilient hypermedia pagination
A method that is deletion-resilient
