import eventlet
import socketio
from DataProcessor import DataProcessor
from MLP import MLP
import eventlet
import socketio
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


sio = socketio.Server(cors_allowed_origins='*')

app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on('sentence')
def another_event(sid, data):
    print (data)
    data = data.encode('ascii', 'ignore').decode('ascii')
    features = dataProcessor.getFeature(str(data))
    features = features.reshape(1, len(features))
    label = MLP().predict_labels(features, features_pl, keep_prob_pl, predict, sess)
    print(str(label[0]))
    sio.emit('response', str(label[0]))

@sio.event
def my_message(sid, data):
    print('message ', data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), app)