guilty :- true.    % guilty is true
innocent :- false. % innocent is false

/*
Remember that ; is OR and , is AND, The -> ; combination is if then else.

*/
solve(A,B,C,D,E) :-
    
    %Rule 1: Each individual is either guilty or innocent.
 	maplist(member,[A,B,C,D,E],[[guilty,innocent],[guilty,innocent],[guilty,innocent],[guilty,innocent],[guilty,innocent]]),
 	/*
 	You can also write this rule as follows:
 	member(A, [guilty,innocent]),
    member(B, [guilty,innocent]),
    member(C, [guilty,innocent]),
    member(D, [guilty,innocent]),
    member(E, [guilty,innocent]),
 	*/
 	
 	% Rule 2: At least one is guilty.
    (A = guilty; B = guilty ; C = guilty ; D = guilty ; E = guilty),
    
    
    % Rule 3: If Atherol is guilty and Daghard is innocent, then Barnaby is guilty.
    ((A = guilty, D = innocent) -> B = guilty ; true), 
    
    % Rule 4: If Atherol is innocent, then Eadwulf is innocent.
    (A = guilty -> E = innocent ; true),
	
	% Rule 5: If Daghard is guilty then Eadwulf is guilty.
    (D = guilty -> E = guilty ; true),
    
    % Rule 6: Atherol and Daghard are not both guilty.
    not(A = guilty), not(D = guilty),
    
    % Rule 7: Unless Daghard is guilty, Barnaby is innocent.
    (D = guilty -> true ; B = innocent),
    
    
    true.
/*
The following code is to display the solutions(s). 
format allows you format text. ~n means new line. ~w will display the next item from the
list of arguments after the , and prints it. Here, each format has only one ~w hence only 
one item in the list ([A] or [B] or ...).

*/
find_guilty :-
	solve(A,B,C,D,E),
	writeln('=== SOLUTION ==='),
	format('Atherol is ~w ~n',[A]),
	format('Barnaby is ~w ~n',[B]),
	format('Celandine is ~w ~n',[C]),
	format('Daghard is ~w ~n',[D]),
	format('Eadwulf is ~w ~n',[E]),
    true.
