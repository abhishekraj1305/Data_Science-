letter = '''Dear <|NAME|>,
            You are selected for the position of <|POSITION|> at our company. We were impressed with your skills and experience, \n\t\tand we believe you will be a valuable addition to our team.
            Please let us know if you are interested in accepting this offer. We look forward to hearing from you soon.
<|dATE|>,

Best regards,
HR Team'''


name = input("Enter your name: ")
position = input("Enter the position you are applying for: ")
date = input("Enter the date of the offer: ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|POSITION|>", position)
letter = letter.replace("<|dATE|>", date)
print(letter)

