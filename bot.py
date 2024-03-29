import telebot
import re
import requests
import json
import os

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

wel_mes  = """Hello I can find exam results.
/help for more info """

help_mes = """To check Results send Index Number like this.

/al {Index nNumber}  -  To get AL Rsults
/ol {Index nNumber}  -  To get OL Rsults
/g5 {Index nNumber}  -  To get Grade 5 Scholarship Exam Rsults

e.g. :- /ol 6162XXXX"""

er_mes="Send with index number."

error_mes = "Something went wrong. Please try again later."

def alresult(inumber):
  try:
   result_json = requests.get("https://www.doenets.lk/result/service/AlResult/"+inumber)
   re = json.loads(result_json.text)
   res = """Exam - {}
Year - {} 
Name - {}
Index Number - {} 
NIC Number - {}
District Rank - {}
Island Rank - {} 
ZScore - {} 
Subject Stream - {} 
{} - {} 
{} - {}
{} - {}
{} - {}
{} - {}"""
   res=res.format(re['examination'], re['year'], re['name'], re['indexNo'], re['nic'], re['districtRank'], re['islandRank'], re['zScore'], re['stream'], re['subjectResults'][0]['subjectName'], re['subjectResults'][0]['subjectResult'], re['subjectResults'][1]['subjectName'], re['subjectResults'][1]['subjectResult'], re['subjectResults'][2]['subjectName'], re['subjectResults'][2]['subjectResult'], re['subjectResults'][3]['subjectName'], re['subjectResults'][3]['subjectResult'], re['subjectResults'][4]['subjectName'], re['subjectResults'][4]['subjectResult'])
   return res
  except:
    return error_mes

def olresult(inumber):
  try:
    result_json = requests.get("https://www.doenets.lk/result/service/OlResult/"+inumber)
    re = json.loads(result_json.text)
    res = """Exam - {}
Year - {}
Name - {} 
Index Number - {} 
{} - {}
{} - {}
{} - {}
{} - {}
{} - {}
{} - {}
{} - {}
{} - {}
{} - {}""" 
    res=res.format(re['examination'], re['year'], re['name'], re['indexNo'], re['subjectResults'][0]['subjectName'], re['subjectResults'][0]['subjectResult'], re['subjectResults'][1]['subjectName'], re['subjectResults'][1]['subjectResult'], re['subjectResults'][2]['subjectName'], re['subjectResults'][2]['subjectResult'], re['subjectResults'][3]['subjectName'], re['subjectResults'][3]['subjectResult'], re['subjectResults'][4]['subjectName'], re['subjectResults'][4]['subjectResult'], re['subjectResults'][5]['subjectName'], re['subjectResults'][5]['subjectResult'], re['subjectResults'][6]['subjectName'], re['subjectResults'][6]['subjectResult'], re['subjectResults'][7]['subjectName'], re['subjectResults'][7]['subjectResult'], re['subjectResults'][8]['subjectName'], re['subjectResults'][8]['subjectResult'] )
    return res
  except:
    return error_mes

def g5result(inumber):
  try:
    result_json = requests.get("https://www.doenets.lk/result/service/GvResult/"+inumber)    
    re = json.loads(result_json.text)
    res = """Exam - {}
Year - {}  
Name - {}
Index Number - {} 
Marks - {}  
District Rank - {} """
    res = res.format(re['examination'], re['year'], re['name'], re['indexNo'], re['marks'], re['districtRank'] )
    return res
  except:
    return error_mes

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
    rslt=alresult(x[1])
    bot.reply_to(message,rslt)
  except:
    bot.reply_to(message,er_mes)
  
@bot.message_handler(commands=['ol','OL','Ol'])
def send_ol(message):
   x = re.split("\s", message.text)
   try:
     rslt=olresult(x[1])
     bot.reply_to(message, rslt)
   except:
    bot.reply_to(message,er_mes)     

@bot.message_handler(commands=['g5','G5'])
def send_g5(message):
   x = re.split("\s", message.text)
   try:
     rslt=g5result(x[1])
     bot.reply_to(message, rslt)
   except:
    bot.reply_to(message,er_mes)

bot.polling()
