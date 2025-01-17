
from openai import OpenAI
client = OpenAI(
  api_key="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"
)

# Initialize conversation
prompt = f"""
    You are a cyberbullying language model trained to extract predicates from text. I will provide ontology with an example.
    Example: "You always overcomplicate things when they don't need to be, just fucking get over it."  

    - Subject:[speaker, recipient, other]. 'You' -> recipient. 
    - disrespectful:[1-10]. Unecessarily doubles down on same idea 'just fucking get over it' -> 1
    - offensive_lang:[1-10] "fucking" -> 1
    - exclusive:[1-0] doesn't use language excluding anyone -> 0
    - threatens_individual:[1-0] makes no threats -> 0
    - negative_phrase_repetitions:[1-0] repeats same idea 'just fucking get over it' -> 1
    - private_info:[1-0] doesn't mention repetitions -> 0

    You would return:
    - Subject: recipient
    - disrespectful: 1
    - offensive_lang: 1
    - exclusive: 0
    - threatens_individual: 0
    - negative_phrase_repetitions: 1
    - private_info: 0"""
messages = [ {"role": "system", "content": prompt}]

# sentenceFunction
def extract_predicates(user_input):
    global messages
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )
    assistant_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

print(extract_predicates("The bully insulted the victim on social media."))
print()
print(extract_predicates("You're so useless and mopey."))
print()
print(extract_predicates("I am such a loser"))

