from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.print_tables(verbose=True)

print('---------------------------------')

a = db.pretty_print("""
            SELECT
            Artist.Name
            FROM Artist;
""")

print('---------------------------------')

b = db.pretty_print("""
            SELECT *
            FROM Invoice
            Where Invoice.BillingCountry = "Germany";
""")

print('---------------------------------')

c = db.pretty_print("""
            SELECT COUNT (*)
            FROM Album;
""")

print('---------------------------------')

c = db.pretty_print("""
            SELECT COUNT (*)
            FROM Customer
            WHERE Customer.Country = "France";
""")

print('---------------------------------')

