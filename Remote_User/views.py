from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import ClientRegister_Model, drug_side_effect_prediction, detection_ratio, detection_accuracy

def index(request):
    return render(request, 'RUser/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = ClientRegister_Model.objects.get(username=username)
            if check_password(password, user.password):
                request.session["userid"] = user.id
                return redirect('ViewYourProfile')
            else:
                messages.error(request, 'Invalid username or password')
        except ClientRegister_Model.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    return render(request, 'RUser/login.html')

def Register1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
        ClientRegister_Model.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            phoneno=phoneno,
            country=country,
            state=state,
            city=city,
            address=address,
            gender=gender
        )
        messages.success(request, 'Registration Successful! Please login.')
        return redirect('login')
    return render(request, 'RUser/Register1.html')

def ViewYourProfile(request):
    if 'userid' not in request.session:
        return redirect('login')
    userid = request.session['userid']
    user = ClientRegister_Model.objects.get(id=userid)
    return render(request, 'RUser/ViewYourProfile.html', {'object': user})

def Predict_Drug_Side_Effect_Type(request):
    if 'userid' not in request.session:
        return redirect('login')
    
    if request.method == "POST":
        import pandas as pd
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.ensemble import VotingClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.neural_network import MLPClassifier
        from sklearn import svm
        from sklearn.linear_model import LogisticRegression
        
        uid = request.POST.get('uid')
        Drug_Name = request.POST.get('Drug_Name')
        Condition1 = request.POST.get('Condition1')
        
        try:
            df = pd.read_csv('Datasets.csv', encoding='latin-1')
            
            def apply_results(Rating):
                if int(Rating) <= 7:
                    return 0
                else:
                    return 1
            
            df['Results'] = df['Rating'].apply(apply_results)
            
            X = df['UID'].apply(str)
            y = df['Results']
            
            cv = CountVectorizer()
            X = cv.fit_transform(X)
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
            
            models = []
            
            mlpc = MLPClassifier(max_iter=1000, random_state=42).fit(X_train, y_train)
            models.append(('MLPClassifier', mlpc))
            
            lin_clf = svm.LinearSVC(max_iter=1000, random_state=42)
            lin_clf.fit(X_train, y_train)
            models.append(('svm', lin_clf))
            
            reg = LogisticRegression(random_state=42, solver='lbfgs', max_iter=1000).fit(X_train, y_train)
            models.append(('logistic', reg))
            
            classifier = VotingClassifier(models)
            classifier.fit(X_train, y_train)
            
            predict_text = cv.transform([str(uid)])
            y_pred = classifier.predict(predict_text)
            
            prediction = int(y_pred[0])
            
            if prediction == 0:
                val = 'Low Side Effect Found'
            else:
                val = 'High Side Effect Found'
            
            drug_side_effect_prediction.objects.create(
                uid=uid,
                Drug_Name=Drug_Name,
                Condition1=Condition1,
                Prediction=val
            )
            
            return render(request, 'RUser/Predict_Drug_Side_Effect_Type.html', {'objs': val})
        
        except Exception as e:
            messages.error(request, f'Error in prediction: {str(e)}')
    
    return render(request, 'RUser/Predict_Drug_Side_Effect_Type.html')

def prediction_history(request):
    if 'userid' not in request.session:
        return redirect('login')
    predictions = drug_side_effect_prediction.objects.all().order_by('-date_time')
    return render(request, 'RUser/prediction_history.html', {'predictions': predictions})

def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('index')
