from django.db import models


class Client(models.Model):

    cpf = models.CharField(primary_key=True, max_length=14)
    name = models.CharField(max_length=100, null=False )
    adress = models.CharField(max_length=150)
    phone = models.CharField(max_length=14, unique=True, null=False)

    def __str__(self):
        return f'CPF: {self.cpf} | Nome: {self.name} | Endereço: {self.adress} | Telefone: {self.phone}'


class Vehicle(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    category = models.CharField(max_length=15, null=False)
    fuel = models.CharField(max_length=10, null=False)
    year = models.IntegerField(default=0)
    model = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f'Código: {self.id} | Categoria: {self.category} | Combustível: {self.fuel} | Ano: {self.year} | Modelo: {self.model}'
    

class Rent(models.Model):

    rent_id = models.IntegerField(primary_key=True, auto_created=True)
    cpf = models.ForeignKey(Client, on_delete=models.CASCADE )
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE )
    inicial_date = models.DateField()
    final_date = models.DateField()

    def __str__(self):
        return f'Código: {self.rent_id} | CPF: {self.cpf} | Cód. Veículo: {self.vehicle_id} | Data inicial: {self.inicial_date} | Data Final: {self.final_date}'
