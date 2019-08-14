from django.db import models

 #유저들이 업로드한 것
class UploadFileModel(models.Model):            
    file = models.FileField(null=True)
    productimg = models.FileField(null=True)


    saletype = models.CharField(max_length=20,null=True)
    bidprice = models.IntegerField(null=True)
    biduser = models.CharField(max_length=50,null=True)

    pbrand = models.CharField(max_length=20,null=True)
    pitem = models.CharField(max_length=20, null=True)
    productimg_name = models.CharField(max_length =40, null=True)
 
    originalprice = models.IntegerField(null=True)
    lowerlimit = models.IntegerField(null=True)
    
    user_id = models.CharField(max_length=50,null=True)
    pub_date = models.DateTimeField('date published', null=True)


    def __str__(self):
        return self.productimg_name


