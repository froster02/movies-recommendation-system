# Movies Recommendation System

A machine learning-based recommendation system that suggests movies to users based on their preferences and viewing history. This project utilizes collaborative filtering and content-based filtering techniques to provide accurate and personalized movie recommendations.
Recommendation is based on Cosine Similarity and Weighted Average.

---

## Features

- 🎥 **Movie Recommendations**: Suggests movies based on user preferences, ratings, or similarity to other movies.
- 📊 **Data Analysis**: Performs exploratory data analysis (EDA) on the movie dataset.
- 🧠 **Machine Learning Models**:
  - Collaborative Filtering
  - Content-Based Filtering
- 📂 **Data Handling**: Preprocesses and handles large datasets efficiently.
- 🌐 **User Interface (if applicable)**: A user-friendly interface for interacting with the recommendation system.

---

## Technologies Used

### Language:
- **Python**

### Libraries and Frameworks:
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Scikit-Learn**: For building machine learning models.
- **Matplotlib/Seaborn**: For data visualization.
- **Jupyter Notebook**: For interactive development and demonstration.

---

## Project Structure

- **`data/`**: Contains the movie dataset used for training and testing the recommendation algorithms.
- **`notebooks/`**: Jupyter Notebooks showcasing the development process, EDA, and model building.
- **`models/`**: Saved models for reuse and deployment.
- **`scripts/`**: Python scripts for data preprocessing, model training, and evaluation.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher installed on your system.
- Basic understanding of machine learning and data preprocessing.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/froster02/movies-recommendation-system.git
   cd movies-recommendation-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

---

## Usage

1. **Load Dataset**:
   - Place your movie dataset in the `data/` directory.
   - Update data paths in the scripts or notebooks as necessary.

2. **Run EDA**:
   - Open the EDA notebook in the `notebooks/` directory.
   - Visualize and preprocess the data.

3. **Train Model**:
   - Use the training notebook to build your recommendation model.
   - Save the trained model for later use.

4. **Make Recommendations**:
   - Run the prediction scripts to generate movie recommendations for users.

---

## Future Enhancements

- 📈 **Integration with a Web Interface**: Build a web application for users to interact with the recommendation system.
- 🤖 **Advanced Algorithms**: Incorporate deep learning techniques for improved recommendations.
- 🗃️ **Dynamic Dataset Updates**: Allow real-time updates to the dataset.

---

## License

This project is currently not licensed. Add a license file if required.

---

## Contact

For questions or feedback, feel free to reach out:

- GitHub: [froster02](https://github.com/froster02)
- # Website
visit link : https://testing-movies.herokuapp.com/

---
# Procedure

Step 1 : The dataset is used is downloaded from Kaggle.
         Dataset : https://www.kaggle.com/tmdb/tmdb-movie-metadata
       
Step 2 : Cleaned the dataset in data_preprocessing.ipynb file to remove the null values and to drop some fields.

Step 3 : Uploaded the dataset on to the [MongoDB Atlas Cluster]() client globally.

Step 4 : Fetch the data from MongoDB using NoSQL queries in Config.py file.

Step 5 : Imported the data into the main.py file to for operating.

Step 6 : Rendered the data onto the localhost using Flask framework.


### Built With

* [NoSQL]()
* [Python]()
* [Flask]()
* [HTML]()
* [CSS]()
---

Made with ❤️ by froster02.
