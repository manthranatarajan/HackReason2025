%Facts
food(salad).
junkfood(pizza).
junkfood(burger).
food(pasta).
drink(water).
fundrink(cola).

%Rules
healthy(X) :- food(X) ; drink(X).
unhealthy(X) :- junkfood(X) ; fundrink(X).


