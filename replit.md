# DeepSide - Drug Side Effect Prediction System

## Overview

DeepSide is a Django-based web application that leverages deep learning and machine learning techniques to predict drug side effects. The system uses an ensemble of algorithms including Multi-modal Neural Networks (MMNN), Support Vector Machines (SVM), and Logistic Regression to analyze drug data and identify potential side effects early in the development process.

The application serves two primary user types:
- **Remote Users**: Researchers and healthcare professionals who can register, make predictions, and view their prediction history
- **Service Providers**: Administrators who can access analytics dashboards and view aggregated prediction data

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack**: Django Templates with vanilla CSS and JavaScript
- Template inheritance using a base template (`templates/base.html`) for consistent UI
- Inline CSS styling with gradient backgrounds and modern card-based layouts
- Chart.js library integration for data visualization in analytics dashboards
- Responsive grid layouts for forms and data display
- Session-based navigation with dynamic content rendering

**Design Pattern**: The frontend follows a traditional server-side rendering approach where Django views render HTML templates with context data. No separate frontend framework is used.

### Backend Architecture

**Framework**: Django 5.2.4 (Python web framework)

**Application Structure**: 
- Modular Django apps pattern with two main applications:
  - `Remote_User`: Handles user registration, authentication, predictions, and user-facing features
  - `Service_Provider`: Manages analytics and administrative dashboards

**Authentication & Session Management**:
- Custom authentication system using Django's session framework
- Password hashing with Django's `make_password` and `check_password` utilities
- Session-based user tracking (stores `userid` in session)
- No built-in Django authentication models - uses custom `ClientRegister_Model`

**URL Routing**:
- Root URL configuration in `DeepSide/urls.py` includes both app URL patterns
- App-specific URL patterns in respective `urls.py` files
- Static and media file serving configured for development mode

**Prediction Logic**: 
- The prediction functionality appears to integrate machine learning models (MMNN, SVM, Logistic Regression)
- Prediction results are classified as "Low" or "High" side effect risk
- Historical predictions are stored with timestamps for trend analysis

### Data Storage Solutions

**Database**: SQLite3 (default Django database for development)
- MySQL support available via `mysqlclient==2.2.7` connector if needed for production

**Data Models**:

1. **ClientRegister_Model**: User registration and profile data
   - Stores username, email, hashed password, contact details, location data, and demographics
   - Custom table name: `ClientRegister_Model`

2. **drug_side_effect_prediction**: Prediction records
   - Fields: uid (drug identifier), Drug_Name, Condition1 (medical condition), Prediction result, timestamp
   - Auto-timestamp on creation for tracking prediction history
   - Custom table name: `drug_side_effect_prediction`

3. **detection_ratio**: Stores detection ratio metrics
   - Name-value pairs for tracking prediction ratios

4. **detection_accuracy**: Stores accuracy metrics
   - Name-value pairs for tracking model accuracy

**Design Decision**: The application uses custom table names via Meta classes, suggesting integration with an existing database schema or specific naming requirements.

### Machine Learning Integration

**Libraries Used**:
- scikit-learn (1.7.1): For SVM and Logistic Regression models
- numpy (2.3.1) & pandas (2.3.1): Data processing and manipulation
- joblib (1.5.1): Model serialization and loading
- scipy (1.16.0): Scientific computing support

**Prediction Pipeline**: 
- User inputs drug UID, name, and medical condition
- System processes input through trained ML models
- Returns binary classification (Low/High side effect risk)
- Stores prediction with metadata for analytics

### Analytics & Visualization

**Service Provider Dashboard**:
- Aggregates prediction data from the database
- Generates statistics: low side effect count, high side effect count, total predictions
- Creates visual representations using Chart.js (pie charts, line charts)
- Real-time filtering capabilities using Django ORM queries

**Rationale**: Separating analytics into a service provider module allows for role-based access control and keeps analytical overhead separate from user prediction workflows.

## External Dependencies

### Third-Party Libraries

**Core Framework**:
- Django 5.2.4: Web framework providing ORM, templating, routing, and admin interface
- asgiref 3.9.1: ASGI server support for Django

**Database**:
- mysqlclient 2.2.7: MySQL database adapter for Python/Django
- sqlparse 0.5.3: SQL parsing library used by Django

**Machine Learning**:
- scikit-learn 1.7.1: ML algorithms (SVM, Logistic Regression)
- numpy 2.3.1: Numerical computing
- pandas 2.3.1: Data manipulation and analysis
- scipy 1.16.0: Scientific computing algorithms
- joblib 1.5.1: Model persistence and parallel processing
- threadpoolctl 3.6.0: Thread pool management for numerical libraries

**Data Processing & Export**:
- xlwt 1.3.0: Excel file writing capabilities
- python-dateutil 2.9.0.post0: Date parsing and manipulation

**Utilities**:
- pytz 2025.2: Timezone handling
- tzdata 2025.2: Timezone database
- six 1.17.0: Python 2/3 compatibility utilities

### Frontend Libraries

**Visualization**:
- Chart.js (CDN): JavaScript charting library for creating interactive pie charts and line graphs in the analytics dashboard

### Security Considerations

**Current Configuration**:
- `DEBUG = True`: Currently in development mode (should be disabled in production)
- `SECRET_KEY`: Hardcoded in settings (should use environment variables in production)
- `ALLOWED_HOSTS = ['*']`: Allows all hosts (should be restricted in production)
- Password hashing: Properly implemented using Django's security utilities

**Recommendation**: The application needs production hardening including environment-based configuration, restricted allowed hosts, and secure secret key management.