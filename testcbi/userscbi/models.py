from django.db import models

"""
CBI prueba 

por default django genera su id , asi que solo se hicieron la relaciones entre los modelos.
tuve problemas para acceder a mis datos desde mi entorno virtual y no pude correr las migraciones correscpondientes
hare un PR posterior para arreglarlo con el uso de Docker.
"""


# Create your models here.
class Permisions(models.Model):
    name= models.CharField(verbose_name='nombre del permiso', max_length=50) #Administrador,inversionista ,superusuario 
    detail = models.CharField(verbose_name='observaciones', max_length=250)

    class Meta:
        db_table ='permisos'


class UserCBI(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=150)
    last_name = models.CharField(verbose_name='Apellido', max_length=150)
    phone_number = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=True)
    class Meta:
        db_table = 'usercbi'


class PermisionsAsigned(models.Model):
    sucursal = models.CharField(verbose_name='sucursal', max_length=150)
    permiso = models.ForeignKey(Permisions, verbose_name='permiso_asignado', on_delete=models.CASCADE)
    cargo = models.CharField(verbose_name='cargo', max_length=50)
    user= models.ForeignKey(UserCBI, verbose_name='permision_assigned_user', on_delete=models.CASCADE)

    class Meta:
        db_table= 'permisos_asignados'