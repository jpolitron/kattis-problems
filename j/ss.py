my_info = 'The capital of france is Paris'

top_weekend_movies = ['Black panther', 'Peter Rabbit', 'Fifty Shades Freed', 'Jumanji: welcome ot the jungle', 'The 15:17 to Pari ']

movie_name = my_info[-6:-1] +  ' blues'

if movie_name in top_weekend_movies:
  print(f'{movie_name} made it into the top movies!')
else:
  print(f'{movie_name} did not make it into the top movies!')
