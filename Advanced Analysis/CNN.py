import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten
from keras.optimizers import Adam
from keras import backend as K
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


def preprocess_data_nn(df, year_condition):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'].dt.year.apply(year_condition)]
    df['ExtremeWeather'] = ((df['Max Temperature (F)'] > 92) | (df['Min Temperature (F)'] < 38) |
                            (df['Snow, Ice Pellets, Hail (in)'] > 2)).astype(int)
    X = df[['Total Entries', 'Total Exits']]
    y = df['ExtremeWeather']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_evaluate_nn(X_train, y_train, X_test, y_test, plot_filename):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Neural Network Model
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=200, batch_size=10)

    # Evaluate the model
    scores = model.evaluate(X_test, y_test)
    print("\nAccuracy: %.2f%%" % (scores[1]*100))

    # ROC Curve
    y_prob = model.predict(X_test).ravel()
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.savefig(plot_filename)
    plt.show()

# Main execution
df = pd.read_csv('merged_weather_traffic_data.csv')

# For data before 2020
X_train, X_test, y_train, y_test = preprocess_data_nn(df, lambda x: x < 2020)
train_and_evaluate_nn(X_train, y_train, X_test, y_test, 'roc_curve_nn_before_2020.png')

