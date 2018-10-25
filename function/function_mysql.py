import pymysql as pymysql


class MySQL():
    def __init__(self):
        self.msql = {
            'sorder': r"select a.OrderCode from orderinfo a INNER JOIN userinfo b ON a.UserID=b.UserID where b.Phone='15900283910'ORDER BY a.CreateTime DESC LIMIT 1;"
        }
    # 查询【我的订单】中第一个订单编号


def ordernumber(self):
    # sql1 = "select a.OrderCode from orderinfo a INNER JOIN userinfo b ON a.UserID=b.UserID where b.Phone='13522424639'ORDER BY a.CreateTime DESC LIMIT 1;"
    # sql = "select a.OrderCode from orderinfo a INNER JOIN userinfo b ON a.UserID=b.UserID where b.Phone='15900283910'ORDER BY a.CreateTime DESC LIMIT 1;"
    # 连接数据库查询user表
    conn = pymysql.connect(host="123.56.12", user="admin", password="吧吧吧VB", database="lease", port=3306,
                           charset="utf8")
    # print(type(sql1), sql1)
    curs = conn.cursor()  # 得到游标
    curs.execute(self.msql[self.sorder])  # 执行语句
    userinfo = curs.fetchall()[0][0]  # 抓取所以信息
    print(" MySQL " + userinfo)
    return userinfo


if __name__ == '__main__':

    select = MySQL()
    select.ordernumber()