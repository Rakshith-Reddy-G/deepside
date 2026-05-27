# DeepSide: A Deep Learning Framework for Drug Side Effect Prediction

> An AI-powered drug side effect prediction system built using Deep Learning, Machine Learning, Django, and Biomedical datasets to identify adverse drug reactions before clinical deployment.


# 📌 Project Overview

DeepSide is a biomedical AI framework designed to predict potential drug side effects using:

- Drug chemical structures

- SMILES molecular representations

- Gene expression data

- Machine Learning & Deep Learning models

The system helps reduce:

- Drug development costs

- Clinical trial failures

- Unexpected adverse drug reactions (ADRs)

By leveraging AI-driven prediction models, researchers can identify dangerous side effects early in the drug discovery pipeline.

---

# 🚀 Key Features

- Drug Side Effect Prediction

- Multi-Model Machine Learning Pipeline

- Django Web Application

- User Authentication System

- Dataset Processing & Feature Engineering

- Visualization Charts (Pie & Line Charts)

- Prediction Confidence Analysis

- Biomedical Data Handling

- Multi-Class Side Effect Analysis

---

# 🧠 Technologies Used

## 🔹 Frontend Technologies

- HTML5

- CSS3

- JavaScript

- Bootstrap

- Django Templates

---

## 🔹 Backend Technologies

- Python 3.x

- Django Framework

---

## 🔹 Machine Learning & Deep Learning Libraries

### Core AI Libraries

- Scikit-learn

- Pandas

- NumPy

### Machine Learning Models Used

- MLPClassifier (Multi-Layer Perceptron)

- Logistic Regression

- Support Vector Machine (SVM)

- Voting Classifier Ensemble

### NLP & Feature Extraction

- CountVectorizer

---

# 🗄️ Database

- MySQL

- WAMP Server
  
---

# 🧪 Datasets Used

## 1. LINCS L1000 Dataset

Used for:

- Gene expression profiling

- Drug-cell interaction analysis

## 2. SIDER Dataset

Used for:

- Drug side effect validation

- ADR mapping

---

# 🏗️ System Architecture

```text

User Interface

      ↓

Django Views & Controllers

      ↓

Machine Learning Prediction Engine

      ↓

Feature Extraction & Vectorization

      ↓

Dataset Processing

      ↓

MySQL Database

```

---

# 📂 Project Structure

```bash

deepside/

│

├── templates/

│   ├── login.html

│   ├── Register1.html

│   ├── Predict_Drug_Side_Effect_Type.html

│

├── static/

│   ├── css/

│   ├── js/

│   ├── images/

│

├── models.py

├── views.py

├── urls.py

├── settings.py

├── manage.py

│

├── datasets/

│   ├── Datasets.csv

│

├── requirements.txt

└── README.md

```

---

# ⚙️ Installation Guide

## 📌 Prerequisites

Before running the project, install:

- Python 3.7+

- MySQL Server

- WAMP/XAMPP (optional)

- pip

- Git

---

# 🔧 Step 1: Clone the Repository

```bash

git clone https://github.com/Rakshith-Reddy-G/deepside.git

```

```bash

cd deepside

```

---

# 🔧 Step 2: Create Virtual Environment

## Windows

```bash

python -m venv venv

```

Activate virtual environment:

```bash

venv\Scripts\activate

```

---

## macOS/Linux

```bash

python3 -m venv venv

```

Activate:

```bash

source venv/bin/activate

```

---

# 🔧 Step 3: Install Dependencies

```bash

pip install -r requirements.txt

```

If `requirements.txt` is missing, install manually:

```bash

pip install django

pip install pandas

pip install numpy

pip install scikit-learn

pip install mysqlclient

```

---

# 🔧 Step 4: Configure MySQL Database

Create a MySQL database:

```sql

CREATE DATABASE deepside_db;

```

---

# 🔧 Step 5: Update Django Database Settings

Open:

```text

settings.py

```

Update:

```python

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'deepside_db',

        'USER': 'root',

        'PASSWORD': 'your_password',

        'HOST': 'localhost',

        'PORT': '3306',

    }

}

```

---

# 🔧 Step 6: Run Migrations

```bash

python manage.py makemigrations

```

```bash

python manage.py migrate

```

---

# 🔧 Step 7: Start Development Server

```bash

python manage.py runserver

```

---

# 🌐 Access the Application

Open browser:

```text

http://127.0.0.1:8000/

```

---

# 🔐 Authentication Module

The system supports:

- User Registration

- User Login

- Session Management

- Profile Viewing

---

# 📈 Visualization Features

- Pie Chart Analysis

- Line Chart Analysis

- Prediction Distribution

- Accuracy Comparisons

---

# 📬 Contact

## Rakshith Reddy Gaddam

- GitHub: https://github.com/Rakshith-Reddy-G

- LinkedIn: https://linkedin.com/in/rakshith-reddy-gaddam-6a7715281

- Email: gaddamrakshithreddy3625@gmail.com
