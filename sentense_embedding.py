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
##################################
embedding_sentences_file1 = "selected_and_positive_tweets.txt"

corpus1 = get_all_sentences(embedding_sentences_file1)

corpus_embeddings1 = embedder.encode(corpus1)
'''
save_embedding(embedding_sentences_file1,corpus_embeddings1)
'''
###################################

embedding_sentences_file2 = "texts_clean.txt"

corpus2 = get_all_sentences(embedding_sentences_file2)

corpus_embeddings2 = embedder.encode(corpus2)
'''
save_embedding(embedding_sentences_file2,corpus_embeddings2)
'''

# Perform kmean clustering
num_clusters = 1
clustering_model = KMeans(n_clusters=num_clusters)
clustering_model.fit(corpus_embeddings1)
print("cluster_center is:")
print(clustering_model.cluster_centers_)
