from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

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

embeddings_positives = embed(embedder,"selected_and_positive_tweets.txt",False)

embeddings_unknowns = embed(embedder,"texts_clean.txt",False)

# Perform kmean clustering
num_clusters = 1
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(embeddings_positives)
print("cluster_center is:")
print(clustering_model.cluster_centers_)
