## Hashmaps

Hashmaps hold data in a table with a key-value structure.
This makes data easy and quick to access, so long as you have the key.
The hash function is where this data structure gets its name. This function
takes in the key, and determines where to store the data. For this reason, keys
must be unique, as the same key will produce the same output in the hash
function.

Like Linked Lists, the hashmap does not store its data in a contiguous region of
memory, so it can be dynamically resized. The key structure is more efficient
then a linked list, since we don't need to traverse the entire linked list to
get the data we want. Insertion, deletion and lookup are much faster using a
hashtable.
