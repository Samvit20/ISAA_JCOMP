# -*- coding: utf-8 -*-

# importing libraries
# from sklearn.externals import joblib
import joblib
import extractElementsFromURL
import re
# load the pickle file
classifier = joblib.load('final_models/rf_final.pkl')

# input url
print("enter url")
url = input()
if(not(re.search(r'^(http|ftp)s?://', url))):
    print("INVALID URL")
else:
    # checking and predicting
    checkprediction = extractElementsFromURL.main(url)
    prediction = classifier.predict(checkprediction)
    if prediction == -1:
        # print "The website is safe to browse"
        print("SAFE")
    elif prediction == 1:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")
