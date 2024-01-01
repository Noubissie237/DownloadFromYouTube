from pytube import YouTube

url = "https://www.youtube.com/watch?v=TB5Zq0I79mg"

objet_youtube = YouTube(url)

def getNumber(first : int, last : int, message : str) -> int :

    number = checkNaN(input(message))
    
    while number < first or number > last:

        number = checkNaN(input(f"Veuillez entrer un nombre compris entre {first} et {last} : "))

    return number
            

def checkNaN(value : any) -> int:

    try:

        value = int(value)

        return value
    
    except:

        return -88
    

print("Souhaitez vous telecharger << {} >> sous le format : \n\t1. VIDEO  \n\t2. AUDIO?".format(objet_youtube.title))

format = getNumber(1, 2, "\nFormat : ")

if format == 1:
    
    print('Quelle qualite video souhaitez vous telecharger ? \n')

    print("\t1. 144p\n\t2. 360p\n\t3. 720p\n\t4. 1080p")

    quality = getNumber(1, 4, "\nQualite : ")

    if quality == 1:

        tag = 17

    elif quality == 2:

        tag = 18

    elif quality == 3:

        tag = 22

    else:

        tag = 137

else : 
    
    tag = 140
    

if objet_youtube.age_restricted == True:
    
    try:

        stream = objet_youtube.streams.get_by_itag(tag)

        print('Telechargement en cours ...')

        stream.download()

        print('Telechargement effectue avec succes')

    except:

        print("Un probleme est survenu lors du telechargement")

else:

    try:

        objet_youtube.streams.filter(adaptive=True, file_extension="mp4").first().download()

        print('Telechargement effectue avec succes')
        
    except:
            
        print("\nCe contenu youtube poccede certaines restrictions qui empechent son telechargement de cette façon !")

        print("Mais vous pouvez vous rendre sur le site https://savefrom.net et entrer l'url de ce contenu youtube pour le telecharger")
    
