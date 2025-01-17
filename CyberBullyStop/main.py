import nltk
from gptParse import extract_predicates
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')




dictOfFlags = {"empathy":[],"kind":[],"apology":[],"gratitude":[],"offers_help":[],"inclusive":[],
               "sociopathy":[],"abuse":[],"disrespectful":[],"offensive_lang":[],"exclusive":[],
               "threatens_individual":[],"negative_phrase_repetitions":[],"private_info":[],"comedy":[],
               "sarcasm":[],"exaggeration":[],"angry":[],"happy":[],"sad":[],"worried":[]}

for key in dictOfFlags:
    dictOfFlags[key] = [0,0,0]

inputText = """John went to the store and bought some milk. He saw Mary there and talked with her about their plans for the weekend."""


text = """I forgot to cook you dinner, not sorry."
    "You're fucking shit."
    "We're going to the party without you."
    "I am going to attack you."
    "You never listen you never listen you never listen."
    "You live on circleBlue street, george."""


sentences = sent_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_sentences = [
    " ".join([word for word in sentence.split() if word.lower() not in stop_words])
    for sentence in sentences
]

for sentence in filtered_sentences:
  print( extract_predicates(sentence) )
  print()
  


