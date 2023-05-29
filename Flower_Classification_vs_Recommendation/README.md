# Flower Classification & Recommendation

This notebook is the submission for team T1-G02. Follow the instructions below to set up the environment and run the notebook.


## Prerequisites

- Python 3.x
- pip package manager

## Local setup
1. Open a terminal or command prompt and navigate to the project directory.

2. Create a new virtual environment:

   ```shell
   python3 -m venv myenv
    ```
3. Activate the virtual environment:

+ For Windows:
    ```shell
   myenv\Scripts\activate
    ```
+ For macOS/Linux:
    ```shell
   source myenv/bin/activate
    ```
  
4. Install the required packages:
   ```shell
   pip3 install -r requirements.txt
    ```

## Run the Notebook
1. Start Jupyter Notebook
   ```shell
   jupyter notebook
    ```
2. In your web browser, navigate to the provided notebook URL (e.g., http://localhost:8888).
3. Open and run the notebooks in sequence.
- Notebook 1: Data Preprocessing and EDA:
   - Open Explanatory_Data_Analysist.ipynb.
   - Follow the instructions to preprocess and prepare the flower dataset.
- Notebook 2: Data Cleaning:
  - Open Data_Cleaning.ipynb.
  - Follow the instructions to train the flower classification model.
- Notebook 3: Task 1 - Classify flower type:
  - Open Classify_Images.ipynb.
  - Follow the instructions to evaluate the trained model and analyze the results.
- Notebook 4: Task 2 -  Recommend similar flowers:
  - Open Recommend_Similar_Image.ipynb.
  - Follow the instructions to make predictions on new flower images and visualize the results.
4. When you're finished with a notebook, save your changes and close the Jupyter Notebook interface.
5. Proceed to the next notebook in the sequence, opening and running it as described in step 3.
5. When you're finished, close the Jupyter Notebook interface and deactivate the virtual environment:
   ```shell
   deactivate
    ```

## Web app

Please run `streamlit run webapp/home.py` to open the streamlit web application

## License
This project is licensed under the MIT License.

