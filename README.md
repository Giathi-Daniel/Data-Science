# Road Accident Severity Prediction

This repository houses a linear regression model developed to estimate specific outcomes of road accidents by examining several factors, such as speed level, precipitation, road type, time of occurrence, and alcohol influence. The idea here is to analyze patterns to forecast the result of an accident and offer recommendations that can help reduce traffic accidents in developing nations.

## Project Overview

### Problem Statement:
Hypothetical factors have been identified, including speed, weather conditions, type of road, driver behavior, and the like, as far as the intensity of road accidents. Linear regression is then employed to estimate the likelihood for a given level of each of the factors considered herein on the expectations that the stakeholders will take precautionary measures to prevent the occurrence of severe road accidents.

### Dataset:
This dataset is a fictional collection of road accidents with the following columns:
- `Speed`: Speed of the vehicle in km/h
- `Weather`: Encoded (0 = Clear, 1 = Rainy, 2 = Foggy, etc.)
- `Road_Type`: Encoded (0 = Urban roads, 1 = Highways, etc.)
- `Time_of_Day`: Time of the accident (in 24-hour format)
- `Alcohol`: Binary (0 = No, 1 = Yes for alcohol involvement)
- `Driver_Age`: Age of the driver in years
- `Vehicle_Type`: Encoded (0 = Car, 1 = Motorbike, 2 = Truck, etc.)
- `Vehicles_Involved`: Number of vehicles involved in the accident
- `Seatbelt`: Binary (0 = No, 1 = Yes for seatbelt usage)
- `Accident_Severity`: The outcome variable (1 = Minor, 2 = Serious, 3 = Fatal)

### Key Features:
- Linear Regression Model for Predicting Accident Severity.
- Data-driven insights into risk factors that determine the severity of accidents.
- It may help prevent traffic accidents and guarantee better road safety.

## Installation

To use or modify this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/road-accident-severity.git
   cd road-accident-severity
   ```

2. **Install the required Python packages:**
   The required libraries are listed in the `requirements.txt` file. You can install them using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the code:**
   Ensure you have a working dataset (or use the provided sample data in the code) and execute the script to train the model and make predictions:
   ```bash
   python road_accident_severity.py
   ```

## Usage

You can use a linear regression model to predict the severity of a road accident based on various independent variables. For instance, to predict the accident severity in case of an event with conditions such as:
- Speed: 85 km/h
- Weather: Clear (0)
- Road Type: Highway (1)
- Time of Day: 10 AM
- Alcohol Involvement: Yes (1)
- Driver's Age: 33 years
- Vehicle Type: Car (0)
- Vehicles Involved: 2
- Seatbelt: Yes (1)

Replace the values in `road_accident_severity.py` with your scenario; the model will predict the accident's severity.

## Model Performance

In the next step, the performance is examined using model performance metrics like:
- **Mean Squared Error (MSE)**: The average of the squared differences between the predicted and actual severity of accidents
- **R-squared Score (R²)**: Indicates how well the independent variables explain the variance in accident severity.

### Example Results:
```bash
Mean Squared Error: 0.35
R-squared Score: 0.78
```

## Future Improvements
- Extending the model by using other techniques for machine learning, like decision trees or random forests. 
- It includes more features such as road conditions, traffic density, and vehicle maintenance records. 
- Integrating the model into a dashboard for real-time accident severity prediction.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.


