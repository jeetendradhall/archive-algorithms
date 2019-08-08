## Introduction

### The problem solving process
(refer ULLDSA section 1.1, 1.2)

#### Modeling a Problem as a Discrete Mathematical Structure

Given a **problem** to be solved, we can **model** _certain aspects_ of the problem by translating it to one or more **discrete mathematical structures** (DMS). E.g. a traffic signal problem can be modeled _using_ a graph structure. A mathematical model can be _represented_ in a programming language by declaring an **abstract data type** (ADT).

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/FromProblems2Instructions.png "From Problems to Machine Instructions")

#### Representing a Discrete Mathematical Structure as an Abstract Data Type

**An ADT is an interface declaration** of the mathematical model it represents. E.g. a 'graph' mathematical structure can be represented in a programming language like Python as a class named Graph with public methods _add_vertex_, _add_edge_, _remove_edge_, etc along with another ADT class named Vertex with public methods _get_neighbors_, _is_neighbor_, _set_property_, etc.

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/Graph_Vertex_ADT.png "Graph and Vertex ADTs")

The discrete mathematical concept of a graph provides numerous operations / methods to be performed on a graph (enumerate edges of a vertex, depth-first search, breadth-first search, etc). From a problem standpoint, we start with thinking of graph as part of the model, and represent it as the Graph and Vertex ADT with relevant public methods only.

Another representation of a set is the ADT priority queue with methods insert and deleteMin. Usually, many ADTs (list, stack, queue, map, dictionary, priority queue, etc) are available in the language library. For the traffic signal problem, the discrete mathematical structure of Graph will be represented by a class (say) CGraph. It will have methods that return the first node getFirst, the next node getNext, mark a node as colored setColor, etc. The client code for this ADT expects its interface to remain unchanged. The underlying implementation may change without impacting the client. The data fields of an ADT are implemeted using data structures and the interface methods are implemented using algorithms.

#### Data Structures of the Processor (Instruction Set) Architecture
A microprocessor implements circuitory to perform certain operations on values stored in its registers and the on-motherboard storage units (RAM). The circuitory interprets a value stored in the register as a data structure of type integer, real, character/string, boolean, or a pointer. There is also circuitory to perform the operations of creation, selection, updation, and deletion of these data structures. The interpretation of type, and the operation to be performed is encoded in an 'opcode', which acts as an operator. The operands are the data structures, provided to the opcode by various addressing schemes, pointer being one of them. A machine instruction bundles together the opcode and its operands. The specification of opcodes, addressing schemes, data structures, etc is called the Instruction Set Architecture (ISA). A programming language exposes the data types of the underlying ISA as **primitive data types**. 

![alt text](https://github.com/jeetendradhall/algorithms/raw/master/DataStructuresProcessorArchitecture.png "Data Structures of the Processor Architecture")

The programming language also provides _data structuring facilities_ to aggregate primitive data fields and form **composite data types**. These data structuring facilities are things like struct, class, array, file, etc.

The instruction set also provides flow-of-control constructs like LOOP, JMP, CALL, etc. A programming language exposes them as flow control constructs like for, while, if, etc and as function call and return.

#### Data Structures and Algorithms

**Data Structures are composite data types**, implementing the data fields (and how data fields are related) an ADT. For the CGraph ADT, we can choose a 2-dimensional array data structure or an adjacency list data structure. The adjacency list is a composition of an array and a set of linked lists. Algorithms are implementation of the methods of an ADT interface. For CGraph, the algorithms implement the getFirst, getNext, etc methods by internally (private state of the CGraph class) keeping track of the first element and the current element of the enumerated nodes of the graph.

Once we have the ADTs implemented (if they were not provided by the language library), an algorithm can make use of the ADTs and solve the problem. For the traffic signal problem, we chose a graph (discrete mathematical) model, represented as a CGraph ADT, and implemented using adjacency-list data structure. We chose a graph because we wanted to solve the problem using the Graph Coloring algorithm.

#### Algorithm Design

Any composition of flow-of-control constructs is an algorithm. The ADT getFirst method implementation is an algorithm, so is the graph coloring method. There are many standard algorithms known in literature, catering to different discrete mathematical structures. E.g. sorting algorithm can be used to permutate a set till it satisfies a '<' (less than) relation. Permutation, Sets, and Relations are discrete mathematical concepts. **All standard algorithms have some underlying algorithm design principles (Greedy, Dynamic Programming, etc)**. The number of such principles are comparitively few. Knowing those design principles help us in understanding standard algorithms, and also enhances our ability to devise our own algorithms.

## References
1. [ULLDSA](https://www.amazon.com/Data-Structures-Algorithms-Alfred-Aho/dp/0201000237/ref=sr11?crid=PED8DJ3UJARO&keywords=data+structures+and+algorithms.+aho%2C+ullman+%26+hopcroft&qid=1563976870&s=gateway&sprefix=ullman+data+structures+%2Caps%2C375&sr=8-1) - Data Structures and Algorithms - Aho, Hopcroft, Ullman
