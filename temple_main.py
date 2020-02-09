
import sys  # sys нужен для передачи argv в QApplication
import calculation_controllers

from PyQt5 import QtWidgets, QtCore, QtGui

from win_calculate import *  # Это наш конвертированный файл дизайна



class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        self.ui.pushButton.clicked.connect(self.MyFunction) # здесь прописываем события нажатия на кнопку

    def MyFunction(self):
        
        INPUT_OPERATOR = []
        self.ui.textBrowser_outputrezult.setText("")

        AI = self.ui.spinBox_AI.value()
        BI = self.ui.spinBox_BI.value()
        AO = self.ui.spinBox_AO.value()
        BO = self.ui.spinBox_BO.value()
        UI = self.ui.spinBox_UI.value()
        CO = self.ui.spinBox_CO.value()
        
        INPUT_OPERATOR.append(AI)
        INPUT_OPERATOR.append(BI)
        INPUT_OPERATOR.append(AO)
        INPUT_OPERATOR.append(BO)
        INPUT_OPERATOR.append(UI)
        INPUT_OPERATOR.append(CO)
        
        rezult = calculation_controllers.calclulator(INPUT_OPERATOR)
        
        self.ui.textBrowser_outputrezult.setText(str(rezult))
       
        

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()