from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Import broker data"

    def handle(self, *args, **kwargs):
        # SQL to create the table if it doesn't exist
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS tblBroker (
            pkBrokerID INT PRIMARY KEY,
            fldBrokerName VARCHAR(255) NOT NULL,
            fldForeignCompany VARCHAR(255),
            SortOrdertblBroker VARCHAR(10),
            fldfarsiBrokerName VARCHAR(255),
            fldBrokerMaxDebtInUSD DECIMAL(18,4),
            SCode INT
        );
        """

        # SQL to insert data into the table
        sql_insert_data = """
        INSERT INTO tblBroker (pkBrokerID, fldBrokerName, fldForeignCompany, SortOrdertblBroker, fldfarsiBrokerName, fldBrokerMaxDebtInUSD, SCode)
        VALUES 
        (1, 'Broker1', 'Foreign Company1', '22', 'نام 1', 50000000.0000, 30007),
        (2, 'Broker2', 'Foreign Company2', '05', 'نام 2', 100000000.0000, 30003),
        (3, 'Broker3', 'Foreign Company3', '01', 'نام 3', 100000000.0000, 30010),
        (6, 'Broker6', 'Foreign Company6', '33', 'نام 6', 50000000.0000, 121212),
        (7, 'Broker7', 'Foreign Company7', '02', 'نام 7', 100000000.0000, 30008),
        (8, 'Broker8', 'Foreign Company8', '17', 'نام 8', 50000000.0000, 33333),
        (9, 'Broker9', 'Foreign Company9', '07', 'نام 9', 100000000.0000, 30013),
        (10, 'Broker10', 'Foreign Company10', '04', 'نام 10', 50000000.0000, 11111),
        (11, 'Broker11', 'Foreign Company11', '14', 'نام 11', 50000000.0000, 30011),
        (12, 'Broker12', 'Foreign Company12', '21', 'نام 12', 100000000.0000, 30004),
        (13, 'Broker13', 'Foreign Company13', '18', 'نام 13', 50000000.0000, 44444),
        (15, 'Broker15', 'Foreign Company15', '06', 'نام 15', 100000000.0000, 30021),
        (16, 'Broker16', 'Foreign Company16', '23', 'نام 16', 50000000.0000, 66666),
        (18, 'Broker18', 'Foreign Company18', '35', 'نام 18', 50000000.0000, 141414),
        (27, 'Broker27', 'Foreign Company27', '19', 'نام 27', 50000000.0000, 55555),
        (29, 'Broker29', 'Foreign Company29', '10', 'نام 29', 50000000.0000, 30032),
        (30, 'Broker30', 'Foreign Company30', '20', 'نام 30', 50000000.0000, 40018),
        (31, 'Broker31', 'Foreign Company31', '03', 'نام 31', 50000000.0000, 30035),
        (32, 'Broker32', 'Foreign Company32', '08', 'نام 32', 100000000.0000, 30040),
        (1032, 'Broker1032', 'Foreign Company1032', '09', 'نام 1032', 50000000.0000, 22222),
        (1033, 'Broker1033', 'Foreign Company1033', '32', 'نام 1033', 50000000.0000, 99999),
        (1035, 'Broker1035', 'Foreign Company1035', '34', 'نام 1035', 50000000.0000, 131313),
        (1037, 'Broker1037', 'Foreign Company1037', '29', 'نام 1037', 50000000.0000, 77777),
        (1038, 'Broker1038', 'Foreign Company1038', '30', 'نام 1038', 50000000.0000, 40019),
        (1039, 'Broker1039', 'Foreign Company1039', '24', 'نام 1039', 50000000.0000, 30054),
        (1040, 'Broker1040', 'Foreign Company1040', '11', 'نام 1040', 50000000.0000, 30053),
        (1041, 'Broker1041', 'Foreign Company1041', '0', 'نام 1041', 0.0000, 666666),
        (1042, 'Broker1042', 'Foreign Company1042', '37', 'نام 1042', 50000000.0000, 30055),
        (1043, 'Broker1043', 'Foreign Company1043', '28', 'نام 1043', 50000000.0000, 30056),
        (1044, 'Broker1044', 'Foreign Company1044', '12', 'نام 1044', 50000000.0000, 30060),
        (1045, 'Broker1045', 'Foreign Company1045', '25', 'نام 1045', 50000000.0000, 30061);
        """

        try:
            with connection.cursor() as cursor:
                # Create the table
                cursor.execute(sql_create_table)
                # Insert the data
                cursor.execute(sql_insert_data)
            self.stdout.write(self.style.SUCCESS("Successfully imported broker data"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing broker data: {e}"))
