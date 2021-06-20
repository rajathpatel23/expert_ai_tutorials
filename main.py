# use Sentiments, Text subdivision, Classification taxonomy,
# Key elements/Relations/Named entitnies -> help in relating info in sentence together

from expertai.nlapi.cloud.client import ExpertAiClient
import os
import credentials
import sqlite3 as sql

os.environ["EAI_USERNAME"] = credentials.twitter_dev_username
os.environ["EAI_PASSWORD"] = credentials.twitter_dev_password

client = ExpertAiClient()

# raw_text = open(r"C:\Users\LENOVO\PycharmProjects\nlpExpertApi\input_text", "r")
# text = raw_text.read()

db_connect = sql.connect('twitter_data/tweets.db')
db_cursor = db_connect.cursor()
db_cursor.execute("SELECT * from tweets")
tweets = db_cursor.fetchall()

for index, tweet in enumerate(tweets):
    text = tweet[0]

# raw_text = open(r"C:\Users\LENOVO\PycharmProjects\nlpExpertApi\input_text", "r")
# text = raw_text.read()

    taxonomy = 'iptc'
    language = 'en'


    output = client.specific_resource_analysis(body={"document": {"text": text}},params={'language': language, 'resource': 'disambiguation'})
    # for classifying the text categories
    output_class = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})
    output_ent = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'entities'})
    document = client.specific_resource_analysis(body={"document": {"text": text}},  params={'language': language, 'resource': 'relevants'})
    document_relation = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'relations'})
    output_sentiment = client.specific_resource_analysis(body={"document": {"text": text}},params={'language': language, 'resource': 'sentiment'})
    output_full_analysis = client.full_analysis(body={"document": {"text": text}}, params={'language': language})

    print("\n _________ ")
    print("Tweet {}".format(index+1))
    print(text)
    print("\nOutput arrays size:")

    print("knowledge: ", len(output_full_analysis.knowledge))
    print("paragraphs: ", len(output_full_analysis.paragraphs))
    print("sentences: ", len(output_full_analysis.sentences))
    print("phrases: ", len(output_full_analysis.phrases))
    print("tokens: ", len(output_full_analysis.tokens))
    print("mainSentences: ", len(output_full_analysis.main_sentences))
    print("mainPhrases: ", len(output_full_analysis.main_phrases))
    print("mainLemmas: ", len(output_full_analysis.main_lemmas))
    print("mainSyncons: ", len(output_full_analysis.main_syncons))
    print("topics: ", len(output_full_analysis.topics))
    print("entities: ", len(output_full_analysis.entities))
    print("entities: ", len(output_full_analysis.relations))
    print("sentiment.items: ", len(output_full_analysis.sentiment.items))
    print("sentiment.overall: ", len(output_full_analysis.sentiment.overall))

# print("Tab separated list of categories:")
#
# for category in output_class.categories:
#     print(category.id_, category.hierarchy, sep="\t")
#
#
# print (f'{"ENTITY":{50}} {"TYPE":{10}} {"RELEVANCE":{10}}')
# print (f'{"------":{50}} {"----":{10}}')
#
#
# for entity in output_ent.entities:
#     print (f'{entity.lemma:{50}} {entity.type_:{10}} {entity.relevance:{10}}')

# print (f'{"LABEL":{50}} {"HIERARCHY":{10}}')
# print (f'{"------":{50}} {"----":{10}}')
# for entity in output_ent.categories:
#     print (f'{entity.label:{50}} {entity.hierarchy:{10}}')

# print("\n" f'{"LEMMA":{20}} {"SCORE":{5}} ')
#
# for mainlemma in document.main_lemmas:
#     print(f'{mainlemma.value:{20}} {mainlemma.score:{5}}')
#
# for rel in document_relation.relations:
#    print("Verb:", rel.verb.lemma)
#    for r in rel.related:
#       print("Relation:", r.relation, "Lemma:", r.lemma )
