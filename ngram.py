import numpy as np
import re


# What data structure do I want?
# Each ngram should know the (n-1)grams it contains and the (n+1)grams that contain it

class Node:
    def __init__(self, data):
        self.data = data
        self.parents = []
        self.left = None
        self.right = None
        self.count = 0


class NgramGlue:
    def __init__(self):
        self.ngrams = dict()


    def fit(self, text, n):
        # Text should be a list of strings
        # remove the following: ,.
        # 
        cleaned = [ re.sub('[.,]','', s) for s in text]
        parent = self.tree
        for s in cleaned:
            words = cleaned.split():
            words = ['@BOT@'] + words + ['@EOT@']

        for i in range(1,n+1):
            if i not in self.ngrams:
                self.ngrams[i] = dict()
            for j in range(len(words)-i+1):
                ng = tuple(words[j:j+1])
                self.ngrams[i][ng] = self.ngrams[i].get(ng, 0) + 1


    def build_tree(self):
        node_dict = {'': Node('')}
        for key, ngs in self.ngrams.items():
            for ng, ct in ngs.items():
                node = Node(ng)
                node.count = ct
                node_dict[ng] = node

        for s, node in node_dict.items():
            node.left = node_dict[s[:-1]]
            node.right = node_dict[s[1:]]
            node.left.parents.append(node)
            node.right.parents.append(node)



