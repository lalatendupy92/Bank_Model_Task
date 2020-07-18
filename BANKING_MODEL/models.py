from django.db import models


class Account_type(models.Model):
    account_type = models.CharField(max_length=100)

    def __str__(self):
        return self.account_type

class User_Details(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_phone = models.IntegerField(unique=True)
    user_email = models.EmailField(max_length=50, unique=True)
    user_account_type = models.ForeignKey(Account_type, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='images/')
    user_status = models.CharField(max_length=30,default=False)


