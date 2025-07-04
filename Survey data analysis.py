
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/Lav/Desktop/DAIICT/sem 1/Communication skills and Technical Writing/Project/Swiggy Instamart User Experience Survey (Responses).xlsx")

# 39 data samples are there

#%%

# 1. age distribution

age = df.iloc[:, 1]

age_freq = np.array(age.value_counts())

age_types = np.array(age.value_counts().index)

plt.figure(dpi = 500)

plt.pie(age_freq, labels = age_types, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'})

plt.title('Age distribution of users')

plt.show()

#%%

# function for the above (pie chart plotting) functionality

def pie_chart(column_index, plot_title):
    column = df.iloc[:, column_index]
    column_freq = np.array(column.value_counts())
    column_types = np.array(column.value_counts().index)
    
    plt.figure(dpi = 500)
    
    plt.pie(column_freq, labels = column_types, autopct='%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'})
    
    plt.title(plot_title)
    
    plt.show()
    
#%%

# 2. college student/working professional

pie_chart(3, 'Types of users')

# the beauty of functions!!

#%%

# 3. frequency of ordering

# pie_chart(9, 'Frequency of ordering')

frequency = df.iloc[:, 9]

frequency_freq = np.array(frequency.value_counts())

frequency_types = np.array(frequency.value_counts().index)

plt.figure(dpi = 500)

plt.pie(frequency_freq, labels = frequency_types, autopct='%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'})

plt.title('Frequency of ordering')

plt.show()

#%%

# updated pie chart function

def pie_chart(column_index, text_size, plot_title):
    column = df.iloc[:, column_index]
    column_freq = np.array(column.value_counts())
    column_types = np.array(column.value_counts().index)
    
    plt.figure(dpi = 500)
    
    plt.pie(column_freq, labels = column_types, autopct='%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': text_size})
    
    plt.title(plot_title)
    
    plt.show()

#%%

# 4. Overall rating

pie_chart(15, 6, 'Overall rating')

#%%

# 5. Satisfaction with range of products

pie_chart(17, 7, 'Satisfaction with range of products')

#%%

# 6. Usual time of placing order

pie_chart(19, 7, 'Usual time of placing order')

#%%

# 7. Delivery time period

pie_chart(22, 7, 'Delivery time period')

#%%

# 8. Usual mode of payment

pie_chart(24, 7, 'Usual mode of payment')

#%%

# 9. Satisfaction with packaging

pie_chart(25, 7, 'Satisfaction with packaging')

#%%

# 10. Frequency of receiving a spoilt product

pie_chart(27, 7, 'Frequency of receiving a spoilt product')

#%%

# 11. Time taken by Swiggy Instamart to reply to a complaint

pie_chart(29, 7, 'Time taken by Swiggy Instamart to reply to a complaint')

#%%

# 12. Frequency of users experiencing lags and slow loading times and crashes on the app

pie_chart(32, 7, 'Frequency of users experiencing lags and slow loading times and crashes on the app')

#%%

# 13. Satisfaction with freshness level of fruits and vegetables

pie_chart(35, 8, 'Satisfaction with freshness level of fruits and vegetables')

#%%

# 14. Ease and efficiency of using the app

pie_chart(36, 7, 'Ease and efficiency of using the app')

#%%

"""             Stacked bar plots               """

# 15. impact of frequency of ordering on overall rating

f1 = np.array(df[df.iloc[:, 9] == 'Once every 2-3 months'].iloc[:, 15].value_counts())
t1 = np.array(df[df.iloc[:, 9] == 'Once every 2-3 months'].iloc[:, 15].value_counts().index)

f1 = np.array([0, 0, 1, 2, 0])

t = np.array([1, 2, 3, 4, 5])

f2 = np.array(df[df.iloc[:, 9] == 'Once a month'].iloc[:, 15].value_counts())
t2 = np.array(df[df.iloc[:, 9] == 'Once a month'].iloc[:, 15].value_counts().index)

f2 = np.array([1, 1, 6, 10, 2])

f3 = np.array(df[df.iloc[:, 9] == 'Twice a month'].iloc[:, 15].value_counts())
t3 = np.array(df[df.iloc[:, 9] == 'Twice a month'].iloc[:, 15].value_counts().index)

f3 = np.array([0, 0, 2, 3, 1])

