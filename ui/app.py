import sys
from typing import Callable, List

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from core.agente import Agente
from core.memoria import Memoria
from core.modos import MODO_LABELS, MODOS
from core.orquestador import Orquestador
from services.ai_client import GroqClient


class ConversationWorker(QThread):
    mensaje_nuevo = pyqtSignal(str)
    estado = pyqtSignal(str)
    error = pyqtSignal(str)
    terminado = pyqtSignal()

    def __init__(self, agentes: List[Agente], tema: str, usuario: str, modo: str, parent=None):
        super().__init__(parent)
        self._detener = False
        self.agentes = agentes
        self.tema = tema
        self.usuario = usuario
        self.modo = modo
        self.memoria = Memoria()

    def run(self) -> None:
        if not self.agentes:
            self.error.emit("No hay agentes activos para iniciar la conversación.")
            self.terminado.emit()
            return

        orquestador = Orquestador(self.agentes, memoria=self.memoria, max_turnos=12, delay=1.0)

        def callback(texto: str) -> None:
            self.mensaje_nuevo.emit(texto)

        def stop_checker() -> bool:
            return self._detener

        try:
            self.estado.emit("Iniciando conversación...")
            orquestador.iniciar(
                tema=self.tema,
                usuario_texto=self.usuario,
                modo=self.modo,
                callback=callback,
                stop_checker=stop_checker,
            )
            self.estado.emit("Conversación finalizada.")
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.terminado.emit()

    def detener(self) -> None:
        self._detener = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Multi-Agente AI")
        self.setMinimumSize(950, 700)

        self.worker: ConversationWorker | None = None
        self.client = GroqClient()

        self._crear_componentes()
        self._construir_layout()
        self._cargar_agentes_predeterminados()

    def _crear_componentes(self) -> None:
        self.agent_table = QTableWidget(3, 6)
        self.agent_table.setHorizontalHeaderLabels([
            "IA",
            "Personalidad",
            "Región",
            "Tema",
            "Participa",
            "Responde usuario",
        ])
        self.agent_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.agent_table.verticalHeader().setVisible(False)

        self.tema_input = QLineEdit()
        self.tema_input.setPlaceholderText("Ingrese el tema principal de la conversación")

        self.usuario_input = QLineEdit()
        self.usuario_input.setPlaceholderText("Ingrese la pregunta o comentario del usuario")

        self.modo_selector = QComboBox()
        for modo in MODOS:
            self.modo_selector.addItem(MODO_LABELS[modo], modo)

        self.start_button = QPushButton("Iniciar conversación")
        self.stop_button = QPushButton("Detener conversación")
        self.stop_button.setEnabled(False)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.status_label = QLabel("Listo")

        self.start_button.clicked.connect(self.iniciar_conversacion)
        self.stop_button.clicked.connect(self.detener_conversacion)

    def _construir_layout(self) -> None:
        panel_config = QGroupBox("Configuración de agentes")
        layout_config = QVBoxLayout(panel_config)
        layout_config.addWidget(self.agent_table)

        panel_controls = QGroupBox("Controles")
        layout_controles = QGridLayout(panel_controls)
        layout_controles.addWidget(QLabel("Tema:"), 0, 0)
        layout_controles.addWidget(self.tema_input, 0, 1)
        layout_controles.addWidget(QLabel("Entrada usuario:"), 1, 0)
        layout_controles.addWidget(self.usuario_input, 1, 1)
        layout_controles.addWidget(QLabel("Modo de conversación:"), 2, 0)
        layout_controles.addWidget(self.modo_selector, 2, 1)
        layout_controles.addWidget(self.start_button, 3, 0)
        layout_controles.addWidget(self.stop_button, 3, 1)

        panel_salida = QGroupBox("Consola de conversación")
        layout_salida = QVBoxLayout(panel_salida)
        layout_salida.addWidget(self.output_text)
        layout_salida.addWidget(self.status_label)

        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)
        layout.addWidget(panel_config)
        layout.addWidget(panel_controls)
        layout.addWidget(panel_salida)

        self.setCentralWidget(contenedor)

    def _cargar_agentes_predeterminados(self) -> None:
        datos = [
            ("IA1", "Optimista", "Colombia", "Fútbol", True, True),
            ("IA2", "Crítico", "Argentina", "Fútbol", True, False),
            ("IA3", "Analítico", "España", "Fútbol", True, True),
        ]

        for fila, fila_data in enumerate(datos):
            for columna, valor in enumerate(fila_data):
                if columna in (4, 5):
                    casilla = QCheckBox()
                    casilla.setChecked(bool(valor))
                    casilla.setStyleSheet("margin-left:25px;")
                    self.agent_table.setCellWidget(fila, columna, casilla)
                else:
                    item = QTableWidgetItem(str(valor))
                    self.agent_table.setItem(fila, columna, item)

    def iniciar_conversacion(self) -> None:
        agentes = self._leer_agentes_desde_tabla()
        tema = self.tema_input.text().strip()
        usuario_texto = self.usuario_input.text().strip()
        modo = self.modo_selector.currentData()

        if not tema:
            self._append_output("⚠️ Debes ingresar un tema para iniciar.")
            return

        if not agentes:
            self._append_output("⚠️ Debes activar al menos un agente.")
            return

        self._set_ui_activa(False)
        self.output_text.clear()
        self._append_output(f"▶️ Iniciando modo: {MODO_LABELS[modo]}")
        self._append_output(f"📌 Tema: {tema}")
        if usuario_texto:
            self._append_output(f"👤 Usuario: {usuario_texto}")

        self.worker = ConversationWorker(agentes, tema, usuario_texto, modo)
        self.worker.mensaje_nuevo.connect(self._append_output)
        self.worker.estado.connect(self._set_estado)
        self.worker.error.connect(self._handle_error)
        self.worker.terminado.connect(self._conversation_ended)
        self.worker.start()

    def detener_conversacion(self) -> None:
        if self.worker is not None:
            self.worker.detener()
            self._append_output("⏹️ Solicitud de detención recibida...")
            self.stop_button.setEnabled(False)

    def _leer_agentes_desde_tabla(self) -> List[Agente]:
        agentes: List[Agente] = []

        for fila in range(self.agent_table.rowCount()):
            nombre_item = self.agent_table.item(fila, 0)
            personalidad_item = self.agent_table.item(fila, 1)
            region_item = self.agent_table.item(fila, 2)
            tema_item = self.agent_table.item(fila, 3)
            participa_widget = self.agent_table.cellWidget(fila, 4)
            responde_widget = self.agent_table.cellWidget(fila, 5)

            if not nombre_item or not nombre_item.text().strip():
                continue

            nombre = nombre_item.text().strip()
            personalidad = personalidad_item.text().strip() if personalidad_item else "Neutral"
            region = region_item.text().strip() if region_item else "Global"
            tema = tema_item.text().strip() if tema_item else self.tema_input.text().strip()
            participa = bool(participa_widget.isChecked()) if participa_widget else True
            responde_usuario = bool(responde_widget.isChecked()) if responde_widget else False

            agente = Agente(
                nombre=nombre,
                personalidad=personalidad,
                region=region,
                tema=tema,
                participa=participa,
                responde_usuario=responde_usuario,
                client=self.client,
            )
            agentes.append(agente)

        return agentes

    def _append_output(self, mensaje: str) -> None:
        self.output_text.append(mensaje)

    def _set_estado(self, texto: str) -> None:
        self.status_label.setText(texto)

    def _handle_error(self, mensaje: str) -> None:
        self._append_output(f"❌ Error: {mensaje}")
        self._set_estado("Error")
        self._conversation_ended()

    def _conversation_ended(self) -> None:
        self._set_estado("Finalizado")
        self._set_ui_activa(True)

    def _set_ui_activa(self, activa: bool) -> None:
        self.start_button.setEnabled(activa)
        self.stop_button.setEnabled(not activa)
        self.agent_table.setEnabled(activa)
        self.tema_input.setEnabled(activa)
        self.usuario_input.setEnabled(activa)
        self.modo_selector.setEnabled(activa)


def ejecutar_aplicacion() -> None:
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
