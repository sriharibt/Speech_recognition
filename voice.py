import speech_recognition as sr
import os
import webbrowser
r =sr.Recognizer()

#add your own commands
def execute_command(text):
	parameter = ""
	text = text.lower()
	command = text.split(' ', 1)[0]
	if ' ' in text:
		parameter = text.split(' ', 1)[1]
	if command == "open":
		if parameter != "":
			webbrowser.open_new_tab("http://" + parameter.replace(" ", "") + ".com")
		else:
			webbrowser.open_new_tab("http://google.co.in")
			# try "youtube Roar"
	elif command == "youtube":
		webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + parameter.replace(" ", "+"))
	elif 'play' in command:
		os.system("rhythmbox-client --play")

        
    
        



while True:
	#get the input from the microphone
	with sr.Microphone() as voice:
		print("I'm Listnening")
		audio = r.listen(voice)
	try:
		text = r.recognize_google(audio)
		print("You said : " + text )
		text =text.lower()
		
		#user defined function 
		execute_command(text)
		if text == 'stop':
			break
	except sr.UnknownValueError:
		print("Didn't catch that!")
	except sr.RequestError as e:
		print("Error; {0}".format(e))
	except:
		pass		
