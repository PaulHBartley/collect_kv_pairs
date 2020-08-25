# Form a single dictionary of collected key:value pairs from a list of dictionaries

list_of_dicts = [{'A': 1, 'B': 2}, 
                 {'A': 3, 'B': 4},
                 {'A': 5, 'B': 6}]

collected_kv_pairs = {value['A']:value['B'] for value in list_of_dicts}

print(collected_kv_pairs)