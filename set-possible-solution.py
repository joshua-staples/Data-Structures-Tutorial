def common_words(string1, string2):
    # first we need to make all lower case
    string1 = string1.lower()
    string2 = string2.lower()
    # second we need to get rid of all the punctuation in the sentence. 
    punctuation = "!@#$%^&*()-=+'_\/`~<>\",.?;:{[]}"
    for char in punctuation: 
        string1 = string1.replace(char,"")
        string2 = string2.replace(char,"")
        
    # then conver the string to a set, by spliting the string at the spaces
    string1_set = set(string1.split(" "))
    string2_set = set(string2.split(" "))

    #then compare the two set and return intersecting values
    print("The common words are: " + str(string1_set.intersection(string2_set)))

trial_sentence_1 = 'How often does "the dog" jump over the far fence?'
trial_sentence_2 = "I wonder why my dog is always staring at my fence in the distance..."

common_words(trial_sentence_1, trial_sentence_2) # should output {'dog', 'the', 'fence'} order may not match

trial_sentence_1 = "I wonder how long this assignment has taken me in total?"
trial_sentence_2 = "This assignment has taken me far too long, but it was also very fun."

common_words(trial_sentence_1, trial_sentence_2) # should output {'me', 'long', 'assignment', 'has', 'taken', 'this'}

trial_sentence_1 = "These sentences are the exact same."
trial_sentence_2 = "These sentences are the exact same."

common_words(trial_sentence_1, trial_sentence_2) # should return every word, not in any particular order.