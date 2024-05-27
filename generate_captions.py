import os
from PIL import Image
import matplotlib.pyplot as plt

BASE_DIR='/uploads'

def generate_caption(image_name):
    # Load the image
    image_id = image_name.split('.')[0]
    img_path = os.path.join(BASE_DIR, "Images", image_name)
    image = Image.open(img_path)

    # Display actual captions
    captions = mapping[image_id]
    print("Actual Captions:")
    for caption in captions:
        print(caption)

    # Predict the caption
    y_pred = predict_caption(model, features[image_id], tokenizer, max_length)
    print("Predicted Caption:")
    print(y_pred)

    # Display the image
    plt.imshow(image)
    plt.show()  