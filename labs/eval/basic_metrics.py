# Basic regression metric (MAE)
from sklearn.metrics import mean_absolute_error

y_true = [3.0, 4.5, 5.0]
y_pred = [2.5, 4.0, 5.5]
print('MAE:', mean_absolute_error(y_true, y_pred))
