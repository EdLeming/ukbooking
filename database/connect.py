import psycopg2


class database(object):
    ''' Connect to the postgresql database server'''
    def __init__(self, url):
        self._conn = None
        try:
            self._conn = psycopg2.connect(url)    
        except (Exception, psycopg2.DatabaseError) as e:
            print e
            if self._conn is not None:
                self._conn.close()
            
        self._cur = self._conn.cursor()
        self._cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = self._cur.fetchone()
        print db_version

    def __del__(self):
        # close the communication with the PostgreSQL
        if  self._conn is not None:
            self._conn.close()


    def list_apartment_tables(self):
        sql = "select * from ukbooking_apartment;"
        self._cur.execute(sql)
        rows = self._cur.fetchall()
        for row in rows:
            print row

    def list_bed_tables(self):
        sql = "select * from ukbooking_bed;"
        self._cur.execute(sql)
        rows = self._cur.fetchall()
        for row in rows:
            print row

    def update_apartments_contact(self, new_details):
        sql = "UPDATE ukbooking_apartment SET Contact = %s;"
        self._cur.execute(sql, (new_details,))
        updated_rows = self._cur.rowcount
        self._conn.commit()

    def update_apartment_name(self, new_details):
        sql = """UPDATE ukbooking_apartment SET Short_name=%s WHERE Id=1;"""
        self._cur.execute(sql, (new_details,))
        updated_rows = self._cur.rowcount
        self._conn.commit()

    def update_house_name(self, new_details):
        sql = """UPDATE ukbooking_apartment SET Short_name=%s WHERE Id=2;"""
        self._cur.execute(sql, (new_details,))
        updated_rows = self._cur.rowcount
        self._conn.commit()

    def update_house_info(self, new_details):
        sql = """UPDATE ukbooking_apartment SET Information = %s WHERE Id=2;"""
        self._cur.execute(sql, (new_details,))
        updated_rows = self._cur.rowcount
        self._conn.commit()


    def make_second_beds_doubles(self):
        sql = """UPDATE ukbooking_bed SET Type='DOUBLE' WHERE Number=2;"""
        self._cur.execute(sql)
        updated_rows = self._cur.rowcount
        self._conn.commit()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str,
                        help="URL of heroku database. The command '$ heroku pg:credentials:url DATABASE' will return the required URL")
    args = parser.parse_args()


    db = database(args.url)
    db.list_apartment_tables()
    
    # Some previous updates
    #db.update_apartments_contact("edward.leming@physics.ox.ac.uk")
    #db.update_apartment_name("Apartment")
    #db.update_house_name("House")
    #db.update_house_info("Fully furnished + lovely basement")
    #db.list_apartment_tables()

    #db.list_bed_tables()
    #db.make_second_beds_doubles()
    #db.list_bed_tables()
