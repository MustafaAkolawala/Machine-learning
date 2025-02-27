# Step 1: Install LightGBM if not already installed
# !pip install lightgbm
# Step 2: Import necessary libraries
import lightgbm as lgb
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Step 3: Load the Breast Cancer dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)
# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 5: Create the LightGBM model
lgb_model = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.1)
# Step 6: Train the model
lgb_model.fit(X_train, y_train)
# Step 7: Make predictions
y_pred = lgb_model.predict(X_test)
# Step 8: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy of LightGBM model: {accuracy * 100:.2f}%")
print("\nClassification Report By Sudheendra 211P048:")
print(classification_report(y_test, y_pred, target_names=data.target_names))
# Optional: Feature Importance Plot
lgb.plot_importance(lgb_model, max_num_features=10, importance_type='split', title='Feature Importance By Sudheendra 211P048')
plt.show()