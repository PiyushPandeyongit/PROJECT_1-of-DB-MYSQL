# this is the railway ticket booking simple mysql database program
# where user have choices 1 to insert 2 to delete 3 to update 
import mysql.connector
connection=mysql.connector.connect(host="localhost",
                                  username="root",
                                  password="piyushPanday90",
                                  database="railway_ticketbooking")

if connection.is_connected():
     createTable="create table if not exists passengersDetails(traveller_name text, train_name text, train_number text,journey_date text, origin_station text,destiny_station text , mobile_no text )"
     mycursor = connection.cursor()
     mycursor.execute(createTable)
     connection.commit()
     print("Table successfully created")
     while True:
          print("Menu:")
          print("1.Insert Details")
          print("2.Delete Details")
          print("3.Update Details")
          print("4.Invalid choice")
          choice=input("enter choice=")
          if choice=='1':
               # insertion:
               insertQuery="insert into passengersdetails values('{}','{}','{}','{}','{}','{}','{}')".format(
                     input("enter traveller_name= "),input("enter train_name= "),input("enter train_number= "),
                     input("enter journey_date= "),input("enter origin_station= "),input("enter destiny_station= "),
                     input("enter mobile_no= "))
               mycursor.execute(insertQuery)
               connection.commit()
               print("Ticket booked successfully.")
          elif choice=='2':
               #   deletion
                deleteQuery = "delete from passengersdetails where mobile_no='{}'".format(
                               input("Enter mobile number to delete: ")
                               )
                mycursor.execute(deleteQuery)
                connection.commit()
                print("Record deleted successfully.")

          elif choice=='3':
                
              
               updateQuery = "update passengersdetails set train_name='{}', train_number='{}', journey_date='{}', origin_station='{}', destiny_station='{}'  where mobile_no='{}'".format(
                              input("Enter new train name: "),
                               input("Enter new train number: "),
                               input("Enter new journey date : "),
                               input("Enter new origin station: "),
                              input("Enter new destiny station: "),
                              input("Enter mobile number to update: ")  
                              )
               mycursor.execute(updateQuery)
               connection.commit()
               print("Record updated successfully.")

 
          elif choice == '4':
                # Exit
                break
            
          else:
                print("Invalid choice, Please try again.")

     mycursor.close()
     connection.close()
     print("MySQL connection is closed.")
else:
      print("db is not connected")         
           
                 
          
                  




