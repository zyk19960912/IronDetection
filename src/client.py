# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 8080                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
s.send("This is really really a good thing, especially in the rainy days !!!")
# receive data from the server 
print s.recv(1024) 
# close the connection 
s.close()


# from DataProcessor import DataProcessor
# from MLP import MLP
# import numpy as np

# n_fold = 10
# train_file = "data/SemEval2018-T3-taskA.txt"
# test_file = "data/SemEval2018-T3_input_test_taskA.txt"

# dataProcessor = DataProcessor()

# train_data, test_data = dataProcessor.process_data(train_file, test_file, load_saved_data=False)
# features = dataProcessor.getFeature('@Callisto1947 Can U Help?||More conservatives needed on #TSU + get paid 4 posting stuff like this!||YOU $ can go to http://t.co/JUmMWi0AyT')
# print(features.shape)
# features = features.reshape(1,len(features))
# print(features.shape)
# # label = MLP().predict_labels(features, features_pl, keep_prob_pl, predict, session)