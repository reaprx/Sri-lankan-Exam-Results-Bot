import telebot
import re
import requests
import json
import os

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

wel_mes  = """Hello I can find exam results.
/help for more info

Powered By @xreapr"""
help_mes = """To get Results send Index Number as Following.
/al {Index nNumber}  -  To get AL Rsults
/ol {Index nNumber}  -  To get OL Rsults
/g5 {Index nNumber}  -  To get Grade 5 Scholarship Exam Rsults

e.g. :- /ol 6162XXXX"""
type_error = "Wrong Index Number"
in_error = "Check the index number again"

def alresult(inumber):
  result_json = requests.get("https://www.doenets.lk/result/service/AlResult/"+inumber)
  try:
   re = json.loads(result_json.text)
   global res
   res = "\nExam - " + re['examination'] + "\nYear - "+ re['year'] + "\nName - " + re['name'] + "\nIndex Number - " + re['indexNo'] + "\nNIC Number - " + re['nic'] + "\nDistrict Rank - " + re['districtRank'] + "\nIsland Rank - " + re['islandRank'] + "\nZScore - " + re['zScore'] + "\nSubject Stream - " + re['stream'] + "\nResults \n" + re['subjectResults'][0]['subjectName'] + " - " + re['subjectResults'][0]['subjectResult'] + "\n" + re['subjectResults'][1]['subjectName'] + " - " + re['subjectResults'][1]['subjectResult'] + "\n" + re['subjectResults'][2]['subjectName'] + " - " + re['subjectResults'][2]['subjectResult'] + "\n" + re['subjectResults'][3]['subjectName'] + " - " + re['subjectResults'][3]['subjectResult'] + "\n" + re['subjectResults'][4]['subjectName'] + " - " + re['subjectResults'][4]['subjectResult']
  except TypeError:
   res= type_error

def olresult(inumber):
  result_json = requests.get("https://www.doenets.lk/result/service/OlResult/"+inumber)
  try:  
    re = json.loads(result_json.text)
    global res
    res = "\nExam - " + re['examination'] +"\nYear - " + re['year'] + "\nName - " + re['name'] + "\nIndex Number - " + re['indexNo'] + "\nResults \n" + re['subjectResults'][0]['subjectName'] + " - " + re['subjectResults'][0]['subjectResult'] + "\n" + re['subjectResults'][1]['subjectName'] + " - " + re['subjectResults'][1]['subjectResult'] + "\n" + re['subjectResults'][2]['subjectName'] + " - " + re['subjectResults'][2]['subjectResult'] + "\n" + re['subjectResults'][3]['subjectName'] + " - " + re['subjectResults'][3]['subjectResult'] + "\n" + re['subjectResults'][4]['subjectName'] + " - " + re['subjectResults'][4]['subjectResult'] + "\n" + re['subjectResults'][5]['subjectName'] + " - " + re['subjectResults'][5]['subjectResult'] + "\n" + re['subjectResults'][6]['subjectName'] + " - " + re['subjectResults'][6]['subjectResult'] + "\n" + re['subjectResults'][7]['subjectName'] + " - " + re['subjectResults'][7]['subjectResult'] + "\n" + re['subjectResults'][8]['subjectName'] + " - " + re['subjectResults'][8]['subjectResult']
  except TypeError:
    res=type_error


def g5result(inumber):
  i=1
  try:
    result_json = requests.get("https://www.doenets.lk/result/service/GvResult/"+inumber)    
    re = json.loads(result_json.text)
    global res
    res = """Exam - {}
Year - {}  
Name - {}
Index Number - {} 
Marks - {}  
District Rank - {} """
    res = res.format(re['examination'], re['year'], re['name'], re['indexNo'], re['marks'], re['districtRank'] )
  except:
    while i<3:
        i+=1
        g5result(inumber)
        
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, wel_mes)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, help_mes)

@bot.message_handler(commands=['al','AL','Al'])
def send_al(message):
  x = re.split("\s", message.text)
  try:
    alresult(x[1])
    bot.reply_to(message,res)
  except:
    bot.reply_to(message, in_error)
  
@bot.message_handler(commands=['ol','OL','Ol'])
def send_ol(message):
   x = re.split("\s", message.text)
   try:
     olresult(x[1])
     bot.reply_to(message, res)
   except:
     bot.reply_to(message, in_error)
     

@bot.message_handler(commands=['g5','G5'])
def send_g5(message):
   x = re.split("\s", message.text)
   try:
     g5result(x[1])
     bot.reply_to(message, res)
   except:
     bot.reply_to(message, in_error)

bot.polling()
