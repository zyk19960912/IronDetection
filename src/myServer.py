# first of all import the socket library 
import socket          
from DataProcessor import DataProcessor
from MLP import MLP
import numpy as np
import tensorflow as tf

n_fold = 10
train_file = "data/SemEval2018-T3-taskA.txt"
test_file = "data/SemEval2018-T3_input_test_taskA.txt"
dataProcessor = DataProcessor()

train_data, test_data = dataProcessor.process_data(train_file, test_file, load_saved_data=False)
k_fold_train, k_fold_valid = DataProcessor.split_kfolds(train_data, n_fold)

for i in range(len(k_fold_train)):
    print("====================Fold %d=================" % (i + 1))
    features_pl, keep_prob_pl, predict, sess = MLP().train_model(k_fold_train[i], k_fold_valid[i])

# next create a socket object 
s = socket.socket()          
print "Socket successfully created"
  
# reserve a port on your computer in our 
# case it is 8080 but it can be anything 
port = 8080                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening"            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
    # Establish connection with client. 
    conn, addr = s.accept()      
    print 'Got connection from', addr 
    
    # Read data
    from_client = conn.recv(4096)
  
    # get the input from the front end
    features = dataProcessor.getFeature(from_client)
    features = features.reshape(1,len(features))
#     with tf.device('/cpu:0'):
#         # Perform training
#         config = tf.ConfigProto()
#         with tf.Session(config=config) as sess:
    label = MLP().predict_labels(features, features_pl, keep_prob_pl, predict, sess)
    conn.send(str(label[0]))
    
    # Close the connection with the client 
    conn.close() 