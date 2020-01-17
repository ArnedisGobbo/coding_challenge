import sqlite3


def format_data(x):
    if x is None:
        return "null"
    elif isinstance(x, str):
        return "'''%s'''" % x.replace("'", "''")
    else:
        return x


def join(iterator, separator):
    it = map(str, iterator)
    it = iter(it)
    separator = str(separator)
    string = "'%s'" % next(it, "")
    for s in it:
        string += separator + "'%s'" % s
    return string


def format_data_double_quotes(x):
    if x is None:
        return "null"
    elif isinstance(x, str):
        return "'%s'" % x.replace("'", "''")
    else:
        return x


class SQLiteDBAccess:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def insert(self, table, values_list, columns_names=None):
        """INSERT INTO table (column1, [column2, ... ]) VALUES (value1, [value2, ...])"""

        self.connect()
        target = table
        if columns_names:
            target += '(' + ','.join(columns_names) + ')'

        values = "(%s)" % (','.join(map(str, map(format_data, values_list))))


        # print 'INSERT INTO %s VALUES %s' % (target, values)
        self.cursor.execute('INSERT INTO %s VALUES %s' % (target, values))
        _id = self.cursor.description
        self.cursor.close()
        self.connection.commit()
        self.disconnect()
        return _id

    def select(self, columns_names, table, where_expr=None, order_by_field=None, order_by_ascending=True,
               group_by=None):
        """SELECT columns_names FROM table WHERE expr
        columns_names is '*' or a list of columns names."""
        # if columns_names != '*':
        #    columns_names = ','.join(columns_names)

        self.connect()
        sql_str = "SELECT %s FROM %s" % (columns_names, table)
        if where_expr:
            sql_str += " WHERE %s" % where_expr
        if group_by:
            sql_str += " GROUP BY %s" % group_by
        if order_by_field:
            sql_str += " ORDER BY %s " % order_by_field
            if order_by_ascending:
                sql_str += "ASC"
            else:
                sql_str += "DESC"

        self.cursor.execute(sql_str)
        result = self.cursor.fetchall()
        self.cursor.close()
        self.connection.commit()
        self.disconnect()
        return result

    def delete(self, table, where_expr=None):
        """DELETE FROM table_name [WHERE condition]
        Warning: if condition is None, all the rows in the table are deleted!!!"""

        self.connect()
        sql_str = "DELETE FROM %s" % table
        if where_expr:
            sql_str += " WHERE %s" % where_expr
        # if DEBUG: print sql_str
        self.cursor.execute(sql_str)
        result = self.cursor.rowcount
        self.cursor.close()
        self.connection.commit()
        self.disconnect()
        return result

    def update(self, table, columns_names, values,  where_expr=None):
        # UPDATE STEPS SET stepnumber=stepnumber+1  where proceduresectionid=1 and stepnumber>1

        self.connect()
        expr = ''
        for i in range(len(columns_names)):
            expr += "%s=%s," % (columns_names[i], format_data_double_quotes(values[i]))
        expr = expr[:-1]
        sql_str = "UPDATE %s SET %s" % (table, expr)
        if where_expr:
            sql_str += " WHERE %s" % where_expr
        # if DEBUG: print sql_str
        self.cursor.execute(sql_str)
        result = self.cursor.rowcount
        self.cursor.close()
        self.connection.commit()
        self.disconnect()
        return result
