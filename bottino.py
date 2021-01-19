#Bot copiato dalla guida https://ludusrusso.cc/2017/04/27/implementiamo-un-bot-telegram-con-python/
#content_type can be:   text, audio, document, game, photo, sticker, video, voice, video_note, contact, location, 
#			venue, new_chat_member, left_chat_member, new_chat_title, new_chat_photo, 
#			delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, 
#			migrate_to_chat_id, migrate_from_chat_id, pinned_message, new_chat_members, invoice, successful_payment.


#Importo la libreria  telepot, easy
import telepot

#definisco la funzione principale del programma
#msg è l'argomento della funzione, ovvero il content del messaggio
def bottino(msg):

	#estraggo dal messaggio le 3 variabili: content, type e id
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	#content_type indica la tipologia del messaggio: img, vocale, ecc...
	#chat_type indica la tipologia della chat: gruppo, privata, segreta, ecc...
	#chat_id contiene l'identificativo univoco della chat, per le risposte nella medesima chat
	
	#se il contenuto del messaggio è di tipo testuale
	if content_type == 'text':
		#rispondo
		name = msg["from"]["first_name"]
		txt = msg['text']
		if '/start' in txt:
			bot.sendMessage(chat_id, 'Ciao amico, al momento posso riconoscere la tipologia di messaggio che mi hai mandato, dimmi pure')
		else:
			bot.sendMessage(chat_id, 'Non ho ben capito, questi sono i comandi che per adesso riesco ad utilizzare:\n - /start\n - /cavallo')
	#altrimenti
	else:
		if content_type == 'photo':
			bot.sendMessage(chat_id, 'bella fotina, posso ternela?')
		else:
			if content_type == 'video':
				bot.sendMessage(chat_id, 'potresti evitare i video gentilmente? Grazie.')
			else:
				if content_type == 'location':
					bot.sendMessage(chat_id, 'Mhh, roba piccante, sicuro?')
				else:
					bot.sendMessage(chat_id, 'Non capisco amo, che stai a di?')

	if content_type == 'text':
		name = msg["from"]["first_name"]
		txt = msg['text']
		if '/cavallo' in txt:
			bot.sendMessage(chat_id, 'Il cavallo nitrisce')
#Inserisco il token generato da botfather
TOKEN = 'xxx'
#Creo il bot usando la var TOKEN
bot = telepot.Bot(TOKEN)
#Funzione che intercetta il messaggio
bot.message_loop(bottino)


print ('Listening ...')


import time

while 1:

	time.sleep(10)
