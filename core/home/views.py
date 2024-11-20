from django.shortcuts import render, redirect
from django.views import View
from .forms import CashInForm
from .models import Broker, Client, ForeignCurrency, CashIn
# Create your views here.

class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        # Fetching data for template rendering
        context = {
            'brokers': Broker.objects.all(),
            'clients': Client.objects.all(),
            'foreign_currencies': ForeignCurrency.objects.all(),
            'cash_ins': CashIn.objects.all(),
            'form': CashInForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CashInForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            cash_in = form.save(commit=False)

            # Optional: Perform additional calculations or processing here
            cash_in.FldCompanyWage = (
                cash_in.FldCashInAmount * cash_in.FldCompanyWageCoeff
            )
            cash_in.FldBrokerWage = (
                cash_in.FldCashInAmount * cash_in.FldBrokerWageCoeff
            )
            cash_in.FldNetCashIn = (
                cash_in.FldCashInAmount - cash_in.FldCompanyWage - cash_in.FldBrokerWage
            )

            cash_in.save()
            return redirect('home')  # Replace 'home' with the name of your view/URL

        # If the form is invalid, re-render the template with errors
        context = {
            'brokers': Broker.objects.all(),
            'clients': Client.objects.all(),
            'foreign_currencies': ForeignCurrency.objects.all(),
            'cash_ins': CashIn.objects.all(),
            'form': form,
        }
        return render(request, self.template_name, context)