# RecipeCraft

## Overview
`RecipeCraft` is a web-based application that suggests recipes to users based on their nutritional preferences and available ingredients. By leveraging machine learning techniques, the system delivers personalized recipe recommendations that meet users' specific dietary needs.

## Features
- **Personalized Recommendations:** Suggests recipes based on nutritional values and ingredients provided by the user.

- **Machine Learning:** Utilizes the K-Nearest Neighbors (KNN) algorithm to identify and recommend similar recipes.

- **User-Friendly Interface:** A responsive web interface designed using Flask and Bootstrap, ensuring an intuitive and seamless user experience.

## Functionality
- **Form Submission:** Users enter their desired nutritional values and ingredients. Numerical features such as calories, fat, carbohydrates, protein, cholesterol, sodium, and fiber are normalized using StandardScaler. This ensures that these features contribute equally to the distance calculations in the recommendation model.
- **Recommendation Generation:** The system processes the input and retrieves the top 5 most similar recipes using the KNN model.The recommendation system utilizes the K-Nearest Neighbors (KNN) algorithm. KNN is a non-parametric method used for classification and regression. In this context, it identifies the most similar recipes to the input recipe based on Euclidean distance.
The KNN model is trained on the combined feature set of recipes, allowing it to make recommendations based on the similarities between recipes in both numerical and ingredient feature spaces.

- **Display:** Recommended recipes are presented with details such as name, ingredients, and an image. 

## Tools and Technologies
### Data Processing
- **TF-IDF Vectorizer:** Converts ingredient lists into numerical vectors based on term importance.
- **StandardScaler:** Normalizes numerical features to standardize their range.
- **NumPy:** Used for handling numerical operations and feature combination.

### Machine Learning
- **K-Nearest Neighbors (KNN):** Algorithm for identifying similar recipes based on Euclidean distance in the feature space.

### Web Development
- **Flask:** Framework for building the web application.
- **Bootstrap:** CSS framework for styling the web interface and ensuring responsiveness.

---


To set up the RecipeCraft application, you'll need to manually install a few Python frameworks and libraries. Follow these steps:
1. Open a terminal or command prompt on your system.
2. Make sure you have python installed and add the required frameworks and libraries by running the following combined command:

   ```bash
   pip install Flask numpy scikit-learn pandas
3. Run the Flask application to start the web server:
   ```bash
   flask run

This command will start the development server, and you should be able to access the RecipeCraft application via your web browser at http://127.0.0.1:5000

## Conclusion
RecipeCraft combines data processing, machine learning, and web development to offer a tailored culinary experience. By analyzing user inputs, the system identifies and presents recipes that align with users' dietary needs, making it easier to discover meals that are both nutritious and delicious.
