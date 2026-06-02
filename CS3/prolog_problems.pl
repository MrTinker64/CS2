/*
Problem 1.
Given the following facts of the form father(name1,name2) (name1 is the father of name2), 
complete the rules for the following:   
    (a) sibling(X,Y).       (true if X and Y are siblings)
    (b) cousin(X,Y).        (true if X and Y are cousins)
    (c) grandchild(X,Y).    (true if X is the grandchild of Y).
    (d) descendant(X,Y).    (true if X is the descendant of Y).

    Before testing your predicates, guess the order in which they are generated 
    by your definitions for the queries.

*/ 

father(a,b).    
father(a,c).
father(b,d).
father(b,e).
father(c,f).

sibling(X,Y) :- father(Z,X), father(Z,Y), X \= Y.
cousin(X,Y) :- father(A,X), father(B,Y), sibling(A,B).
grandchild(X,Y) :- father(Y,Z), father(Z,X).
descendant(X,Y) :- father(Y,X).
descendant(X,Y) :- father(Y,Z), descendant(X,Z).

/* 
Problem 2.
Write the a prolog rule to calculate the sum of two numbers: sum(A,B,C) where C is the sum of A and B.

sum(A,B,C) :-    C is A + B.

*/

sum(A,B,C) :- C is A + B.


/*
Problem 3.
Refer to the diagram in the Reader. Solve the crossword puzzle in the diagram on using only 
the words abalone, abandon, anagram, connect, elegant, enhance
*/

/* (a) Enter the information for the other words using the model below.*/

word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).
word(enhance,e,n,h,a,n,c,e).


/* (b) Complete the predicate crosswd  that has 6 inputs, that computes all the 
different ways of filling the grid. 
I have started it for you...

crosswd(V1,V2,V3,H1,H2,H3) :-   word(V1,_,A,_,B,_,C,_),
                                word(H1,_,A,_,D,_,G,_),
                                ...
*/

crosswd(V1,V2,V3,H1,H2,H3) :- word(V1,_,A,_,B,_,C,_),
                                word(H1,_,A,_,D,_,G,_),
                                word(V2,_,D,_,E,_,F,_),
                                word(H2,_,B,_,E,_,H,_),
                                word(V3,_,G,_,H,_,I,_),
                                word(H3,_,C,_,F,_,I,_).


/* 
Problem 4(a).
Use the definition of factorial and the first two facts about Fibonacci numbers below 
to help you write the rules for finding the Nth Fibonacci number. 

        ?- factorial(5, F).
        F = 120

        ?- fib(6,F).
        F = 8.
*/
factorial(0,1).
factorial(N, F) :- 
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.


fib(0,0).
fib(1,1).
fib(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, F1),
    fib(N2, F2),
    F is F1 + F2.


/*
Problem 5.
Define a predicate sumlist(L,N) where L is a list of integers and N 
is the sum of all the elements of L.
            ?- sumlist([1,2,3,4],K).
            K = 10
*/
sumlist([], 0).
sumlist([H|T], N) :-
    sumlist(T, N1),
    N is H + N1.

/*
Problem 6. 
Define a predicate add_up_list(L,K) which, given a list of integers L, 
returns a list of integers in which each element is the sum of all the 
elements in L up to the same position.
        ?- add_up_list([1,2,3,4],K).
        K = [1,3,6,10]

*/

add_up_list(L, K) :- add_up_list(L, 0, K).
add_up_list([], _, []).
add_up_list([H|T], Acc, [S|K]) :-
    S is Acc + H,
    add_up_list(T, S, K).

