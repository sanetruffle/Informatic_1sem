import pandas as pd
import random
from tkinter import *
from tkinter import ttk, filedialog, messagebox

def load_movies():
    filepath = filedialog.askopenfilename(title="файл с фильмами", filetypes=[("CSV files", "*.csv")])
    if filepath:
        try:
            films = pd.read_csv(filepath)
            return films
        except Exception as e:
            messagebox.showerror("ошибка", f"не загружает файл: {e}")
    return None

def prepare_genres(films):
    film_genres_list = list(films['Genre'])
    complex_genres = []
    
    for film_genre in film_genres_list:
        genres = film_genre.split(' | ')
        if len(genres) > 1:
            for genre in genres:
                film_genres_list.append(genre)
            complex_genres.append(film_genre)
    
    for genre in complex_genres:
        film_genres_list.remove(genre)
    
    genres_set = set(film_genres_list)
    return list(genres_set)

def select_random_movie(films, selected_genre):
    filtered_movies = films[films['Genre'].str.contains(selected_genre)]
    if not filtered_movies.empty:
        random_movie = filtered_movies.sample().iloc[0]
        return f"выбранный фильм: {random_movie['Title']} ({random_movie['Year']})"
    return "нет фильмов такого жанра"

def create_interface():
    root = Tk()
    root.title("Random Movie Selector")
    root.geometry("19200x1080")

    films = load_movies()
    if films is None:
        return

    genres_list = prepare_genres(films)

    Label(root, text="укажите жанр:").pack(pady=10)
    genre_combobox = ttk.Combobox(root, values=genres_list)
    genre_combobox.pack(pady=5)

    result_label = Label(root, text="", wraplength=300)
    result_label.pack(pady=5)

    def on_select():
        selected_genre = genre_combobox.get()
        if selected_genre:
            result = select_random_movie(films, selected_genre)
            result_label.config(text=result)
        else:
            result_label.config(text="укажите жанр")

    select_button = Button(root, text="выбрать фильм", command=on_select)
    select_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_interface()
