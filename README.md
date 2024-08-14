# RecipeCraft

## Overview
`RecipeCraft` is a web-based application that suggests recipes to users based on their nutritional preferences and available ingredients. By leveraging machine learning techniques, the system delivers personalized recipe recommendations that meet users' specific dietary needs.

## Features
- **Personalized Recommendations:** Suggests recipes based on nutritional values and ingredients provided by the user.
- **Machine Learning:** Utilizes the K-Nearest Neighbors (KNN) algorithm to identify and recommend similar recipes.
- **User-Friendly Interface:** A responsive web interface designed using Flask and Bootstrap, ensuring an intuitive and seamless user experience.

## Functionality
- **Form Submission:** Users enter their desired nutritional values and ingredients.
- **Recommendation Generation:** The system processes the input and retrieves the top 5 most similar recipes using the KNN model.
- **Display:** Recommended recipes are presented with details such as name, ingredients, and an image. 

## Installation
To set up the RecipeCraft application, you'll need to manually install a few Python frameworks and libraries. Follow these steps:

Open a terminal or command prompt on your system.

Install the required frameworks and libraries by running the following combined command:

bash
Copy code
pip install Flask numpy scikit-learn pandas
This command will install:

Flask: A lightweight web framework for building the web application.
NumPy: A library for numerical operations and data handling.
Scikit-learn: A machine learning library for implementing K-Nearest Neighbors (KNN) and other data processing tools.
Pandas: A library for data manipulation and analysis.
Run the Flask application to start the web server:

bash
Copy code
flask run
Access the application in your web browser by navigating to:

arduino
Copy code
http://127.0.0.1:5000/
Interact with RecipeCraft:

Enter your nutritional preferences and available ingredients.
Receive personalized recipe recommendations directly through the web interface.
