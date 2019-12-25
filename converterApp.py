from tkinter import *
# from PIL import Image, ImageTk


start_app = Tk()
start_app.title('Converter App')
start_app.configure(background="yellow")
# start_app.geometry("100x150")

photo = PhotoImage(file="image.gif")
background_label = Label(start_app, image=photo)
background_label.place(relwidth=1, relheight=1)

# CLICK THE CONVERT BUTTON WITH NO INPUT NUMBERS
default = "APP ENDED"


# START FUNCTION
def start():
    app = Tk()
    app.title('Converter App')
    app.iconbitmap('C:/Users/bupal/OneDrive/Documents/PycharmProjects/Tkinter/ConvertApp')
    app.geometry("450x150")

    # Setting background colour
    app.configure(background="pink")

    # Create miles to km function
    def miles_km():
        number = miles.get()

        # Do the equation
        equation = float(number) * 2.2

        # Round it to 2 decimal places
        result = round(equation, 2)

        # Print out the result in  text box
        km.insert(0, str(result) + ' km')

    # Create celsius to fahrenheit converter function
    def cel_fah():
        number = celsius.get()

        # Do the equation
        equation = (float(number) * 9 / 5) + 32

        result = round(equation, 2)
        # Print out the result in  text box
        fah.insert(0, str(result) + ' fahrenheit')

    # Create kg to pound converter function
    def kg_pound():
        number = kilo_gram.get()

        # Do the equation
        equation = float(number) * 2.2

        # Round it to 2 decimal places
        result = round(equation, 2)

        # Print out the result in  text box
        pounds.insert(0, str(result) + ' pounds')

    # Quit the whole process -->  function
    def end():
        app.destroy()
        start_app.destroy()
        print(default)

    # MILES TO KM
    # Create a miles text boxes
    miles = Entry(app, width=10, borderwidth=2)
    miles.grid(row=2, column=0, padx=20, pady=(10, 0))

    # Create a converting button button
    convert_btn = Button(app, text="CONVERT", command=miles_km)
    convert_btn.grid(row=2, column=1, padx=5, pady=5, ipadx=50)

    # Create a km text boxes
    km = Entry(app, width=20, borderwidth=2)
    km.grid(row=2, column=2, padx=20, pady=(10, 0))

    # Create a celsius text boxes
    celsius = Entry(app, width=10, borderwidth=2)
    celsius.grid(row=3, column=0, padx=20, pady=(10, 0))

    # Create a converting button button
    convert_btn = Button(app, text="CONVERT", command=cel_fah)
    convert_btn.grid(row=3, column=1, padx=5, pady=5, ipadx=50)

    # Create a fahrenheit text boxes
    fah = Entry(app, width=20, borderwidth=2)
    fah.grid(row=3, column=2, padx=20, pady=(10, 0))

    # Create a kg text boxes
    kilo_gram = Entry(app, width=10, borderwidth=2)
    kilo_gram.grid(row=4, column=0, padx=20, pady=(10, 0))

    # Create a converting button
    convert_btn = Button(app, text="CONVERT", command=kg_pound)
    convert_btn.grid(row=4, column=1, padx=5, pady=5, ipadx=50)

    # Create a pound text boxes
    pounds = Entry(app, width=20, borderwidth=2)
    pounds.grid(row=4, column=2, padx=20, pady=(10, 0))

    # Converting button
    convert = Button(app, text="END", command=end)
    convert.grid(row=5, column=1, columnspan=1, padx=5, pady=5, ipadx=50)


# Start button
start_btn = Button(start_app, text="START", width=15, bg='red', fg='white', command=start)
start_btn.grid(row=1, column=1, columnspan=3, padx=15, pady=15)

start_app.mainloop()
