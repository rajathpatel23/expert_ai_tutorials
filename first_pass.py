from expertai.nlapi.cloud.client import ExpertAiClient
import os
import pdb
os.environ["EAI_USERNAME"] = 'rpatel12@umbc.edu'
os.environ["EAI_PASSWORD"] = '@Rhp1993'
client = ExpertAiClient()


#text = "Michael Jordan è stato uno dei migliori giocatori di pallacanestro di tutti i tempi. Fare canestro è stata la capacità in cui Jordan spiccava, ma ancora detiene un record NBA di gioco difensivo, con otto palle rubate in metà partita."
text = "Michael Jordan"
language= 'en'

# output = client.specific_resource_analysis(
#     body={"document": {"text": text}}, 
#     params={'language': language, 'resource': 'emotional-traits'
# })
# pdb.set_trace()
# print(output)

# for token in output.tokens:
#     print (f'{text[token.start:token.end]:{20}} {token.lemma:{8}}')

import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('ggplot')

taxonomy='iptc'

document = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy,'language': language})

categories = []
scores = []

print (f'{"CATEGORY":{27}} {"IPTC ID":{10}} {"FREQUENCY":{8}}')
for category in document.categories:
    categories.append(category.label)
    scores.append(category.frequency)
    print (f'{category.label:{27}} {category.id_:{10}}{category.frequency:{8}}')
