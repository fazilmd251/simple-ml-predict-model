# Ride Predictor

A simple web application that predicts the number of weekly taxi rides based on input features using a trained machine learning model.

## Features

- Predict weekly riders using price per week, population, monthly income, and average parking per month.
- Built with Flask and scikit-learn.
- Clean and responsive UI using Tailwind CSS.

## Project Structure

uber-project/
├── app.py # Flask application
├── MLmode.ipynb # Jupyter notebook for model training
├── model.pkl # Trained ML model
├── poetry.lock # Poetry dependency lock file
├── pyproject.toml # Poetry project configuration
├── taxi.csv # Dataset used for training
├── static/ # CSS and other static files
├── templates/ # HTML templates
└── README.md # This file

## Getting Started

### Prerequisites

- Python 3.8+
- Poetry (for dependency management)

### Installation

1. Clone the repository:
git clone https://github.com/yourusername/uber-project.git
cd uber-project

2. Install dependencies using Poetry:
poetry install


3. Activate the virtual environment:
poetry shell

### Usage

1. Start the Flask app:
python app.py

2. Open your browser and go to `http://localhost:5000`.

3. Enter the required features and click "Predict" to see the result.

## Data

- The dataset (`taxi.csv`) contains historical data on taxi rides and related features.
- The model is trained using scikit-learn's Linear Regression.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors of scikit-learn, Flask, and Tailwind CSS for their excellent libraries.
