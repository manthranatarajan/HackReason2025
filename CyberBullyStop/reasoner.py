import subprocess

def run_scasp(options):
    parameters = ['scasp']
    parameters.extend(options)

    call = subprocess.Popen(
        parameters, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
        text=True, universal_newlines=True
    )

    try:
        output, _ = call.communicate(timeout=10800)
    except subprocess.TimeoutExpired:
        call.kill()
        return None

    if 'ANSWER:' in output:
        return True
    elif 'no models' in output or 'false' in output:
        return False
    return None

def scasp_query(predicate:dict):
    pred = []
    for value in predicate.values():
        if value == 'True':
            pred.append('yes')
        elif value == 'False':
            pred.append('no')
        else:
            pred.append(f"-{value}")

    if __name__ == "__main__":
    # Updated s(CASP) content to match the provided s(CASP) code
        scasp_content = """
contains_offensive_language(f{pred[1]}).
targets_individual(f"{pred[3]}").
repeats_negative_phrases(f"{pred[4]}").
mentions_private_info(f"{pred[5]}").
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


    """

    # Queries to test all rules
    queries = [
    "?- harassment.",
    "?- harassment_response.",
    "?- threat.",
    "?- threat_response.",
    "?- exclusion.",
    "?- exclusion_response.",
    "?- discrimination.",
    "?- discrimination_response.",
    "?- unclassified_bullying.",
    "?- unclassified_response.",
    "?- positive_message.",
    "?- good_behavior.",
    "?- motivated_message.",
    "?- negative_behavior.",
    "?- at_risk_message.",
    "?- not_at_risk.",
    "?- maybe_at_risk."
]


    # Write the content to cyber_bully.pl
    with open('cyber_bully.pl', 'w') as f:
        f.write(scasp_content)

    # Iterate through queries and print the results
    for query in queries:
        # print(f"Running query: {query}")

        # Append the query to the s(CASP) file
        with open('cyber_bully.pl', 'a') as f:
            f.write(f"\n{query}\n")

        # Call s(CASP) with the file and the "-n1" option
        result = run_scasp(['cyber_bully.pl', '-n1'])

        # Print the result
        if result is True:
            print(f"{query} is true.")
        elif result is False:
            print(f"{query} is false.")
        else:
            print(f"{query} returned an unknown result.")

        # Reset the file for the next query
        with open('cyber_bully.pl', 'w') as f:
            f.write(scasp_content)
scasp_query(1)