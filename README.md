# 🚀 💎 GemFinder AI: The "Hidden Gem" Movie Recommender

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

### 📍 The Problem
In the era of "Trending" lists, high-quality indie and niche films often get buried under massive marketing budgets. Most recommendation engines create a **popularity bias**, suggesting the same 50 blockbusters to everyone.

### 💡 The Solution
**GemFinder AI** is an end-to-end data product that surfaces high-quality, low-popularity movies. By combining **Natural Language Processing (NLP)** for plot similarity with a **Weighted Rating Algorithm**, the system ensures you discover "Hidden Gems" that actually match your taste.

---

## 🛠️ Tech Stack & Skills Demonstrated
* **Data Engineering:** Pandas for data cleaning and JSON parsing of nested metadata.
* **NLP:** `CountVectorizer` for text vectorization and Bag-of-Words modeling.
* **Mathematics:** Cosine Similarity for high-dimensional vector distance and the IMDB Weighted Rating formula for statistical smoothing.
* **Full-Stack AI:** Streamlit for UI/UX development.



[Image of Content-Based Filtering workflow diagram]


---

## 🧠 Core Methodology

### 1. Vectorization & Similarity
I transformed movie "tags" (overviews + genres) into numerical vectors.
* **Algorithm:** Cosine Similarity.
* **Why?** It measures the cosine of the angle between two vectors, focusing on the orientation (content) rather than the magnitude (length), making it ideal for text comparison.

$$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

### 2. The "Hidden Gem" Logic
To be classified as a "Gem," a movie must pass two filters:
1.  **The Quality Threshold:** Must have a **Weighted Rating** higher than the global average.
2.  **The Discovery Filter:** Must have a **Popularity Score** below the 75th percentile to ensure it isn't a mainstream blockbuster.

---

## 📸 Features
* 🔍 **Semantic Search:** Find movies based on plot "DNA" rather than just titles.
* 🎨 **Modern UI:** Custom CSS-styled cards with dynamic genre tags.
* 🔽 **Pagination:** "Load More" feature using Streamlit Session State for seamless browsing.

---

## 🚀 Installation & Usage

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/yourusername/GemFinder-AI.git](https://github.com/yourusername/GemFinder-AI.git)
   cd GemFinder-AI

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt

3. **Run the App**
   ```bash
   streamlit run app.py
