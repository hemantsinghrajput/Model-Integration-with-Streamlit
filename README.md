# Model-Integration-with-Streamlit
This script is a Streamlit application that allows users to predict the quality of wine based on input features. Here's a brief description of the script:

The script begins by importing the necessary libraries: streamlit, numpy, pickle, and PIL (Python Imaging Library).

It then loads the pre-trained scaler and logistic regression (LR) model using the pickle.load() function. The scaler is used to transform the input features, and the LR model is used for making predictions.

The script opens an image file of a wine bottle using the Image.open() function from PIL and displays it using st.image(). This provides a visual representation for the user interface.

The script utilizes st.number_input() to prompt the user to enter values for the volatile acidity, citric acid, total sulfur dioxide, sulphates, and alcohol of the wine. These inputs are assigned to the corresponding variables va, ca, sd, su, and al.

A button labeled "Predict" is created using st.button().

When the user clicks the "Predict" button, the if btn_click: condition is triggered.

Inside the condition, the script checks if all the input variables (va, ca, sd, su, and al) have valid values.

If the inputs are valid, the script creates a numpy array (query_point) with the input values and reshapes it to match the expected shape for prediction. The scaler is then applied to the query_point using scaler.transform().

The pre-trained logistic regression model (lr_model) predicts the wine quality by calling lr_model.predict() on the transformed query point. The predicted result is stored in the pred variable.

Finally, if the inputs are valid, the script uses st.success() to display the predicted wine quality (pred[0]). If any input values are missing or invalid, the script uses st.error() to prompt the user to enter the values properly.

This script provides a simple and interactive way to predict the quality of wine using a pre-trained model.
