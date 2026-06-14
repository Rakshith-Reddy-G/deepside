import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression

def train_model(csv_path='Datasets.csv', model_dir='ml/artifacts'):
    print(f"Loading data from {csv_path}...")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path, encoding='latin-1')
    
    # Preprocessing
    def apply_results(Rating):
        try:
            if int(Rating) <= 7:
                return 0
            else:
                return 1
        except (ValueError, TypeError):
            return 0
    
    df['Results'] = df['Rating'].apply(apply_results)
    
    # Feature Engineering: Combine UID, Drug_Name, and Condition for a slightly better model
    # The original only used UID, which is very weak.
    df['features'] = df['UID'].astype(str) + " " + df['Drug_Name'].astype(str) + " " + df['Condition'].astype(str)
    
    X = df['features']
    y = df['Results']
    
    print("Vectorizing features...")
    cv = CountVectorizer()
    X_vec = cv.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.20, random_state=42)
    
    print("Training models...")
    models = []
    
    mlpc = MLPClassifier(max_iter=1000, random_state=42).fit(X_train, y_train)
    models.append(('MLPClassifier', mlpc))
    
    lin_clf = svm.LinearSVC(max_iter=1000, random_state=42)
    lin_clf.fit(X_train, y_train)
    models.append(('svm', lin_clf))
    
    reg = LogisticRegression(random_state=42, solver='lbfgs', max_iter=1000).fit(X_train, y_train)
    models.append(('logistic', reg))
    
    print("Creating Voting Classifier...")
    classifier = VotingClassifier(models)
    classifier.fit(X_train, y_train)
    
    # Evaluate
    score = classifier.score(X_test, y_test)
    print(f"Model Accuracy: {score:.4f}")
    
    # Save artifacts
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        
    joblib.dump(classifier, os.path.join(model_dir, 'model.joblib'))
    joblib.dump(cv, os.path.join(model_dir, 'vectorizer.joblib'))
    print(f"Artifacts saved to {model_dir}")

if __name__ == "__main__":
    train_model()
