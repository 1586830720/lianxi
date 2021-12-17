# 导包
import pymysql


# 创建类
# import requests


class DBUtils:
    __conn = None
    __cursor = None

    # 创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="211.103.136.244",
                                         port=7061,
                                         user="student",
                                         password="iHRM_student_2021",
                                         database="ihrm",
                                         charset="utf8",
                                         autocommit=False)
        return cls.__conn

    # 获取游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exe_sql(cls, sql):
        try:
            cursor = cls.__get_cursor()
            # 执行sql语句
            cursor.execute(sql)
            # 判断 是 查询
            if sql.split()[0].lower() == "select":
                # 返回所有查询数据
                return cursor.fetchall()
            # 否则（非查询）
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回影响的结果行数
                return cursor.rowcount
        except Exception as e:
            # 打印异常信息
            print(e)
            # 回滚事务
            cls.__conn.rollback()
        finally:
            # 关闭游标
            cls.__close_cursor()
            # 关闭连接
            cls.__close_conn()

    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None

if __name__ == '__main__':
    sql = "select version()"
    print(DBUtils.exe_sql(sql))