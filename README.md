# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built with Python and Streamlit that recommends similar movies based on a user's selected movie. The application uses a precomputed similarity matrix to identify and display the top 5 similar movies along with their posters.

## 🚀 Features

- **Movie Selection:** Search for or select a movie from a dropdown menu.
- **Content-Based Filtering:** Find movies similar to the selected movie using similarity scores.
- **Top 5 Recommendations:** Display five recommended movies for the selected title.
- **Movie Posters:** Show movie posters alongside recommendations.
- **Interactive Web Interface:** Simple and user-friendly interface built with Streamlit.
- **Precomputed Similarity:** Load the saved similarity matrix and movie data for recommendations.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Pandas** — Data manipulation and processing
- **NumPy** — Numerical operations
- **Scikit-learn** — Feature extraction and similarity calculations
- **Pickle** — Saving and loading movie data and similarity objects
- **Streamlit** — Interactive web application
- **TMDB API** — Fetching movie posters (if configured in the application)

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── model/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

Replace `YOUR_USERNAME` with your GitHub username and adjust the repository name if necessary.

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

Activate the environment.

**Windows:**

```bash
myenv\Scripts\activate
```

**macOS/Linux:**

```bash
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn requests
```

Save the required dependencies to a file:

```bash
pip freeze > requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🧠 How It Works

1. **Data Preparation:** Movie information is processed into a suitable format for content-based recommendations.
2. **Feature Extraction:** Movie features are transformed into numerical representations.
3. **Similarity Calculation:** A similarity matrix is generated to measure how closely movies relate to one another.
4. **Movie Selection:** The user selects a movie from the Streamlit dropdown.
5. **Recommendation Generation:** The system finds the selected movie's index, retrieves its similarity scores, and ranks similar movies.
6. **Results Display:** The top five recommendations and their posters are displayed in the web interface.

## 📸 Application Preview

The application allows users to select a movie and view five similar movie recommendations with their posters.

*Add a screenshot of your running Streamlit application here.*

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building an interactive machine learning application.
- Implementing content-based recommendation logic.
- Working with similarity matrices and precomputed model artifacts.
- Integrating Python data processing with a Streamlit frontend.
- Displaying dynamic recommendations and movie posters.

## 🔮 Future Improvements

- Add movie ratings, genres, and descriptions.
- Improve the interface with a responsive movie-card layout.
- Add filtering by genre and release year.
- Deploy the application for public access.
- Improve recommendation quality through feature engineering and evaluation.

## 👨‍💻 Author

**Aman Shah**

BS Information Technology Student | Junior Data Scientist | Machine Learning & Deep Learning

- GitHub: [amanshah362](https://github.com/amanshah362)
- Kaggle: [amanshah32](https://www.kaggle.com/amanshah32)

---

⭐ If you find this project useful, consider giving the repository a star!

*Built with Python, Machine Learning, and Streamlit.*
