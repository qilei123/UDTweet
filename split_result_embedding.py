import os

def split_result_embedding(src_file):
    src_file_header = open(src_file)
    dst_embedding_header = open(src_file.replace(".txt","_embeddings.txt"),"w")
    dst_result_header = open(src_file.replace(".txt","_scores.txt"),"w")
    line = src_file_header.readline()
    count = 1
    while line:
        if count%3==1:
            dst_embedding_header.write(line)
        else:
            dst_result_header.write(line)
        count+=1
        line = src_file_header.readline()

split_result_embedding("texts_clean2_result.txt")