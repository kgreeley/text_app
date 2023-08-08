import assemblyai as aai

# Your API token is already set here
aai.settings.api_key = input("You should tell me your API Key otherwise I will take a nap. ")

# Define the Transcriber and create an object
transcriber = aai.Transcriber()

transcript_group = transcriber.transcribe_group(
    [
        input("Donde esta tu archivo? ")
    ],
)

# User decided whether to receive a summary or action items from the call
user_input = input("What doth the user decide? [Summarize or Action Items] ")

if user_input == "Summarize":
    params = {
          "context": input("What is the context? "),
          "answer_format": input("What answer format do you want? ")
        }
    result = transcript_group.lemur.summarize(**params)
    print(result.response)
else:
    params = {
    "context": input()
        }
    #run LeMUR with Action Items
    result = transcript_group.lemur.action_items(**params)
    print(result.response)