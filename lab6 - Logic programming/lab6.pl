% -- Facts:--
date(2019).

man(marcus).
man(jaan).
man(francesco).

born(marcus, 40).
born(jaan, 1977).
born(francesco, 1989).

lives(marcus, pompeii).
lives(francesco, pompeii).

% -- Predicates:--
mortal(Person) :-
    man(Person).

death_from_old_age(Person) :-
    mortal(Person),
    born(Person, Year),
    date(Today),
    Year+150<Today.

death_from_volcanic_eruption(Person) :-
    mortal(Person),
    born(Person, Year),
    lives(Person, pompeii),
    Year<79.

deceased(Person) :-
    (   death_from_old_age(Person)
    ;   death_from_volcanic_eruption(Person)
    ).

alive(Person) :-
    mortal(Person),
    \+ deceased(Person).


% -- Queries:--

% alive(marcus). // false
% alive(jaan).  // true
% alive(francesco).  // true