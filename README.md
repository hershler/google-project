
# google-project-hershler (by ADVA program & Elevation bootcamp)
sentences auto-complete

<img width="376" alt="GUI_demo" src="https://user-images.githubusercontent.com/57594477/92389249-6b062100-f121-11ea-8c17-7378a182b931.PNG">

## description:
Flow: The user types in part of sentence he's in search for, the program recievs the partial sentence that was typed and returns 5 of the best options for completion.

In order to provide a good user experience the program works in two phases: offline and online, so in offline phase we will do everything possible to make the online stage highly efficient.

### offline
We run offline a program that will store all sentences in a Hash-table (dictionary) and parse all the possible substrings of all sentences into a Trie which every node has a list of IDs of the best sentences to complete.
time-complexity: O(n^3)

### online
We recive online a substring to be completed, and search for completion's IDs in the trie (in the last node of the substring), then we access the dictionary to get the full sentences, in case of list less than 5, we search for more completions with one character wrong (miss, add or replace).
time complexity: O(1) at best and average, and anyway not more than input length - if it's long the efficency is not so important.

### implementation
I implemented the program with python3, using data structures like python dict and self-implemented trie.
In addition I provided a simple GUI using TKinter.

-----
thanks to ADVA and Elevation team and all google mentors!.
