# collect_kv_pairs

This is a short Python script demonstrating how to collect key:value pairs from values contained within a list of dictionaries.

# Script Operation

We start with the initial list of dictionaries.
```python
  list_of_dicts = [{'A': 1, 'B': 2}, 
                   {'A': 3, 'B': 4},
                   {'A': 5, 'B': 6},
                   {'A': 7, 'B': 8},
                   {'A': 9, 'B': 10}]
```
Next, we generate a new dictionary whose key:value pairs are formed of the values from each dictionary in the list.
```python
  collected_kv_pairs = {entry['A']:entry['B'] for entry in list_of_dicts}
```
The resulting `collected_kv_pairs` dictionary is shown below.
```python
  {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}
```

