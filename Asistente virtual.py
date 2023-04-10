import openai
import pyttsx3

#Establecer la API key de OpenAI#
openai.api_key = "YOUR API KEY"

#Iniciar el motor de texto a voz#
engine = pyttsx3.init()

#Función para obtener la respuesta del modelo y reproducirlo en voz#
def get_model_response(prompt):
    response = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=20,
    )
    return response.choices[0].text.strip()

def speak(text):
    #Configurar el motor de texto a voz#
    engine.setProperty('rate',150) #Esta es la velocidad del habla por minuto#
    engine.setProperty('volume',1) #Configurar el volumen del habla de 0 a 1

    #Reproducir el texto a voz#
    engine.say(text)
    engine.runAndWait()

#Función principal en el asistente virtual#
def main():
    speak("Hola, soy tu asistente virtual creado por Niki. ¿En qué puedo ayudarte?")

    while True:
        #Obtener la entrada del usuario#
        entrada_usuario =input("Tú: ")

        #Si el usuario escribe "SALIR", termina el programa#
        if entrada_usuario.lower()=="salir":
            speak("De acuerdo, Hasta luego. ¡Que tengas un buen día!")
            break

        #Obtener la respuesta del modelo y la reproduce en voz#
        respuesta = get_model_response(entrada_usuario)
        speak(respuesta)

if __name__ == "__main__":
    main()
