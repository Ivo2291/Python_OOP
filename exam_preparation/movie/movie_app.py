from Python_OOP.exam_preparation.movie.movie_specification.movie import Movie
from Python_OOP.exam_preparation.movie.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def user_exist(self, username):
        for u in self.users_collection:
            if u.username == username:
                return True

    def movie_exist(self, movie_title):
        for m in self.movies_collection:
            if m.title == movie_title:
                return True

    def check_liked_movies(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True

    def register_user(self, username: str, age: int):
        if self.user_exist(username):
            raise Exception("User already exists!")

        user = User(username, age)

        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.user_exist(username):
            raise Exception("This user does not exist!")

        if self.movie_exist(movie.title):
            raise Exception("Movie already added to the collection!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        movie.owner.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.movie_exist(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.movie_exist(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        movie_name = movie.title
        self.movies_collection.remove(movie)
        movie.owner.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie_name} movie."

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.check_liked_movies(username, movie.title):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1

        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        if not self.check_liked_movies(username, movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        movie_name = movie.title

        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.remove(movie)

        return f"{username} disliked {movie_name} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = []

        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())

        return '\n'.join(result)

    def __str__(self):
        if not self.users_collection:
            users = "No Users."
        else:
            users = ', '.join([user.username for user in self.users_collection])

        if not self.movies_collection:
            movies = "No movies."
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        delimiter = '\n'

        return f"All users: {users}{delimiter}All movies: {movies}"
