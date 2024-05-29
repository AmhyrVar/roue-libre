def create_dictionary(data):
    new_dict = {}
    for key, value in data.items():
        new_dict[key] = value.split()
    return new_dict

def highlight_key_expression(words_list, annotation_key):
    # Initialize the result list with 0s
    result = [0] * len(words_list)
    
    # Split the key expression into words
    key_words = annotation_key.split()
    
    # Iterate over the first list to find the key expression words
    key_index = 0
    for i, word in enumerate(words_list):
        if key_index < len(key_words) and word.lower().startswith(key_words[key_index].lower()):
            result[i] = 1
            key_index += 1
        else:
            result[i] = 0
    
    return result

def write_dataset(dico):
    dataset = []
    
    for i, (key, value) in enumerate(dico.items()):
        tokens = value
        annotation = highlight_key_expression(tokens, key)
        entry = {"id": str(i), "tokens": tokens, "ner_tags": annotation}
        dataset.append(entry)
    
    return dataset

