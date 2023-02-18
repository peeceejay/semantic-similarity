## This program suggests a similar movie to a user-selected movie, from a movie database.
## It uses the spaCy library to run a language model 
## that quantifies the level of similarity between the descriptions of the selected and database movies.

 
import spacy
nlp = spacy.load('en_core_web_md')

def similar_movie(description):
    
    description = nlp(description)
    similarity_list = []

    # generates a list of similarity values for each movie
    for movie_ in movies:
        movie_desc = movie_[9:]     # removes movie title
        movie_desc = nlp(movie_desc)
        similarity_list.append(movie_desc.similarity(description))

    movie_index = similarity_list.index(max(similarity_list))   # movie description with the highest similarity
    suggested_movie = movies[movie_index][:7]
    print(suggested_movie)
    return 

# reads from text file containing movie descriptions
movies = ''
with open('./movies.txt', 'r+') as f:
    for line in f:
        movies += line
movies = movies.split('\n')
movies = list(filter(None, movies))

Planet_Hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

similar_movie(Planet_Hulk)
