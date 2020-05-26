#!/usr/bin/env python
# coding: utf-8




file= open("/ml/conf.txt", "r")
count=int(file.readline())
neuron=int(file.readline())
epoch=int(file.readline())
file.close()




count+=1





neuron*=2


# In[4]:


epoch*=2


# In[5]:


file= open("/ml/conf.txt", "w")
file.write(str(count)+"\n"+str(neuron)+"\n"+str(epoch))
file.close()


# In[ ]:




