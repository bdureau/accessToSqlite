# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from os import walk
import sqlite3
from Databases import DB

def dbInt(intVal):
    if intVal is None:
        ret = "Null"
    else:
        ret =str(intVal)
    return ret

def dbStr(strVal):
    if strVal is None:
        ret = ""
    else:
        ret =str(strVal)
    return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filenames = next(walk("databases"), (None, None, []))[2]  # [] if no file

    # create an array of file name first the open the db with the first one
    stampCountries = []
    for file in filenames:
        shortFile = file.rsplit(".")
        if shortFile[0] != "master":
            if shortFile[1] == "mdb":
                stampCountries.append(shortFile[0])

    for country in stampCountries:
        con = sqlite3.connect(country+".db")
        cur = con.cursor()

        # cur.execute("CREATE TABLE movie(title, year, score)")
        res = cur.execute("SELECT name FROM sqlite_master WHERE name='stamp_list'")
        # print(res.fetchone())
        if res.fetchone() is None:
            cur.execute("CREATE TABLE stamp_list(key INTEGER, NBR TEXT, SUB_NBR TEXT, SEQUENCE INTEGER, \
                        year TEXT, valuecolor TEXT, \
                        stampDescription1 TEXT, stampDescription TEXT, width TEXT, height TEXT, country TEXT, Type TEXT, \
                        Serie TEXT, ASCII_SEQ TEXT)")

        res = cur.execute("SELECT name FROM sqlite_master")
        print(res.fetchone())
        print(res)

        db = DB(country)
        results = db.loadAllCountryStamps()
        for row in results.fetchall():
            print(row[0])
            cur.execute("INSERT INTO stamp_list VALUES (" + dbInt(row[0]) + ",'"
                        + dbStr(row[1]).translate(str.maketrans({"'": r"''"})) + "',"
                        + dbInt(row[2]) + ","
                        + dbInt(row[3]) + ",'"
                        + dbStr(row[4]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[5]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[6]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[7]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[8]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[9]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[10]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[11]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[12]).translate(str.maketrans({"'": r"''"})) + "','"
                        + dbStr(row[13]).translate(str.maketrans({"'": r"''"}))
                        + "')")
        con.commit()
        cur.execute("SELECT distinct type FROM Stamp_List")

    # convert the master db
    con = sqlite3.connect("master.db")
    cur = con.cursor()


    res = cur.execute("SELECT name FROM sqlite_master WHERE name='StampBox'")
    # print(res.fetchone())
    if res.fetchone() is None:
        cur.execute("CREATE TABLE StampBox(id INTEGER, pochette TEXT, designation TEXT, LX INTEGER, LY INTEGER)")

    res = cur.execute("SELECT name FROM sqlite_master")


    db = DB(country)
    results = db.loadAllBoxList()
    for row in results.fetchall():
        print(row[0])
        cur.execute("INSERT INTO StampBox VALUES (" + dbInt(row[0]) + ",'"
                    + dbStr(row[1]).translate(str.maketrans({"'": r"''"})) + "','"
                    + dbStr(row[2]).translate(str.maketrans({"'": r"''"})) + "',"
                    + dbInt(row[3]) + ","
                    + dbInt(row[4])
                    + ")")

    con.commit()