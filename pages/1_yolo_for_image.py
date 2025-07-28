

import streamlit as st
from yolo_predictions_1 import YOLO_Pred
from PIL import Image
import numpy as np



st.set_page_config(page_title="Hardware Tool Kit Detection",
                   layout='wide',
                   page_icon='./images/object.png')

st.title('Welcome to the Hardware Tool Detection App')
st.write('Please Upload Image to get detections')

with st.spinner('Please wait model is loading'):
    yolo=YOLO_Pred(onnx_model='./best.onnx',
                   data_yaml='./data.yaml')
    st.balloons()

def upload_image():

    image_file=st.file_uploader(label='Upload Image')
    if image_file is not None:
        size_mb=image_file.size/(1024**2)
        file_details={"filename":image_file.name,
                    "filetype":image_file.type,
                    "filesize":"{:,.2f} MB".format(size_mb)}
        st.json(file_details)

        if file_details['filetype'] in ('image/png','image/jpeg'):
            st.success('Valid Image File Type')
            return {"file":image_file,
                    "details":file_details}
        else:
            st.error('Invalid Image File Type')
            st.error('Upload only jpeg or png format')
            return None
        
def main():
    object=upload_image()

    if object:
        prediction=False
        image_obj=Image.open(object['file'])
        

        col1,col2=st.columns(2)

        with col1:
            st.info('Preview of image')
            st.image(image_obj)

        with col2:
            st.subheader('Check below for thee file details')
            st.json(object['details'])
            button=st.button('Get Detection from YOLO')
            if button:
                image_array=np.array(image_obj)
                pred_img=yolo.predictions(image_array)
                pred_img_obj=Image.fromarray(pred_img)
                prediction=True
        if prediction:
            resized_img = pred_img_obj.resize((800, 600))  # Resize for visibility
            st.image(resized_img, caption="Detection Output", use_container_width=False)

        
        
        #if prediction:
            #st.image(pred_img_obj)

if __name__ == "__main__":
    main()