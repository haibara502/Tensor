import keras
import string
from keras.layers import Dense, Input
from keras.layers import Embedding
from keras.layers import Concatenate
from keras.models import Model

USER_SIZE = 10
ITEM_SIZE = 10
LOCATION_SIZE = 10
LABEL_SIZE = 2
EMBEDDING_DIM = 100
HIDDEN_DIM = 100

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

