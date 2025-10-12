from django.db import models

class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'ClientRegister_Model'
    
    def __str__(self):
        return self.username

class drug_side_effect_prediction(models.Model):
    uid = models.CharField(max_length=100)
    Drug_Name = models.CharField(max_length=200)
    Condition1 = models.CharField(max_length=200)
    Prediction = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'drug_side_effect_prediction'
    
    def __str__(self):
        return self.Drug_Name

class detection_ratio(models.Model):
    names = models.CharField(max_length=200)
    ratio = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'detection_ratio'
    
    def __str__(self):
        return self.names

class detection_accuracy(models.Model):
    names = models.CharField(max_length=200)
    ratio = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'detection_accuracy'
    
    def __str__(self):
        return self.names
