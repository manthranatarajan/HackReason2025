
from openai import OpenAI
client = OpenAI(
  api_key="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"
)

# Initialize conversation
prompt = f"""
    You are a cyberbullying language model trained to extract predicates from text. I will provide ontology with an example.
    Example: "You always overcomplicate things when they don't need to be, just fucking get over it."  

    - Subject:[speaker, recipient]. 'You' -> recipient. 
    - disrespectful:[1-10]. Unecessarily doubles down on same idea 'just fucking get over it' -> 1
    - offensive_lang:[1-10] "fucking" -> 1
    - exclusive lang:[1-10] doesn't exclude people from events -> 0
    - threatens_individual:[1-10] makes no threats -> 0
    - negative_phrase_repetitions:[1-10] repeats same idea 'just fucking get over it' -> 1
    - private_info:[1-10] doesn't mention private information -> 0

    You would generate but NOT return:
    - Subject: recipient
    - disrespectful: 8
    - offensive_lang: 10
    - exclusive: 0
    - threatens_individual: 3
    - negative_phrase_repetitions: 8
    - private_info: 0
    
    And return in the format:
    [recipient, 8, 10, 0, 3, 8, 0]"""

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






