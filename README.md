# 🎬 Movie Recommendation System

A content-based **Movie Recommendation System** built using Python and Machine Learning. The system recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview.

## 📌 Project Overview

Finding a good movie to watch can be difficult when there are thousands of options available. This project uses **content-based filtering** to recommend movies based on their similarity to a movie selected by the user.

The recommendation engine processes movie metadata, converts it into numerical feature vectors, and calculates similarity between movies using **Cosine Similarity**.

## 🚀 Features

* 🎥 Search and select movies
* 🤖 Content-based movie recommendations
* 🔍 Movie similarity using machine learning
* 🎭 Uses genres, keywords, cast, crew, and overview
* 📊 Data preprocessing and feature engineering
* 🧠 Text vectorization using `CountVectorizer`
* 📐 Similarity calculation using Cosine Similarity
* 🌐 Interactive frontend using Streamlit

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine learning and similarity calculation
* **NLTK** – Text preprocessing
* **AST** – Parsing metadata stored as strings
* **Streamlit** – Web application
* **Joblib/Pickle** – Model and data serialization

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── notebooks/
│   └── movie_recommendation.ipynb
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

> The exact project structure may vary depending on your implementation.

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**, containing information about movies including:

* Movie title
* Movie overview
* Genres
* Keywords
* Cast
* Crew
* Movie ID

## ⚙️ How It Works

### 1. Data Collection

Movie information is loaded from the TMDB datasets.

### 2. Data Preprocessing

Unnecessary columns are removed and missing values and duplicate records are handled.

The important features used for recommendation include:

```text
genres
keywords
cast
crew
overview
```

### 3. Feature Extraction

The selected features are combined into a single `tags` column representing the characteristics of each movie.

### 4. Text Vectorization

The movie tags are converted into numerical vectors using `CountVectorizer`.

### 5. Similarity Calculation

Cosine similarity is calculated between movie vectors.

Movies with higher similarity scores are considered more relevant recommendations.

### 6. Recommendation

When a user selects a movie, the system finds movies with the highest similarity scores and displays the recommended movies.

## 🧠 Recommendation Approach

This project uses **Content-Based Filtering**.

For example:

```text
Selected Movie
      ↓
Movie Metadata
      ↓
Feature Combination
      ↓
Text Vectorization
      ↓
Cosine Similarity
      ↓
Similar Movies
      ↓
Top Recommendations
```

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

Move into the project directory:

```bash
cd movie-recommendation-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📸 Application Preview

Add screenshots of your Streamlit application here.

```text
screenshots/
├── home.png
└── recommendations.png
```

## 🔮 Future Improvements

* Add movie posters and trailers
* Add movie ratings
* Add release-year filtering
* Add genre-based filtering
* Improve recommendation accuracy
* Implement collaborative filtering
* Build a hybrid recommendation system
* Deploy the application online
* Add user accounts and personalized recommendations

## 🎯 Learning Outcomes

Through this project, I learned:

* Data cleaning with Pandas
* Feature engineering
* Text preprocessing
* Vectorization
* Cosine similarity
* Content-based recommendation systems
* Machine learning workflow
* Model/data serialization
* Streamlit application development
* Deploying ML projects

## 👨‍💻 Author

**Harsh Mishra**

This project was developed as part of my Machine Learning and Data Science learning journey.

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
