## Introduction

### The problem solving process
(refer ULLDSA section 1.1, 1.2)

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/FromProblems2Instructions.png "From Problems to Machine Instructions")

#### Modeling a Problem as a Discrete Mathematical Structure

Given a **problem** to be solved, we can **model** _certain aspects_ of the problem by translating it to one or more **discrete mathematical structures** (DMS). E.g. a traffic signal problem can be modeled _using_ a graph structure.

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/Intersection.png "Road intersection near JoJo's bar near Princeton University, NJ, USA")

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/Graph_Model.png "graph model of the problem")

#### Representing a Discrete Mathematical Structure as an Abstract Data Type

A mathematical model can be _represented_ in a programming language by declaring an **abstract data type** (ADT).

**An ADT is an interface declaration** of the mathematical model it represents. E.g. a 'graph' mathematical structure can be represented in a programming language like Python as a class named Graph with public methods _add_vertex_, _add_edge_, _remove_edge_, etc along with another ADT class named Vertex with public methods _get_neighbors_, _is_neighbor_, _set_property_, etc.

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/Graph_Vertex_ADT.png "Graph and Vertex ADTs")

The discrete mathematical concept of a graph provides numerous operations / methods to be performed on a graph (enumerate edges of a vertex, depth-first search, breadth-first search, etc). From a problem standpoint, we start with thinking of graph as part of the model, and represent it as the Graph and Vertex ADT with relevant public methods only. The interface for these ADTs remain unchanged, so that programs (client code) can be written assuming this interface / contract. The underlying implementation may change without impacting the client. The data fields of an ADT are implemeted using _data structures_ and the interface methods are implemented using _algorithms_ operating on those data structures.

Another example of modeling is the Knapsack problem, where a set of commodities are given and we have to choose commodities such that their vale is maximized, subject to a maximum weight constraint on the chosen commodities. The modeling involves the discrete mathematical structure of a set. The representation of the set is the ADT priority queue with methods insert and deleteMin. Usually, many ADTs (list, stack, queue, map, dictionary, priority queue, etc) are available in the language library. 

#### Data Structures and Algorithms of the Processor (Instruction Set) Architecture
A microprocessor implements circuitory to perform certain operations on values stored in its registers and the on-motherboard storage units (RAM). The circuitory interprets a value stored in the register as a data structure of type integer, real, character/string, boolean, or a pointer. There is also circuitory to perform the operations of creation, selection, updation, and deletion of these data structures. The interpretation of type, and the operation to be performed is encoded in an 'opcode', which acts as an operator. The operands are the data structures, provided to the opcode by various addressing schemes, pointer being one of them. A machine instruction bundles together the opcode and its operands. The specification of opcodes, addressing schemes, data structures, etc is called the Instruction Set Architecture (ISA). A programming language exposes the data types of the underlying ISA as **primitive data types**. 

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/DataStructuresProcessorArchitecture.png "Data Structures of the Processor Architecture")

The programming language also provides _data structuring facilities_ to aggregate primitive data fields and form **composite data types**. These data structuring facilities are things like struct, class, array, file, etc.

The instruction set also provides flow-of-control constructs like LOOP, JMP, CALL, etc. A programming language exposes them as flow control constructs like for, while, if, etc and as function call and return.

#### Data Structures and Algorithms of the Abstract Data Types

The data fields and methods of ADTs are implemented using the data structuring facilities and flow-of-control constructs provided by the programming language. For the Graph ADT, we can choose a 2-dimensional array data structure or an adjacency list data structure. The adjacency list is a composition of an array with each element being a linked list. It may as well be a map of vertex_id to Vertex ADT, with Vertex ADT having a map of neighbors mapping neighbor vertex name to the weight of the edge. So, we may have nested ADTs that are eventually implemented using data structures like arrays, linked lists, trees, hash tables, etc.

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/DMS-ADT-DS.png "Discrete Mathematical Structures, Abstract Data Types, and Data Structures")

Many ADTs and their implementation are provided by the language library. For the ADTs that are not provided, we need to declare and implement it. Once we have the ADTs implemented, an algorithm can make use of the ADTs and solve the problem. For the traffic signal problem, we chose a graph (discrete mathematical) model, represented as a Graph ADT, and implemented using adjacency-list data structure. We chose a graph because we wanted to solve the problem using the _Graph Coloring_ algorithm.

These problem solving algorithms (they are different from the ADT method algorithms that only serve the structural and navigational needs of an ADT) are huge in number, but there is a set of underlying patterns they follow. The number of those patterns are less and can be understood. A catalog of those patterns comes under the purview of _Algorithm Design_.

#### Algorithm Design

Any composition of flow-of-control constructs is an algorithm. The ADT getFirst method implementation is an algorithm, so is the graph coloring method. There are many standard algorithms known in literature, catering to different discrete mathematical structures. E.g. sorting algorithm can be used to permutate a set till it satisfies a '<' (less than) relation. Permutation, Sets, and Relations are discrete mathematical concepts. **All standard algorithms have some underlying algorithm design principles (Greedy, Dynamic Programming, etc)**. The number of such principles are comparitively few. Knowing those design principles help us in understanding standard algorithms, and also enhances our ability to devise our own algorithms.

## References
1. [ULLDSA](https://www.amazon.com/Data-Structures-Algorithms-Alfred-Aho/dp/0201000237/ref=sr11?crid=PED8DJ3UJARO&keywords=data+structures+and+algorithms.+aho%2C+ullman+%26+hopcroft&qid=1563976870&s=gateway&sprefix=ullman+data+structures+%2Caps%2C375&sr=8-1) - Data Structures and Algorithms - Aho, Hopcroft, Ullman
