# 🎬 Movie Recommendation System

This project builds a **movie recommendation system** using the MovieLens dataset.  
The system recommends movies similar to a selected movie based on **user rating patterns**.

The application is built using **Python, Pandas, Scikit-learn, and Streamlit**, and also integrates the **TMDB API** to display movie posters.

---

## 🚀 Features

- Movie recommendation using **collaborative filtering**
- **Cosine similarity** based item-item recommendation
- Interactive **Streamlit web interface**
- **Movie poster integration** using TMDB API
- Data analysis using **Jupyter Notebook**

---

## 🧠 How the Recommendation System Works

1. Load the **MovieLens dataset** (`movies.csv` and `ratings.csv`)
2. Merge movie information with user ratings
3. Create a **user-movie rating matrix** using `pandas pivot_table`
4. Compute **cosine similarity** between movies
5. Recommend the **top similar movies** to the selected movie

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TMDB API

---

## 📂 Project Structure
