import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version = 1)
X = mnist['data']/255.0
Y = mnist['target'].astype(int)

X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 , random_state=42 )

model = LogisticRegression(max_iter=10000)
model.fit(X_train , Y_train)


y_pred = model.predict(X_test)
accuray = metrics.accuracy_score(Y_test, y_pred)

print("test accuracy" , accuray)

for i in range(5):
    plt.imshow(X_test.iloc[i].values.reshape(28, 28), cmap=plt.cm.binary)
    plt.title(f"predicted: {y_pred[i]} , Actual: {Y_test.iloc[i]}") 
    plt.show()