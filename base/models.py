from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    cloth_type_choices = [
        ('T-Shirt', 'T-Shirt'),
        ('Jeans', 'Jeans'),
        ('Jacket', 'Jacket'),
        ('Shirt', 'Shirt'),
        ('Shoes','Shoes'),
    ]
    type = models.CharField(max_length=255, choices=cloth_type_choices)
    
    patterns = [
        ('Horizontal Stripes', 'Horizontal Stripes'),
        ('Vertical Stripes', 'Vertical Stripes'),
        ('Checkered', 'Checkered'),
        ('Graphic Print', 'Graphic Print'),
        ('Plain', 'Plain'),
    ]


    pattern = models.CharField(max_length=255 , choices = patterns)

    MATERIAL_CHOICES = [
        ('cotton', 'Cotton'),
        ('polyester', 'Polyester'),
        ('linen', 'Linen'),
        ('wool', 'Wool'),
        ('silk', 'Silk'),
        ('denim', 'Denim'),
        ('leather', 'Leather'),
        ('nylon', 'Nylon'),
                        ]
    material = models.CharField(max_length=255,choices = MATERIAL_CHOICES)
    color = models.CharField(max_length=255)

    conditions = [
        ('New','New'),
        ('Worn','Worn'),
                            ]
    condition = models.CharField(max_length = 255 , choices = conditions)
    photo = models.ImageField(upload_to='myimage')   
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{{self.type}} - {{self.color}}'
    
