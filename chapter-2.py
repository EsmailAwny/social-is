#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[12]:


G = nx.DiGraph()
G.add_edges_from([('Indianapolis','a'),('a','b'),('b','c'),('c','Fairbanks')])
nx.draw(G,with_labels=True,node_color='pink',node_size=1500,font_color='red',font_size=17)
nx.has_path(G,'Indianapolis','Fairbanks')
list(nx.all_simple_paths(G,'Indianapolis','Fairbanks'))


# In[13]:


G = nx.DiGraph()
G.add_edges_from([('Indianapolis','a'),('a','Fairbanks'),('a','b'),('b','a'),('b','Fairbanks'),('Fairbanks','c'),('c','Indianapolis'),('Fairbanks','b'),('a','Indianapolis')])
nx.draw(G,with_labels=True,node_color='pink',node_size=1500,font_color='red',font_size=17)
nx.has_path(G,'Indianapolis','Fairbanks')
nx.shortest_path(G,'Indianapolis','Fairbanks')


# In[14]:


G = nx.DiGraph()
G.add_edges_from([('airport1','a'),('a','airport1'),('a','b'),('b','a'),('d','c'),('b','c'),('c','d'),('c','b'),('airport2','b'),('b','airport2'),('d','airport1'),('airport2','c'),('airport1','d'),('airport1','airport2')])
nx.draw(G,with_labels=True,node_color='pink',node_size=1500,font_color='red',font_size=17)
list(nx.all_simple_paths(G,'airport1','airport2'))


# In[ ]:




