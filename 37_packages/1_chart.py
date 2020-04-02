import matplotlib.pyplot as plt

labels ='דואמ', 'הדימב הבר','ללכב אל' 
sizes = [492, 50, 2]
colors = ['gold', 'yellowgreen', 'lightcoral']
plt.pie(sizes,labels=labels,colors=colors,
autopct='%1.1f%%')
plt.show()
