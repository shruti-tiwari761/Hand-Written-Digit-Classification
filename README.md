# Handwritten Digit Recognition  

## 📌 Project Overview  
This project is a **Handwritten Digit Recognition System** built using Django and a deep learning model (TensorFlow/PyTorch). The user can draw a digit on a web interface, and the model will predict the digit.  

## 📦 Essential Libraries  
To run this project, install the following libraries:  

- **django** – Web framework for the backend  
- **pillow** – For image handling in Django  
- **numpy** – For numerical computations  
- **opencv-python** – For image preprocessing  
- **tensorflow** or **torch** + **torchvision** – For digit classification (choose one)  

## 🔹 Optional Libraries  
These libraries are not mandatory but can enhance the project:  

- **djangorestframework** – If you're building a REST API  
- **matplotlib** – For visualizing data  
- **scikit-learn** – For additional ML utilities  

## ⚡ Installation  
Use the following command to install the necessary dependencies:  

```sh
pip install django pillow numpy opencv-python tensorflow  # If using TensorFlow  
pip install django pillow numpy opencv-python torch torchvision  # If using PyTorch  
Run the Django server: python manage.py runserver
