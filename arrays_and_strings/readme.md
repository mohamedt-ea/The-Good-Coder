## Hash Tables

- ### Objectives:

    1. **What is a hash table?**
        - Hash table is a data structure that maps *keys* to a *values* for higly effecient lookup **O(1)**, same of the array but more memory efficient. 
        - Hash table is like a dictionay or index of a book, have a key to get the value.
        - inorder to get the value just use it's key.
        - Hash means converting a key into a number(index), hasing used in encoding or cryptography. Hash value is a value that has a fixed length and it generated from mathematical formula.
        - Hash values are used because they have fixed length size regardless of the values that were used to generate them. It makes hash values to occupy minimal space compared to other values of varying lengths; **How that?**, *look at how hash table works?*
        
    2. **What are problems that hash table solve?**
        - Hash table solves the problem of fast lookup or how to get an item from storage(list-array-...) instantly O(1) rather than searching for it.

    3. **How Hash Tables work?**
        - We have a value that is related to a unique key, we need to store it somehow in order to get it instantly if we need that value:
            1. Use hash function(converts key(string-integer) to a hash code (int/long))
                -  The purpose of a hash function is to create a key that will be used to reference the value that we want to store.
                ```
                h(k) = k1 % m // example of hash function; k1 is the key m is the length of the indexing list
                ```
            2. store value in the index that have been generated from the hash function.
            3. What if there is more than one hash value with the index? do we replace the last value with new one!
                - No, this is called a collision we can solve it by using [many techniques](https://iq.opengenus.org/different-collision-resolution-techniques-in-hashing/)
                    - Open Hashing (Separate chaining) `-->` simple but common implementation. 
                    - Closed Hashing (Open Addressing)
                        - Liner Probing
                        - Quadratic probing
                        - Double hashing
            4. store vlaues into a chain of cells or nodes of linked list that related to each index, What i mean that each index contains a pointer to the head node of linked list.
            5. Hash tables operations:
                - **Insertion** – this Operation is used to add an element to the hash table.
                - **Searching** – this Operation is used to search for elements in the hash table using the key.
                - **Deleting** – this Operation is used to delete elements from the hash table.

    4. **what is the relationship between hash tables and storage?**
        - I will provide an example:

    5. **How to solve collisions?**
        - store vlaues into a chain of cells or nodes of linked list that related to each index, What i mean that each index contains a pointer to the head node of linked list.

    6. **what are the difference between hash tables and arrays?**
        - arrays are ordered (indexed) and have a contiguous number of cells in the memory. So if you want to extend or shrink the array you have to copy all of its items to another addresses.
        - the main advantage of array is that each element has a fixed address(index) so just provide index you will get the value instantly. So whay we don't use a linked list instead to solve the storage problem?
            - ok you can use linked list to solve storagr problem (extending, shrinking) elemnts, but you need to loop and go over all elemnts to search for the value you need which takes O(N) in the worest case.
            - So **How hash tables solve both of these problems(storage and speed)?**
                - extending a new elemnt to a predefined array costs O(N) time. While using a hash table with a chain list (open addressing) costs only O(1)(properities of linked list).
                - also deleting an element in array makes a usefulless cells (removing pointers), rather than using all un used cell in linked list which costs O(1) for deleting an element.
                - so hash table can easily accommodate a large number of values as long as free space is available.  
                - searching with specific key is fast in array also in hash table if all cells(index) contains just one node(value), in the worest case which all values have the same index it will take O(N).

    7. **What is the difference between dictionaries and hash tables?**
        - Hash tables are a very practical way to maintain a dictionary

    8. **Adavntages and disadvantages of hash tables**.
