from tabulate import tabulate
import mysql.connector as p

db = p.connect(host="localhost", user="root", password="Hanuman@_ji1971749905")
cur = db.cursor()
dbs = "create database if not exists book_shop"
cur.execute(dbs)
use = "use book_shop"
cur.execute(use)

t1 = "create table if not exists books(bookid varchar(13) primary key not null,title varchar(30) not null,author varchar(20) not null,publisher varchar(40) not null,class integer not null,retailprice integer not null,quantity integer not null)"
cur.execute(t1)
t2 = "create table if not exists sale(bookid varchar(13) not null,title varchar(30) not null,author varchar(20) not null,publisher varchar(40) not null,class integer not null,retailprice integer not null,date date not null,quantity integer not null)"
cur.execute(t2)
t3 = "create table if not exists purchase(bookid varchar(13) not null,title varchar(30) not null,author varchar(20) not null,publisher varchar(40) not null,class integer not null,date date not null,quantity integer not null)"
cur.execute(t3)


def addbook():
    while True:
        print("\n1. ADD BOOK RECORD")
        print("2. BACK TO ADMINISTER MENU")
        while True:
            zy = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
            if zy in [1, 2]:
                break
            else:
                print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 OR 2)")
                continue
        if zy == 1:
            while True:
                while True:
                    bookid = input("\nENTER THE BOOK ID:")
                    if len(bookid) != 13:
                        print("\nENTER A VALID BOOK ID (BOOK ID SHOULD BE OF 13 DIGITS)")
                    else:
                        break
                title = input("\nENTER THE TITLE OF THE BOOK:")
                author = input("\nENTER THE AUTHOR OF THE BOOK:")
                publisher = input("\nENTER THE PUBLISHER OF THE BOOK:")
                rprice = int(input("\nENTER THE RETAIL PRICE OF THE BOOK :"))
                qt = int(input("\nENTER THE NUMBER OF BOOKS :"))
                while True:
                    clss = int(input("\nPROVIDE US THE CLASS:"))
                    if clss > 12:
                        print("\nENTER A VALID CLASS. (CLASS SHOULD BE BETWEEN 1 TO 12 ONLY")
                    else:
                        break
                y = int(input("\nENTER THE YEAR OF INVOICE :"))
                if y % 4 == 0:
                    while True:
                        m = int(input("\nENTER THE MONTH OF INVOICE :"))
                        if m > 12:
                            print("\nENTER A VALID MONTH (MONTH SHOULD BE ENTERED FROM 1 TO 12 ONLY)")
                        elif m in [1, 3, 5, 7, 8, 10, 12]:
                            while True:
                                d1 = int(input("\nENTER THE DAY OF INVOICE :"))
                                if d1 > 31:
                                    print("\nENTER A VALID DAY (DATE SHOULD BE ENTERED FROM 1 TO 31 ONLY)")
                                else:
                                    re11 = (str(y) + "-" + str(m) + "-" + str(d1))
                                    ins = "insert into books (bookid,title,author,publisher,class,retailprice,quantity) values ('{}','{}','{}','{}',{},{},{})".format(bookid, title, author, publisher, clss, rprice, qt)
                                    cur.execute(ins)
                                    db.commit()
                                    deal = "insert into purchase(bookid,title,author,publisher,class,date,quantity) values('{}','{}','{}','{}',{},'{}',{})".format(bookid, title, author, publisher, clss, re11, qt)
                                    cur.execute(deal)
                                    db.commit()
                                    break
                            break
                        elif m in [2, 4, 6, 9, 11]:
                            while True:
                                d2 = int(input("\nENTER THE DAY OF INVOICE :"))
                                if d2 > 30:
                                    print("\nENTER A VALID DAY (DATE SHOULD BE ENTERED FROM 1 TO 30 ONLY)")
                                else:
                                    date = (str(y) + "-" + str(m) + "-" + str(d2))
                                    ins = "insert into books (bookid,title,author,publisher,class,retailprice,quantity) values ('{}','{}','{}','{}',{},{},{})".format(bookid, title, author, publisher, clss, rprice, qt)
                                    cur.execute(ins)
                                    db.commit()
                                    deal = "insert into purchase(bookid,title,author,publisher,class,date,quantity) values('{}','{}','{}','{}',{},'{}',{})".format(bookid, title, author, publisher, clss, date, qt)
                                    cur.execute(deal)
                                    db.commit()
                                    break
                            break
                        elif m == 2:
                            while True:
                                d3 = int(input("\nENTER THE DAY OF INVOICE :"))
                                if d3 > 29:
                                    print("\nENTER A VALID DAY (DAY SHOULD BE ENTERED FROM 1 TO 29 ONLY)")
                                else:
                                    date = (str(y) + "-" + str(m) + "-" + str(d3))
                                    ins = "insert into books (bookid,title,author,publisher,class,retailprice,quantity) values ('{}','{}','{}','{}',{},{},{})".format(bookid, title, author, publisher, clss, rprice, qt)
                                    cur.execute(ins)
                                    db.commit()
                                    deal = "insert into purchase(bookid,title,author,publisher,class,date,quantity) values('{}','{}','{}','{}',{},'{}',{})".format(bookid, title, author, publisher, clss, date, qt)
                                    cur.execute(deal)
                                    db.commit()
                                    break
                            break
                else:
                    while True:
                        m = int(input("\nENTER THE MONTH OF INVOICE :"))
                        if m > 12:
                            print("\nENTER A VALID MONTH ")
                        elif m in [1, 3, 5, 7, 8, 10, 12]:
                            while True:
                                d1 = int(input("\nENTER THE DAY OF INVOICE :"))
                                if d1 > 31:
                                    print("\nENTER A VALID DAY (DATE SHOULD BE ENTERED FROM 1 TO 31 ONLY)")
                                else:
                                    re11 = (str(y) + "-" + str(m) + "-" + str(d1))
                                    ins = "insert into books (bookid,title,author,publisher,class,retailprice,quantity) values ('{}','{}','{}','{}',{},{},{})".format(bookid, title, author, publisher, clss, rprice, qt)
                                    cur.execute(ins)
                                    db.commit()
                                    deal = "insert into purchase(bookid,title,author,publisher,class,date,quantity) values('{}','{}','{}','{}',{},'{}',{})".format(bookid, title, author, publisher, clss, re11, qt)
                                    cur.execute(deal)
                                    db.commit()
                                    break
                            break
                        elif m in [2, 4, 6, 9, 11]:
                            while True:
                                d2 = int(input("\nENTER THE DAY OF INVOICE :"))
                                if d2 > 30:
                                    print("\nENTER A VALID DAY (DATE SHOULD BE ENTERED FROM 1 TO 30 ONLY)")
                                else:
                                    date = (str(y) + "-" + str(m) + "-" + str(d2))
                                    ins = "insert into books (bookid,title,author,publisher,class,retailprice,quantity) values ('{}','{}','{}','{}',{},{},{})".format(bookid, title, author, publisher, clss, rprice, qt)
                                    cur.execute(ins)
                                    db.commit()
                                    deal = "insert into purchase(bookid,title,author,publisher,class,date,quantity) values('{}','{}','{}','{}',{},'{}',{})".format(bookid, title, author, publisher, clss, date, qt)
                                    cur.execute(deal)
                                    db.commit()
                                    break
                            break
                        elif m == 2:
                            while True:
                                d3 = int(input("\nENTER THE DAY OF INVOICE :"))
                                if d3 > 28:
                                    print("\nENTER A VALID DAY (DAY SHOULD BE ENTERED FROM 1 TO 28 ONLY)")
                                else:
                                    date = (str(y) + "-" + str(m) + "-" + str(d3))
                                    ins = "insert into books (bookid,title,author,publisher,class,retailprice,quantity) values ('{}','{}','{}','{}',{},{},{})".format(bookid, title, author, publisher, clss, rprice, qt)
                                    cur.execute(ins)
                                    db.commit()
                                    deal = "insert into purchase(bookid,title,author,publisher,class,date,quantity) values('{}','{}','{}','{}',{},'{}',{})".format(bookid, title, author, publisher, clss, date, qt)
                                    cur.execute(deal)
                                    db.commit()
                                    break
                            break
                x = input("\nDO YOU WANT TO ADD MORE RECORDS ENTER ('Y'/'y') :\n")
                if x != "Y" or x != "y":
                    break
        elif zy == 2:
            break


