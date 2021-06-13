# use Sentiments, Text subdivision, Classification taxonomy,
# Key elements/Relations/Named entitnies -> help in relating info in sentence together

from expertai.nlapi.cloud.client import ExpertAiClient
import os
import credentials

os.environ["EAI_USERNAME"] = credentials.twitter_dev_username
os.environ["EAI_PASSWORD"] = credentials.twitter_dev_password

client = ExpertAiClient()

raw_text = open(r"C:\Users\LENOVO\PycharmProjects\nlpExpertApi\input_text", "r")
text = raw_text.read()

taxonomy = 'iptc'
language = 'en'

output = client.specific_resource_analysis(
    body={"document": {"text": text}},
    params={'language': language, 'resource': 'disambiguation'})

# for classifying the text categories
output_class = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})
output_ent = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'entities'})
document = client.specific_resource_analysis(body={"document": {"text": text}},  params={'language': language, 'resource': 'relevants'})
document_relation = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'relations'})

print("Tab separated list of categories:")

for category in output_class.categories:
    print(category.id_, category.hierarchy, sep="\t")


print (f'{"ENTITY":{50}} {"TYPE":{10}} {"RELEVANCE":{10}}')
print (f'{"------":{50}} {"----":{10}}')


for entity in output_ent.entities:
    print (f'{entity.lemma:{50}} {entity.type_:{10}} {entity.relevance:{10}}')

# print (f'{"LABEL":{50}} {"HIERARCHY":{10}}')
# print (f'{"------":{50}} {"----":{10}}')
# for entity in output_ent.categories:
#     print (f'{entity.label:{50}} {entity.hierarchy:{10}}')

print("\n" f'{"LEMMA":{20}} {"SCORE":{5}} ')

for mainlemma in document.main_lemmas:
    print(f'{mainlemma.value:{20}} {mainlemma.score:{5}}')

for rel in document_relation.relations:
   print("Verb:", rel.verb.lemma)
   for r in rel.related:
      print("Relation:", r.relation, "Lemma:", r.lemma )
