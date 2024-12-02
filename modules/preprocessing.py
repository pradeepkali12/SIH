import cv2

def preprocess_document(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    _, binarized_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return binarized_image