def removebook():
    while True:
        print("\nREMOVE BOOK BY THE FOLLOWING :")
        print("\n")
        print("1. REMOVE BOOK BY BOOK ID ")
        print("2. REMOVE BOOK BY NAME ")
        print("3. BACK TO ADMINISTER MENU")
        print("\n")
        while True:
            y = int(input("SELECT A DESIRE OPTION FROM ABOVE : "))
            if y in [1, 2, 3]:
                break
            else:
                print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 TO 3)")
                continue

        if y == 1:
            while True:
                f = input("\nENTER THE BOOK ID FOR DELETING RECORD:")
                if len(f) != 13:
                    print("\nENTER A VALID BOOK ID (BOOKID SHOULD BE OF 13 DIGITS ONLY)")
                else:
                    break
            de = "delete from books where bookid='{}'".format(f)
            de1 = "delete from purchase where bookid='{}'".format(f)
            cur.execute(de)
            cur.execute(de1)
            db.commit()
            print("\nDATA DELETED SUCCESSFULLY...")
        elif y == 2:
            h = input("\nENTER THE TITLE OF THE BOOK :")
            it = "delete from books where title='{}'".format(h)
            it1 = "delete from books where title='{}'".format(h)
            cur.execute(it)
            cur.execute(it1)
            db.commit()
            print("\nDATA DELETED SUCCESSFULLY...")
        elif y == 3:
            break


