%Facts

    %Language
        abusive_words(message).
        -threatening_words(message).
        comedic_words(message).
        sarcastic_words(message).
        exaggerated_words(message).
        exclusionary_words(message).
        angry_words(message).

        repeated_language(message).


%%Rules
    %Tone
        hostile(X)  :- threatening_words(X).
        humorous(X) :- comedic_words(X).
        sarcastic(X)  :- sarcastic_words(X).
        aggressive(X) :- angry_words(X). 
        ridiculing(X) :- comedic_words(X) , abusive_words(X).


    %Type
        harrassment(X) :- ridiculing(X) , repeated_language(X).
        threat(X) :- hostile(X) , aggressive(X).
        mockery(X) :- humorous(X), abusive_words(X).
    