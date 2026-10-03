
        def build_trie(_dict):
            trie = {}
            for word in _dict:
                t = trie
                for c in word:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                t["_"] = True
            return trie