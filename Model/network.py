import keras
import string
from keras.layers import Dense, Input
from keras.layers import Embedding
from keras.layers import Concatenate
from keras.models import Model
from keras.utils import to_categorical
import numpy as np

USER_SIZE = 210
ITEM_SIZE = 210
LOCATION_SIZE = 210
LABEL_SIZE = 2
EMBEDDING_DIM = 20
HIDDEN_DIM = 50

def read_data(paths):
	index = int(paths[2])

	dataset_x = []
	dataset_y = []
	dataset_z = []
	labels = []

	for i in range(1, index + 1):
		file_name = paths[0] + chr(48 + i) + paths[1]
		print file_name
		read_file = open(file_name, "r")
		while 1:
			line = read_file.readline()
			if not line:
				break
			numbers = line.split(' ')
			dataset_x.append(numbers[0])
			dataset_y.append(numbers[1])
			dataset_z.append(numbers[2])
			label = np.array(numbers[3])
			label = to_categorical(label, num_classes = LABEL_SIZE)
			labels.append(label)

	return dataset_x, dataset_y, dataset_z, labels

train_x, train_y, train_z, train_label = read_data(["../reu/enron_train_", ".txt", 6])
test_x, test_y, test_z, test_label = read_data(["../reu/enron_test_", ".txt", 5])

train_x = np.array(train_x)
train_y = np.array(train_y)
train_z = np.array(train_z)
train_label = np.array(train_label)

test_x = np.array(test_x)
test_y = np.array(test_y)
test_z = np.array(test_z)
test_label = np.array(test_label)

input_user = Input(shape = (1, ))
imbed_user = Embedding(USER_SIZE, output_dim = EMBEDDING_DIM)(input_user)	

input_item = Input(shape = (1, ))
imbed_item = Embedding(ITEM_SIZE, output_dim = EMBEDDING_DIM)(input_item)

input_location = Input(shape = (1, ))
imbed_location = Embedding(LOCATION_SIZE, output_dim = EMBEDDING_DIM)(input_location)

input_all_params = Concatenate(axis = -1)([imbed_user, imbed_item, imbed_location])

hidden_layer = Dense(HIDDEN_DIM, activation = 'sigmoid')(input_all_params)
hidden_layer = Dense(HIDDEN_DIM, activation = 'sigmoid')(hidden_layer)

output_label = Dense(LABEL_SIZE, activation = 'softmax')(hidden_layer)

model = Model(inputs = [input_user, input_item, input_location], outputs = output_label)
model.summary()

model.compile(optimizer = 'SGD', loss = 'binary_crossentropy', metrics=['accuracy'])
model.fit([train_x, train_y, train_z], train_label, batch_size = 10, epochs = 100, verbose = 1, validation_split = 0.1, shuffle = True)
score, acc = model.evaluate([test_x, test_y, test_z], test_label, batch_size = 10, verbose = 1)
print score
print acc
