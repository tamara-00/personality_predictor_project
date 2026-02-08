from django.db import models
# from django.contrib.auth.models import User

# class SurveyResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     favorite_color = models.CharField(max_length=100)
#     hobby = models.CharField(max_length=200)
#     stress_reaction = models.TextField()
#     extrovert_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
#     openness_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     prediction = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Анкета од {self.user.username} на {self.submitted_at.strftime('%d.%m.%Y')}"
