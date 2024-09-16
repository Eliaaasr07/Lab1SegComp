import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

def leer_auto():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos de autos')

    layout = QFormLayout()
    
    for i in range(1, 4):
        nombre_input = QLineEdit()
        tipo_input = QLineEdit()
        edad_input = QLineEdit()

        layout.addRow(f'Nombre del Auto {i}:', nombre_input)
        layout.addRow(f'Tipo de Auto {i}:', tipo_input)
        layout.addRow(f'Año del Auto {i}:', edad_input)

    ventana.setLayout(layout)
    ventana.resize(300, 300)
    ventana.show()
    sys.exit(app.exec_())

leer_auto()