## Introduction

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/FromProblems2Instructions.png "From Problems to Machine Instructions")

### The problem solving process
(refer ULLDSA section 1.1, 1.2)
Given a problem to be solved, we can formalize (model) **certain aspects** of the problem by translating it to one or more discrete mathematical structures. E.g. a **traffic signal** problem can be modeled **using** a graph structure and an accompanying **graph coloring algorithm**, both from graph theory which is one of the topics under discrete mathematics. A mathematical model can be **represented** in a programming language by defining **abstract data types** (ADT).

An ADT is a non-primitive data type. It is a _declaration_ of the interface of the mathematical model it represents. E.g. a discrete mathematical concept of a SET can be represented in a programming language like C++ as a class with a name (say) _CDictionary_ and public methods _insert_, _delete_, and _isMember_. Here, the discrete mathematical concept of set is being used as a _dictionary_ ADT. From a problem standpoint, we may have started with thinking of dictionary as part of the model. But, it helps to keep in mind that dictionary is not a discrete mathematical structure (set is). Another representation of a set is the ADT _priority queue_ with methods _insert_ and _deleteMin_. Usually, many ADTs (list, stack, queue, map, dictionary, priority queue, etc) are available in the language library. For the traffic signal problem, the discrete mathematical structure of Graph will be represented by a class (say) _CGraph_. It will have methods that return the first node _getFirst_, the next node _getNext_, mark a node as colored _setColor_, etc. The client code for this ADT expects its interface to remain unchanged. The underlying implementation may change without impacting the client. The _data fields_ of an ADT are **implemeted** using **data structures** and the _interface methods_ are **implemented** using **algorithms**.

There are some data types like integer, float, character, string, pointer, etc that are provided directly as part of the **instruction set** of the underlying **computer architecture**. A programming language exposes them as **primitive data types**. The programming language also provides **data structuring facilities** to aggregate primitive data fields and form _composite data types_. These data structuring facilities are things like _struct_, _class_, _array_, etc. The _pointer_ type in C++ is exposed by usage of symbols like '*' and '&'.

The instruction set also provides flow-of-control constructs like LOOP, JMP, CALL, etc. A programming language exposes them as flow control constructs like for, while, if, etc and as function call and return.

A programming language bridges the gap between low-level instruction set constructs and high level mathematical model constructs and programming paradigms, both of which help model a problem.

**Data Structures** are composite data types, implementing the data fields (and how data fields are related) an ADT. For the CGraph ADT, we can choose a _2-dimensional array_ data structure or an _adjacency list_ data structure. The adjacency list is a composition of an array and a set of linked lists. **Algorithms** are implementation of the methods of an ADT interface. For CGraph, the algorithms implement the getFirst, getNext, etc methods by internally (private state of the CGraph class) keeping track of the first element and the current element of the enumerated nodes of the graph.

Once we have the ADTs implemented (if they were not provided by the language library), an algorithm can make use of the ADTs and solve the problem. For the traffic signal problem, we chose a graph (discrete mathematical) model, represented as a CGraph ADT, and implemented using adjacency-list data structure. We chose a graph because we wanted to solve the problem using the **Graph Coloring algorithm**.

_Any composition of flow-of-control constructs is an algorithm_. The ADT getFirst method implementation is an algorithm, so is the graph coloring method. There are many standard algorithms known in literature, catering to different discrete mathematical structures. E.g. _sorting_ algorithm can be used to _permutate_ a _set_ till it satisfies a '<' (less than) _relation_. Permutation, Sets, and Relations are discrete mathematical concepts. All standard algorithms have some underlying **algorithm design** principles (Greedy, Dynamic Programming, etc). The number of such principles are comparitively few. Knowing those design principles helps us in understanding standard algorithms, and also enhances our ability to devise our own algorithms.

## References
1. ULLDSA - Data Structures and Algorithms - Aho, Hopcroft, Ullman


Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a 
* **lightweight** 
	* and easy-to-use syntax for styling your writing.
* It includes conventions for

![Algo Design](https://github.com/jeetendradhall/algorithms/raw/master/heuristic.png "Algorithm Designs")

v4

Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

```markdown
#read data
df_data = pd.read_csv ('./datasets/boston-housing.csv')
#train and test data separation
msk = np.random.rand(len(df_data)) < 0.9
df = df_data[msk]
df_test = df_data[~msk]
df.head (2)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/jeetendradhall/algorithms/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
