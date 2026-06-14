# DeepSide: A Deep Learning Framework for Drug Side Effect Prediction

DeepSide is a biomedical AI framework designed to predict potential drug side effects using machine learning models. This project has been modernized for production-ready deployment.

## 🚀 Key Features
- **Fast Inference:** Models are pre-trained and serialized, ensuring sub-second prediction times.
- **Production Ready:** Configured for deployment on platforms like Render, Railway, or Heroku.
- **Security:** Secrets managed via environment variables.
- **Modernized Pipeline:** Separated training and inference logic.
- **Dockerized:** Containerized for easy development and deployment.

## 🏗️ Architecture
- **Web Framework:** Django 4.2+
- **ML Models:** Voting Classifier (MLP, SVM, Logistic Regression)
- **Deployment:** Gunicorn + WhiteNoise
- **Infrastructure:** Docker & Docker Compose support

## 🛠️ Local Setup

### 1. Prerequisites
- Python 3.9+
- Docker (optional)

### 2. Manual Installation
```bash
# Clone the repository
git clone https://github.com/Rakshith-Reddy-G/deepside.git
cd deepside

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your settings
```

### 3. Initialize Database & ML Model
```bash
# Run migrations
python manage.py migrate

# Train the ML model (generates artifacts)
python ml/train.py

# Collect static files
python manage.py collectstatic --noinput
```

### 4. Run Development Server
```bash
python manage.py runserver
```

### 5. Using Docker
```bash
docker-compose up --build
```

## 🌐 Deployment

This project is configured for easy deployment.
- **Procfile:** Provided for Gunicorn serving.
- **Static Files:** Managed via WhiteNoise.
- **Database:** Environment-based configuration via `DATABASE_URL`.

To deploy on Render/Railway:
1. Connect your repository.
2. Set up the Environment Variables from `.env.example`.
3. Build Command: `pip install -r requirements.txt && python ml/train.py && python manage.py migrate && python manage.py collectstatic --noinput`
4. Start Command: `gunicorn DeepSide.wsgi:application`

## 📂 Project Structure
- `DeepSide/`: Main project settings and configuration.
- `Remote_User/`: User registration and prediction interface.
- `Service_Provider/`: Analytics and reporting dashboard.
- `ml/`: Machine learning pipeline (train.py, inference.py, artifacts/).
- `templates/`: HTML templates with Bootstrap.
- `static/`: Static assets (CSS/JS).

## 🔐 Security Note
Never commit your `.env` file or SQLite database. Use the provided `.gitignore`.

## 📬 Contact
**Rakshith Reddy Gaddam**
- GitHub: [Rakshith-Reddy-G](https://github.com/Rakshith-Reddy-G)
- Email: gaddamrakshithreddy3625@gmail.com
