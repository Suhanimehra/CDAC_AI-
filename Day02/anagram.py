def anagram():

    words=["eat", "tea", "tan", "ate", "nat", "bat"]

    groups={}

    for word in words:
        sorted_word="".join(sorted(word))

        if sorted_word not in groups:
            groups[sorted_word]=[]

        groups[sorted_word].append(word) # groups = dictionary sorted_word 
        # is the key here we store the value of worf in key(sorted_word)
    
    print(list(groups.values()))


anagram()