def update():
    def contuple(net):
        nest = [['Book ID', 'Title', 'Author', 'Publisher', 'Class', 'Retail Price', 'Date', 'Quantity']]
        for ele in net:
            nest.append(list(ele))
        print(tabulate(nest, headers="firstrow", tablefmt="fancy_grid"))
    while True:
        print("\n1. UPDATE TITLE OF THE BOOK")
        print("2. UPDATE BOOK ID")
        print("3. UPDATE AUTHOR OF THE BOOK")
        print("4. UPDATE PUBLISHER OF THE BOOK ")
        print("5. UPDATE PRICE OF THE BOOK ")
        print("6. UPDATE QUANTITY OF THE BOOK ")
        print("7. UPDATE CLASS OF THE BOOK ")
        print("8. BACK TO MAIN MENU")
        while True:
            c = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
            if c in [1, 2, 3, 4, 5, 6, 7, 8]:
                break
            else:
                print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 TO 8)")
                continue

        if c == 1:
            while True:
                a1 = input("\nENTER  THE BOOK ID OF THE BOOK WHOSE TITLE IS TO BE UPDATED:")
                if len(a1) != 13:
                    print("\nENTER A VALID BOOK ID (BOOK ID SHOULD BE OF 13 DIGITS ONLY)")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(a1)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            tz = input("\nENTER THE NEW BOOK TITLE : ")
            u1 = "update books set title='{}' where bookid='{}'".format(tz, a1)
            cur.execute(u1)
            db.commit()
            print("\nDATA UPDATED SUCCESSFULLY...")
        if c == 2:
            while True:
                b = input("\nENTER THE  BOOK ID TO BE UPDATED:")
                if len(b) != 13:
                    print("\nENTER A VALID BOOK ID ( BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(b)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            while True:
                o = input("\nENTER THE NEW BOOK ID :")
                if len(o) != 13:
                    print("\nENTER A VALID BOOK ID (BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            u2 = "update books set bookid='{}' where bookid='{}'".format(o, b)
            cur.execute(u2)
            db.commit()
            print("\nBOOK ID UPDATED SUCCESSFULLY...")
        elif c == 3:
            while True:
                a2 = input("\nENTER  THE BOOK ID OF THE BOOK WHOSE AUTHOR IS TO BE UPDATED :")
                if len(a2) != 13:
                    print("\nENTER A VALID BOOK ID ( BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(a2)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            au2 = input("\nENTER THE NEW NAME OF THE AUTHOR :")
            u3 = "update books set author='{}' where bookid='{}'".format(au2, a2)
            cur.execute(u3)
            db.commit()
            print("\nAUTHOR UPDATED SUCCESSFULLY...")
        elif c == 4:
            while True:
                a3 = input("\nENTER  THE BOOK ID OF THE BOOK WHOSE PUBLISHER IS TO BE UPDATED :")
                if len(a3) != 13:
                    print("\nENTER A VALID BOOK ID (BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(a3)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            pu2 = input("\nENTER THE NEW NAME OF THE PUBLISHER:")
            u4 = "update books set publisher='{}' where bookid='{}'".format(pu2, a3,)
            cur.execute(u4)
            db.commit()
            print("\nPUBLISHER UPDATED SUCCESSFULLY...")
        elif c == 5:
            while True:
                a4 = input("\nENTER  THE BOOK ID OF THE BOOK WHOSE PRICE IS TO BE UPDATED :")
                if len(a4) != 13:
                    print("\nENTER A VALID BOOK ID (BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(a4)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            pr2 = int(input("\nENTER THE NEW RETAIL PRICE OF THE BOOK :"))
            u5 = "update books set retailprice={} where bookid='{}'".format(pr2, a4)
            cur.execute(u5)
            db.commit()
            print("\nRETAIL PRICE UPDATED SUCCESSFULLY...")
        elif c == 6:
            while True:
                a5 = input("\nENTER  THE BOOK ID OF THE BOOK WHOSE QUANTITY IS TO BE UPDATED :")
                if len(a5) != 13:
                    print("\nENTER A VALID BOOK ID ( BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(a5)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            qt2 = int(input("\nENTER THE NEW QUANTITY OF THE BOOK :"))
            u6 = "update books set quantity={} where bookid='{}'".format(qt2, a5)
            cur.execute(u6)
            db.commit()
            print("\nQUANTITY UPDATED SUCCESSFULLY...")
        elif c == 7:
            while True:
                a6 = input("\nENTER THE BOOK ID OF THE BOOK WHOSE CLASS  :")
                if len(a6) != 13:
                    print("\nENTER A VALID BOOK ID ( BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                else:
                    break
            s2 = "select * from sale where bookid='{}'".format(a6)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)
            cl2 = int(input("\nENTER THE NEW CLASS :"))
            u7 = "update books set class={} where bookid='{}'".format(cl2, a6)
            cur.execute(u7)
            db.commit()
            print("\nCLASS UPDATED SUCCESSFULLY...")
        elif c == 8:
            break


def saleinvoice():
    while True:
        print("\n1. SHOW ALL SALES INVOICE.")
        print("2. SEARCH SALES INVOICE BY BOOK ID")
        print("3. SEARCH SALES INVOICE BY DATE")
        print("4. SEARCH SALES INVOICE BY AUTHOR ")
        print("5. BACK TO ADMINISTER MENU")
        while True:
            sql = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
            if sql in [1, 2, 3, 4, 5]:
                break
            else:
                print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 TO 7)")
                continue

        def contuple(net):
            nest = [['Book ID', 'Title', 'Author', 'Publisher', 'Class', 'Retail Price', 'Date', 'Quantity']]
            for ele in net:
                nest.append(list(ele))
            print(tabulate(nest, headers="firstrow", tablefmt="fancy_grid"))

        if sql == 1:
            s1 = "select * from sale"
            cur.execute(s1)
            r1 = cur.fetchall()
            contuple(r1)

        elif sql == 2:
            q2 = input("\nENTER THE BOOK ID :")
            s2 = "select * from sale where bookid='{}'".format(q2)
            cur.execute(s2)
            r2 = cur.fetchall()
            contuple(r2)

        elif sql == 3:
            y = int(input("\nENTER THE YEAR OF INVOICE :"))
            if y % 4 == 0:
                while True:
                    m = int(input("\nENTER THE MONTH OF INVOICE :"))
                    if m > 12:
                        print("\nENTER A VALID MONTH ( MONTH SHOULD BE BETWEEN 1 TO 12 ONLY )")
                    else:
                        break
                    if m in [1, 3, 5, 7, 8, 10, 12]:
                        while True:
                            d1 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d1 > 31:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 31 )")
                            else:
                                re11 = (str(y) + "-" + str(m) + "-" + str(d1))
                                sy11 = "select * from purchase where date='{}'".format(re11)
                                cur.execute(sy11)
                                re1 = cur.fetchall()
                                contuple(re1)
                                break
                    elif m in [4, 6, 9, 11]:
                        while True:
                            d2 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d2 > 30:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 30 )")
                            else:
                                re12 = (str(y) + "-" + str(m) + "-" + str(d2))
                                sy12 = "select * from purchase where date='{}'".format(re12)
                                cur.execute(sy12)
                                re2 = cur.fetchall()
                                contuple(re2)
                                break
                    elif m == 2:
                        while True:
                            d3 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d3 > 29:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 29 )")
                            else:
                                re13 = (str(y) + "-" + str(m) + "-" + str(d3))
                                sy13 = "select * from purchase where date='{}'".format(re13)
                                cur.execute(sy13)
                                re3 = cur.fetchall()
                                contuple(re3)
                                break
                    break
            else:
                while True:
                    m = int(input("\nENTER THE MONTH OF INVOICE :"))
                    if m > 12:
                        print("\nENTER A VALID MONTH ( MONTH SHOULD BE FROM 1 TO 12 ONLY )")
                    elif m in [1, 3, 5, 7, 8, 10, 12]:
                        while True:
                            d1 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d1 > 31:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 31 )")
                            else:
                                re11 = (str(y) + "-" + str(m) + "-" + str(d1))
                                sy11 = "select * from purchase where date='{}'".format(re11)
                                cur.execute(sy11)
                                re1 = cur.fetchall()
                                contuple(re1)
                                break
                    elif m in [4, 6, 9, 11]:
                        while True:
                            d2 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d2 > 30:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 30 )")
                            else:
                                re12 = (str(y) + "-" + str(m) + "-" + str(d2))
                                sy12 = "select * from purchase where date='{}'".format(re12)
                                cur.execute(sy12)
                                re2 = cur.fetchall()
                                contuple(re2)
                                break
                    elif m == 2:
                        while True:
                            d3 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d3 > 28:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 28 )")
                            else:
                                re13 = (str(y) + "-" + str(m) + "-" + str(d3))
                                sy13 = "select * from purchase where date='{}'".format(re13)
                                cur.execute(sy13)
                                re3 = cur.fetchall()
                                contuple(re3)
                                break
                    break
        elif sql == 4:
            au3 = input("\nENTER THE NAME OF THE AUTHOR :")
            s5 = "select * from sale where author='{}'".format(au3)
            cur.execute(s5)
            r5 = cur.fetchall()
            contuple(r5)
        elif sql == 5:
            break


