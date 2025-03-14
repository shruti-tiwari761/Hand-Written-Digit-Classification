from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO
from django.shortcuts import render

# Load your trained ML model (Make sure the path is correct)
model = tf.keras.models.load_model("classifier/digit_classifier.h5")  # Update with actual path

@csrf_exempt  # Remove this once CSRF is properly handled
def classify_digit(request):
    """Handle digit classification logic."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            image_data = data.get("image")  # Extract base64 image
            
            if not image_data:
                return JsonResponse({"error": "No image data received"}, status=400)
            
            # Convert base64 to PIL image
            image_data = image_data.split(",")[1]  # Remove base64 header
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes)).convert("L")  # Convert to grayscale
            image = image.resize((28, 28))  # Resize to match model input shape
            image_array = np.array(image) / 255.0  # Normalize pixel values
            image_array = image_array.reshape(1, 28, 28, 1)  # Reshape for model input

            # Predict using the model
            predictions = model.predict(image_array)
            predicted_digit = np.argmax(predictions)  # Get the digit with highest probability

            return JsonResponse({"digit": int(predicted_digit)})

        except Exception as e:
            print(f"❌ Error: {e}")  # Print error in console
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request"}, status=400)
@csrf_exempt
def draw_page(request):
    """Render the HTML page with the canvas."""
    return render(request, "draw.html")