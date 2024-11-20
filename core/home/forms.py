from django import forms
from .models import CashIn

class CashInForm(forms.ModelForm):
    class Meta:
        model = CashIn
        fields = [
            'fkClientID', 'fkBrokerID', 'FkForeignCurrencyId',
            'FldCashInAmount', 'FldCompanyWageCoeff',
            'FldBrokerWageCoeff', 'FldCompanyWage',
            'FldBrokerWage', 'FldNetCashIn'
        ]
        widgets = {
            'FkClientId': forms.Select(attrs={'class': 'form-control'}),
            'FkBrokerId': forms.Select(attrs={'class': 'form-control'}),
            'FkForeignCurrencyId': forms.Select(attrs={'class': 'form-control'}),
            'FldCashInAmount': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'FldCompanyWageCoeff': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'FldBrokerWageCoeff': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'FldCompanyWage': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'FldBrokerWage': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'FldNetCashIn': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }
        labels = {
            'FkClientId': 'انتخاب مشتری',
            'FkBrokerId': 'انتخاب کارگزاری',
            'FkForeignCurrencyId': 'ارز مبداء',
            'FldCashInAmount': 'مبلغ (ارز مبداء)',
            'FldCompanyWageCoeff': 'ضریب کارمزد شرکت',
            'FldBrokerWageCoeff': 'ضریب کارمزد کارگزار',
            'FldCompanyWage': 'کارمزد شرکت',
            'FldBrokerWage': 'کارمزد کارگزار',
            'FldNetCashIn': 'مبلغ خالص ورودی',
        }
