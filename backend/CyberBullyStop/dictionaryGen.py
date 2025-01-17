import nltk
from gptParse import extract_predicates
from nltk.tokenize import sent_tokenize
nltk.download('punkt_tab')

def getFlagDictionary(text):
  #initializations
  dictOfFlags = {"disrespectful":0,"offensive_lang":1,"exclusive":2, "threatens_individual":3,"negative_phrase_repetitions":4,"private_info":5}
  speakerFlags = [0] * 6
  recipientFlags = [0] * 6

  #parsing
  sentences = sent_tokenize(text)

  #getFlagNumbers
  for sentence in sentences:
    predicates =  extract_predicates(sentence) 
    predicates = predicates.strip("[]").replace(" ", "").split(",")

    if predicates[0] == 'speaker':
      predicates = predicates[1:]

      for i in range(0,6):
        speakerFlags[i] += int(predicates[i])

    if predicates[0] == 'recipient':
      predicates = predicates[1:]

      for i in range(0,6):
        recipientFlags[i] += int(predicates[i])

  # print(recipientFlags)
  # print(speakerFlags)


  #create boolean flagDictionary
  for flag in dictOfFlags:
    currFlagLevel = recipientFlags[dictOfFlags[flag]] 

    if currFlagLevel > 5:
      dictOfFlags[flag] = True    #repurposes dictOfFlags
    else:
      dictOfFlags[flag] =  False

  return dictOfFlags