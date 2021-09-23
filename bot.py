import telebot
import re
import requests
import json

bot_token = #REPLACE_BOT_TOKEN

bot = telebot.TeleBot(bot_token)

def alresult(inumber):
  result_json = requests.get("https://www.doenets.lk/result/service/AlResult/"+inumber)
  try:
   re = json.loads(result_json.text)
   global res
   res = "\nExam - " + re['examination'] + "\nYear - "+ re['year'] + "\nName - " + re['name'] + "\nIndex Number - " + re['indexNo'] + "\nNIC Number - " + re['nic'] + "\nDistrict Rank - " + re['districtRank'] + "\nIsland Rank - " + re['islandRank'] + "\nZScore - " + re['zScore'] + "\nSubject Stream - " + re['stream'] + "\nResults \n" + re['subjectResults'][0]['subjectName'] + " - " + re['subjectResults'][0]['subjectResult'] + "\n" + re['subjectResults'][1]['subjectName'] + " - " + re['subjectResults'][1]['subjectResult'] + "\n" + re['subjectResults'][2]['subjectName'] + " - " + re['subjectResults'][2]['subjectResult'] + "\n" + re['subjectResults'][3]['subjectName'] + " - " + re['subjectResults'][3]['subjectResult'] + "\n" + re['subjectResults'][4]['subjectName'] + " - " + re['subjectResults'][4]['subjectResult']
  except TypeError:
   res="Wrong Index Number"

def olresult(inumber):
  result_json = requests.get("https://www.doenets.lk/result/service/OlResult/"+inumber)
  try:  
    re = json.loads(result_json.text)
    global res
    res = "\nExam - " + re['examination'] +"\nYear - " + re['year'] + "\nName - " + re['name'] + "\nIndex Number - " + re['indexNo'] + "\nResults \n" + re['subjectResults'][0]['subjectName'] + " - " + re['subjectResults'][0]['subjectResult'] + "\n" + re['subjectResults'][1]['subjectName'] + " - " + re['subjectResults'][1]['subjectResult'] + "\n" + re['subjectResults'][2]['subjectName'] + " - " + re['subjectResults'][2]['subjectResult'] + "\n" + re['subjectResults'][3]['subjectName'] + " - " + re['subjectResults'][3]['subjectResult'] + "\n" + re['subjectResults'][4]['subjectName'] + " - " + re['subjectResults'][4]['subjectResult'] + "\n" + re['subjectResults'][5]['subjectName'] + " - " + re['subjectResults'][5]['subjectResult'] + "\n" + re['subjectResults'][6]['subjectName'] + " - " + re['subjectResults'][6]['subjectResult'] + "\n" + re['subjectResults'][7]['subjectName'] + " - " + re['subjectResults'][7]['subjectResult'] + "\n" + re['subjectResults'][8]['subjectName'] + " - " + re['subjectResults'][8]['subjectResult']
  except TypeError:
    res="Wrong Index Number"


def g5result(inumber):
  result_json = requests.get("https://www.doenets.lk/result/service/GvResult/"+inumber)
  try:  
    re = json.loads(result_json.text)
    global res
    res = "\nExam - " + re['examination'] + "\nYear - " + re['year'] + "\nName - " + re['name'] + "\nIndex Number - " + re['indexNo'] + "\nMarks - " + re['marks'] + "\nDistrict Rank - " + re['districtRank']
  except TypeError:
    res="Wrong Index Number"

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello I can find exam results.\n/help for more info\n\nPowered By @xreapr")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, """To get Results send Index Number as Following.

/al {Index nNumber}  -  To get AL Rsults
/ol {Index nNumber}  -  To get OL Rsults
/g5 {Index nNumber}  -  To get Grade 5 Scholarship Exam Rsults""")

@bot.message_handler(commands=['al','AL','Al'])
def send_al(message):
  x = re.split("\s", message.text)
  try:
    alresult(x[1])
    bot.reply_to(message,res)
  except:
    bot.reply_to(message, "Index Number?")
  
@bot.message_handler(commands=['ol','OL','Ol'])
def send_ol(message):
   x = re.split("\s", message.text)
   try:
     olresult(x[1])
     bot.reply_to(message, res)
   except:
     bot.reply_to(message, "Index Number?")
     

@bot.message_handler(commands=['g5','G5'])
def send_g5(message):
   x = re.split("\s", message.text)
   try:
     g5result(x[1])
     bot.reply_to(message, res)
   except:
     bot.reply_to(message, "Index Number?")

bot.polling()
