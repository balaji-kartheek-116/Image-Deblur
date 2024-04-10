import cv2
import numpy as np
import streamlit as st

# Function to apply sharpening filter and deblur the image
def deblur_image(image):
    # Define a sharpening kernel to enhance details
    sharpen_kernel = np.array([[-1, -1, -1],
                               [-1, 9.125, -1],
                               [-1, -1, -1]])
    # Apply sharpening filter to enhance details
    sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)
    return sharpened_image

# Streamlit app
def main():
    st.title('Image Deblurring App')
    
    # Upload image
    uploaded_file = st.file_uploader("Upload a blurred image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        # Read the uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        
        # Display the original image
        st.image(image, caption='Original Blurred Image', use_column_width=True)
        
        # Deblur the image
        deblurred_image = deblur_image(image)
        
        # Display the deblurred image
        st.image(deblurred_image, caption='Deblurred Image', use_column_width=True)
        
# Run the app
if __name__ == "__main__":
    main()
