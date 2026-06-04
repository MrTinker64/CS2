% ============================================
% WHO IS GUILTY? - LOGIC PUZZLE 2
% ============================================

/*
1 means guilty, 0 means innocent.
Each person is either guilty (1) or innocent (0).
Clue 1: If Alasdair is innocent, then either Blair or Callum is guilty.
Clue 2: If Blair is guilty, then Dugald is innocent.
Clue 3: If Callum is innocent, then both Ewan and Finlay are guilty.
Clue 4: If Dugald is guilty, then Alasdair is also guilty.
Clue 5: If Ewan is innocent, then Alasdair is guilty.
Clue 6: If Finlay is innocent, then both Blair and Dugald are guilty.
Clue 7: At least one person is guilty.
Clue 8: At most 3 people are guilty.
*/

solve(A, B, C, D, E, F) :- 
    maplist(member,[A,B,C,D,E,F],[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]),
	(A = 0 -> (B = 1 ; C = 1) ; true),
	(B = 1 -> D = 0 ; true),
	(C = 0 -> (E = 1, F = 1) ; true),
	(D = 1 -> A = 1 ; true),
	(E = 0 -> F = 1 ; true),
	(F = 0 -> (B = 1, D = 1) ; true),
	Total is A + B + C + D + E + F,
    Total >= 1,
	Total =< 3.

% Display solution
find_guilty :-
    solve(A, B, C, D, E, F),
    writeln('=== SOLUTION ==='),
    display_person('Alasdair', A),
    display_person('Blair', B),
    display_person('Callum', C),
    display_person('Dugald', D),
    display_person('Ewan', E),
    display_person('Finlay', F),
    nl,
    ( \+ solve(_, _, _, _, _, _) -> 
        writeln('No more solutions.') 
    ; 
        true 
    ).

display_person(Name, 1) :- format('~w is GUILTY~n', [Name]).
display_person(Name, 0) :- format('~w is innocent~n', [Name]).


