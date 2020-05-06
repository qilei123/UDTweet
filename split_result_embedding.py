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

#split_result_embedding("texts_clean2_result.txt")
def get_score_list(score_file,score_type = "consin"):
    mod_end = 0
    if score_type=="consin":
        mod_end = 0
    elif score_type =="eula":
        mod_end = 1
    score_file_header = open(score_file)
    
    line = score_file_header.readline()
    scores_list = []
    count=0
    while line:
        line = line[:-2]
        consin_scores = []
        if count%2==mod_end:
            
            scores = line.split(" ")

            for score in scores:

                consin_scores.append(float(score))
            scores_list.append(consin_scores)
        count+=1
        line = score_file_header.readline()

    return scores_list

scores_list = get_score_list("texts_clean2_result_scores.txt")

def get_modelx_score_list(scores_list,x=0):
    score_list = []

    for scores in scores_list:
        score_list.append(scores[x])

    return score_list

import numpy as np

score_list1 = get_modelx_score_list(scores_list,0)
print(score_list1)
print(np.argsort(score_list1))