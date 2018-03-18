import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3
conn = sqlite3.connect("Dsouza.db")
cur = conn.cursor()

def CreateTables():
        cur.executescript("""drop table if exists Days;create table Days (DoY int not null,DoW text,Holiday int,Weather text);""")
        cur.executescript("""drop table if exists Sales;create table Sales (TrxId int,DoY int not null,StoreId int,SoupId int,PromoId int, Sales float);""")
        cur.executescript("""drop table if exists Stores;create table Stores (StoreID int,Location text,Elevation text,Size text,MgrId,MgrName text);""")
        cur.executescript("""drop table if exists Managers;create table Managers (MgrId int,MgrName text,Grade text, Years int);""")
        cur.executescript("""drop table if exists Soups;create table Soups (SoupId int, Type text,Vendor text, Mode text,Style text);""")
        cur.executescript("""drop table if exists Promotion;create table Promotion (PromoId int,Medium text,Target text,Interval text);""")
        return
    
def InsertSoups(record):
        SoupId = int(record[13])
        Type = record[14]
        Vendor = record[15]
        Mode = record[16]
        Style = record[17]
        row = [SoupId,Type,Vendor,Mode,Style]
        cur.execute("SELECT * from Soups")
        out2=cur.fetchall()
        i=0
        x= len(out2)
        if x!=0:
            while i<len(out2):
                if row[0]==out2[i][0]:
                    return
                else:
                    i+=1     
        cur.execute("INSERT INTO Soups VALUES(?,?,?,?,?)",row)
        return

def InsertPromotion(record):
        PromoId = int(record[18])
        Medium = record[19]
        Target = record[20]
        Interval = record[21]
        row = [PromoId,Medium,Target,Interval]
        cur.execute("SELECT * from Promotion")
        out2=cur.fetchall()
        i=0
        x= len(out2)
        if x!=0:
            while i<len(out2):
                if row[0]==out2[i][0]:
                    return
                else:
                    i+=1     
        cur.execute("INSERT INTO Promotion VALUES(?,?,?,?)",row)
        return

def InsertManagers(record):
        MgrId = int(record[9])
        MgrName = record[10]
        Grade = record[11]
        Years = int(record[12])
        row = [MgrId,MgrName,Grade,Years]
        cur.execute("SELECT * from Managers")
        out2=cur.fetchall()
        i=0
        x= len(out2)
        if x!=0:
            while i<len(out2):
                if row[0]==out2[i][0]:
                    return
                else:
                    i+=1     
        cur.execute("INSERT INTO Managers VALUES(?,?,?,?)", row)
        return

def InsertStores(record):
        StoreID = int(record[5])
        Location = record[6]
        Elevation =record[7]
        Size =record[8]
        MgrId = record[9]
        MgrName = record[10]
        row = [StoreID,Location,Elevation,Size,MgrId,MgrName]
        cur.execute("SELECT * from Stores")
        out2=cur.fetchall()
        i=0
        x= len(out2)
        if x!=0:
            while i<len(out2):
                if row[0]==out2[i][0]:
                    return
                else:
                    i+=1
        cur.execute("INSERT INTO Stores VALUES(?, ?, ?,?,?,?)", row)
        return

def InsertSales(record):
        TrxId = int(record[0])
        DoY = int(record[1])
        StoreId = int(record[5])
        SoupId = int(record[13])
        PromoId = int(record[18])
        Sales = float(record[22])
        row = [TrxId,DoY,StoreId,SoupId, PromoId, Sales]
        cur.execute("INSERT INTO Sales VALUES(?, ?, ?,?,?,?)", row)
        return

def InsertDays(record):
        DoY = int(record[1])
        DoW = record[2]
        Holiday = int(record[3])
        Weather = record[4]
        row = [DoY,DoW,Holiday,Weather]
        cur.execute("SELECT * from Days")
        out2=cur.fetchall()
        i=0
        x= len(out2)
        if x!=0:
            while i<len(out2):
                if row[0]==out2[i][0]:
                    return
                else:
                    i+=1     
        cur.execute("INSERT INTO Days VALUES(?,?,?,?)", row)
        return

