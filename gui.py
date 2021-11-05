from tkinter import *
import joblib
import extractElementsFromURL
import re
# load the pickle file
classifier = joblib.load('final_models/rf_final.pkl')

# input url
#print("enter url")


root = Tk()
# root.geometry("500x200")
headerText = Label(root, text="MALICIOUS ULR DETECTION PROJECT", font=("Arial", 25), padx=10, pady=10).grid(
    row=1, column=1)
inputLabel = Label(root, text="Enter the ULR", font=(
    "Arial", 20), padx=10, pady=5).grid(row=2, column=1)
inputBox = Entry(root, width=100, font=("Arial", 12))
inputBox.grid(row=3, column=1)


def fun():
    print(inputBox.get())


my_string_var = StringVar()
label = Label(root, textvariable=my_string_var,
              font=("Arial", 25), padx=10, pady=10)


def url_detection():
    #url = input()
    url = inputBox.get()

    if(not(re.search(r'^(http|ftp)s?://', url))):
        #print("INVALID URL")
        my_string_var.set("invalid URL")
    else:
        # checking and predicting
        checkprediction = extractElementsFromURL.main(url)
        prediction = classifier.predict(checkprediction)
        if prediction == -1:
            # print "The website is safe to browse"
            # print("SAFE")
            my_string_var.set("The website is safe to browse")
        elif prediction == 1:
            # print "The website has phishing features. DO NOT VISIT!"
            my_string_var.set(
                "The website has phishing features. DO NOT VISIT!")


btnGetURL = Button(root, text="CHECK", font=("Arial", 10), padx=3, pady=3, bg="black", fg="white",
                   command=url_detection).grid(row=4, column=1)
label.grid(row=5, column=1)

root.mainloop()
