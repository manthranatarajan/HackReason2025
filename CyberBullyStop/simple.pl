father(adam,bill).
father(adam,brian).
father(bill,charlie).
mother(alice, bill).
mother(alice, brian).
mother(briana, charlie).


parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).

% s(CASP)/ASP
has_sibling(X) :- parent(P,X), parent(P,Y), X \= Y.
only_child(X) :- parent(P,X), not has_sibling(X).

?- has_sibling(A).