from django.db import models

# Create your models here.
class EmailList(models.Model):
      email = models.EmailField(blank=False, null=False)
      date_joined = models.DateTimeField(auto_now_add=True, blank=True)

      def __str__(self) -> str:
            return self.email