f4 = np.array(df[df.iloc[:, 9] == '2-3 times a week'].iloc[:, 15].value_counts())
t4 = np.array(df[df.iloc[:, 9] == '2-3 times a week'].iloc[:, 15].value_counts().index)

f4 = np.array([0, 0, 1, 5, 3])

f5 = np.array(df[df.iloc[:, 9] == '4-5 times a week'].iloc[:, 15].value_counts())
t5 = np.array(df[df.iloc[:, 9] == '4-5 times a week'].iloc[:, 15].value_counts().index)

f5 = np.array([0, 0, 0, 1, 0])

labels = ['Once every 2-3 months', 'Once a month', 'Twice a month', '2-3 times a week', '4-5 times a week']

y1 = np.array([0, 1, 0, 0, 0])
y2 = np.array([0, 1, 0, 0, 0])
y3 = np.array([1, 6, 2, 1, 0])
y4 = np.array([2, 10, 3, 5, 1])
y5 = np.array([0, 2, 1, 3, 0])

plt.figure(dpi = 500, figsize = (12, 10))

plt.bar(labels, y1, edgecolor = 'black', color = 'tab:red')
plt.bar(labels, y2, bottom = y1, edgecolor = 'black', color = 'tab:purple')
plt.bar(labels, y3, bottom = y1 + y2, edgecolor = 'black', color = 'tab:orange')
plt.bar(labels, y4, bottom = y1 + y2 + y3, edgecolor = 'black', color = 'tab:blue')
plt.bar(labels, y5, bottom = y1 + y2 + y3 + y4, edgecolor = 'black', color = 'tab:green')

plt.legend(['1 star rating', '2 star rating', '3 star rating', '4 star rating', '5 star rating'])

plt.xlabel('Frequency of ordering')
plt.ylabel('Number of users')

plt.title('Impact of frequency of ordering on overall rating')

plt.show()

#%%

# 16. impact of satisfaction with freshness level of fruits and vegetables on overall rating

f1 = np.array(df[df.iloc[:, 35] == 'Supremely fresh quality, feels like they have been brought straight from the farm'].iloc[:, 15].value_counts())
t1 = np.array(df[df.iloc[:, 35] == 'Supremely fresh quality, feels like they have been brought straight from the farm'].iloc[:, 15].value_counts().index)

l1 = ['4 stars', '5 stars', '1 star']

c1 = ['tab:blue', 'tab:green', 'tab:red']

f2 = np.array(df[df.iloc[:, 35] == 'Fairly fresh quality, I am satisfied with what I get'].iloc[:, 15].value_counts())
t2 = np.array(df[df.iloc[:, 35] == 'Fairly fresh quality, I am satisfied with what I get'].iloc[:, 15].value_counts().index)

l2 = ['4 stars', '3 stars', '5 stars']

c2 = ['tab:blue', 'tab:orange', 'tab:green']

f3 = np.array(df[df.iloc[:, 35] == 'Usually not fresh quality, I feel like I could get much better quality from roadside vegetable vendors'].iloc[:, 15].value_counts())
t3 = np.array(df[df.iloc[:, 35] == 'Usually not fresh quality, I feel like I could get much better quality from roadside vegetable vendors'].iloc[:, 15].value_counts().index)

l3 = ['3 stars', '4 stars']

c3 = ['tab:orange', 'tab:blue']

f4 = np.array(df[df.iloc[:, 35] == 'Very unsatisfactory quality, I usually avoid ordering fruits and vegetables'].iloc[:, 15].value_counts())
t4 = np.array(df[df.iloc[:, 35] == 'Very unsatisfactory quality, I usually avoid ordering fruits and vegetables'].iloc[:, 15].value_counts().index)

l4 = ['2 stars']

c4 = ['tab:purple']

plt.figure(dpi = 500)

plt.subplot(2, 2, 1)

plt.pie(f1, labels = l1, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c1)
plt.title("Users saying 'Supremely fresh quality, feels like \nthey have been brought straight from the farm'", fontsize = 7)

plt.subplot(2, 2, 2)

plt.pie(f2, labels = l2, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c2)
plt.title("Users saying 'Fairly fresh quality, I am satisfied \nwith what I get'", fontsize = 7)

plt.subplot(2, 2, 3)

