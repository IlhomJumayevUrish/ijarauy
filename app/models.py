from django.conf import settings
from django.db import models
from django.conf import settings
from parler.models import TranslatedFields, TranslatableModel
from django.contrib.auth.models import User

# Create image folder
def image_folder(product,filename):
    names="Rasmlar"
    rasm_image_folder="{}/{}".format(names,filename)
    return rasm_image_folder

#  Create UserData for Users
class UserData(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="userlar",verbose_name="User")
    name=models.CharField("Name",max_length=50,blank=True)
    phone=models.CharField("Telefon",max_length=14,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Mijoz"
        verbose_name_plural="Mijozlar"
# Create district for location
class Tumanlar(TranslatableModel):
    translations = TranslatedFields(
    name=models.CharField('Nomi',max_length=50,blank=True),
    slug=models.SlugField('slug',blank=True),
    )
    def __str__(self):
        return self.name

# Create Home for Users
class Uylar(TranslatableModel):
    translations = TranslatedFields(
    manzil=models.CharField('Manzil',max_length=200,blank=True),
    turi=models.CharField('Turi (dom,hovli)',max_length=50,blank=True),
    kimga=models.CharField("Kim uchun",max_length=100,blank=True),
    remont=models.CharField('Remont',max_length=50,blank=True),
    qoshimchamalumot=models.CharField("Qo'shimcha ma'lumotlar",max_length=200,blank=True),
    qoshimchajxozlar=models.CharField("Qo'chimcha jixozlar",max_length=100),
    )
    user=models.ForeignKey(UserData,on_delete=models.CASCADE,verbose_name="Mijoz",related_name="Mijoz")
    tumanda=models.ForeignKey(Tumanlar,on_delete=models.CASCADE,verbose_name='Tumanda',related_name='tumanda')
    xona_soni=models.IntegerField('Xona soni',blank=True)
    narx=models.IntegerField('Narxi($)',blank=True)
    vaqt=models.DateField('Qushilgan sana',auto_now_add=True)
    aloqa=models.CharField("Telefon",max_length=15,blank=True)
    def __str__(self):
        return self.tumanda.name+' '+str(self.xona_soni)+'-xona'
    class Meta:
        ordering=['-id']
# Create image for homes
class Rasmlar(models.Model):
    uy=models.ForeignKey(Uylar,on_delete=models.CASCADE,verbose_name='rasm',related_name="rasm")
    image=models.ImageField(upload_to=image_folder)
    def __str__(self):
        return self.uy.aloqa