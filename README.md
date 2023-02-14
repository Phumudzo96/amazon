# amazon

Write code to read the content of the text ﬁle input.txt.

For each line in input.txt, write a new line in the new text ﬁle output.txt
that computes the answer to some operation on a list of numbers.

If the input.txt has the following:

     o Min: 1,2,3,5,6

     o Max: 1,2,3,5,6

     o Avg: 1,2,3,5,6

Your program should generate output.txt as follows:

     o The min of [1, 2, 3, 5, 6] is 1.

     o The max of [1, 2, 3, 5, 6] is 6.

     o The avg of [1, 2, 3, 5, 6] is 3.4.
     
Assume that the only operations given in the input ﬁle are min, max and
avg, and that the operation is always followed by a list of
comma-separated integers.

You should deﬁne the functions min, max and avg that take in a list of
integers and return the min, max or avg of the list.

Your program should handle any combination of operations and any
length of input numbers.

You can assume that the list of input numbers are always valid integers
and that the list is never empty.

Hint: there is something strange about the ﬁrst line of input.txt...
