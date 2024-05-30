pyside6-uic mainwindow.ui -o ui_mainwindow.py
pyside6-uic protocolAnalyzerUI.ui -o ui_protocolAnalyzerUI.py
pyside6-rcc Icons.qrc -o Icons_rc.py
python main.py