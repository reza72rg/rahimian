from django.core.management.base import BaseCommand
from ...models import Client

class Command(BaseCommand):
    help = "Import client data"

    def handle(self, *args, **kwargs):
        data = [
            (1, 'Client1', '30', 40001),
            (2, 'Client2', '01', 40002),
            (3, 'Client3', '31', 40004),
            (4, 'Client4', '32', 40006),
            (5, 'Client5', '33', 40009),
            (6, 'Client6', '09', 30016),
            (7, 'Client7', '34', 333999),
            (8, 'Client8', '12', 40007),
            (9, 'Client9', '10', 40005),
            (10, 'Client10', '11', 40008),
            (12, 'Client12', '04', 40013),
            (13, 'Client13', '13', 40010),
            (14, 'Client14', '35', 2222111),
            (15, 'Client15', '36', 40003),
            (16, 'Client16', '37', 222444),
            (17, 'Client17', '38', 2222555),
            (18, 'Client18', '02', 40012),
            (19, 'Client19', '14', 202020),
            (20, 'Client20', '39', 2222666),
            (21, 'Client21', '03', 30017),
            (22, 'Client22', '07', 40016),
            (23, 'Client23', '15', 40017),
            (24, 'Client24', '40', 272727),
            (25, 'Client25', '06', 40020),
            (26, 'Client26', '16', 40021),
            (27, 'Client27', '05', 40022),
            (28, 'Client28', '41', 282828),
            (29, 'Client29', '08', 40025),
            (30, 'Client30', '19', 333555),
            (31, 'Client31', '42', 210210),
            (32, 'Client32', '17', 2121212),
            (34, 'Client34', '44', 220220),
            (35, 'Client35', '45', 320320),
            (36, 'Client36', '46', 141421),
            (38, 'Client38', '18', 40026),
            (39, 'Client39', '47', 1515428),
            (40, 'Client40', '48', 2154863),
            (41, 'Client41', '49', 40018),
            (42, 'Client42', '28', 40024),
            (43, 'Client43', '21', 40030),
            (44, 'Client44', '22', 30002),
            (46, 'Client46', '23', 40031),
            (1045, 'Client1045', '24', 40032),
            (1046, 'Client1046', '25', 40033),
            (1047, 'Client1047', '26', 333777),
            (1048, 'Client1048', '27', 333888),
            (1049, 'Client1049', '29', 40035),
            (1050, 'Client1050', '20', 333666),
        ]

        clients = [Client(pkClientID=item[0], fldClientName=item[1].strip(), SortOrderClient=item[2], SCode=item[3]) for item in data]

        Client.objects.bulk_create(clients)

        self.stdout.write(self.style.SUCCESS("Successfully imported client data"))
