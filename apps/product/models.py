from django.db import models

class Categoria(models.Model):

    name = models.CharField("Nome", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Produto(models.Model):

    name = models.CharField("Nome", max_length=120)
    description = models.TextField("Descrição", blank=True, null=True)
    price = models.DecimalField("Preço", max_digits=6, decimal_places=2)
    category = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='static', verbose_name='Imagem',
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"






     
