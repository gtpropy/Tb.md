#!/bin/bash

# Root directory
ROOT_DIR=$(pwd)

# Create directories for client (React) and server (Flask)
echo "Creating project structure..."
mkdir -p client server/api server/config server/models server/routes

# Initialize the React app in client/
echo "Setting up React app..."
cd $ROOT_DIR/client
npx create-react-app .  # Set up React app in the client directory

# Navigate back to the root directory
cd $ROOT_DIR

# Set up Flask app in the server/ folder
echo "Setting up Flask app..."
cd $ROOT_DIR/server
touch app.py requirements.txt  # Create the entry point and dependency files

# Add Flask dependencies in requirements.txt
echo "Flask==2.1.0" > requirements.txt
echo "flask-cors" >> requirements.txt  # Add CORS support

# Create environment variable file
cd $ROOT_DIR
echo "Creating .env file..."
touch .env
echo "SECRET_KEY=mysecretkey" > .env

# Instructions for running the frontend and backend
echo "---------------------------------------------------"
echo "Project structure created successfully!"
echo "To run the React frontend:"
echo "  1. cd client"
echo "  2. npm start"
echo ""
echo "To run the Flask backend:"
echo "  1. cd server"
echo "  2. pip install -r requirements.txt"
echo "  3. python app.py"
echo "---------------------------------------------------"
