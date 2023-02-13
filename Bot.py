import telebot
bot = telebot.TeleBot("5789503010:AAFoNzeSH58unG0CbinReHzrN2GepVBC7JM")

@bot.message_handler(commands=['/start'])
def calculator(message):
    # Get the text from the message
    text = message.text
    # Split the text into an array of operands and operators
    tokens = text.split()
    # Check if there are enough tokens to make a calculation
    if len(tokens) < 3:
        bot.send_message(message.chat.id, "Not enough operands and operators!")
    else:
        # Initialize the result
        result = 0
        # Get the first operand and assign it to the result
        result = float(tokens[1])
        # Iterate over the rest of the tokens
        for i in range(2, len(tokens), 2):
            # Get the operator and the operand
            operator = tokens[i]
            operand = float(tokens[i+1])
            # Do the calculation
            if operator == "+":
                result = result + operand
            elif operator == "-":
                result = result - operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                result = result / operand
            else:
                bot.send_message(message.chat.id, "Invalid operator!")
                return
        # Send the result back to the user
        bot.send_message(message.chat.id, str(result))

bot.polling()
