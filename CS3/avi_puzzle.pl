% ============================================
% WHO STOLE THE PAINTING? - LOGIC PUZZLE 2
% ============================================

/*
1 means guilty, 0 means innocent.
Each person is either guilty (1) or innocent (0).
Clue 1: If Haruki is guilty, then both Ingrid and Katya are innocent.
Clue 2: If Ingrid is innocent, then Jasper is guilty.
Clue 3: If Jasper is guilty, then Liam is innocent.
Clue 4: If Katya is guilty, then Mira is innocent.
Clue 5: If Liam is innocent, then either Haruki or Mira is guilty.
Clue 6: If Mira is guilty, then Ingrid is guilty.
Clue 7: If Liam is guilty, then Jasper is guilty.
Clue 8: Exactly 3 people are guilty.
*/

solve(H, I, J, K, L, M) :-
    maplist(member,[H,I,J,K,L,M],[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]),
	(H = 1 -> (I = 0, K = 0) ; true),
	(I = 0 -> J = 1 ; true),
	(J = 1 -> L = 0 ; true),
	(K = 1 -> M = 0 ; true),
	(L = 0 -> (H = 1 ; M = 1) ; true),
	(M = 1 -> I = 1 ; true),
	(L = 1 -> J = 1 ; true),
	Total is H + I + J + K + L + M,
    Total =:= 3.

% Display solution
find_guilty :-
    solve(H, I, J, K, L, M),
    writeln('=== SOLUTION ==='),
    display_person('Haruki', H),
    display_person('Ingrid', I),
    display_person('Jasper', J),
    display_person('Katya', K),
    display_person('Liam', L),
    display_person('Mira', M),
    nl,
    ( \+ solve(_, _, _, _, _, _) ->
        writeln('No more solutions.')
    ;
        true
    ).

display_person(Name, 1) :- format('~w is GUILTY~n', [Name]).
display_person(Name, 0) :- format('~w is innocent~n', [Name]).