plt.pie(f3, labels = l3, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c3)
plt.title("Users saying 'Usually not fresh quality, \nI feel like I could get much better quality from \nroadside vegetable vendors'", fontsize = 7)

plt.subplot(2, 2, 4)

plt.pie(f4, labels = l4, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c4)
plt.title("Users saying 'Very unsatisfactory quality, \nI usually avoid ordering fruits and vegetables'", fontsize = 7)

plt.suptitle('Impact of satisfaction with freshness level of \nfruits and vegetables on overall rating', fontsize = 6.5, fontweight = 'extra bold')
print('\n')

plt.show()

#%%

# 17. impact of frequency of users experiencing lags and slow loading times and crashes on overall rating

f1 = np.array(df[df.iloc[:, 32] == 'Never'].iloc[:, 15].value_counts())
t1 = np.array(df[df.iloc[:, 32] == 'Never'].iloc[:, 15].value_counts().index)

l1 = ['2 stars', '5 stars', '4 stars']

c1 = ['tab:purple', 'tab:green', 'tab:blue']

f2 = np.array(df[df.iloc[:, 32] == 'Rarely'].iloc[:, 15].value_counts())
t2 = np.array(df[df.iloc[:, 32] == 'Rarely'].iloc[:, 15].value_counts().index)

l2 = ['4 stars', '3 stars', '5 stars']

c2 = ['tab:blue', 'tab:orange', 'tab:green']

f3 = np.array(df[df.iloc[:, 32] == 'Sometimes'].iloc[:, 15].value_counts())
t3 = np.array(df[df.iloc[:, 32] == 'Sometimes'].iloc[:, 15].value_counts().index)

l3 = ['4 stars', '3 stars', '1 star']

c3 = ['tab:blue', 'tab:orange', 'tab:red']

f4 = np.array(df[df.iloc[:, 32] == 'Often'].iloc[:, 15].value_counts())
t4 = np.array(df[df.iloc[:, 32] == 'Often'].iloc[:, 15].value_counts().index)

l4 = ['3 stars', '4 stars', '5 stars']

c4 = ['tab:orange', 'tab:blue', 'tab:green']

f5 = np.array(df[df.iloc[:, 32] == 'Always'].iloc[:, 15].value_counts())
t5 = np.array(df[df.iloc[:, 32] == 'Always'].iloc[:, 15].value_counts().index)

l5 = ['4 stars']

plt.figure(dpi = 500)

plt.subplot(2, 2, 1)

plt.pie(f1, labels = l1, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c1)
plt.title("Users 'never' experiencing lags", fontsize = 7)

plt.subplot(2, 2, 2)

plt.pie(f2, labels = l2, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c2)
plt.title("Users 'rarely' experiencing lags", fontsize = 7)

plt.subplot(2, 2, 3)

plt.pie(f3, labels = l3, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c3)
plt.title("Users 'sometimes' experiencing lags", fontsize = 7)

plt.subplot(2, 2, 4)

plt.pie(f4, labels = l4, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c4)
plt.title("Users 'often' experiencing lags", fontsize = 7)

plt.suptitle('Impact of frequency of users experiencing lags and \nslow loading times and crashes on overall rating', fontsize = 8, fontweight = 'extra bold')

plt.show()

#%%

# 18. Impact of delivery time period on overall rating

f1 = np.array(df[df.iloc[:, 22] == 'Under 10 minutes'].iloc[:, 15].value_counts())
t1 = np.array(df[df.iloc[:, 22] == 'Under 10 minutes'].iloc[:, 15].value_counts().index)

l1 = ['3 stars', '1 star']

c1 = ['tab:orange', 'tab:red']

f2 = np.array(df[df.iloc[:, 22] == '10-20 minutes'].iloc[:, 15].value_counts())
t2 = np.array(df[df.iloc[:, 22] == '10-20 minutes'].iloc[:, 15].value_counts().index)

l2 = ['4 stars', '5 stars', '3 stars']

c2 = ['tab:blue', 'tab:green', 'tab:orange']

f3 = np.array(df[df.iloc[:, 22] == '20-30 minutes'].iloc[:, 15].value_counts())
t3 = np.array(df[df.iloc[:, 22] == '20-30 minutes'].iloc[:, 15].value_counts().index)

l3 = ['4 stars', '3 stars', '2 stars', '5 stars']

