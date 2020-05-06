from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import time
#embedder = SentenceTransformer('bert-base-nli-mean-tokens')
embedder = SentenceTransformer('bert-large-nli-mean-tokens')
#embedder = SentenceTransformer('roberta-base-nli-mean-tokens')
#embedder = SentenceTransformer('roberta-large-nli-mean-tokens')
#embedder = SentenceTransformer('distilbert-base-nli-mean-tokens')

def save_embedding(file_name,embedding_list):
    save_file_header = open(file_name.replace(".txt","_embedding.txt"),"w")
    for embedded_codes in embedding_list:
        for code in embedded_codes:
            save_file_header.write(str(code)+" ")
        save_file_header.write("\n")

def get_all_sentences(file_name):
    file_header = open(file_name)
    line = file_header.readline()
    sentence_list = []
    while line:
        if line =="\n":
            continue
        line = line.replace("\n","")
        sentence_list.append(line)
        line = file_header.readline()
    return sentence_list

def load_embedded_codes(file_name):
    file_header = open(file_name)
    line = file_header.readline()
    feature_list = []
    while line:
        line.replace("\n","")
        eles = line.split(" ")
        feature = []
        for ele in eles:
            feature.append(float(ele))
        feature_list.append(feature)
        line = file_header.readline()
    return feature_list


def embed(embedder,src_file,will_save=False):
    corpus = get_all_sentences(src_file)

    corpus_embeddings = embedder.encode(corpus)
    if will_save:
        save_embedding(src_file,corpus_embeddings)
    return corpus_embeddings

embeddings_positives1 = embed(embedder,"positive_library/selected.txt",True)
embeddings_positives2 = embed(embedder,"positive_library/selected_and_positive_tweets.txt",True)
embeddings_positives3 = embed(embedder,"positive_library/selected_and_positive_tweets_and_positive_web.txt",True)
embeddings_positives4 = embed(embedder,"positive_library/positive_tweets_and_positive_web.txt",True)

#embeddings_unknowns = embed(embedder,"texts_clean.txt",False)

num_clusters = 1

clustering_model1 = KMeans(n_clusters=num_clusters)
clustering_model1.fit(embeddings_positives1)
print("The center of selected is:")
print(clustering_model1.cluster_centers_)

clustering_model2 = KMeans(n_clusters=num_clusters)
clustering_model2.fit(embeddings_positives2)
print("The center of selected_and_positive_tweets is:")
print(clustering_model2.cluster_centers_)

clustering_model3 = KMeans(n_clusters=num_clusters)
clustering_model3.fit(embeddings_positives3)
print("The center of selected_and_positive_tweets_and_positive_web is:")
print(clustering_model3.cluster_centers_)

clustering_model4 = KMeans(n_clusters=num_clusters)
clustering_model4.fit(embeddings_positives4)
print("The center of positive_tweets_and_positive_web is:")
print(clustering_model4.cluster_centers_)

unknown_sentenses_file = "texts_clean2.txt"
unknown_sentenses_file_header = open(unknown_sentenses_file)
line = unknown_sentenses_file_header.readline()
while line:
    line = line.replace("\n","")
    line_list = []
    line_list.append(line)
    embedded_line = embedder.encode(line_list)
    print(embedded_line)
    time.sleep(1)
    