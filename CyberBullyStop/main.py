import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')

from openai import OpenAI
client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write code to solve the twosum problem"}
  ]
)

print(completion.choices[0].message);


dictOfFlags = {"empathy":[],"kind":[],"apology":[],"gratitude":[],"offers_help":[],"inclusive":[],
               "sociopathy":[],"abuse":[],"disrespectful":[],"offensive_lang":[],"exclusive":[],
               "threatens_individual":[],"negative_phrase_repetitions":[],"private_info":[],"comedy":[],
               "sarcasm":[],"exaggeration":[],"angry":[],"happy":[],"sad":[],"worried":[]}

for key in dictOfFlags:
    dictOfFlags[key] = [0,0,0]

inputText = """John went to the store and bought some milk. He saw Mary there and talked with her about their plans for the weekend."""

sentences = sent_tokenize(inputText)


stop_words = set(stopwords.words('english'))

filtered_sentences = [
    " ".join([word for word in sentence.split() if word.lower() not in stop_words])
    for sentence in sentences
]

# Resulting sentences ready for LLM input
print("Filtered Sentences:", filtered_sentences)


