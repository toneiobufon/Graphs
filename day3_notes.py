import string
​
words = set()
​
with open("words.txt") as f:
    for word in f:
        words.add(word.lower().strip())
​
class Queue():
    def __init__(self):
        self.queue = []
​
    def enqueue(self, value):
        self.queue.append(value)
​
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
​
    def size(self):
        return len(self.queue)
​
cache = {}
​
def get_neighbors(word):
    if word not in cache:
        neighbors = []
​
        # O(26680*n) == O(n)
        for w in words: # O(26680)
            if len(w) != len(word):
                continue
​
            diffs = 0
​
            for i in range(len(w)): # O(n) over the length of the word
                if w[i] != word[i]:
                    diffs += 1
​
            if diffs == 1:
                neighbors.append(w)
​
            cache[word] = neighbors
​
    return cache[word]
​
def get_neighbors_2(word):     # word = "sail"
    word_letters = list(word)  # word_letters = ['s', 'a', 'i', 'l']
​
    neighbors = []
​
    # O(26*n) == O(n)
    for i in range(len(word)):  # i from 0 to 3   O(n) over the length of the word
        for l in string.ascii_lowercase:  # l from a...z  O(26)
            candidate_letters = list(word_letters) # make a copy of word_letters = ['s', 'a', 'i', 'l']
            candidate_letters[i] = l  # ['s', 'a', 'i', 'l'] -> ['a', 'a', 'i', 'l']
            candidate = "".join(candidate_letters)  # ['a', 'a', 'i', 'l'] -> "aail"
​
            if candidate != word and candidate in words:  # is "aail" in the dictionary?
                neighbors.append(candidate)
​
    return neighbors
​
def bfs(begin_word, end_word):
    visited = set()
    q = Queue()
​
    q.enqueue([begin_word])
​
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
​
        if v not in visited:
            visited.add(v)
​
            if v == end_word:
                return path
​
            for neighbor in get_neighbors_2(v):
                q.enqueue(path + [neighbor])  # Makes a new list
                #path_copy = list(path)
                #path_copy.append(neighbor)
                #q.enqueue(path_copy)
​
print(bfs("sail", "boat"))




#############################################################



Using Graphs to Solve Problems
------------------------------
1. Translate the problem into graph terminology
2. Build the graph from the problem data
3. Traverse/Search or whatever combination you need
Word Ladders Problem
--------------------
Given two words (begin_word and end_word), and a dictionary's word list, return
the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not
a transformed word.  Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
For there to be a path, begin_word and end_word must be the same length.
If there are multiple equal-length paths, choose any of them.
sail -> bail
sail -> bail -> boil -> boll -> bolt -> boat
Option A: Try every letter combination in the word, checking to see if
the result is in the dictionary.
Option B: Look through all the words in the dictionary, finding those that
only differ by one letter.
sail
aail
bail <<
cail
dail
eail
fail <<
gail <<
zail
sbil


#####################################################


image_str = [
    '##########################',
    '#                        #',
    '#        #######         #',
    '#      ##       #        #',
    '#       #####   #        #',
    '#            #  #        #',
    '#       #####   #        #',
    '#      #        #        #',
    '#      #        #        #',
    '#       #########        #',
    '#                        #',
    '##########################'
]
​
# Convert from strings to lists
image = []
for s in image_str:
    image.append(list(s))
​
def print_image():
    for i in image:
        print("".join(i))
​
def floodfill(row, col, char):
    # if the pixel at row, col is not a space: return
    if image[row][col] != ' ':
        return
​
    # set the character at this "pixel" to char
    image[row][col] = char
​
    # floodfill neighbors
    floodfill(row-1, col, char)
    floodfill(row+1, col, char)
    floodfill(row, col-1, char)
    floodfill(row, col+1, char)
​
floodfill(7, 14, 'x')
floodfill(7, 3, '.')
​
print_image()
