import urllib.request
from bs4 import *
import smtplib
import csv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import numpy as np
from email.mime.image import MIMEImage
msg=[]
data=[]
with open("C:/Users/bakkolla/Desktop/mini/StockSymbols.csv") as csvfile:
    symbollist = csv.DictReader(csvfile)
    for row in symbollist:
        url = "http://www.bloomberg.com" + "/quote/" +row['SYMBOL'] +":US"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page,'html.parser')
        value = soup.find('span', {'class': 'priceText__1853e8a5'}).text
        msg.append("The stock price of " + row['SYMBOL'] + '= ' +str(value) + '\n')
        data.append((row['SYMBOL'],value))
with open('index.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for name, value in data:
       writer.writerow([name, value])
outfile = open("index.csv","r")
file=csv.reader(outfile)
#next(file, None)
stock = []
values = []

for row in file:
    stock.append(row[0])
    values.append(float(row[1].replace(",",'')))
explode = list()
for k in stock:
    explode.append(0.1)

pie=plt.pie(values, labels=stock, explode=explode, autopct='%1.1f%%')
plt.legend(pie[0],stock, labels=['%s, %1.2f %%' % (l, s) for l, s in zip(stock, values)], loc="center", bbox_to_anchor=(0.58,0.54,0.5,0.5),
                         bbox_transform=plt.gcf().transFigure,title='in Dollars($)')
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
plt.axis('equal') # make the pie chart circular

plt.savefig("ex.png")

strFrom = '' #fromEmail ID
strTo = ''  #toEmail ID

msgRoot = MIMEMultipart('Example')
msgRoot['Subject'] = 'Daily Stock Digest'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<img src="cid:image1"><br>', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('ex.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.gmail.com')
smtp.starttls()
smtp.login('', '') #fromEmailID, Password
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()


