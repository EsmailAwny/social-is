#!/usr/bin/env python
# coding: utf-8

# In[3]:


print('Hello python ')


# In[4]:


string = 'Hello'
intger = 16

print(string)
print(intger)


# In[7]:


number_of_Oranges = 3

if number_of_Oranges < 1:
    print('You have no Oranges')
elif number_of_Oranges == 1:
    print('You have one Orange')
elif number_of_Oranges< 4:
    print('You have a few Oranges')
else:
    print('You have many Oranges!')


# In[8]:


student_names = ['Ali', 'ahmed', 'saad', 'mo']
student_names[1]


# In[9]:


student_names[-1]


# In[10]:


student_names[1:3]


# In[11]:


student_names[2:]


# In[13]:


student_names.append('asd')
student_names


# In[14]:


student_names.insert(2, 'X')
student_names


# In[15]:


del student_names[2]
student_names


# In[16]:


student_names = ['Ali', 'ahmed', 'mo', 'asd']

for student_name in student_names:
    print('Hello ' + student_name + '!')


# In[20]:


student_names = ['Ali', 'ahmed', 'saad', 'asd']

student_x = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_x.append(
            (student_name_0, student_name_1)
        )

student_pairs


# In[21]:


student_x[0]


# In[24]:


student_grade = ('Ali', 'saad', 'c-')
student_grade


# In[25]:


student_grade[0]


# In[27]:


student_grade = ('Ali', 'saad', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)


# In[29]:


student_grades = [
    ('Ali', 'saad', 'A'),
    ('ahmed', 'asd', 'C'),
    ('mo', 'wiled', 'B+'),
    ('salah', 'esmail', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# In[30]:


for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])


# In[33]:


foreign_languages = {
    'Ali': 'Spanish',
    'ahmed': 'French',
    'addallh': 'Italian',
    'asd': 'Italian',
}


# In[35]:


foreign_languages['asd']


# In[36]:


'Ali' in foreign_languages


# In[37]:


del foreign_languages['asd']
foreign_languages


# In[38]:


for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)


# In[39]:


student_grade = ('Ali', 'Spanish', 'A')


# In[40]:


student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)


# In[42]:


record = {
    'name': 'Ali',
    'subject': 'Spanish',
    'grade': 'c',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])


# In[43]:


student_grades = [
    ('Ali', 'Spanish', 'A'),
    ('asd', 'French', 'C'),
    ('asdl', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]


# In[44]:


student_grades[1][2]


# In[45]:


student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# In[46]:


student_grade_records[1]['grade']


# In[47]:


for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('Congratulations', record['name'], 
              'on getting an', record['grade'], 
              'in', record['subject'])


# In[48]:


foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades


# In[49]:


foreign_language_grades['Ali']['grade']


# In[50]:


student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades


# In[52]:


student_report_cards = {}
for student_name, subject, grade in student_grades:
  
    if student_name not in student_report_cards:
        student_report_cards[student_name] = {}
    student_report_cards[student_name][subject] = grade


# In[54]:


student_report_cards


# In[ ]:





# In[ ]:




