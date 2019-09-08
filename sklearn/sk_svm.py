from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4)

clf = SVC(gamma='scale')

clf.fit(X_train, y_train)  
print(clf.score(X_test, y_test))
print(list(clf.predict(X_test[:20])))
print(list(y_test[:20]))

X_train, X_test, y_train, y_test=train_test_split(iris.data, iris.target_names[iris.target],test_size=0.2)
clf.fit(X_train, y_train)

print(list(clf.predict(X_test[:10])))

print(list(y_test[:10]))
