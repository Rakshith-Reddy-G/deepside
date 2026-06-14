import os
import joblib
from django.conf import settings

# Global variables to cache the model and vectorizer
_model = None
_vectorizer = None

def load_artifacts():
    global _model, _vectorizer
    
    # Use BASE_DIR from settings to create absolute paths
    model_dir = os.path.join(settings.BASE_DIR, 'ml', 'artifacts')
    model_path = os.path.join(model_dir, 'model.joblib')
    vec_path = os.path.join(model_dir, 'vectorizer.joblib')
    
    if not os.path.exists(model_path) or not os.path.exists(vec_path):
        return False
    
    try:
        _model = joblib.load(model_path)
        _vectorizer = joblib.load(vec_path)
        return True
    except Exception:
        return False

def predict_side_effect(uid, drug_name, condition):
    global _model, _vectorizer
    
    if _model is None or _vectorizer is None:
        if not load_artifacts():
            return "Error: Model artifacts not found or corrupted"
            
    # Prepare input features same as training
    feature_text = f"{uid} {drug_name} {condition}"
    
    try:
        X_vec = _vectorizer.transform([feature_text])
        prediction = _model.predict(X_vec)[0]
        
        if prediction == 0:
            return 'Low Side Effect Found'
        else:
            return 'High Side Effect Found'
    except Exception as e:
        return f"Error during prediction: {str(e)}"
