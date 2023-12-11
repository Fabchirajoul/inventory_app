from django.db import models

# Create your models here.


class Devices(models.Model):

    order_id = models.IntegerField()
    product = models.CharField(max_length=20, blank=False)
    cartegory = models.CharField(max_length=20, blank=False)
    sales_channel = models.CharField(max_length=20, blank=False)
    instructions = models.CharField(max_length=20, blank=False)
    items = models.IntegerField()
    status = models.CharFieldmodels.CharField(max_length=20, blank=False)

    def __str__(self):
        return 'Order_id: {0} Product: {1} Cartegoty:{2} Sales_channel:{3} Instructions:{4} Items:{5} Status:{6}'.format(self.Order_id, self.Product, self.Cartegory, self.Sales_channel, self.Instructions, self.Items, self.Status)

# Using the power of inheritance to reduce the number of line codes needed for the different modeels

    class Meta:
        abstract = True


class Tomatoes(Devices):
    pass


class Watermelon(Devices):
    pass


class Orange(Devices):
    pass


class Cucumber(Devices):
    pass


class Avocado(Devices):
    pass