def prinvoice():
    def convtuple(net):
        nest = [['Book ID', 'Title', 'Author', 'Publisher', 'Class', 'Retail Price', 'Date', 'Quantity']]
        for ele in net:
            nest.append(list(ele))
        print(tabulate(nest, headers="firstrow", tablefmt="fancy_grid"))
    while True:
        print("\n")
        print("\n")
        print("1. SHOW ALL PURCHASE INVOICE")
        print("2. SEARCH PURCHASE INVOICE BY BOOK ID")
        print("3. SEARCH PURCHASE INVOICE BY DATE")
        print("4. SEARCH PURCHASE INVOICE BY AUTHOR")
        print("5. BACK TO ADMINISTER MENU")
        while True:
            ch7 = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
            if ch7 in [1, 2, 3, 4, 5]:
                break
            else:
                print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 TO 7)\n")
                continue

        if ch7 == 1:
            sy1 = "select * from purchase"
            cur.execute(sy1)
            ry1 = cur.fetchall()
            convtuple(ry1)
        elif ch7 == 2:
            while True:
                ins1 = input("\nENTER THE BOOK ID :")
                if len(ins1) != 13:
                    print("\nENTER A VALID BOOK ID ( BOOK ID SHOULD BE OF 13 DIGITS ONLY )")
                sy2 = "select * from purchase where bookid='{}'".format(ins1)
                cur.execute(sy2)
                ry2 = cur.fetchall()
                convtuple(ry2)
                break
        elif ch7 == 3:
            y = int(input("\nENTER THE YEAR OF INVOICE :"))
            if y % 4 == 0:
                while True:
                    m = int(input("\nENTER THE MONTH OF INVOICE :"))
                    if m > 12:
                        print("\nENTER A VALID MONTH ( MONTH SHOULD BE FROM 1 TO 12 )")

                    elif m in [1, 3, 5, 7, 8, 10, 12]:
                        while True:
                            d1 = int(input("\nENTER THE DAY OF INVOICE  :"))
                            if d1 > 31:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 31 ONLY )")
                            else:
                                re11 = (str(y)+"-"+str(m)+"-"+str(d1))
                                sy11 = "select * from purchase where date='{}'".format(re11)
                                cur.execute(sy11)
                                re1 = cur.fetchall()
                                convtuple(re1)
                                break
                    elif m in [4, 6, 9, 11]:
                        while True:
                            d2 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d2 > 30:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 30 ONLY )")
                            else:
                                re12 = (str(y)+"-"+str(m)+"-"+str(d2))
                                sy12 = "select * from purchase where date='{}'".format(re12)
                                cur.execute(sy12)
                                re2 = cur.fetchall()
                                convtuple(re2)
                                break
                    elif m == 2:
                        while True:
                            d3 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d3 > 29:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 29 ONLY )")
                            else:
                                re13 = (str(y)+"-"+str(m)+"-"+str(d3))
                                sy13 = "select * from purchase where date='{}'".format(re13)
                                cur.execute(sy13)
                                re3 = cur.fetchall()
                                convtuple(re3)
                                break
                    break
            else:
                while True:
                    m = int(input("\nENTER THE MONTH OF INVOICE :"))
                    if m > 12:
                        print("\nENTER A VALID MONTH ( MONTH SHOULD BE BETWEEN 1 TO 12 )")

                    elif m in [1, 3, 5, 7, 8, 10, 12]:
                        while True:
                            d1 = int(input("\nENTER THE DAY OF INVOICE  :"))
                            if d1 > 31:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 31 ONLY )")
                            else:
                                re11 = (str(y)+"-"+str(m)+"-"+str(d1))
                                sy11 = "select * from purchase where date='{}'".format(re11)
                                cur.execute(sy11)
                                re1 = cur.fetchall()
                                convtuple(re1)
                                break
                    elif m in [4, 6, 9, 11]:
                        while True:
                            d2 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d2 > 30:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 30 ONLY )")
                            else:
                                re12 = (str(y)+"-"+str(m)+"-"+str(d2))
                                sy12 = "select * from purchase where date='{}'".format(re12)
                                cur.execute(sy12)
                                re2 = cur.fetchall()
                                convtuple(re2)
                                break
                    elif m == 2:
                        while True:
                            d3 = int(input("\nENTER THE DAY OF INVOICE :"))
                            if d3 > 28:
                                print("\nENTER A VALID DAY ( DAY SHOULD BE FROM 1 TO 28 ONLY )")
                            else:
                                re13 = (str(y)+"-"+str(m)+"-"+str(d3))
                                sy13 = "select * from purchase where date='{}'".format(re13)
                                cur.execute(sy13)
                                re3 = cur.fetchall()
                                convtuple(re3)
                                break
                    break
        elif ch7 == 4:
            ins3 = input("\nENTER THE NAME OF THE AUTHOR :")
            sy4 = "select * from purchase where author='{}'".format(ins3)
            cur.execute(sy4)
            ry4 = cur.fetchall()
            convtuple(ry4)
        elif ch7 == 5:
            break


