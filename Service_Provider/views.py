from django.shortcuts import render
from Remote_User.models import drug_side_effect_prediction
from django.db.models import Count

def index(request):
    return render(request, 'ServiceProvider/index.html')

def view_analytics(request):
    predictions = drug_side_effect_prediction.objects.all()
    
    low_count = drug_side_effect_prediction.objects.filter(Prediction__icontains='Low').count()
    high_count = drug_side_effect_prediction.objects.filter(Prediction__icontains='High').count()
    
    chart_data = {
        'low_count': low_count,
        'high_count': high_count,
        'total': low_count + high_count
    }
    
    return render(request, 'ServiceProvider/analytics.html', {
        'predictions': predictions,
        'chart_data': chart_data
    })
