import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QHBoxLayout,
                             QGridLayout, QVBoxLayout, QWidget, QLabel, QPushButton, QScrollArea, QGroupBox)
import pymysql

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Airplane Tracking System")
        self.setGeometry(0,0, 500, 500)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.setCentralWidget(central_widget)

        self.button1 = QPushButton('Add Airplane', self)
        self.button2 = QPushButton('Add Airport', self)
        self.button3 = QPushButton('Add Person', self)
        self.button4 = QPushButton('Grant or Revoke Pilot License', self)
        self.button5 = QPushButton('Offer Flight', self)
        self.button6 = QPushButton('Flight Landing', self)
        self.button7 = QPushButton('Flight Takeoff', self)
        self.button8 = QPushButton('Passengers Board', self)
        self.button9 = QPushButton('Passengers Disembark', self)
        self.button10 = QPushButton('Assign Pilot', self)
        self.button11 = QPushButton('Recycle Crew', self)
        self.button12 = QPushButton('Retire Flight', self)
        self.button13 = QPushButton('Simulation Cycle', self)
        self.button14 = QPushButton("Flights in the Air", self)
        self.button15 = QPushButton('Flights on the Ground', self)
        self.button16 = QPushButton('People in the Air', self)
        self.button17 = QPushButton('People on the Ground', self)
        self.button18 = QPushButton('Route Summary', self)
        self.button19 = QPushButton('Alternative Airports', self)
        self.button20 = QPushButton("View Tables", self)
        
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        layout.addWidget(self.button11)
        layout.addWidget(self.button12)
        layout.addWidget(self.button13)
        layout.addWidget(self.button14)
        layout.addWidget(self.button15)
        layout.addWidget(self.button16)
        layout.addWidget(self.button17)
        layout.addWidget(self.button18)
        layout.addWidget(self.button19)
        layout.addWidget(self.button20)

        self.button1.clicked.connect(self.add_airplane_window)
        self.button2.clicked.connect(self.add_airport_window)
        self.button3.clicked.connect(self.add_person_window)
        self.button4.clicked.connect(self.grant_revoke_window)
        self.button5.clicked.connect(self.offer_flight_window)
        self.button6.clicked.connect(self.flight_landing_window)
        self.button7.clicked.connect(self.flight_takeoff_window)
        self.button8.clicked.connect(self.passengers_board_window)
        self.button9.clicked.connect(self.passengers_disembark_window)
        self.button10.clicked.connect(self.assign_pilot_window)
        self.button11.clicked.connect(self.recycle_crew_window)
        self.button12.clicked.connect(self.retire_flight_window)
        self.button13.clicked.connect(self.simulation_cycle_window)
        self.button14.clicked.connect(self.planes_in_air_window)
        self.button15.clicked.connect(self.planes_on_ground_window)
        self.button16.clicked.connect(self.people_in_air_window)
        self.button17.clicked.connect(self.people_on_ground_window)
        self.button18.clicked.connect(self.route_summary_window)
        self.button19.clicked.connect(self.alternative_airports_window)
        self.button20.clicked.connect(self.view_tables_window)

        
        central_widget.setLayout(layout)


    def add_airplane_window(self):
        self.hide()
        self.pro1_window = add_airplane_window(self)
        self.pro1_window.show()

    def add_airport_window(self):
        self.hide()
        self.pro2_window = add_airport_window(self)
        self.pro2_window.show()

    def add_person_window(self):
        self.hide()
        self.pro3_window = add_person_window(self)
        self.pro3_window.show()

    def grant_revoke_window(self):
        self.hide()
        self.pro4_window = grant_revoke_window(self)
        self.pro4_window.show()

    def offer_flight_window(self):
        self.hide()
        self.pro5_window = offer_flight_window(self)
        self.pro5_window.show()

    def flight_landing_window(self):
        self.hide()
        self.pro6_window = flight_landing_window(self)
        self.pro6_window.show()

    def flight_takeoff_window(self):
        self.hide()
        self.pro7_window = flight_takeoff_window(self)
        self.pro7_window.show()

    def passengers_board_window(self):
        self.hide()
        self.pro8_window = passengers_board_window(self)
        self.pro8_window.show()

    def passengers_disembark_window(self):
        self.hide()
        self.pro9_window = passengers_disembark_window(self)
        self.pro9_window.show()

    def assign_pilot_window(self):
        self.hide()
        self.pro10_window = assign_pilot_window(self)
        self.pro10_window.show()

    def recycle_crew_window(self):
        self.hide()
        self.pro11_window = recycle_crew_window(self)
        self.pro11_window.show()

    def retire_flight_window(self):
        self.hide()
        self.pro12_window = retire_flight_window(self)
        self.pro12_window.show()

    def simulation_cycle_window(self):
        self.hide()
        self.pro13_window = simulation_cycle_window(self)
        self.pro13_window.show()

    def planes_in_air_window(self):
        self.hide()
        view  = "SELECT * from flights_in_the_air"
        data, headers = db.get_view(view)
        self.flights_in_the_air_window = flights_in_air_window(data, headers, self)
        self.flights_in_the_air_window.show()

    def planes_on_ground_window(self):
        self.hide()
        view  = "SELECT * from flights_on_the_ground"
        data, headers = db.get_view(view)
        self.flights_on_the_ground_window = flights_on_ground_window(data, headers, self)
        self.flights_on_the_ground_window.show()

    def people_in_air_window(self):
        self.hide()
        view  = "SELECT * from people_in_the_air"
        data, headers = db.get_view(view)
        self.people_in_the_air_window = people_in_the_air_window(data, headers, self)
        self.people_in_the_air_window.show()

    def people_on_ground_window(self):
        self.hide()
        view  = "SELECT * from people_on_the_ground"
        data, headers = db.get_view(view)
        self.people_on_the_ground_window = people_on_the_ground_window(data, headers, self)
        self.people_on_the_ground_window.show()

    def route_summary_window(self):
        self.hide()
        view  = "SELECT * from route_summary"
        data, headers = db.get_view(view)
        self.route_summary_window = route_summary_window(data, headers, self)
        self.route_summary_window.show()

    def alternative_airports_window(self):
        self.hide()
        view  = "SELECT * from alternative_airports"
        data, headers = db.get_view(view)
        self.alternative_airports_window = alternative_airports_window(data, headers, self)
        self.alternative_airports_window.show()

    def view_tables_window(self):
        self.hide()
        self.view_tables_window = view_tables_window(self)
        self.view_tables_window.show()

