
from joblib import load
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved models

Prediction_model = load('E:/Study Material/College Projects/House_Price_Prediction_System/Project.joblib')



# Create Menu Option
with st.sidebar:
    
    
    selected = option_menu('HOUSE PRICE PREDICTION SYSTEM',
                           ['Show Prediction'],
                        
                           
                           default_index = 0)
    
if(selected == 'Show Prediction'):

    
    # page title
    st.title('House Price Prediction using ML')
    
    col1,col2 = st.columns(2)
    with col1:
         CRIM = st.text_input('Per capita crime rate by own', value = 0.0063)
    with col2:
         ZN = st.text_input('Proportion of residential land', value = 18)
    with col1:
         INDUS = st.text_input('Proportion of non-retail business acres per town', value = 2.31)
    with col2:
         CHAS = st.text_input('Charles River dummy variable', value = 0)
    with col1:
         NOX = st.text_input('Nitric oxides concentration', value = 0.538)
    with col2:
         RM = st.text_input('Average number of rooms per dwelling', value = 6.575)
    with col1:
         AGE = st.text_input('Proportion of owner-occupied units ', value= 65.2)
    with col2:
         DIS = st.text_input('weighted distances to five Boston employment centre', value= 4.09)
    with col1:
         RAD = st.text_input('Index of accessibility to radial highways', value = 1)
    with col2:
         TAX = st.text_input('Full-value property-tax rate per $10,000', value = 296)
    with col1:
         PTRATIO = st.text_input('Pupil-teacher ratio by town', value = 15.3)
    with col2:
         B = st.text_input('1000(Bk - 0.63)^2 where Bk is the proportion of blacks ', value = 396.9)
    with col1:
         LSTAT = st.text_input(' Percentage lower status of the population', value = 4.98)
    

     
    #creating button for prediction
    
    if st.button('Check'):
             if not CRIM or not  ZN or not INDUS  or not CHAS  or not NOX  or not RM  or not  AGE  or not DIS or not RAD or not TAX or not PTRATIO or not B or not LSTAT:
                st.warning('Please fill out this field before submitting!')
             else:
                 value = Prediction_model.predict([[ CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
                 cost = value.item()*1000
                 st.success("$ "+ str(cost))

        
        
