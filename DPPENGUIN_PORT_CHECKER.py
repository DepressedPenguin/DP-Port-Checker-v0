#!/usr/bin/python3
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QTextEdit, QWidget,QPushButton
from PyQt6.QtGui import QIcon
from scapy.all import *
from PyQt6.QtMultimedia import QSoundEffect

def Main_Checker():
	global input_ip,textarea_output
	app = QApplication(sys.argv)
	w = QWidget()
	w.setGeometry(100,120,285,245)
	w.setFixedSize(285,245)
	w.setWindowTitle("DP PORT CHECKER V0")
	w.setWindowIcon(QIcon("icon"))
	#STYLE_THE _WINDOW
	w.setStyleSheet("""
		background-color:#373D3D;
		""")
	title_app = QLabel(w)
	title_app.setText("PORT CHECK V0 BY PENGUIN")
	#STYLE_THE TITLE
	title_app.setStyleSheet("""
		color:white;
		font-size:16px;
		border-bottom:1px solid white;
		""")
	title_app.move(40,5)
	title_app.show()
	# LINE TO SPLIT THE TITLE
	split = QLabel(w)
	split.setGeometry(0,35,400,2)
	split.setStyleSheet("background-color:white;")
	split.show()
	w.show()

	#MAKE_PLACE_FOR_INPUT_IP
	text_input_ip = QLabel(w)
	text_input_ip.setText("IP :")
	text_input_ip.setStyleSheet("""
		color:gold;
		font-size:20px;
		""")
	text_input_ip.move(25,50)
	text_input_ip.show()

	#MAKE_INPUT_FOR_THE_IP
	input_ip = QLineEdit(w)
	input_ip.setGeometry(70,45,170,40)
	input_ip.setStyleSheet("""
		border:1px solid grey;
		border-radius:5px;
		font-size:19px;
		color:white;
		padding:5px;
		""")
	input_ip.setPlaceholderText("EX : 12.212.312.31")
	# input_ip.move(100,100)
	input_ip.show()
	#MAKE_BTN_TO_CHECK

	# TEST FUNCTION
	def show_data():
		global textarea_output, input_ip
		ur_ip = input_ip.text()
		textarea_output.setPlainText("")

		dport_list = [80, 22, 434, 90, 21, 55, 645, 64, 443, 25, 143, 110, 3389, 1521, 3306, 5432, 8080, 5900, 161, 162, 69, 123, 137, 138, 139, 445, 514, 636, 989, 990, 1433, 389, 636, 873, 1194, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 10000, 5000, 7001, 8000, 8081, 8443]
		Packet_For_Ports = sr(IP(dst=ur_ip,ttl=20)/TCP(dport=dport_list), retry=1,timeout=1)

		data_retrieved = []

		if Packet_For_Ports:
			ans,unans = Packet_For_Ports

			for packet in ans:
				data_retrieved.append(packet[1].summary())

			print("Data Retrieved:")
			for summary in data_retrieved:
				# print(summary)
				if "SA" and "http" in summary:
					# textarea_output.setPlainText(textarea_output.toPlainText() )
					# print("PORT 80 : OPEN")
					textarea_output.setPlainText(textarea_output.toPlainText() + "PORT 80 : OPEN\n")
				elif "SA" and "8080" in summary:
					# print("8080:HTTP : OPEN:")
					textarea_output.setPlainText(textarea_output.toPlainText() + "8080:HTTP : OPEN:\n")
				elif "SA" and "https" in summary:
					# print("443:HTTPS: OPEN ")
					textarea_output.setPlainText(textarea_output.toPlainText() + "443:HTTPS: OPEN\n")
				elif "SA" and "8443" in summary:
					# print("ALR:HTTPS:8443: OPEN")
					textarea_output.setPlainText(textarea_output.toPlainText() + "ALR:HTTPS:8443: OPEN\n")
				elif "SA" and "3306" in summary:
					# print("MYSQL_DATA:3306 : OPEN")
					textarea_output.setPlainText(textarea_output.toPlainText() + "MYSQL_DATA:3306 : OPEN\n")
				else:
					print("CLOSED!")
				# print(summary)
		else:
			print("Nothing")

	#Title_port
	# title_port = QLabel(w)
	# title_port.setText("PORTS :")
	# #Style_This_Title
	# title_port.setStyleSheet("""
	# 	color:gold;
	# 	font-size:18px;
	# 	""")
	# title_port.move(15,102)
	# title_port.show()

	# #SECTION_FOR_PORTS
	# port1 = QLineEdit(w)
	# port1.setGeometry(90,100,60,30)
	# port1.setStyleSheet("""
	# 	border:1px solid grey;
	# 	border-radius:5px;
	# 	color:white;
	# 	font-size:18px;
	# 	""")
	# port1.show()

	# #Port2_Section
	# port2 = QLineEdit(w)
	# port2.setGeometry(165,100,60,30)
	# port2.setStyleSheet("""
	# 	border:1px solid grey;
	# 	border-radius:5px;
	# 	color:white;
	# 	font-size:18px;
	# 	""")
	# port2.show()

	# #port3_Section

	# port3 = QLineEdit(w)
	# port3.setGeometry(240,100,60,30)
	# port3.setStyleSheet("""
	# 	border:1px solid grey;
	# 	border-radius:5px;
	# 	color:white;
	# 	font-size:18px;
	# 	""")
	# port3.show()

	# #port4_Section
	# port4 = QLineEdit(w)
	# port4.setGeometry(315,100,60,30)
	# port4.setStyleSheet("""
	# 	border:1px solid grey;
	# 	border-radius:5px;
	# 	color:white;
	# 	font-size:18px;
	# 	""")
	# port4.show()

	btn = QPushButton(w)
	btn.setText("CHECK")
	#SET_THE_SIZE_OF_THE_WINDOW
	btn.setGeometry(100,100,100,30)
	btn.setStyleSheet("""
		background-color:white;
		border:1px solid grey;
		border-radius:5px;
		font-family:courier;
		letter-spacing:3px;
		""")
	btn.show()

	#MAKE_TEXTAREA_FOR_THE_OUPUT

	textarea_output = QTextEdit(w)
	#SET_TEXT_AREA
	textarea_output.setGeometry(10,140,265,95)

	textarea_output.setStyleSheet("""
		border:1px solid white;
		border-radius:5px;
		color:white;
		font-size:20px;
		""")
	textarea_output.show()

	btn.clicked.connect(show_data)

	sys.exit(app.exec())

Main_Checker()