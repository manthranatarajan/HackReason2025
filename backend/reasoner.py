import subprocess

def scasp_call(options: list) -> bool:
    """
    Call s(CASP) through the command line.
    Returns True if the query is satisfied (models found), False otherwise.
    """
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

if __name__ == "__main__":
    # The Prolog content for cyber_bully.pl
    scasp_content = """
    abusive_words(message).
    threatening_words(message).
    comedic_words(message).
    sarcastic_words(message).
    exaggerated_words(message).
    exclusionary_words(message).
    angry_words(message).

    repeated_language(message).

    hostile(X)  :-   threatening_words(X).
    humorous(X) :-   comedic_words(X).
    sarcastic(X)  :- sarcastic_words(X).
    aggressive(X) :- angry_words(X). 
    ridiculing(X) :- comedic_words(X) , abusive_words(X).

    harrassment(X) :- ridiculing(X) , repeated_language(X).
    threat(X) :- hostile(X) , aggressive(X).
    mockery(X) :- humorous(X), abusive_words(X).

    ?- harrassment(message).
    """
    query = "?- mockery(message)."
    # Write the content to cyber_bully.pl
    with open('cyber_bully.pl', 'w') as f:
        f.write(scasp_content + '\n' + query)

    # Call scasp with the file and the "-n1" option
    result = scasp_call(['cyber_bully.pl', '-n1'])

    # Print the result
    if result:
        print(f"{query} is true.")
    else:
        print(f"{query} is false.")
