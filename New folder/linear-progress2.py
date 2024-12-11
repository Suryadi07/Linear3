import cv2
import numpy as np
import os

# Path to the image
image_path = "image.png"  # Ganti dengan path gambar Anda

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: File '{image_path}' not found. Check the path.")
else:
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load the image. Ensure the file is a valid image format.")
    else:
        # Display the original image
        cv2.imshow("Original Image", image)

        # Get image dimensions
        rows, cols = image.shape[:2]

        # 1. Rotation
        angle = 45  # Rotate 45 degrees
        rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
        cv2.imshow("Rotated Image", rotated_image)

        # 2. Scaling
        scale_x, scale_y = 1.5, 1.5  # Scale by 1.5x
        scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
        cv2.imshow("Scaled Image", scaled_image)

        # 3. Translation
        tx, ty = 50, 100  # Translate by 50 pixels (x) and 100 pixels (y)
        translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
        translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
        cv2.imshow("Translated Image", translated_image)

        # 4. Skewing
        skew_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])
        skewed_image = cv2.warpAffine(image, skew_matrix, (int(cols * 1.5), int(rows * 1.5)))
        cv2.imshow("Skewed Image", skewed_image)

        # Wait until any key is pressed and close all windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