class add_airplane_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Add Airplane")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.airlineID = QLineEdit()
        self.airlineID.setPlaceholderText("AirlineID")
        self.tail_num = QLineEdit()
        self.tail_num.setPlaceholderText('Tail Number')
        self.seat_cap = QLineEdit()
        self.seat_cap.setPlaceholderText('Seat Capacity')
        self.speed = QLineEdit()
        self.speed.setPlaceholderText('Speed')
        self.locationID = QLineEdit()
        self.locationID.setPlaceholderText('Location ID')
        self.plane_type = QLineEdit()
        self.plane_type.setPlaceholderText('Plane Type')
        self.maintenanced = QLineEdit()
        self.maintenanced.setPlaceholderText('Maintenanced')
        self.model = QLineEdit()
        self.model.setPlaceholderText('Model')
        self.neo = QLineEdit()
        self.neo.setPlaceholderText('Neo-Variant')

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.airlineID)
        self.layout1.addWidget(self.tail_num)
        self.layout1.addWidget(self.seat_cap)
        self.layout1.addWidget(self.speed)
        self.layout1.addWidget(self.locationID)
        self.layout2.addWidget(self.plane_type)
        self.layout2.addWidget(self.maintenanced)
        self.layout2.addWidget(self.model)
        self.layout2.addWidget(self.neo)
        self.layout3.addWidget(self.message)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "airlineID": self.airlineID.text(),
        "tail_num": self.tail_num.text(),
        "seat_cap": self.seat_cap.text(),
        "speed": self.speed.text(),
        "locationID": self.locationID.text(),
        "plane_type": self.plane_type.text(),
        "maintenanced": self.maintenanced.text(),
        "model": self.model.text(),
        "neo": self.neo.text()
        }
        if data['airlineID'] == '':
            self.message.setText('AirlineID cannot be empty')
            return
        elif data['tail_num'] == '':
            self.message.setText('Tail Number cannot be empty')
            return
        elif data['seat_cap'] == '':
            self.message.setText('Seat Capacity cannot be empty')
            return
        elif int(data['seat_cap']) <= 0:
            self.message.setText('Seat Capacity has to be greater than 0')
            return
        elif data['speed'] == '':
            self.message.setText('Speed cannot be empty')
            return
        elif int(data['speed']) <= 0:
            self.message.setText('Speed has to be greater than 0')
            return
        elif data['plane_type'] == 'Boeing':
            if data['neo'] != '':
                    self.message.setText('Boeing planes must have no value for neo-variant')
                    return
            elif data['maintenanced'] != "True" and data['maintenanced'] != 'False':
                    self.message.setText('Boeing planes must have a True or Talse value for maintenanced')
                    return
            elif data['model'] == '':
                    self.message.setText('Boeing planes must have a value for model')
                    return
        elif data['plane_type'] == 'Airbus':
            if data['neo'] != "True" and data['neo'] != 'False':
                    self.message.setText('Airbus planes must have a True or False value for Neo-Variant')
                    return
            elif data['maintenanced'] != '':
                    self.message.setText('Airbus planes must have no value for maintenanced')
                    return
            elif data['model'] != '':
                    self.message.setText('Airbus planes must have no value for model')
                    return
            
        airlines = db.get_foreign_key('select airlineID from airplane')
        if data['airlineID'] not in airlines:
            self.message.setText('Airline must be already in existence.')
            return
        
        airplanes = db.get_foreign_key('select airlineID, tail_num from airplane')
        if (data['airlineID'], data['tail_num']) in airplanes:
            self.message.setText('Airplane cannot already be existing')
            return

        locations = db.get_foreign_key('select locationID from airplane')
        if data['locationID'] in locations:
            self.message.setText('Location cannot already be existing')
            return
        
        for key in data:
            val = data[key]
            if val == '':
                data[key] = None
            elif val == 'True':
               data[key] = True
            elif val == 'False':
                data[key] = False
            else:
                if key == 'model':
                    pass
                try:
                    data[key] = int(val)
                except (ValueError, TypeError):
                    pass 
        
        values = (
            data["airlineID"], data["tail_num"], data["seat_cap"], data["speed"],
            data["locationID"], data["plane_type"], data["maintenanced"],
            data["model"], data["neo"]
        )

        db.add_airplane(values)
        self.airlineID.clear()
        self.tail_num.clear()
        self.seat_cap.clear()
        self.speed.clear()
        self.locationID.clear()
        self.plane_type.clear()
        self.maintenanced.clear()
        self.model.clear()
        self.neo.clear()
        self.message.setText('Submited to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class add_airport_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Add Airport")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.airportID = QLineEdit()
        self.airportID.setPlaceholderText("AirportID")
        self.airport_name = QLineEdit()
        self.airport_name.setPlaceholderText('Airport Name')
        self.city = QLineEdit()
        self.city.setPlaceholderText('City')
        self.state = QLineEdit()
        self.state.setPlaceholderText('State')
        self.country = QLineEdit()
        self.country.setPlaceholderText('Country')
        self.locationID = QLineEdit()
        self.locationID.setPlaceholderText('Location ID')

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.airportID)
        self.layout1.addWidget(self.airport_name)
        self.layout1.addWidget(self.city)
        self.layout1.addWidget(self.state)
        self.layout1.addWidget(self.country)
        self.layout2.addWidget(self.locationID)
        self.layout3.addWidget(self.message)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "airportID": self.airportID.text(),
        "airport_name": self.airport_name.text(),
        "city": self.city.text(),
        "state": self.state.text(),
        "country": self.country.text(),
        "locationID": self.locationID.text(),
        }
        if data['airportID'] == '':
            self.message.setText('AirportID cannot be empty')
            return
        elif data['city'] == '':
            self.message.setText('City cannot be empty')
            return
        elif data['state'] == '':
            self.message.setText('State cannot be empty')
            return
        elif data['country'] == '':
            self.message.setText('Country cannot be empty')

        

        locations = db.get_foreign_key('select locationID from airport')
        if data['locationID'] in locations:
            self.message.setText('Location cannot already be existing')
            return
        
        airportIDs = db.get_foreign_key('select airportID from airport')
        if data['airportID'] in airportIDs:
            self.message.setText('AirportID cannot already be existing')
            return

        values = (
            data["airportID"], data["airport_name"], data["city"], data["state"],
            data["country"], data["locationID"]
        )

        db.add_airport(values)
        self.airportID.clear()
        self.airport_name.clear()
        self.city.clear()
        self.state.clear()
        self.country.clear()
        self.locationID.clear()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class add_person_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Add Person")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.personID = QLineEdit()
        self.personID.setPlaceholderText("PersonID")
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText('First Name')
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText('Last Name')
        self.locationID = QLineEdit()
        self.locationID.setPlaceholderText('Location ID')
        self.taxID = QLineEdit()
        self.taxID.setPlaceholderText('Tax ID')
        self.experience = QLineEdit()
        self.experience.setPlaceholderText('Experience')
        self.miles = QLineEdit()
        self.miles.setPlaceholderText('Miles')
        self.funds = QLineEdit()
        self.funds.setPlaceholderText('Funds')

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.personID)
        self.layout1.addWidget(self.first_name)
        self.layout1.addWidget(self.last_name)
        self.layout1.addWidget(self.locationID)
        self.layout2.addWidget(self.taxID)
        self.layout2.addWidget(self.experience)
        self.layout2.addWidget(self.miles)
        self.layout2.addWidget(self.funds)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)
        self.layout3.addWidget(self.message)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "personID": self.personID.text(),
        "first_name": self.first_name.text(),
        "last_name": self.last_name.text(),
        "locationID": self.locationID.text(),
        "taxID": self.taxID.text(),
        "experience": self.experience.text(),
        "miles": self.miles.text(),
        "funds": self.funds.text()
        }
        if data['personID'] == '':
            self.message.setText('PersonID cannot be empty')
            return
        elif data['first_name'] == '':
            self.message.setText('First Name cannot be empty')
            return
        elif data['locationID'] == '':
            self.message.setText('LocationID cannot be empty')
            return
        
        if (data['taxID'] != '' and data['experience'] != '') and (data['miles'] != '' and data['funds'] != ''):
            self.message.setText('A person can only have either taxID and experience OR miles and funds, not both')
            return
        elif (data['taxID'] == '' and data['experience'] == '') and (data['miles'] == '' and data['funds'] == ''):
            self.message.setText('You must provide either taxID and experience OR miles and funds')
            return

        locations = db.get_foreign_key('select locationID from person')
        if data['locationID'] not in locations:
            self.message.setText('Location must be already existing')
            return
        
        personIDs = db.get_foreign_key('select personID from person')
        if data['personID'] in personIDs:
            self.message.setText('PersonID cannot already be existing')
            return
        
        for key in data:
            val = data[key]
            if val == '':
                data[key] = None
            else:
                try:
                    data[key] = int(val)
                except (ValueError, TypeError):
                    if key in ['experience', 'miles', 'funds'] and val is not None:
                        self.message.setText(f'{key.capitalize()} must be an integer')
                        return

        values = (
            data["personID"], data["first_name"], data["last_name"], data["locationID"],
            data["taxID"], data["experience"], data['miles'], data['funds']
        )

        db.add_person(values)
        self.personID.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.locationID.clear()
        self.taxID.clear()
        self.experience.clear()
        self.miles.clear()
        self.funds.clear()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class grant_revoke_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Grant or Revoke License")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.personID = QLineEdit()
        self.personID.setPlaceholderText("PersonID")
        self.license = QLineEdit()
        self.license.setPlaceholderText('License')

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.personID)
        self.layout2.addWidget(self.license)
        self.layout3.addWidget(self.message)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "personID": self.personID.text(),
        "license": self.license.text(),
        }
        if data['personID'] == '':
            self.message.setText('PersonID cannot be empty')
            return
        elif data['license'] == '':
            self.message.setText('License cannot be empty')
            return

        pilots = db.get_foreign_key('select personID from pilot')
        if data['personID'] not in pilots:
            self.message.setText('Person must be a pilot')
            return

        values = (
            data["personID"], data["license"]
        )

        db.grant_or_revoke_pilot_license(values)
        self.personID.clear()
        self.license.clear()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class offer_flight_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Offer Flight")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")
        self.routeID = QLineEdit()
        self.routeID.setPlaceholderText('RouteID')
        self.support_airline = QLineEdit()
        self.support_airline.setPlaceholderText('Support Airline')
        self.support_tail = QLineEdit()
        self.support_tail.setPlaceholderText('Support Tail')
        self.progress = QLineEdit()
        self.progress.setPlaceholderText('Progress')
        self.next_time = QLineEdit()
        self.next_time.setPlaceholderText('Next Time (00:00:00)')
        self.cost = QLineEdit()
        self.cost.setPlaceholderText('Cost')

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.flightID)
        self.layout1.addWidget(self.routeID)
        self.layout1.addWidget(self.support_airline)
        self.layout1.addWidget(self.support_tail)
        self.layout2.addWidget(self.progress)
        self.layout2.addWidget(self.next_time)
        self.layout2.addWidget(self.cost)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)
        self.layout3.addWidget(self.message)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "flightID": self.flightID.text(),
        "routeID": self.routeID.text(),
        "support_airline": self.support_airline.text(),
        "support_tail": self.support_tail.text(),
        "progress": self.progress.text(),
        "next_time": self.next_time.text(),
        "cost": self.cost.text()
        }
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        elif data['routeID'] == '':
            self.message.setText('RouteID cannot be empty')
            return
        
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] in flights:
            self.message.setText('Flight already exists')
            return

        airplanes = db.get_foreign_key('select airlineID, tail_num from airplane')
        if (data['support_airline'], data['support_tail']) not in airplanes:
            self.message.setText('Airplane must already be existing')
            return
        
        routes = db.get_foreign_key('select routeID from route')
        if data['routeID'] not in routes:
            self.message.setText('Route must already be existing')
            return

        airplane_flights = db.get_foreign_key('select support_airline, support_tail from flight')
        if (data['support_airline'], data['support_tail']) in airplane_flights:
            self.message.setText('Airplane is already in flight')
            return

        for key in data:
            val = data[key]
            if val == '':
                data[key] = None
            else:
                try:
                    data[key] = int(val)
                except (ValueError, TypeError):
                    if key in ['progress', 'cost'] and val is not None:
                        self.message.setText(f'{key.capitalize()} must be an integer')
                        return

        query = f"select count(*) from route_path where routeID = '{data['routeID']}'"
        num_stops = db.get_foreign_key(query)
        if data['progress'] > num_stops[0]:
            self.message.setText(f'Progress must be less than the number of stops on this route: {num_stops}')
            return
        
        query = f"select sequence from route_path where routeID = '{data['routeID']}' order by sequence desc limit 1"
        max_progress = db.get_foreign_key(query)
        if data['progress'] == max_progress[0]:
            self.message.setText(f'Flight cannot be at the last stop of the route')
            return
        
        values = (
            data["flightID"], data["routeID"], data["support_airline"], data["support_tail"],
            data["progress"], data['next_time'], data['cost']
        )

        db.offer_flight(values)
        self.flightID.clear()
        self.routeID.clear()
        self.support_airline.clear()
        self.support_tail.clear()
        self.progress.clear()
        self.next_time.clear()
        self.cost.clear()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class flight_landing_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Flight Landing")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout = QVBoxLayout()

        submit_button = QPushButton("Submit", self)
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        submit_button.clicked.connect(self.submit)


        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")
        self.layout1.addWidget(self.flightID)
        self.message = QLabel('')
        self.layout3.addWidget(self.message)
        self.layout2.addWidget(back_button)
        self.layout2.addWidget(submit_button)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)


        self.setLayout(self.layout)
    def go_back(self):
        self.close()
        self.main_window.show()

    def submit(self):
        data = {"flightID": self.flightID.text()}
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('FlightID does not exist')
            return
        query = f"select flightID from flight where airplane_status = 'on_ground'"
        flightsOnGround =db.get_foreign_key(query)
        #print(flightsOnGround)
        if data['flightID'] in flightsOnGround:
            self.message.setText('Flight is on ground therefore it cannot ground')
            return
        values = (data["flightID"])
        db.flight_landing(values)
        self.flightID.clear()

        self.message.setText('Submitted to SQL.')