def section():
    while True:
        se = int(input("\nWHICH CLASS BOOK YOU WANT TO PURCHASE(10 or 12) : "))
        if 10 == se or se == 12:
            break
        else:
            print("\n INVALID OPTION GIVEN. ENTER THE CORRECT VALUE {10 OR 12 }...")
            continue
    return se


def fn1():
    def convtuple(net):
        nest = [['Book ID', 'Title', 'Author', 'Publisher', 'Class', 'Retail Price', 'Quantity']]
        for ele in net:
            nest.append(list(ele))
        print(tabulate(nest, headers="firstrow", tablefmt="fancy_grid"))
    while True:
        print1 = "select * from books"
        cur.execute(print1)
        r1 = cur.fetchall()
        convtuple(r1)
        print("\n***************************************************************************************************\n")
        print("1.PURCHASE BOOK BY BOOK NAME.")
        print("2.PURCHASE BOOK BY BOOK ID")
        print("3.BACK TO CUSTOMER MENU.")
        print("\n***************************************************************************************************\n")
        while True:
            bo = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
            if bo in [1, 2, 3]:
                break
            else:
                print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1/3)")
                continue

        if bo == 1:
            order = input("\nPROVIDE US THE NAME OF THE BOOK YOU WANT TO PURCHASE : ")
            x = section()
            consignment = int(input("\nENTER THE NUMBER OF BOOKS THAT YOU  WANT TO PURCHASE : "))
            string1 = "select quantity from books where title = '{}' ".format(order)
            cur.execute(string1)
            res1 = cur.fetchall()
            for i in res1:
                rec = order
                g = i[0]
                if g == 0:
                    print("\nBOOK CANNOT BE SOLD AS IT IS NOT AVAILABLE IN OUR STOCK\n")
                    break
                elif consignment > g:
                    print("\nTHERE ARE ONLY ", g, "COPIES LEFT OF THIS BOOK")
                    while True:
                        purchase = input("\nDO YOU WANT TO PURCHASE LESS COPIES THAN YOUR NEED ? (Y/N) :")
                        if purchase == "Y" or "y":
                            cons = int(input("\nENTER THE NUMBER OF BOOKS YOU WANT TO PURCHASE FROM LEFT OVER STOCK :"))
                            chy = "update books set quantity = quantity-{} where title='{}' and class={}".format(cons, rec, x, )
                            cur.execute(chy)
                            db.commit()
                            print("\nBOOK PURCHASED SUCCESSFULLY...\n")
                            break
                        else:
                            print("\nTHANK YOU FOR VISITING US...")
                            break
                else:
                    chz = "update books set quantity = quantity-{} where title='{}' and class={}".format(consignment, order, x, )
                    cur.execute(chz)
                    db.commit()
                    print("\nBOOK PURCHASED SUCCESSFULLY...\n")
                    break
            break
        elif bo == 2:
            while True:
                identity = input("\nPROVIDE US THE BOOK ID OF THE BOOK YOU WANT TO PURCHASE : ")
                if len(str(identity)) < 13:
                    print("\nSHORT ID GIVEN PLEASE ENTER 13 DIGIT BOOK ID \n")
                    continue
                elif len(str(identity)) > 13:
                    print("\nLONG ID GIVEN PLEASE ENTER 13 DIGIT BOOK ID \n")
                    continue
                else:
                    break
            x = section()
            consignment = int(input("\nENTER THE NUMBER OF BOOKS THAT YOU  WANT TO PURCHASE : "))
            s = "select quantity from books where bookid={}".format(identity, )
            cur.execute(s)
            item = cur.fetchall()
            for i in item:
                pro = i[0]
                if pro == 0:
                    print("\nBOOK CANNOT BE SOLD AS IT IS NOT AVAILABLE IN OUR STOCK\n")
                elif consignment > pro:
                    print("\nTHERE ARE ONLY ", pro, "COPIES LEFT OF THIS BOOK")
                    while True:
                        purchase = input("\nDO YOU WANT TO PURCHASE LESS COPIES THAN YOUR NEED ? (Y/N) :")
                        if purchase == "Y" or purchase == "y":
                            cons = int(input("\nENTER THE NUMBER OF BOOKS YOU WANT TO PURCHASE FROM LEFT OVER STOCK :"))
                            chy = "update books set quantity = quantity-{} where bookid={} and class={}".format(cons, identity, x,)
                            cur.execute(chy)
                            db.commit()
                            print("\nBOOK PURCHASED SUCCESSFULLY...\n")
                            break
                        else:
                            print("\nTHANK YOU FOR VISITING US...")
                            break
                else:
                    chx = "update books set quantity = quantity-{} where bookid={}".format(consignment, identity, )
                    cur.execute(chx)
                    db.commit()
                    print("\nBOOK PURCHASED SUCCESSFULLY...\n")
                    break
            break
        elif bo == 3:
            break


