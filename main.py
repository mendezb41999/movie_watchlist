# from db import init_db, add_movie, mark_watched, get_all_movies
from api import search_movie
from utils import display_movie_info
from db import init_db, add_movie, mark_watched, get_all_movies

init_db()

def main():
    while True:
        print("\n1. Search movie")
        print("2. View watchlist")
        print("3. Mark as watched")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter movie title: ")
            movie = search_movie(title)
            if movie.get("Response") == "True":
                display_movie_info(movie)
                save = input("Add to watchlist? (y/n): ").lower()
                if save == "y":
                    add_movie(movie["Title"], movie["Year"])
            else:
                print("Movie not found.")
        
        elif choice == "2":
            movies = get_all_movies()
            for m in movies:
                watched = "✅" if m[3] else "❌"
                print(f"[{m[0]}] {m[1]} ({m[2]}) Watched: {watched}")
        
        elif choice == "3":
            movie_id = input("Enter movie ID to mark as watched: ")
            mark_watched(movie_id)
            print("Updated.")
        
        elif choice == "4":
            break
        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()