class flight_takeoff_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Flight Takeoff")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout = QVBoxLayout()

        submit_button = QPushButton("Submit", self)
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        submit_button.clicked.connect(self.submit)


        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")
        self.layout1.addWidget(self.flightID)
        self.message = QLabel('')
        self.layout3.addWidget(self.message)
        self.layout2.addWidget(back_button)
        self.layout2.addWidget(submit_button)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)


        self.setLayout(self.layout)

    def go_back(self):
        self.close()
        self.main_window.show()

    def submit(self):
        data = {"flightID": self.flightID.text()}
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('FlightID does not exist')
            return
        query = f"select flightID from flight where airplane_status = 'on_ground'"
        flightsOnGround =db.get_foreign_key(query)
        #print(flightsOnGround)
        if data['flightID'] not in flightsOnGround:
            self.message.setText('Flight is in air and cannot takeoff')
            return

        values = (data["flightID"])
        db.flight_takeoff(values)
        self.flightID.clear()

        self.message.setText('Submitted to SQL.')

class passengers_board_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Passengers Board")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout = QVBoxLayout()

        submit_button = QPushButton("Submit", self)
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        submit_button.clicked.connect(self.submit)


        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")
        self.layout1.addWidget(self.flightID)
        self.message = QLabel('')
        self.layout3.addWidget(self.message)
        self.layout2.addWidget(back_button)
        self.layout2.addWidget(submit_button)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)


        self.setLayout(self.layout)
    def go_back(self):
        self.close()
        self.main_window.show()

    def submit(self):
        data = {"flightID": self.flightID.text()}
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('FlightID does not exist')
            return
        values = (data["flightID"])
        query = f"select flightID from flight where airplane_status = 'on_ground'"
        flightsOnGround =db.get_foreign_key(query)
        #print(flightsOnGround)
        if data['flightID'] not in flightsOnGround:
            self.message.setText('Flight is in air you can not board')
            return
        db.passengers_board(values)
        self.flightID.clear()

        self.message.setText('Submitted to SQL.')

