
def get_indices_of_item_weights(weights, length, limit): 
    ht = {} 

# Enumerate 
    for i, w in enumerate(weights): 
        ht[w] = i 

# Enumerate 
    for i, w in enumerate(weights): 
        value = ht.get(limit - w, None) 
        if value: 
            return [ value, i ] 

    return None 