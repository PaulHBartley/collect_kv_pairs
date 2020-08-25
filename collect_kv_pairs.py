# Get all titles from movies list and store them as {title: id}

movies = [{'title': 'Sonic the Hedgehog', 'id': '001'}, 
           {'title': 'Inside Out', 'id': '002'},
           {'title': 'Toy Story IV', 'id': '003'}]

collect_kv_pairs = {movie['title']:movie['id'] for movie in movies}

print(collect_kv_pairs)