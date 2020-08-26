# Collect values from a list of dictionaries and store them as the key:value pairs within one single dictionary.

list_of_dicts = [{'A': 1, 'B': 2, 'C': 3}, 
                 {'A': 4, 'B': 5, 'C': 6},
                 {'A': 7, 'B': 8, 'C': 9},
                 {'A': 10, 'B': 11, 'C': 12},
                 {'A': 13, 'B': 14, 'C': 15}]

collected_kv_pairs = {entry['A']:entry['C'] for entry in list_of_dicts}

print(collected_kv_pairs)