#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Convolution2D,MaxPooling2D,Flatten
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import random
import pandas as pd
from keras.optimizers import RMSprop


# In[2]:


file= open("/ml/conf.txt", "r")
count=int(file.readline())
neuron=int(file.readline())
epoch=int(file.readline())
file.close()


# In[3]:


dataset = mnist.load_data('mymnist.db')


# In[4]:


train , test = dataset


# In[5]:


X_train , y_train = train
X_test , y_test = test


# In[6]:


X_train_1d = X_train.reshape(60000, 28,28,1)
X_train_1d.shape


# In[7]:


X_test_1d = X_test.reshape(10000, 28,28,1)
X_test_1d.shape


# In[8]:


#Converting the datatype 
X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')


# In[9]:


y_train_cat = to_categorical(y_train)


# In[10]:


#Create sequential model
model = Sequential()


# In[11]:


#Adding input layer
model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(28,28,1)
                       ))
#Reducing the size by 2x2
model.add(MaxPooling2D(pool_size=(2, 2)))
#Creating list 
model.add(Flatten())


# In[12]:


model.summary()



temp=1
while (count >= temp ):
    model.add(Dense(units=neuron*count, activation='relu'))
    temp+=1




model.summary()




#Adding Output Layer
model.add(Dense(units=10, activation='softmax'))


# In[21]:


model.summary()


# In[24]:


with open('/var/www/html/index.html','w') as fh:
    model.summary(print_fn=lambda x: fh.write(x + '\n'))


# In[ ]:


model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )


# In[ ]:


model.summary()
file= open("/var/www/html/index.html", "a")
file.write("\nEpoches: "+str(epoch)+"\n")
file.close()


# In[ ]:



h = model.fit(X_train, y_train_cat, epochs=epoch)


# In[ ]:


a=h.history['accuracy'][-1]


# In[ ]:


a


# In[ ]:


f = open("/ml/accuracy.txt", "w")
f.write(str(a))
f.close()


# In[ ]:


if a > 0.95:
    
    file= open("/ml/conf.txt", "w")
    file.write(str(1)+"\n"+str(32)+"\n"+str(1))
    file.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




