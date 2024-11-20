from django.core.management.base import BaseCommand
from ...models import ForeignCurrency

class Command(BaseCommand):
    help = "Import foreign currency data"

    def handle(self, *args, **kwargs):
        data = [
            (1, 'AED', 4.0924, 784),
            (2, 'EUR', 1.0000, 978),
            (3, 'USD', 1.1143, 840),
            (4, 'TRY', 0.0332, 650),
            (5, 'CNY', 7.9498, 156),
            (6, 'IQD', 0.0007, 720),
            (7, 'RUB', 101.9615, 460),
            (8, 'GBP', 0.8521, 230),
        ]

        currencies = [
            ForeignCurrency(
                pkForeignCurrencyID=item[0],
                fldForeignCurrencyName=item[1],
                fldForeignCurrency2USD=item[2],
                SCode=item[3],
            )
            for item in data
        ]

        ForeignCurrency.objects.bulk_create(currencies)

        self.stdout.write(self.style.SUCCESS("Successfully imported foreign currency data"))
