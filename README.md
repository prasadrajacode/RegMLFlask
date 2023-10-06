
#Creating the Model 

1. Understand Business Problem - Create a model to predict the salary of a new hire based on the historic data with test_score, interview_score and experience (I/P).  HR should be able to enter the details in a  form and should receive predicted salary from the model. 
2. Data Collection
￼
1. Data Exploration - info(),describe()
2. Data Cleaning 
3. Data Wrangling
4. Modelling  
    1. Train-Test Split 
    2. Creating model 
    3. Training model with Train Data (X_Train and Y_Train.        
5. Evaluate the model with Test Data(X_Test) 
   RMSE and R2
6. Dumping the model - Save the model to a local folder   

#Creating the Flask Application 

   1. Load the model 
   2. Creating the routes 
          /Index - For HTML page
          /predict For calling the model with predicted data
   3. Test /predict endpoint from the postman POST request 
   3. Creating the HTML Page and calling /predict route   
