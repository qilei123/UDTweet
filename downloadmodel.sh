#download the model to local so it can be used again and again
mkdir universal_sentence_encoder
# Download the module, and uncompress it to the destination folder. 
curl -L "https://tfhub.dev/google/universal-sentence-encoder-large/3?tf-hub-format=compressed" | tar -zxvC universal_sentence_encoder