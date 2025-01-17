
contains_offensive_language(yes).
targets_individual(yes).
repeats_negative_phrases(no).
mentions_private_info(yes).
message_length(short).
contains_threatening_language(no).
is_anonymous(no).
contains_discriminatory_language(-yes).
message_history(-repeated_offenses).

harassment :-
    contains_offensive_language(yes),
    targets_individual(yes),
    not is_anonymous(yes).

harassment_response :- 
    harassment,
    write('This is harassment.'), nl.

threat :-
    contains_offensive_language(yes),
    mentions_private_info(yes),
    is_anonymous(yes).

threat_response :-
    threat,
    write('This is a threat.'), nl.

exclusion :-
    repeats_negative_phrases(yes),
    targets_individual(yes),
    not mentions_private_info(yes).

exclusion_response :-
    exclusion,
    write('This is exclusionary behavior.'), nl.

discrimination :-
    contains_discriminatory_language(yes),
    targets_individual(yes).

discrimination_response :-
    discrimination,
    write('This is discriminatory behavior.'), nl.

% Default for Unclassified Bullying
unclassified_bullying :-
    contains_offensive_language(yes),
    not harassment,
    not threat,
    not exclusion,
    not discrimination.

unclassified_response :-
    unclassified_bullying,
    write('This is inappropriate content.'), nl.

% Positive Message Characteristics
positive_message :-
    not contains_offensive_language(yes),
    not contains_discriminatory_language(yes),
    message_length(long).

good_behavior :-
    positive_message,
    not targets_individual(yes).

% Motivated Message Characteristics
motivated_message :-
    positive_message,
    message_history(no_offenses).

% Negative Behavior Assessment
negative_behavior :-
    contains_offensive_language(yes),
    message_history(repeated_offenses).

% At-Risk Messages
at_risk_message :-
    negative_behavior,
    is_anonymous(yes).

% Not At Risk
not_at_risk :-
    motivated_message,
    good_behavior,
    not at_risk_message.

% Maybe At Risk
maybe_at_risk :-
    contains_offensive_language(yes),
    message_history(isolated_incident),
    not at_risk_message.


    