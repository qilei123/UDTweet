from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

#embedder = SentenceTransformer('bert-base-nli-mean-tokens')
embedder = SentenceTransformer('bert-large-nli-mean-tokens')
#embedder = SentenceTransformer('roberta-base-nli-mean-tokens')
#embedder = SentenceTransformer('roberta-large-nli-mean-tokens')
#embedder = SentenceTransformer('distilbert-base-nli-mean-tokens')

def save_embedding(file_name,embedding_list):
    save_file_header = open(file_name.replace(".txt","_embedding.txt"),"w")
def get_all_sentences(file_name):
    file_header = open(file_name)

    line = file_header.readline()
    sentence_list = []
    while line:
        line.replace("\n","")
        sentence_list.append(line)
        line = file_header.readline()
    print(sentence_list)
corpus = get_all_sentences("manually_selected_clean.txt")
corpus_embeddings = embedder.encode(corpus)

# Perform kmean clustering
num_clusters = 1
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

clustered_sentences = [[] for i in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, cluster in enumerate(clustered_sentences):
    print("Cluster ", i+1)
    print(cluster)
    print("")
