def login():
  print("Logging")
def fetching_data():
  print("Fetching Data")
def displaying_dashboard():
  print("Display Dashboard")
def logging_out():
  print("Logging out")
  
  
def user_activity(a,b):
  if username == 'Mubashir' and password == 123:
    login()
    fetching_data()
    displaying_dashboard()
    logging_out()


username = 'Mubashir'
password = 123

user_activity(username,password)