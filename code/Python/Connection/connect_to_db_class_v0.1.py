
import pandas as pd
from valid8 import validate_arg
from valid8.validation_lib import instance_of
from dateutil.relativedelta import relativedelta
from datetime import datetime
import logging, logging.config, traceback
import psycopg2
import psycopg2.extras
import os, sys, time

#%%
class CommonModule:
    def __init__(self, dbconn=None, tables=None, paths=None, logbundle=None, fname=None):
        self.conn = None
        self.cur = None
        self.fname = fname
        self.tables = tables
        
        if dbconn: 
            self.connet_to_datebase(dbconn)
            self.m_message = tables.get('message',{}).get('management',{})
            self.r_message = tables.get('message',{}).get('result',{})
            self.r_message_m = tables.get('message',{}).get('mresult',{})
            
        if paths: 
            self.get_logging_dirs(paths)
            self.logger = None
            self.formatters = logbundle[0]
            self.handlers = logbundle[1]
    
    
    @validate_arg('dbconn', instance_of(dict))
    def connet_to_datebase(self, dbconn):
        self.dbconn = dbconn
        self.conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}" \
        .format(self.dbconn['host'],
        self.dbconn['port'],
        self.dbconn['dbname'],
        self.dbconn['username'],
        self.dbconn['pwd']))
        self.cur = self.conn.cursor()
        if self.conn.closed == 0: print("Database connected")
    
    
    @validate_arg('paths', instance_of(dict))
    def get_logging_dirs(self, paths, today=datetime.today()):
        self.paths = paths
        print('FNAME:----------->' + self.fname)
        log_path = '{}/{}_{}.log'.format(self.paths.get('log',{}),str(today).split(' ')[0],
        self.fname.split('/')[-1].split('.')[0])
        elog_path = '{}{}/{}_{}_ERR.log'.format(self.paths.get('log',{}),self.paths.get('error',{}),
        str(today).split(' ')[0],self.fname.split('/')[-1].split('.')[0])
        self.log_path = paths.get('master',{}) + log_path
        self.elog_path = paths.get('master',{}) + elog_path
    
    
    @validate_arg('logger_name', instance_of(str))
    def get_logger(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        log_path = self.log_path
        if logger_name == 'ERR': log_path = self.elog_path
        fhandlers = logging.FileHandler(log_path, mode='a+', encoding='utf-8')
        fhandlers.setFormatter(logging.Formatter(self.formatters))
        shandlers = logging.StreamHandler(stream=sys.stdout)
        shandlers.setFormatter(logging.Formatter(self.formatters))
        self.logger.addHandler(shandlers)
        self.logger.addHandler(fhandlers)
        self.logger.setLevel(logging.DEBUG)
        return self.logger
    
    
    @validate_arg('category', instance_of(str))
    def get_essential_bundle(self, category, batch='martDaily', today=datetime.today()):
        model = '/src'
        if category is 'EQU': model = self.paths.get('resource',{}).get('model','/NONE')
        if category is 'SKU': model = self.paths.get('resource',{}).get('sku','/NONE')
        if (category is 'EQU') or (category is 'GWR'): batch = 'martMonthly'
        mart = self.tables.get(batch,{}).get(category,{})
        master = self.paths.get('master',{})
        sql = self.paths.get('resource',{}).get('sql',{})
        return mart, model, master, sql
    
    
    @validate_arg('df', instance_of(pd.DataFrame))
    @validate_arg('category', instance_of(str))
    def dataframe_to_pkl(self, df, category, today=datetime.today()):
        pkl_path = '{}/{}_{}_{}.pkl'.format(self.paths.get('pkl',{}),str(today).split(' ')[0],
        category, self.fname.split('/')[-1].split('.')[0])
        self.pkl_path = self.paths.get('master',{}) + pkl_path
        df.to_pickle(self.pkl_path)
    
    
    @validate_arg('file_name', instance_of(str))
    def run_src_file(self, file_name):
        os.system("python3 {}".format(os.path.join(self.paths.get('master',{}),
        os.path.join('src',file_name))))
    
    
    def check_log_directory_exists(self):
        dicts = {
        'LOG': self.paths.get('master',{}) + self.paths.get('log',{}),
        'PKL': self.paths.get('master',{}) + self.paths.get('pkl',{}),
        'ERR': self.paths.get('master',{}) + self.paths.get('log',{}) + self.paths.get('error',{})
        }
        for k,v in dicts.items():
            if not os.path.exists(v):
                os.makedirs(v)
        
    
    def close_db_connection(self):
        if False is self.cur.closed:
            self.cur.close()
        if False is self.conn.closed:
            self.conn.close()
            print("Database connection closed")
    
    @validate_arg('query', instance_of(str))
    def create_mart_from_query(self, query):
        """
        Create mart from sql query
        usage: create_mart_from_query(query)
        :param query: input query (type: str)
        :return: NONE
        """
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            self.conn.commit()
            self.cur.close()
        except Exception as e:
            self.logger.error(traceback.format_exc())
            self.cur = self.conn.cursor()
            self.cur.execute("ROLLBACK")
            self.conn.commit()
            self.cur.close()
    
    
    @validate_arg('query', instance_of(str))
    def select_query_return_df(self, query) -> pd.DataFrame:
        """
        Get dataframe from sql query
        usage: select_query_return_df(query)
        :param query: input query w/o where condition(type: str) (ex. select * from table_name)
        :return: dataframe from sql query
        """
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            data = self.cur.fetchall()
            col_names = [desc[0] for desc in self.cur.description]
            df = pd.DataFrame(data, columns = col_names)
            self.conn.commit()
            self.cur.close()
            return df
        except Exception as e:
            self.logger.error(traceback.format_exc())
            self.cur = self.conn.cursor()
            self.cur.execute("ROLLBACK")
            self.conn.commit()
            self.cur.close()
    
    
    @validate_arg('series_data', instance_of(pd.Series))
    def make_lpad(self, series_data, num) -> pd.Series:
        """
        Make string data with lpad
        usage: make_lpad(series_data, num)
        :param series_data: input data(type: Series)
        :param num: length of data to fill (ex. 123, 5)
        :return: series data filled with 0 (lpad, ex. 00123)
        """
        return series_data.apply(lambda x: str(x).zfill(num))
    
    
    @validate_arg('interval', instance_of(int))
    def get_time_interval_condition(self, interval, today=datetime.today()) -> int:
        """
        Get sql query in where condition (range of months)
        usage: get_time_interval_condition(interval)
        :param interval: time interval (ex. 3)
        :param today: default, current time
        :return: range of months - between min and max (ex. between '201907' and '201909')
        """
        min_today = str(today - relativedelta(months=interval)).split('-')
        max_today = str(today - relativedelta(months=1)).split('-')
        min_ym = min_today[0] + min_today[1]
        max_ym = max_today[0] + max_today[1]
        interval_condition = " between '"+min_ym+"' and '"+max_ym+"'"
        return interval_condition
    
    
    def get_current_date(self) -> str:
        """
        Get today datetime
        usage: get_current_date()
        :param: NONE
        :return: yyyymmdd (ex. 20191105)
        """
        today = str(datetime.today()).split(' ')
        today = today[0].split('-')
        yyyymmdd = today[0]+today[1]+today[2]
        return yyyymmdd
    
    def get_year_month(self, flag, today=datetime.today()) -> str:
        """
        Get today datetime
        usage: get_year_month()
        :param flag: 0 -> current month, 1 -> last month
        :return: yyyymm (ex. 201911)
        """
        if flag==0:
            thismonth = str(today).split('-')
            yyyymm = thismonth[0] + thismonth[1]
        else:
            lastmonth = str(today - relativedelta(months=1)).split('-')
            yyyymm = lastmonth[0] + lastmonth[1]
        return yyyymm
    
    
    def get_length_of_table(self, flag=False, table_name='NONE'):
        """
        Get length of table
        usage: get_length_of_table(table)
        :param flag: input flag(0: before, 1: after)
        :param table_name: table name to get length (default: msg_output_table)
        :return: NONE
        """
        if table_name is 'NONE':
            table_name = self.r_message
        query = "select * from {}".format(table_name)
        len_table = len(self.select_query_return_df(query))
        if False is flag: 
            self.logger.info('Original table length: {}'.format(len_table))
        else:
            self.logger.info('Current table length: {}'.format(len_table))
    
    
    @validate_arg('category', instance_of(str))
    def msg_pool_load(self, category) -> pd.DataFrame:
        """
        Get message pool from table
        usage: input category without number - msg_pool_load('EQU')
        :param category: input data (type: str, ex. EQU)
        :return: message pool dataframe with input category
        """
        self.cur = self.conn.cursor()
        self.cur.execute("select * from {} where act_yn='Y' ".format(self.m_message))
        temp_mart = self.cur.fetchall()
        col_names = [desc[0] for desc in self.cur.description]
        message_pool_df = pd.DataFrame(temp_mart, columns=col_names)
        message_pool_df = message_pool_df.sort_values(by=['category','opt'])
        mask = message_pool_df['category'].apply(lambda x: any(pd.Series(x).str.contains(category, na=False)))
        self.conn.commit()
        self.cur.close()
        return message_pool_df[mask]
    
    
    @validate_arg('msg_df', instance_of(pd.DataFrame))
    def msg_result_insert(self, msg_df, table_name='NONE'):
        """
        Insert result messages to table
        usage: input final message dataframe - msg_result_insert(msg_df)
        :param msg_df: final message dataframe
        :param table_name: table name to insert (default: msg_output_table)
        :return: NONE
        """
        if table_name is 'NONE': 
            table_name = self.r_message
        if (table_name is 'EQU') or (table_name is 'GWR'):
            table_name = self.r_message_m
        self.cur = self.conn.cursor()
        mart_create_time = time.time()
        fields = ','.join(msg_df.keys())
        values = "VALUES({}, now())".format(",".join(["%s" for _ in list(msg_df)]))
        insert_stmt = """INSERT INTO {} ({}, mod_date) {} """.format(table_name, fields, values)
        psycopg2.extras.execute_batch(self.cur, insert_stmt, msg_df.values)
        self.conn.commit()
        mart_end_time = time.time()
        runtime=mart_end_time-mart_create_time
        self.cur.close()
    
    
    def check_if_error_occurred(self):
        if os.path.exists(self.elog_path):
            with open(self.elog_path, encoding='utf8') as f:
                line = f.readline()
        if not line:
            os.remove(self.elog_path)
            print("No error, ERR log removed.")
            f.close()
    
    
    def __del__(self):
        self.close_db_connection()
        
#%% example
        
# connect
conInit = CommonModule()
conInform = {
        "host" : "127.0.0.1",
        "port" : "5432",
        "dbname" : "postgres",
        "username" : "doubles",
        "pwd" : "powerfm1"
        }
conInit.connet_to_datebase(conInform)

# select query
query = """
    select *
      from "Chilsung".dt_mes_as_scada_sodapet_rids_20200229;
"""
df = conInit.select_query_return_df(query)
# error 시 logger 내용이 없어서 -> 이 부분은 해결 요망

conInit.close_db_connection()