c3 = ['tab:blue', 'tab:orange', 'tab:purple', 'tab:green']

f4 = np.array(df[df.iloc[:, 22] == '30-45 minutes'].iloc[:, 15].value_counts())
t4 = np.array(df[df.iloc[:, 22] == '30-45 minutes'].iloc[:, 15].value_counts().index)

l4 = ['4 stars', '3 stars']

c4 = ['tab:blue', 'tab:orange']

plt.figure(dpi = 500)

plt.subplot(2, 2, 1)

plt.pie(f1, labels = l1, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c1)
plt.title("Users getting delivery in under 10 minutes", fontsize = 7)

plt.subplot(2, 2, 2)

plt.pie(f2, labels = l2, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c2)
plt.title("Users getting delivery in 10 - 20 minutes", fontsize = 7)

plt.subplot(2, 2, 3)

plt.pie(f3, labels = l3, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 4.5}, colors = c3)
plt.title("Users getting delivery in 20 - 30 minutes", fontsize = 7)

plt.subplot(2, 2, 4)

plt.pie(f4, labels = l4, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 'smaller'}, colors = c4)
plt.title("Users getting delivery in 30 - 45 minutes", fontsize = 7)

plt.suptitle('Impact of delivery time period on overall rating', fontsize = 8, fontweight = 'extra bold')

plt.show()

#%%

# 19. Relation of age group of users with their usual time of placing order

stars = ['5 stars', '4 stars', '3 stars', '2 stars', '1 star']
colours = ['tab:green', 'tab:blue', 'tab:orange', 'tab:purple', 'tab:red']

f1 = np.array(df[df.iloc[:, 1] == '20-30 years'].iloc[:, 19].value_counts())
t1 = np.array(df[df.iloc[:, 1] == '20-30 years'].iloc[:, 19].value_counts().index)

c1 = ['tab:blue', 'tab:orange', 'tab:green', 'tab:purple', 'tab:red']

f2 = np.array(df[df.iloc[:, 1] == '40-50 years'].iloc[:, 19].value_counts())
t2 = np.array(df[df.iloc[:, 1] == '40-50 years'].iloc[:, 19].value_counts().index)

c2 = ['tab:blue', 'tab:green', 'tab:purple']

f3 = np.array(df[df.iloc[:, 1] == '30-40 years'].iloc[:, 19].value_counts())
t3 = np.array(df[df.iloc[:, 1] == '30-40 years'].iloc[:, 19].value_counts().index)

c3 = ['tab:blue', 'tab:green']

f4 = np.array(df[df.iloc[:, 1] == '50-60 years'].iloc[:, 19].value_counts())
t4 = np.array(df[df.iloc[:, 1] == '50-60 years'].iloc[:, 19].value_counts().index)

c4 = ['tab:blue', 'tab:purple']

plt.figure(dpi = 500)

plt.subplot(2, 2, 1)

plt.pie(f1, labels = t1, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 6}, colors = c1)
plt.title("Users in age range 20 - 30 years", fontsize = 8)

plt.subplot(2, 2, 2)

plt.pie(f2, labels = t2, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 6}, colors = c2)
plt.title("Users in age range 40 - 50 years", fontsize = 8)

plt.subplot(2, 2, 3)

plt.pie(f3, labels = t3, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 6}, colors = c3)
plt.title("Users in age range 30 - 40 years", fontsize = 8)

plt.subplot(2, 2, 4)

plt.pie(f4, labels = t4, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 6}, colors = c4)
plt.title("Users in age range 50 - 60 years", fontsize = 8)

plt.suptitle('Relation of age group of users with their usual time of placing order', fontsize = 10, fontweight = 'extra bold')

plt.show()

#%%

# colour coding?!

f = [4, 3, 2, 1.5, 1]

labels = ['blue', 'orange', 'green', 'red', 'purple']

# coding

stars = ['5 stars', '4 stars', '3 stars', '2 stars', '1 star']
colours = ['tab:green', 'tab:blue', 'tab:orange', 'tab:purple', 'tab:red']

#         

plt.figure(dpi = 500)

plt.pie(f, labels = labels, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black', 'linewidth': 1}, textprops = {'size': 6}, colors = ['tab:green', 'tab:blue', 'tab:orange', 'tab:purple', 'tab:red'])

plt.show()