class passengers_disembark_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Passengers Disembark")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout = QVBoxLayout()

        submit_button = QPushButton("Submit", self)
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        submit_button.clicked.connect(self.submit)


        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")
        self.layout1.addWidget(self.flightID)
        self.message = QLabel('')
        self.layout3.addWidget(self.message)
        self.layout2.addWidget(back_button)
        self.layout2.addWidget(submit_button)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)


        self.setLayout(self.layout)

    def go_back(self):
        self.close()
        self.main_window.show()

    def submit(self):
        data = {"flightID": self.flightID.text()}
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('FlightID does not exist')
            return
        query = f"select flightID from flight where airplane_status = 'on_ground'"
        flightsOnGround =db.get_foreign_key(query)
        #print(flightsOnGround)
        if data['flightID'] not in flightsOnGround:
            self.message.setText('Flight is in air and you can not board')
            return
        values = (data["flightID"])
        db.passengers_disembark(values)
        self.flightID.clear()

        self.message.setText('Submitted to SQL.')

class assign_pilot_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Assign Pilot")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout = QVBoxLayout()

        submit_button = QPushButton("Submit", self)
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        submit_button.clicked.connect(self.submit)


        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")
        self.personID = QLineEdit()
        self.personID.setPlaceholderText("PersonID")
        self.layout1.addWidget(self.flightID)
        self.layout1.addWidget(self.personID)
        self.message = QLabel('')
        self.layout3.addWidget(self.message)
        self.layout2.addWidget(back_button)
        self.layout2.addWidget(submit_button)
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)


        self.setLayout(self.layout)

    def go_back(self):
        self.close()
        self.main_window.show()

    def submit(self):
        data = {"flightID": self.flightID.text(), "personID":self.personID.text()}
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('FlightID does not exist')
            return
        if data['personID'] == '':
            self.message.setText('PersonID cannot be empty')
        pilotrecord = db.get_foreign_key('select personID from pilot')
        #personrecord = db.get_foreign_key('select personID from person')
        if data['personID'] not in pilotrecord:
            self.message.setText('Pilot PersonID does not exist')
            return
        # if data['personID'] not in personrecord:
        #     self.message.setText('Person does not exist')

        values = (data["flightID"], data["personID"])
        db.assign_pilot(values)
        self.flightID.clear()
        self.personID.clear()

        self.message.setText('Submitted to SQL.')