class Form( QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.pbutton0 = QPushButton("Load Data")
        self.lineedit0 = QLineEdit("Enter Input File Name")
        self.pbutton1 = QPushButton("Total Row Count")
        self.lineedit1 = QLineEdit("")
        self.pbutton2 = QPushButton("Table Row Count")
        self.lineedit2 = QLineEdit("Enter Table Name")
        self.pbutton3 = QPushButton("List Table")
        self.lineedit3 = QLineEdit("Enter Table Name")
        self.pbutton4 = QPushButton("Custom SQL Statement")
        self.lineedit4 = QLineEdit("Enter SQL Statement")
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.pbutton0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        self.lineedit1.setFocus()
        self.connect(self.pbutton0, SIGNAL("clicked()"),self.button0Pressed)
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        self.setWindowTitle("Data Processor")
        return
 
    def button0Pressed(self):
        x = str(self.lineedit0.text())
        try:
                f = open(x,'r')
        except:
                self.lineedit0.setText("File not found.")
                return
        
        linecount = 0
        CreateTables()
        line = f.readline()
        while line != "":
            linecount = linecount + 1
            line = line.replace("\n","")
            line = line.replace("\r","")
            linelist = line.split("\t")
            InsertStores(linelist)
            InsertManagers(linelist)
            InsertDays(linelist)
            InsertSoups(linelist)
            InsertPromotion(linelist)
            InsertSales(linelist)
            line = f.readline()
        self.lineedit0.setText("All Loaded")
        conn.commit()
        f.close()

    def button1Pressed(self):
        num1=[]
        cur.execute("SELECT Count(*) FROM Sales")
        num=cur.fetchall()
        num1.append(num[0][0])
        cur.execute("SELECT Count(*) FROM Soups")
        num=cur.fetchall()
        num1.append(num[0][0])
        cur.execute("SELECT Count(*) FROM Managers")
        num=cur.fetchall()
        num1.append(num[0][0])
        cur.execute("SELECT Count(*) FROM Days")
        num=cur.fetchall()
        num1.append(num[0][0])
        cur.execute("SELECT Count(*) FROM Promotion")
        num=cur.fetchall()
        num1.append(num[0][0])
        cur.execute("SELECT Count(*) FROM Stores")
        num=cur.fetchall()
        num1.append(num[0][0])
        sum1 = sum(num1)
        str1 = "Sales: "+str(num1[0])+"  Soups: "+str(num1[1])+"  Managers: "+str(num1[2])+"  Days: "+str(num1[3])+"  Promotion: "+str(num1[4])+"  Stores: "+str(num1[5])+"  Total: "+str(sum1)
        self.lineedit1.setText(str1)
       
    def button2Pressed(self):
        x = str(self.lineedit2.text())
        x=x.lower()
        if x=="sales":
            cur.execute("SELECT Count(*) FROM Sales")
            num=cur.fetchall()
            self.lineedit2.setText(str(num[0][0]))

        elif x=="soups":
            cur.execute("SELECT Count(*) FROM Soups")
            num=cur.fetchall()
            self.lineedit2.setText(str(num[0][0]))

        elif x=="managers":
            cur.execute("SELECT Count(*) FROM Managers")
            num=cur.fetchall()
            self.lineedit2.setText(str(num[0][0]))

        elif x=="days":
            cur.execute("SELECT Count(*) FROM Days")
            num=cur.fetchall()
            self.lineedit2.setText(str(num[0][0]))

        elif x=="promotion":
            cur.execute("SELECT Count(*) FROM Promotion")
            num=cur.fetchall()
            self.lineedit2.setText(str(num[0][0]))

        elif x=="stores":
            cur.execute("SELECT Count(*) FROM Stores")
            num=cur.fetchall()
            self.lineedit2.setText(str(num[0][0]))

        else:
            self.lineedit2.setText("No such table found.")
            
    def button3Pressed(self):
        x = str(self.lineedit3.text())
        str2="Select * from "+x+";"
        try:
                cur.execute(str2)
        except:
                self.lineedit3.setText("No such table found.")
                return
        st1=""
        out=cur.fetchall()
        g=len(out)
        h=0
        self.lineedit3.setText("Output on IDLE")
        print"Table ",x," contents:"
        while g>0:
                for y in out[h]: 
                        st1+=str(y)
                        st1+=' '
                print st1
                st1=""
                g-=1
                h+=1
                                    
    def button4Pressed(self):
        x = str(self.lineedit4.text())
        try:
                cur.execute(x)
        except:
                self.lineedit4.setText("Invalid Statement. Try again.")
                return
        st1=""
        out=cur.fetchall()
        g=len(out)
        h=0
        self.lineedit4.setText("Output on IDLE")
        print "\n"
        while g>0:
                for y in out[h]: 
                        st1+=str(y)
                        st1+=' '
                print st1
                st1=""
                g-=1
                h+=1
        print("\nSQL Statement Executed.")               
        
    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
        
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
