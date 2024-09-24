import gradio as gr
import torch
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import os

# Load pre-trained model and feature extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Define class names
class_names = model.config.id2label


# Function to handle image classification
def predict(image):
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    return class_names[predicted_class_id]


# Define Gradio interface
def classify_image(image):
    # Run classification
    category = predict(image)
    return category


# Gradio interface setup
interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(),
    title="VisionTrack - Smart Inventory Management System",
    description="VisionTrack is designed to leverage advanced computer vision and AI technologies to handle and monitor inventory. VisionTrack automates product recognition and stock tracking."
)
proxy_prefix = os.environ.get("PROXY_PREFIX")

# Run the Gradio app
if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix, share=True)
