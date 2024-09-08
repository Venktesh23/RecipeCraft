from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)  # Initialize the Flask app

# Load the dataset containing recipes
# Absolute path example
data = pd.read_csv("Notebook/recipe_final (1).csv")

# Preprocess Ingredients by converting the ingredient list into TF-IDF vectors
vectorizer = TfidfVectorizer()
X_ingredients = vectorizer.fit_transform(data['ingredients_list'])

# Normalize Numerical Features (e.g., calories, fat, etc.) using StandardScaler
scaler = StandardScaler()
X_numerical = scaler.fit_transform(data[['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']])

# Combine numerical and textual (ingredient) features into a single feature matrix
X_combined = np.hstack([X_numerical, X_ingredients.toarray()])

# Train KNN Model using Euclidean distance and considering 3 nearest neighbors
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(X_combined)

# Function to recommend recipes based on user input
def recommend_recipes(input_features):
    # Scale the numerical part of input features
    input_features_scaled = scaler.transform([input_features[:7]])
    # Transform the ingredient part of input features using the TF-IDF vectorizer
    input_ingredients_transformed = vectorizer.transform([input_features[7]])
    # Combine scaled numerical and transformed ingredient features
    input_combined = np.hstack([input_features_scaled, input_ingredients_transformed.toarray()])
    # Get the nearest neighbors (similar recipes) to the input
    distances, indices = knn.kneighbors(input_combined)
    # Return the top 5 recommended recipes with name, ingredients, and image URL
    recommendations = data.iloc[indices[0]]
    return recommendations[['recipe_name', 'ingredients_list', 'image_url']].head(5)

# Function to truncate long product names for display
def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text

# Main route for the Flask app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        calories = float(request.form['calories'])
        fat = float(request.form['fat'])
        carbohydrates = float(request.form['carbohydrates'])
        protein = float(request.form['protein'])
        cholesterol = float(request.form['cholesterol'])
        sodium = float(request.form['sodium'])
        fiber = float(request.form['fiber'])
        ingredients = request.form['ingredients']
        # Combine the user input into a single list of features
        input_features = [calories, fat, carbohydrates, protein, cholesterol, sodium, fiber, ingredients]
        # Get recipe recommendations based on user input
        recommendations = recommend_recipes(input_features)
        # Render the index.html template with the recommendations and truncation function
        return render_template('index.html', recommendations=recommendations.to_dict(orient='records'), truncate=truncate)
    # Render an empty recommendation list when loading the page initially
    return render_template('index.html', recommendations=[])

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)

