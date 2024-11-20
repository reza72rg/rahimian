from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Import cash-in data"

    def handle(self, *args, **kwargs):
        # SQL to create the table if it doesn't exist
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS tblCashIn (
            pkCashIn INT PRIMARY KEY,
            fkClientID INT NOT NULL,
            fkBrokerID INT NOT NULL,
            fkForeignCurrencyID INT NOT NULL,
            fldCashInDate DATETIME NOT NULL,
            fldCashInAmount DECIMAL(18,4) NOT NULL,
            fldRefrence VARCHAR(255),
            fldCompanyWageCoeff DECIMAL(10,4),
            fldBrokerWageCoeff DECIMAL(10,4),
            fldNetCashIn DECIMAL(18,4),
            fldCompanyWage DECIMAL(18,4),
            fldBrokerWage DECIMAL(18,4),
            fkDestinationCurrency INT NOT NULL,
            fldXERate DECIMAL(18,4),
            fldCashInNet_Dest_currency DECIMAL(18,4),
            fldRegisterDate DATETIME NOT NULL,
            fldReverseExchange INT DEFAULT 0,
            PassedDate DATETIME NULL
        );
        """

        # SQL to insert data into the table
        sql_insert_data = """
        INSERT INTO tblCashIn (
            pkCashIn, fkClientID, fkBrokerID, fkForeignCurrencyID, 
            fldCashInDate, fldCashInAmount, fldRefrence, fldCompanyWageCoeff, fldBrokerWageCoeff,
            fldNetCashIn, fldCompanyWage, fldBrokerWage, fkDestinationCurrency, fldXERate, fldCashInNet_Dest_currency, 
            fldRegisterDate, fldReverseExchange, PassedDate
        ) VALUES 
        (1, 18, 2049, 1, '2024-01-06 00:00:00', 1448343.0000, '14', 0, 0.003, 1443997.9710, 0.0000, 4345.0290, 1, 1, 1443997.9710, '2024-01-06 16:42:15', 0, NULL),
        (2, 18, 1042, 1, '2024-01-08 00:00:00', 731554.0000, '27', 0, 0, 731554.0000, 0.0000, 0.0000, 1, 1, 731554.0000, '2024-01-08 12:45:17', 0, NULL),
        (3, 18, 2049, 1, '2024-01-09 00:00:00', 2300000.0000, '37', 0, 0.003, 2293100.0000, 0.0000, 6900.0000, 1, 1, 2293100.0000, '2024-01-10 10:12:15', 0, NULL),
        (4, 1046, 1046, 2, '2024-01-10 00:00:00', 2000000.0000, '41', 0, 0.004, 1992000.0000, 0.0000, 8000.0000, 2, 1, 1992000.0000, '2024-01-10 10:18:57', 0, NULL),
        (5, 18, 1039, 1, '2024-01-10 00:00:00', 2979000.0000, '42', 0, 0.003, 2970063.0000, 0.0000, 8937.0000, 1, 1, 2970063.0000, '2024-01-10 16:33:39', 0, NULL);
        """

        try:
            with connection.cursor() as cursor:
                # Create the table
                cursor.execute(sql_create_table)
                # Insert the data
                cursor.execute(sql_insert_data)
            self.stdout.write(self.style.SUCCESS("Successfully imported cash-in data"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing cash-in data: {e}"))