class recycle_crew_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Recycle crew")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.flightID)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)
        self.layout3.addWidget(self.message)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "flightID": self.flightID.text()
        }
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('Flight does not exist')
            return
        
        grounded = db.get_foreign_key('select flight_list from flights_on_the_ground')
        if data['flightID'] not in grounded:
            self.message.setText('Flight not grounded')
            return
        
        queryMax = f"select count(*) from route_path where routeID = (select routeID from flight where flightID ='{data['flightID']}');"
        queryCurr = f"select progress from flight where flightID ='{data['flightID']}';"
        
        if db.get_foreign_key(queryMax) > db.get_foreign_key(queryCurr):
            self.message.setText('Flight has more legs')
            return
        
        for key in data:
            val = data[key]
            if val == '':
                data[key] = None
            else:
                try:
                    data[key] = int(val)
                except (ValueError, TypeError):
                    if key in ['progress', 'cost'] and val is not None:
                        self.message.setText(f'{key.capitalize()} must be an integer')
                        return
        
        values = (data["flightID"],)

        db.recycle_crew(values)
        self.flightID.clear()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class retire_flight_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Offer Flight")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.flightID = QLineEdit()
        self.flightID.setPlaceholderText("FlightID")

        self.message = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout1.addWidget(self.flightID)
        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)
        self.layout3.addWidget(self.message)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        data = {
        "flightID": self.flightID.text()
        }
        if data['flightID'] == '':
            self.message.setText('FlightID cannot be empty')
            return
        
        flights = db.get_foreign_key('select flightID from flight')
        if data['flightID'] not in flights:
            self.message.setText('Flight does not exist')
            return
        
        grounded = db.get_foreign_key('select flight_list from flights_on_the_ground')
        if data['flightID'] not in grounded:
            self.message.setText('Flight not grounded')
            return

        for key in data:
            val = data[key]
            if val == '':
                data[key] = None
            else:
                try:
                    data[key] = int(val)
                except (ValueError, TypeError):
                    if key in ['progress', 'cost'] and val is not None:
                        self.message.setText(f'{key.capitalize()} must be an integer')
                        return
        
        values = (
            data["flightID"]
        )

        db.retire_flight(values)
        self.flightID.clear()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class simulation_cycle_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Simulation Cycle")
        self.add_airplane_widget = QWidget()
        self.add_airplane_widget.setGeometry(0,0, 500, 500)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.message = QLabel('')
        self.submit_button = QPushButton('Cycle')
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)
        self.submit_button.clicked.connect(self.submit)

        self.layout4.addWidget(self.submit_button)
        self.layout4.addWidget(self.back_button)
        self.layout3.addWidget(self.message)
        
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout4)
        self.setLayout(self.layout)

    def submit(self):
        db.simulation_cycle()
        self.message.setText('Submitted to SQL.')

    def go_back(self): 
        self.close()
        self.main_window.show()

