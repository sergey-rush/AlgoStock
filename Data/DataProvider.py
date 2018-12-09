import psycopg2

from Core.Stock import Stock


class DataProvider:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5432
        self.dbname = 'exchangedb'
        self.user = 'postgres'
        self.password = 'postgres'
        self.connection = None
        self.cursor = None

    def _open_connection(self):
        conn_string = "host='{}' port={} dbname='{}' user='{}' password='{}'".format(self.host, self.port, self.dbname,
                                                                                     self.user, self.password)
        try:
            self.connection = psycopg2.connect(conn_string)
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_stock_by_stock_id(self, stock_id):
        self._open_connection()
        self.cursor.execute("SELECT id, issuer_id, ticker, per, trade_date, open, high, low, close, volume FROM stocks WHERE id = %s;", [stock_id])
        item = self.cursor.fetchone()
        self.connection.close()
        stock = Stock(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9])
        return stock

    def insert_stock(self, stock):
        self._open_connection()
        self.cursor.execute("INSERT INTO stocks (issuer_id, ticker, per, trade_date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;", (stock.issuer_id, stock.ticker, stock.per, stock.trade_date, stock.open, stock.high, stock.low, stock.close, stock.volume))
        id = self.cursor.fetchone()[0]
        self.connection.commit()
        self.connection.close()
        return id

    def get_stocks_by_issuer_id(self, issuer_id):
        self._open_connection()
        self.cursor.execute("SELECT id, issuer_id, ticker, per, trade_date, open, high, low, close, volume FROM stocks WHERE issuer_id = %s;", [issuer_id])
        items = self.cursor.fetchall()
        self.connection.close()
        item_list = []
        for item in items:
            stock = Stock(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9])
            item_list.append(stock)
        return item_list

    def copy_probs_from_file(self):
        self._open_connection()
        self.cursor.execute("COPY probs FROM '/tmp/new_probs.csv' DELIMITER ',' CSV;")
        self.connection.commit()
        self.connection.close()

    def copy_probs(self):
        self._open_connection()
        self.cursor.execute("COPY (SELECT keyword, ratio, discount FROM temp_probs) TO '/tmp/new_probs.csv' CSV HEADER;")
        self.connection.close()

    def update_game(self, stock_id, issuer_id):
        self._open_connection()
        self.cursor.execute("UPDATE stocks SET issuer_id = %s WHERE id = %s;", (stock_id, issuer_id))
        self.connection.commit()
        self.connection.close()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
