# COSC 2789 Group Assignment 3
## Colon Cancer - Predictions
#### Lecturer: Dr. Thuy Nguyen
#### Group 3
#### Group Members:
    -  Tran Phan Hoang Phuc - s3929597
    -  Nguyen Xuan Thanh - s3915468
    -  Bui Minh Nhat - s3878174

Project structure :

```
|
|
|__requirements.txt
|
|__converted_data (contains process data)
|
|__patch_images (contains image dataset)
|
|__original_data (contains original data)
|       |
|       |_data_labels_extraData.csv 
|       |
|       |_data_labels_mainData.csv
|
|__EDA_PreProcessing.ipynb
|
|__DataCleaning.ipynb
|
|__EDA_PostProcessing.ipynb
|
|__FeatureEngineering.ipynb
|
|__Model_Constructing_XGBoost.ipynb
|
|__Model_Constructing_Lightgbm.ipynb
|
|__Model_Constructing_RCC_Net.ipynb
|
|__Model_Constructing_Ensemble.ipynb

```

## Prerequisites:
-  MacOS or Linux operating system
-  Python 3.9
-  Jupyter

## Installation:
- Create new virtual environment
- Install requirements.txt
- Cd to the project directory
- Run Jupyter

Notebook including and executing order:
<br>

                -   1) EDA_PreProcessing.ipynb
                -   2) DataCleaning.ipynb
                -   3) EDA_PostProcessing.ipynb
                -   4) FeatureEngineering.ipynb
                -   5) Model_Constructing_XGBoost.ipynb
                -   6) Model_Constructing_Lightgbm.ipynb
                -   7) Model_Constructing_RCC_Net.ipynb
                -   8) Model_Constructing_Ensemble.ipynb
                
## Project Information
Cancer is one of the most dangerous and life-threatening diseases in modern society, it is responsible for I out of
every 6 deaths in 2021 worldwide, an alarming statistic about this disease. As the mortality rate is quite
significant and has an extremely high chance of growing over time, it's crucial to identify whether or not a
patient has developed cancerous cells during the early stages of examination. This can create a major difference
in the long-term survival rate for the patient as they can be accompanied for assistance and support. Considering
this, the team has created and built a machine-learning model for classification to determine a patient's odds of
developing or already having a cancer cell within their body. Inside the study the team has developed, we have
created and tested three different classification models: traditional machine-learning models, XGBoost,
LightGBM, and Voting Classifier. As well as a convolutional neural network model named RCC-Net.