class flights_in_air_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from flights_in_the_air")
        self.setWindowTitle("Flights in the Air")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()
        
class flights_on_ground_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from flights_on_the_ground")
        self.setWindowTitle("Flights on the Ground")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class people_in_the_air_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from people_in_the_air")
        self.setWindowTitle("People in the Air")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class people_on_the_ground_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from people_on_the_ground")
        self.setWindowTitle("People on the Ground")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
    
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class route_summary_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from route_summary")
        self.setWindowTitle("Route Summary")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class alternative_airports_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from alternative_airports")
        self.setWindowTitle("Alternative Airports")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class view_tables_window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("View Tables")
        
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_widget.setGeometry(500,500,1000,1000)
        self.content_layout.setSpacing(30)
        
        button1 = QPushButton('Airline', self)
        button2 = QPushButton('Airplane', self)
        button3 = QPushButton('Airport', self)
        button4 = QPushButton('Flight', self)
        button5 = QPushButton('Leg', self)
        button6 = QPushButton('Location', self)
        button7 = QPushButton('Passenger', self)
        button8 = QPushButton('Passenger Vacations', self)
        button9 = QPushButton('Person', self)
        button10 = QPushButton('Pilot', self)
        button11 = QPushButton('Pilot Licenses', self)
        button12 = QPushButton('Route', self)
        button13 = QPushButton('Route Path', self)

        back_button = QPushButton("Back",self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(button8)
        layout.addWidget(button9)
        layout.addWidget(button10)
        layout.addWidget(button11)
        layout.addWidget(button12)
        layout.addWidget(button13)
        layout.addWidget(back_button)

        button1.clicked.connect(self.airline_window)
        button2.clicked.connect(self.airplane_window)
        button3.clicked.connect(self.airport_window)
        button4.clicked.connect(self.flight_window)
        button5.clicked.connect(self.leg_window)
        button6.clicked.connect(self.location_window)
        button7.clicked.connect(self.passenger_window)
        button8.clicked.connect(self.passenger_vacations_window)
        button9.clicked.connect(self.person_window)
        button10.clicked.connect(self.pilot_window)
        button11.clicked.connect(self.pilot_licenses_window)
        button12.clicked.connect(self.route_window)
        button13.clicked.connect(self.route_path_window)

        self.setLayout(layout)
        
    def go_back(self):
        self.close()
        self.main_window.show()

    def airline_window(self):
        self.hide()
        view  = "SELECT * from airline"
        data, headers = db.get_view(view)
        self.airline_window = airline_window(data, headers, self)
        self.airline_window.show()

    def airplane_window(self):
        self.hide()
        view  = "SELECT * from airplane"
        data, headers = db.get_view(view)
        self.airplane_window = airplane_window(data, headers, self)
        self.airplane_window.show()

    def airport_window(self):
        self.hide()
        view  = "SELECT * from airport"
        data, headers = db.get_view(view)
        self.airport_window = airport_window(data, headers, self)
        self.airport_window.show()

    def flight_window(self):
        self.hide()
        view  = "SELECT * from flight"
        data, headers = db.get_view(view)
        self.flight_window = flight_window(data, headers, self)
        self.flight_window.show()

    def leg_window(self):
        self.hide()
        view  = "SELECT * from leg"
        data, headers = db.get_view(view)
        self.leg_window = leg_window(data, headers, self)
        self.leg_window.show()

    def location_window(self):
        self.hide()
        view  = "SELECT * from location"
        data, headers = db.get_view(view)
        self.location_window = location_window(data, headers, self)
        self.location_window.show()

    def passenger_window(self):
        self.hide()
        view  = "SELECT * from passenger"
        data, headers = db.get_view(view)
        self.passenger_window = passenger_window(data, headers, self)
        self.passenger_window.show()

    def passenger_vacations_window(self):
        self.hide()
        view  = "SELECT * from passenger_vacations"
        data, headers = db.get_view(view)
        self.passenger_vacations_window = passenger_vacations_window(data, headers, self)
        self.passenger_vacations_window.show()

    def person_window(self):
        self.hide()
        view  = "SELECT * from person"
        data, headers = db.get_view(view)
        self.person_window = person_window(data, headers, self)
        self.person_window.show()

    def pilot_window(self):
        self.hide()
        view  = "SELECT * from pilot"
        data, headers = db.get_view(view)
        self.pilot_window = pilot_window(data, headers, self)
        self.pilot_window.show()

    def pilot_licenses_window(self):
        self.hide()
        view  = "SELECT * from pilot_licenses"
        data, headers = db.get_view(view)
        self.pilot_licenses_window = pilot_licenses_window(data, headers, self)
        self.pilot_licenses_window.show()

    def route_window(self):
        self.hide()
        view  = "SELECT * from route"
        data, headers = db.get_view(view)
        self.route_window = route_window(data, headers, self)
        self.route_window.show()

    def route_path_window(self):
        self.hide()
        view  = "SELECT * from route_path order by routeID, sequence"
        data, headers = db.get_view(view)
        self.route_path_window = route_path_window(data, headers, self)
        self.route_path_window.show()

class airline_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from airline")
        self.setWindowTitle("Airlines")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class airplane_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from airplane")
        self.setWindowTitle("Airplanes")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class airport_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from airport")
        self.setWindowTitle("Airports")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class flight_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from flight")
        self.setWindowTitle("Flights")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class leg_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from leg")
        self.setWindowTitle("Legs")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class location_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from location")
        self.setWindowTitle("Locations")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class passenger_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from passenger")
        self.setWindowTitle("Passengers")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class passenger_vacations_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from passenger_vacations")
        self.setWindowTitle("Passenger Vacations")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class person_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from person")
        self.setWindowTitle("People")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class pilot_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from pilot")
        self.setWindowTitle("Pilots")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class pilot_licenses_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from pilot_licenses")
        self.setWindowTitle("Pilot Licenses")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class route_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from route")
        self.setWindowTitle("Routes")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class route_path_window(QWidget):
    def __init__(self, data, headers, main_window):
        super().__init__()
        self.main_window = main_window
        db.get_view("SELECT * from route_path order by routeID asc, sequence")
        self.setWindowTitle("Route Path")
        
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content_widget)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.go_back)
        
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(back_button)

        self.setLayout(layout)
        
        columns = 2
        for idx, data in enumerate(data):
            card = self.create_card(data, headers)
            row_pos = idx // columns
            col_pos = idx % columns
            self.content_layout.addWidget(card, row_pos, col_pos)
        
        
    def create_card(self, data, headers):
        card = QGroupBox()
        card_layout = QVBoxLayout()
        for header, value in zip(headers, data):
            label = QLabel(f"<b>{header}:</b> {value}")
            card_layout.addWidget(label)
        
        card.setLayout(card_layout)
        return card
        
    def go_back(self):
        self.close()
        self.main_window.show()

