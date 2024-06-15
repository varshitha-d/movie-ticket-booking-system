from collections import deque
class Movie_Ticket_Booking:
    def __init__(self):
        self.theatres = {
            "ASIAN_CINEMAS" : ["Manjummel Boys","Hridayam","Pushpa 2","Aavesham"],
        "PVR" : ["Munjya","Kalki","Crew","3 Moonu"],
        "INOX" : ["Manjummel Boys","Munjya","Kalki","Hridayam"],
        "IMAX" : ["Pushpa 2","Crew","Aavesham","3 Moonu"],
        }
        self.credentials = {"Akshaya":"akshu123",
                            "Revathi":"minnu123",
                            "Charitha":"cherry123",
                            "Varshitha":"varsha123",
                            "Rimsha" : "rimsha123"
                        }
        self.booked_tickets = deque()
        self.a = 0
        self.details = []

    def Sign_Up(self):
        print("")
        print("Sign Up to your account.")
        print("-------------------------")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        cnfrm_password = input("Confirm your password: ")
        phn_no = input("Enter your phone number: ")
        if password == cnfrm_password:
            print("You have successfully signed up... Now you can log in...")
            self.credentials[username] = password
            return self.Log_In()
        else:
            print("Password Mismatch... Enter your credentials again...")
            return self.Sign_Up()
        print("")


    def Log_In(self):
        print("")
        print("Log In to your account.")
        print("------------------------")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.credentials.keys() and password == self.credentials[username] :
            self.user = True
        else:
            print("Invalid Credentials.. Do you want to create a account..")
            print("1 Yes")
            print("2 No")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.Sign_Up()
            elif choice == 2:
                self.Log_In()

        print(f"Welcome {username}!")
        if self.a == 1:
            return self.Location()
        else:
            self.a += 1
            return self.Booking()
        print("")
            

    def Location(self):
        location = ["Hyderabad","Warangal","Karimnagar"]
        print("")
        print("Hi! Welcome to Show Time Genie.")
        print("Choose your location: ")
        for i in range(3):
            print(i+1,location[i])
        print("4 Back")
        loc = int(input("Choose an option: "))
        self.details.append(location[loc - 1])
        return self.Movies()
    
    def Movies(self):
        movies = ["Manjummel Boys","Munjya","Hridayam","Kalki","Pushpa 2","Crew","Avesham","3 Moonu"]
        print("")
        print("Select your Vibe(Movie): ")
        for i in range(len(movies)):
            print(i+1,movies[i])
        print(len(movies)+1,"Back")
        movie_index = int(input("Choose an option: "))
        movie = movies[movie_index-1]
        self.details.append(movie)
        return self.Theatre(movie)
    
    def Theatre(self,movie):
        print("")
        print("Choose a theatre: ")
        available_theatres = []

        for theatre, movies in self.theatres.items():
            if movie in movies:
                available_theatres.append(theatre)

        if available_theatres:
            for i in range(len(available_theatres)):
                print(i+1,available_theatres[i])
        print(len(available_theatres)+1,"Back")

        th_index = int(input("Choose an option: "))

        if 1 <= th_index <= len(available_theatres):
            th = available_theatres[th_index-1]
            self.details.append(th)
            return self.Timings(movie,th)
        elif th_index == len(available_theatres) + 1:
            return self.Movies()
            
    def Timings(self,movie,th):
        Screen1 = ["10.00-1.00","1.10-4.10","4.20-7.20","7.30-10.30"]
        Screen2 = ["10.15-1.15","1.25-4.25","4.35-7.35","7.45-10.45"]
        Screen3 = ["10.30-1.30","1.40-4.40","4.50-7.50","8.00-10.45"]
        Screen4 = ["10.45-1.45","1.55-4.55","5.05-7.55","8.10-10.50"]
        print("")
        print("Select timing: ")
        available_movies = []
        available_movies.extend(self.theatres[th])
        for i in available_movies:
            if i == movie:
                sc = available_movies.index(i)+1
        if sc == 1:
            print("Screen1")
            for i in range(len(Screen1)):
                print(i+1,Screen1[i])
            time = int(input("Choose your timing: "))
            self.details.append(Screen1[time-1])
        elif sc == 2:
            print("Screen2")
            for i in range(len(Screen2)):
                print(i+1,Screen2[i])
            time = int(input("Choose your timing: "))
            self.details.append(Screen2[time-1])
        elif sc == 3:
            print("Screen3")
            for i in range(len(Screen3)):
                print(i+1,Screen3[i])
            time = int(input("Choose your timing: "))
            self.details.append(Screen3[time-1])
        elif sc == 4:
            print("Screen4")
            for i in range(len(Screen4)):
                print(i+1,Screen4[i])
            time = int(input("Choose your timing: "))
            self.details.append(Screen4[time-1])
        return self.Seats()
    
    def Seats(self):
        total_availability = 120
        sold = 0
        remaining = 120
        print("")
        print("Total Seats: ",total_availability)
        print("Number of sold seats: ",sold)
        print("Number of seats remaining: ",remaining)
        no_of_seats = int(input("Enter no of seats you want to book: "))
        if remaining >= no_of_seats:
            confirmation = input("Do you want to confirm your booking? (Yes/No) ")
            if confirmation == "Yes":
                self.details.append(no_of_seats)
                remaining -= self.details[len(self.details)-1]
                sold += self.details[len(self.details)-1]
                return self.Booking()
            elif confirmation == "No":
                print("Your booking is not confirmed..")
                return self.Seats()
        else:
            print(no_of_seats," Seats are not available..")
            print("Available seats are: ",remaining)
            back = input("Do you want to go back? Yes/No")
            if confirmation == "Yes":
                return self.Timings(self.details[1],self.details[2],self.details)
            elif confirmation == "No":
                return self.Seats()
            
    def Booking(self):
        if self.a == 1:
            print("*****",self.details[len(self.details)-1]," Seats booked successfully *****")
            self.booked_tickets.append(self.details)
            return self.view_Bookings()
            self.a-=0
        elif self.a == 0:
            return self.Log_In()
        
    def view_Bookings(self):
        if not self.booked_tickets:
            print("\nNo tickets booked yet.")
        else:
            print("\nBooked Tickets:")
            print("==================")
            details = []
            for i in range(len(self.booked_tickets)):
                details.extend(self.booked_tickets[i])
                print(f"Ticket          :   {i+1}")
                print(f"Location        : {details[0]}")
                print(f"Movie Name      : {details[1]}")
                print(f"Theatre         : {details[2]}")
                print(f"Timings         : {details[3]}")
                print(f"Number of seats : {details[4]}")
                print("")
            a = input("Do you want to manage booking or Log out? manage/log out - ")
            if a == "manage":
                return self.manage_booking()
            elif a == "log out":
                return self.Home()
            else:
                print("Invalid option.. Try Again...")
                return self.view_Bookings()
        
    def manage_booking(self):
        booking_id = int(input("Which booking do you want to manage: "))
        cncl_or_mng = input("Do you want to manage this booking? yes/no ")
        details = []
        details = self.booked_tickets[booking_id-1]
        print("")
        print(f"Ticket          : {booking_id}")
        print(f"Location        : {details[0]}")
        print(f"Movie Name      : {details[1]}")
        print(f"Theatre         : {details[2]}")
        print(f"Timings         : {details[3]}")
        print(f"Number of seats : {details[4]}")
        print("")
        if cncl_or_mng == "yes":
            print("What do you want to do?")
            print("1 Increase Seats")
            print("2 Cancel booking")
            self.a = int(input("Choose an option: "))
            if self.a == 1:
                return self.Seats()
            elif self.a == 2:
                self.booked_tickets.remove(details)
                print("Your booking is successfully cancelled.")
                details = []
                for i in range(len(self.booked_tickets)):
                    details.extend(self.booked_tickets[i])
                    print("")
                    print(f"Ticket          :   {i+1}")
                    print(f"Location        : {details[0]}")
                    print(f"Movie Name      : {details[1]}")
                    print(f"Theatre         : {details[2]}")
                    print(f"Timings         : {details[3]}")
                    print(f"Number of seats : {details[4]}")
                    print("")
                return self.Home()

    def Home(self):
        print("")
        home = ["Sign Up","Log In","View Home"]
        for i in range(3):
            print(i+1,home[i])
        select = int(input("Choose an option: "))
        if select == 1:
            self.a += 1
            return self.Sign_Up()
        elif select == 2:
            self.a +=1
            return self.Log_In()
        elif select == 3:
            return self.Location()

mov = Movie_Ticket_Booking()
mov.Home()