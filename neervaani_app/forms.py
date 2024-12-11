from django import forms
from .models import CropCalculator, Product

class CropCalculatorForm(forms.ModelForm):
    class Meta:
        model = CropCalculator
        fields = ['crop_name', 'land_size', 'land_unit', 'irrigation_method',
                  'rainfall_mm', 'irrigation_cycles', 'crop_yield', 'fertilizer_use',
                  'growing_season', 'avg_temperature']
        


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'green_water_footprint', 'blue_water_footprint', 'grey_water_footprint', 'total_water_footprint', 'description']