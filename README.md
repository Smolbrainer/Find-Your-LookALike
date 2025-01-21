# Find Your Celebrity Lookalike! #
This project allows users to upload an image and find their celebrity lookalike by comparing facial features using machine learning models.

## Demo Video ##

https://github.com/user-attachments/assets/f4ee7823-b964-4f46-85d6-d0a93da7ba53

## Libraries Used

The following libraries are utilized in this project:

- **Flask**: A micro web framework used to create the web application, handle routing, and manage user interactions.
- **Pillow (PIL)**: A Python Imaging Library used for opening, manipulating, and saving images in various formats.
- **face_recognition**: A library built using dlib's state-of-the-art face recognition built with deep learning. It provides easy-to-use functions for detecting faces and computing facial embeddings.
- **SQLite3**: A lightweight disk-based database used to store facial encodings of celebrity images for quick retrieval and comparison.

## How Each Library Is Used

- **Flask**:
  - Serves the main web interface where users can upload their images.
  - Handles HTTP requests and responses between the client and server.
  - Renders HTML templates to display results to the user.

- **OpenCV**:
  - Handles image processing tasks such as reading user-uploaded images and converting them to the required format for analysis.
  - Performs image transformations and preprocessing, such as resizing and grayscale conversion, to ensure consistency and accuracy in facial recognition.
  - Aids in detecting and cropping faces in the images before passing them to the facial recognition module.

- **face_recognition**:
  - Detects faces within the uploaded images.
  - Computes facial embeddings (128-dimension vectors) that represent the unique features of each face.
  - Compares the user's facial embeddings with the stored celebrity embeddings to find the closest match.

- **SQLite3**:
  - Stores precomputed facial embeddings of celebrity images along with their metadata (e.g., encoding in bytes, image path).
  - Allows efficient querying to retrieve the most similar celebrity based on the user's facial embedding.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Smolbrainer/Find-Your-LookALike.git
