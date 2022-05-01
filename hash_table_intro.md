# Hash tables
Hash tables are a list that hold key:value pairs; in Python they are called dictionaries.

[More reading about hash tables](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)  
[YouTube Hash Table intro -13min](https://www.youtube.com/watch?v=KyUTuwz_b7Q)

- Hash tables are more efficient than lists/arrays when looking up an item.  Where searching through a list is 0(n), searching through a sorted list is O(log n), searching through a **hash table is generally O(1) or constant**.  
  - At worse case (very rare, very poorly written hash function), a hash table could have an O(n) time complexity when looking up a value.


- **Hash tables** store their data within an **internal array**, which has indices.  The keys are assigned an index through a hash function.  The hash function (generally) uses a **% expression** to ensure that all of the assigned values are within the available indices (avoid an IndexError this way).
- A **collision** occurs when various key:value pairs are assigned the same index in the internal array.   This can be handled in several ways. Some examples:
  1. store a list of key:value pairs at the index, rather than just one.
  2. If one index is occupied, assign to the next one (i+1); continue this until finding an empty index.
  3. If internal array gets too crowded, it can be re-sized and key:value pairs can be re-assigned. Example: double the size of internal array and re-run a hash function.

