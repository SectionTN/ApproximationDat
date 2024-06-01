from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from pickle import dump, load


def rechp(x):
    p = 1
    while p * p < x:
        p += 1
    if p * p == x:
        return p
    else:
        return p - 1


def calcul_rc(x):
    U0 = rechp(x)
    Un = (1 / 2) * (U0 + x / U0)
    while abs(Un - U0) > 0.00001:
        U0 = Un
        Un = (1 / 2) * (U0 + (x / U0))
    return Un


def ajouter():
    x = window.x.text()
    if x == "" or x.isdigit() is False:
        QMessageBox.critical(window, "Erreur", "Veuillez saisir une valeur pour x", QMessageBox.Ok)
    elif not (2 <= int(x) <= 200):
        QMessageBox.critical(window, "Erreur", "Veuillez saisir une valeur entre 2 et 200", QMessageBox.Ok)
    else:
        x = float(x)
        file = open("approchee.dat", "ab")
        e = dict(x=float, RC=float)
        e["x"] = x
        e["RC"] = calcul_rc(x)
        dump(e, file)
        file.close()


def afficher():
    file = open("approchee.dat", "rb")
    eof = False
    i = 0
    try:
        while not eof:
            e = load(file)
            window.table.insertRow(i)
            window.table.setItem(i, 0, QTableWidgetItem(str(e["x"])))
            window.table.setItem(i, 1, QTableWidgetItem(str(e["RC"])))
            i += 1
    except:
        eof = True
        file.close()


application = QApplication([])
window = loadUi("Interface_Racine.ui")
window.ajout.clicked.connect(ajouter)
window.affiche.clicked.connect(afficher)
window.show()
application.exec_()