def fn2():
    replace = input("\n PROVIDE US THE NAME OF THE BOOK YOU WANT TO REPLACE : ")
    s = int(input("\n WHICH CLASS BOOK ARE YOU WILLING TO REPLACE :  "))
    cla=int(input("\n WHICH CLASS BOOK ARE YOU WILLING TO GET :  "))
    new_book = input("\n PROVIDE US THE NAME OF THE NEW BOOK YOU WANT TO  GET IN REPLACEMENT : ")
    bring = "select * from books where title ='{}' and class={}".format(new_book, cla)
    cur.execute(bring)
    gr = cur.fetchall()
    print(gr)
    for i in gr:
        product = i[0]
        if product== 0:
            print("\nBOOK CANNOT BE REPLACED AS IT IS NOT AVAILABLE IN OUR STOCK..\n")
        else:
            query = "update books set quantity = quantity+1 where title='{}' and class={}".format(replace, s, )
            cur.execute(query)
            db.commit()
            chy = "update books set quantity = quantity-1 where title='{}' and class={}".format(new_book, cla, )
            cur.execute(chy)
            db.commit()
            print("\nBOOK REPLACED SUCCESSFULLY...\n")


def fn3():
    refund = input("\n PROVIDE US THE NAME OF THE BOOK FOR WHICH YOU WANT REFUND : ")
    consignment = int(input("\nENTER THE NUMBER OF BOOKS THAT YOU  WANT TO REFUND : "))
    book_class = int(input("\nWHICH CLASS BOOK IS TO BE REFUNDED : "))
    final = "update books set quantity = quantity+{} where title='{}' and class={}".format(consignment, refund, book_class,)
    cur.execute(final)
    db.commit()
    print("\nBOOK REFUNDED SUCCESSFULLY...\n")


