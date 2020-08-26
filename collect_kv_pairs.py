# Collect values from a list of dictionaries as the key:value pairs within one single dictionary.

list_of_dicts = [{'A': 1, 'B': 2}, 
                 {'A': 3, 'B': 4},
                 {'A': 5, 'B': 6},
                 {'A': 7, 'B': 8},
                 {'A': 9, 'B': 10}]

collected_kv_pairs = {entry['A']:entry['B'] for entry in list_of_dicts}

print(collected_kv_pairs)