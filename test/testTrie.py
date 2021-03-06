# coding=utf-8
#!/usr/bin/env python


class TrieNode(object):

    def __init__(self):
        self.value = -1
        self.children = {}


def save_model(data , model):
    from cPickle import dump
    with open(model , 'wb') as f:
        dump(data , f)



def load_model( model_path):
    from cPickle import load
    with open(model_path , 'rb') as f:
        return load(f)


class Trie(object):


    def __init__(self , model_path = None):
        if model_path:
            self.root = load_model(model_path)
        else:
            self.root = TrieNode()

    def __eq__(self, word):
        if word and isinstance(word, (str, unicode)):
            return self.search(word)
        return False

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.search(key)

    def add(self, words, value):
        if words and isinstance(words , basestring):
            if not isinstance(words , unicode):
                words = words.decode('utf-8')
            node = self.root
            for item in words:
                if node.children.has_key(item):
                    node = node.children[item]
                else:
                    tmp = TrieNode()
                    node.children[item] = tmp
                    node = tmp
            node.value = value
            return True
        return False


    def search(self, words):
        if words and isinstance(words , basestring):
            if not isinstance(words , unicode):
                words = words.decode('utf-8')
            node = self.root
            isFind = False
            for word in words:
                isFind = False
                if not node.children.has_key(word):
                    return False
                else:
                    node = node.children[word]
            return True if node.value >=0 else False
        return False


if __name__ == "__main__":
    trie = Trie()
    trie.add("我爱天安门", 1)
    print trie.search("我爱天安门")
    from time import time
    # print time()
    with open('dict.txt') as f:
        for line in f.readlines():
            line = line.strip().split()
            trie.add(line[0] , int(line[1]))
    print time()

    save_model( trie.root ,'d:/tree.bin' )
    print time()
    # t = load_model('d:/tree.bin')
    # x = Trie('d:/tree.bin')
    # print x.search('嗅觉')
    # print time()


