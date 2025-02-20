import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2
from scikeras.wrappers import KerasRegressor  # Corrected import

# Load your data
data = pd.read_csv('p4_combined_data.csv')

# Preprocessing
data['Start_Date'] = pd.to_datetime(data['Start_Date'])
data['Is_Weekend'] = data['Start_Date'].dt.dayofweek.apply(lambda x: 1 if x >= 5 else 0)

# Selecting features and target
X = data[['Daily_Cases', 'Is_Weekend']]
y = data['Total_Rides']

# Normalizing the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Function to create model, required for KerasRegressor
def create_model():
    model = Sequential()
    model.add(Dense(64, input_dim=X_scaled.shape[1], activation='relu', kernel_regularizer=l2(0.001)))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Wrap Keras model using KerasRegressor
model = KerasRegressor(model=create_model, epochs=100, batch_size=10, verbose=0)

# K-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Results from K-fold cross-validation
results = cross_val_score(model, X_scaled, y, cv=kfold, scoring='neg_mean_squared_error')
print("Cross-validated MSE:", -results.mean())
print("Cross-validated Std of MSE:", results.std())
