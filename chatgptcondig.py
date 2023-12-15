openai = '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'
def chatgpt(message):
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = message.text,
        temperature = 0.5,
        max_tokens = 1000,
        top_p = 1.0,
        frequency_penalty = 0.5,
        presence_penalty = 0.5
    )
    gpt_text = response['choices'][0]['text']
    bot.send_message(message.chat.id, gpt_text)