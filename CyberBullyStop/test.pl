% Possible colour conditions
colour(red) :- not not_red.
colour(blue) :- not not_blue.
colour(green) :- not not_green.

% Exclusivity constraints: ensure only one condition holds
not_red :- colour(blue).
not_red :- colour(green).

not_blue :- colour(red).
not_blue :- colour(green).

not_green :- colour(red).
not_green :- colour(blue).

?- colour(X).