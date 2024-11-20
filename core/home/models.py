from django.db import models
# Create your models here.

from django.db import models


class Broker(models.Model):
    pkBrokerID = models.IntegerField(primary_key=True)
    fldBrokerName = models.CharField(max_length=255)
    fldForeignCompany = models.CharField(max_length=255, null=True, blank=True)
    SortOrdertblBroker = models.CharField(max_length=10, null=True, blank=True)
    fldfarsiBrokerName = models.CharField(max_length=255, null=True, blank=True)
    fldBrokerMaxDebtInUSD = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    SCode = models.IntegerField()

    class Meta:
        db_table = 'tblBroker'

    def __str__(self):
        # Return the name of the broker in the preferred language (English or Farsi)
        return f"{self.fldBrokerName} ({self.fldfarsiBrokerName})"

class CashIn(models.Model):
    pkCashIn = models.AutoField(primary_key=True)
    fkClientID = models.IntegerField()
    fkBrokerID = models.IntegerField()
    fkForeignCurrencyID = models.IntegerField()
    fldCashInDate = models.DateTimeField()
    fldCashInAmount = models.DecimalField(max_digits=18, decimal_places=4)
    fldRefrence = models.CharField(max_length=255, null=True, blank=True)
    fldCompanyWageCoeff = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    fldBrokerWageCoeff = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    fldNetCashIn = models.DecimalField(max_digits=18, decimal_places=4)
    fldCompanyWage = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    fldBrokerWage = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    fkDestinationCurrency = models.IntegerField()
    fldXERate = models.DecimalField(max_digits=18, decimal_places=4)
    fldCashInNet_Dest_currency = models.DecimalField(max_digits=18, decimal_places=4)
    fldRegisterDate = models.DateTimeField()
    fldReverseExchange = models.IntegerField(default=0)
    PassedDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tblCashIn'
        verbose_name = 'Cash In'
        verbose_name_plural = 'Cash Ins'

    def __str__(self):
        return f"CashIn {self.pkCashIn} - Client {self.fkClientID}"

class Client(models.Model):
    pkClientID = models.AutoField(primary_key=True)
    fldClientName = models.CharField(max_length=255)
    SortOrderClient = models.CharField(max_length=10, null=True, blank=True)
    SCode = models.IntegerField()

    class Meta:
        db_table = 'tblClient'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.fldClientName.strip()}"

class ForeignCurrency(models.Model):
    pkForeignCurrencyID = models.AutoField(primary_key=True)
    fldForeignCurrencyName = models.CharField(max_length=50)
    fldForeignCurrency2USD = models.DecimalField(max_digits=10, decimal_places=4)
    SCode = models.IntegerField()

    class Meta:
        db_table = 'tblForeignCurrency'
        verbose_name = 'Foreign Currency'
        verbose_name_plural = 'Foreign Currencies'

    def __str__(self):
        return f"{self.fldForeignCurrencyName}"