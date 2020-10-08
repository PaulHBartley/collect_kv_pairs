# collect_kv_pairs

This is a short Python script demonstrating how to collect values from a list of dictionaries and store them as key:value pairs within one single dictionary.

# Script Operation

We start with the initial list of dictionaries.
```python
  list_of_dicts = [{'A': 1, 'B': 2, 'C': 3}, 
                   {'A': 4, 'B': 5, 'C': 6},
                   {'A': 7, 'B': 8, 'C': 9},
                   {'A': 10, 'B': 11, 'C': 12},
                   {'A': 13, 'B': 14, 'C': 15}]
```
Next, we generate a new dictionary whose key:value pairs are formed of values from dictionaries in the list.
```python
  collected_kv_pairs = {entry['A']:entry['C'] for entry in list_of_dicts}
```
The resulting `collected_kv_pairs` dictionary is shown below.
```python
  {1: 3, 4: 6, 7: 9, 10: 12, 13: 15}
```