class database:
    def __init__(self):
        self.conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "040105",
            database = "flight_tracking"
        )
        
        self.cursor = self.conn.cursor()
        
    def get_view(self, view):
        self.cursor.execute(view)
        rows = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        print(rows)
        return rows, headers
    
    def get_foreign_key(self, query, params = None):
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        if len(rows[0]) == 2:
            alist = [(row[0], row[1]) for row in rows]
        else:
            alist = [row[0] for row in rows]
        return alist
    
    def add_airplane(self, values):
        self.cursor.execute('CALL add_airplane(%s, %s, %s, %s, %s, %s, %s, %s, %s)', values)
        self.conn.commit()


    def add_airport(self, values):
        self.cursor.execute('CALL add_airport(%s, %s, %s, %s, %s, %s)', values)
        self.conn.commit()


    def add_person(self, values):
        self.cursor.execute('CALL add_person(%s, %s, %s, %s, %s, %s, %s, %s)', values)
        self.conn.commit()

    def grant_or_revoke_pilot_license(self, values):
        self.cursor.execute('CALL grant_or_revoke_pilot_license(%s, %s)', values)
        self.conn.commit()

    def offer_flight(self, values):
        self.cursor.execute('CALL offer_flight(%s, %s, %s, %s, %s, %s, %s)', values)
        self.conn.commit()

    def flight_landing(self, values):
        self.cursor.execute('CALL flight_landing(%s)', values)
        self.conn.commit()

    def flight_takeoff(self, values):
        self.cursor.execute('CALL flight_takeoff(%s)', values)
        self.conn.commit()

    def passengers_board(self, values):
        self.cursor.execute('CALL passengers_board(%s)', values)
        self.conn.commit()

    def passengers_disembark(self, values):
        self.cursor.execute('CALL passengers_disembark(%s)', values)
        self.conn.commit()

    def assign_pilot(self, values):
        self.cursor.execute('CALL assign_pilot(%s, %s)', values)
        self.conn.commit()

    def recycle_crew(self, values):
        self.cursor.execute('CALL recycle_crew(%s)', values)
        self.conn.commit()

    def retire_flight(self, values):
        self.cursor.execute('CALL retire_flight(%s)', values)
        self.conn.commit()

    def simulation_cycle(self):
        self.cursor.execute('CALL simulation_cycle()')

    def close(self):
        self.cursor.close()
        self.conn.close()

db = database()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()