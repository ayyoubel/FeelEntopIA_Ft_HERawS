import streamlit as st
from PIL import Image

def main():
    st.title("Simple Streamlit App with PIL")
    st.write("Upload an image and perform basic operations using PIL.")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        
        image = Image.open(uploaded_image)
        
        st.subheader("Image Operations")
        operation = st.selectbox("Select an operation", ("Original", "Rotate", "Resize"))
        
        if operation == "Rotate":
            angle = st.slider("Select rotation angle", -360, 360, 0)
            rotated_image = image.rotate(angle)
            st.image(rotated_image, caption="Rotated Image", use_column_width=True)
        
        elif operation == "Resize":
            width = st.slider("Enter new width", 1, 1000, image.width)
            height = st.slider("Enter new height", 1, 1000, image.height)
            resized_image = image.resize((width, height))
            st.image(resized_image, caption="Resized Image", use_column_width=True)

if __name__ == "__main__":
    main()