while True:
    print("***************************************************************************************************")
    print("***************************************************************************************************")
    print("                                     SHOP MANAGEMENT SYSTEM                                        ")
    print("***************************************************************************************************")
    print("\n============================================MAIN MENU=============================================\n")
    print("1. CUSTOMER.")
    print("2. ADMINISTER.")
    print("3. EXIT")
    print("\n==================================================================================================\n")

    while True:
        ch = int(input("\n ENTER YOUR OPTION(1/3): "))
        if ch in (1, 2, 3):
            break
        elif ch not in (1, 2, 3):
            print("INVALID CHOICE GIVEN . PLEASE ENTER A VALID CHOICE ( 1 to 3 )")
            continue
    if ch == 1:

        while True:
            print("\n******************************************* CUSTOMER ********************************************\n")
            print("1. PURCHASE A BOOK.")
            print("2. REPLACE A BOOK.")
            print("3. REFUND A BOOK.")
            print("4. BACK TO MAIN MENU.")
            print("\n*************************************************************************************************\n")
            while True:
                B = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
                if B in [1, 2, 3, 4]:
                    break
                else:
                    print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 TO 4)\n")
                    continue
            if B == 1:
                fn1()
            elif B == 2:
                fn2()
            elif B == 3:
                fn3()
            elif B == 4:
                break
    elif ch == 2:
        while True:
            print("\n=======================================  ADMINISTER MENU  =======================================\n")
            print("\n")
            print("1. ADD A BOOK TO STOCK")
            print("2. REMOVE A BOOK FROM STOCK")
            print("3. UPDATE BOOK IN STOCK  ")
            print("4. VIEW SALES INVOICE")
            print("5. VIEW PURCHASE INVOICE")
            print("6. BACK TO MAIN MENU")
            print("\n==================================================================================================\n")
            while True:
                Z = int(input("\nSELECT A DESIRE OPTION FROM ABOVE : "))
                if Z in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("\nINVALID OPTION GIVEN . PLEASE ENTER A VALID OPTION(1 TO 6)")
                    continue
            if Z == 1:
                addbook()
            elif Z == 2:
                removebook()
            elif Z == 3:
                update()
            elif Z == 4:
                saleinvoice()
            elif Z == 5:
                prinvoice()
            elif Z == 6:
                break
    elif ch == 3:
        print("\nTHANKS FOR COMING...\n")
        break
