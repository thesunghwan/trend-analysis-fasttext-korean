import numpy, random, sys
from scipy import spatial
word_vectors = []

with open(sys.argv[1]) as f:
    for line in f:
        splitted_line = line.split()
        word_vectors.append({
            "word": splitted_line.pop(0),
            "vector": numpy.array(list(map(float, splitted_line))),
            "cosine_similarity": 0
        })

word_to_test = {
    "word": sys.argv[2],
    "vector": None,
    "cosine_similarity": 0
}

for word_vector in word_vectors:
    if word_vector["word"] == word_to_test["word"]:
        word_to_test["vector"] = word_vector["vector"]

word_vectors.pop(0)
max_cosine_vector = word_vectors.pop(0)

max_cosine_vector["cosine_similarity"] = 1 - spatial.distance.cosine(word_to_test["vector"], max_cosine_vector["vector"])
#max_cosine_vector["cosine_similarity"] = numpy.linalg.norm(word_to_test["vector"] - max_cosine_vector["vector"], 2)
for word_vector in word_vectors:
    if max_cosine_vector["vector"].shape[0] == word_vector["vector"].shape[0]:
        word_vector["cosine_similarity"] = 1 - spatial.distance.cosine(word_to_test["vector"], word_vector["vector"])
        #word_vector["cosine_similarity"] = numpy.linalg.norm(word_to_test["vector"] - word_vector["vector"], 2)

from operator import itemgetter
newlist = sorted(word_vectors, key=itemgetter('cosine_similarity'), reverse=True)

dic = {}
for i in range(20):
    dic[newlist[i]["word"]] = newlist[i]["cosine_similarity"]
    print(newlist[i]["word"], newlist[i]["cosine_similarity"])

import json
with open('static/result.json', 'w') as outfile:
    json.dump(dic, outfile)
