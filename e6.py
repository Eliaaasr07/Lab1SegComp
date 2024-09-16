import sys
from PyQt5.QtWidgets import *

class Formulario(QWidget):
    def __init__(self):  
        super().__init__()  
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Formulario de Usuario')
       
        layout = QVBoxLayout()

        self.genero_label = QLabel('Seleccione su género:')
        self.genero_hombre = QRadioButton('Masculino')
        self.genero_mujer = QRadioButton('Femenino')

        genero_layout = QHBoxLayout()
        genero_layout.addWidget(self.genero_hombre)
        genero_layout.addWidget(self.genero_mujer)
        
        self.ocupacion_label = QLabel('Seleccione su ocupación:')
        self.ocupacion_combobox = QComboBox()
        self.ocupacion_combobox.addItems(['Estudiante', 'Empleado', 'Autónomo', 'Desempleado', 'Jubilado'])
        
        self.edad_label = QLabel('Seleccione su edad:')
        self.edad_spinbox = QSpinBox()
        self.edad_spinbox.setRange(0, 120)
        
        self.enviar_button = QPushButton('Enviar')
        self.enviar_button.clicked.connect(self.mostrar_datos)
        
        layout.addWidget(self.genero_label)
        layout.addLayout(genero_layout)
        layout.addWidget(self.ocupacion_label)
        layout.addWidget(self.ocupacion_combobox)
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_spinbox)
        layout.addWidget(self.enviar_button)
        
        self.setLayout(layout)
    
    def mostrar_datos(self):
        if self.genero_hombre.isChecked():
            genero = 'Masculino'
        elif self.genero_mujer.isChecked():
            genero = 'Femenino'
        else:
            genero = 'No seleccionado'
        
        ocupacion = self.ocupacion_combobox.currentText()
        edad = self.edad_spinbox.value()
        
        mensaje = f"Género: {genero}\nOcupación: {ocupacion}\nEdad: {edad}"
        QMessageBox.information(self, 'Datos Ingresados', mensaje)

if __name__ == '__main__':  
    app = QApplication(sys.argv)
    ventana = Formulario()
    ventana.show()
    sys.exit(app.exec_())
