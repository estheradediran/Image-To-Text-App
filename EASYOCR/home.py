import easyocr as ocr #OCR
import streamlit as st #web app
from PIL import Image #image processing
import numpy as np #image processing


def app():
    #def set_page_config():
     #   st.set_page_config(
      #  page_title="Home",
       # )
    #set_page_config()
    #title
    st.title("Extract Text From Images In English")

   
    #image upload
    image = st.file_uploader(label = "Upload your image here", type=['png','jpg','jpeg'])

    #st.cache decorator lets you cache meaning your application will make it load faster 
    @st.cache_data
    def load_model():
        reader = ocr.Reader(['en'],model_storage_directory='.')
        return reader

    reader = load_model() #load model

    if image is not None:
        input_image = Image.open(image) #read image
        st.image(input_image) #display image

        with st.spinner("🤖...loading...🤖"):
            result = reader.readtext(np.array(input_image))
            result_text = []
            for text in result:
                result_text.append(text[1])

            
            st.write(*result_text)
        #st.success("text extraction successful")

    #else:
       # st.write("upload an Image")
    #st.caption("")




