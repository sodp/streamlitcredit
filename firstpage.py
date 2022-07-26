import streamlit as st
import pickle
import numpy as np

'''
def load_model():
    with open("RFModel.pkl", 'rb') as file:
        data = pickle.load(file)
    return data
data = load_model() 
'''
data = pickle.load(open("sodp/streamlitcredit/main/RFModel.pkl", "rb"))
classification = data["model"]



def show_predict_page():
    
    #st.image('C://Users//Siddhant.Panda//Desktop/MiniProject//ML//header.png')
    st.markdown("<h1 style = 'text-align: center;'>Credit Score Bracket Prediction</h1>", unsafe_allow_html=True)
    instructions = """We need some information to predict your credit score bracket"""
    st.write(instructions)
    
    Age = st.slider("Age" , 0 ,100 ,0)
    Annual_Income = st.number_input('Annual Income ($)', 0, 10000000000)
    Monthly_Inhand_Salary    =  st.number_input("Monthly Inhand Salary ($)" , 0 , 10000000000)
    Num_Bank_Accounts      =  st.number_input("Number Bank Accounts" , 0 , 10)       
    Num_Credit_Card        =  st.number_input("Number of Credit Card" , 0 , 10)       
    Interest_Rate          =  st.number_input("Interest Rate" , 0 , 30)     
    Num_of_Loan            =  st.number_input("Num of Loan" , 0 , 30)      
    Num_of_Delayed_Payment =  st.number_input("Num of Delayed Payment" , 0 , 5000)
    Changed_Credit_Limit   =  st.number_input("Changed Credit Limit" , 0 ,36) 
    Outstanding_Debt       = st.number_input("Outstanding Debt($)" , 0 , 8000)    
    Total_EMI_per_month       = st.number_input("Total EMI per month($)" , 0 ,1000000)
    Amount_invested_monthly =  st.number_input("Amount Invested Monthly($)" , 0 , 1000000)
    Monthly_Balance         =  st.number_input("Monthly Balance ($)" , 0 , 100000)          
    
    ok = st.button("Calculate Credit Score Bracket")
 

    if ok:
        X = np.array([[Age, Annual_Income, Monthly_Inhand_Salary , Num_Bank_Accounts , Num_Credit_Card , Interest_Rate, Num_of_Loan , Num_of_Delayed_Payment , Changed_Credit_Limit ,Outstanding_Debt , Total_EMI_per_month , Amount_invested_monthly ,Monthly_Balance]])
        
        score = classification.predict(X)
        st.subheader("Your Estimated Bracket is!!!!!!!!!!!!")
        if(score == 0):
            st.write("Good Score :)")
        elif(score == 1):
            st.write("Standard Score :-)")
        elif(score == 0):
            st.write("Poor Score (:")


show_predict_page()
