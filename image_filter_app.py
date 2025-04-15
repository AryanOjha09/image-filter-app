from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

# ✅ CHANGE THIS to your actual image name if it's not sample.jpg
image_path = "sample.jpg"  

try:
    # Load the image
    img = Image.open(image_path)

    # Apply filters
    gray_img = img.convert("L")  # Grayscale
    blur_img = img.filter(ImageFilter.BLUR)  # Blur filter
    edge_img = img.filter(ImageFilter.FIND_EDGES)  # Edge detection

    # Plot all images using Matplotlib
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title("Grayscale")
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(blur_img)
    plt.title("Blur")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(edge_img)
    plt.title("Edge Detection")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"❌ Error: The file '{image_path}' was not found.")
    print("👉 Please make sure the image is in the same folder as this script.")
