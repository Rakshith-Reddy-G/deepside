import os
import joblib

# Global variables to cache the model and vectorizer
_model = None
_vectorizer = None

def load_artifacts(model_dir='ml/artifacts'):
    global _model, _vectorizer
    
    model_path = os.path.join(model_dir, 'model.joblib')
    vec_path = os.path.join(model_dir, 'vectorizer.joblib')
    
    if not os.path.exists(model_path) or not os.path.exists(vec_path):
        # In a real app, you might want to trigger training here or raise an error
        return False
    
    _model = joblib.load(model_path)
    _vectorizer = joblib.load(vec_path)
    return True

def predict_side_effect(uid, drug_name, condition):
    global _model, _vectorizer
    
    if _model is None or _vectorizer is None:
        if not load_artifacts():
            return "Error: Model not trained"
            
    # Prepare input features same as training
    feature_text = f"{uid} {drug_name} {condition}"
    
    X_vec = _vectorizer.transform([feature_text])
    prediction = _model.predict(X_vec)[0]
    
    if prediction == 0:
        return 'Low Side Effect Found'
    else:
        return 'High Side Effect Found'
