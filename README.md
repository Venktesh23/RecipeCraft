# RecipeCraft

## Overview
`RecipeCraft` is a web-based application that suggests recipes to users based on their nutritional preferences and available ingredients. By leveraging machine learning techniques, the system delivers personalized recipe recommendations that meet users' specific dietary needs.

## Features
- **Personalized Recommendations:** Suggests recipes based on nutritional values and ingredients provided by the user.

- **Machine Learning:** Utilizes the K-Nearest Neighbors (KNN) algorithm to identify and recommend similar recipes.

- **User-Friendly Interface:** A responsive web interface designed using Flask and Bootstrap, ensuring an intuitive and seamless user experience.

## Functionality
- **Form Submission:** Users enter their desired nutritional values and ingredients.
- **Recommendation Generation:** The system processes the input and retrieves the top 5 most similar recipes using the KNN model.The recommendation system utilizes the K-Nearest Neighbors (KNN) algorithm. KNN is a non-parametric method used for classification and regression. In this context, it identifies the most similar recipes to the input recipe based on Euclidean distance.
The KNN model is trained on the combined feature set of recipes, allowing it to make recommendations based on the similarities between recipes in both numerical and ingredient feature spaces.

- **Display:** Recommended recipes are presented with details such as name, ingredients, and an image. 

## Prerequisites
To set up the RecipeCraft application, you'll need to manually install a few Python frameworks and libraries. Follow these steps:
1. Open a terminal or command prompt on your system.
2. Make sure you have python installed and add the required frameworks and libraries by running the following combined command:

   ```bash
   pip install Flask numpy scikit-learn pandas
3. Run the Flask application to start the web server:
   ```bash
   flask run
## Conclusion
RecipeCraft combines data processing, machine learning, and web development to offer a tailored culinary experience. By analyzing user inputs, the system identifies and presents recipes that align with users' dietary needs, making it easier to discover meals that are both nutritious and delicious.
