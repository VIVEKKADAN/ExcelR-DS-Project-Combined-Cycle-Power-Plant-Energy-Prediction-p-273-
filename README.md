# ExcelR-DS-Project-Combined-Cycle-Power-Plant-Energy-Prediction-p-273-

Business Objective
The primary goal of this project is to optimize the performance of a combined-cycle power plant. This type of power plant employs both gas turbines and steam turbines in a single cycle to generate electricity. The project aims to model the energy production of the power plant based on various input variables, such as exhaust vacuum, ambient conditions (temperature, pressure, humidity), and predict the net hourly electrical energy output. By doing so, the plant's efficiency and energy generation can be enhanced.


Data Set Details
The dataset used for this project contains 9568 observations collected over six years from a combined-cycle power plant operating at full load. The dataset comprises five variables:

Temperature: Ambient temperature in degrees Celsius.
Exhaust Vacuum: Vacuum level in cm Hg.
Ambient Pressure: Atmospheric pressure in millibar.
Relative Humidity: Humidity level in percentage.
Energy Production: Net hourly electrical energy output in MW.


Methodology
Data Preprocessing: The dataset was cleaned by handling missing values, outliers, and ensuring data consistency. Feature scaling and normalization were performed to bring all variables to a common scale.

Exploratory Data Analysis (EDA): The relationships between input variables and energy production were analyzed through visualizations. This helped to identify any patterns or correlations.

Modeling: The objective was to create a predictive model for energy production. A stack model was chosen to combine the strengths of multiple algorithms. This involved training different machine learning algorithms (e.g., Random Forest, Gradient Boosting, etc.) and blending their predictions using another algorithm (e.g., Linear Regression).

Model Evaluation: The model's performance was evaluated using appropriate metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared. Cross-validation was employed to ensure the model's robustness.

Deployment: The final model was deployed using Streamlit, a Python library for creating interactive web applications. The deployed web application allows users to input ambient variables, such as temperature, exhaust vacuum, ambient pressure, and humidity, and obtain a prediction of the net hourly electrical energy output.

Deployment
The deployment of the final model was achieved using Streamlit. Streamlit provides an easy way to create web applications directly from Python scripts. The deployed web application allows users to access the predictive model's functionality through a user-friendly interface. Users can input the ambient conditions, and the application will provide an estimated energy production based on the trained stack model.

The Streamlit app can be accessed by running the following command in the terminal:

streamlit run app.py


Conclusion
By creating a predictive model for energy production in a combined-cycle power plant and deploying it using Streamlit, this project contributes to optimizing the plant's performance. Users can now make informed decisions about plant operation based on predicted energy production under various ambient conditions. The stack model approach ensures accurate predictions, and the user-friendly interface enhances usability.

Feel free to explore the code in this repository and the deployed Streamlit app to learn more about the project's details and outcomes. If you have any questions or feedback, please don't hesitate to reach out.
