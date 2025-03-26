#TCO3V7DGN3 Confirmed. Ksh3,000 sent to FRANCIS KINUNGI on 24/3/25 at 8.02AM
from strings import message


def extract_amount (mpesa_message):
    index_ksh = mpesa_message.index('Ksh')
    index_sent = mpesa_message.index('sent')
    amount = mpesa_message[index_ksh : index_sent]
    amount = amount.replace("Ksh" , "")
    amount = amount.replace("," , "")
    amount = amount.strip()


    print(amount)

message_1 = "TCO3V7DGN3 Confirmed. Ksh3,000 sent to FRANCIS Simeon on 24/3/25 at 8.02AM"
extract_amount(message_1)

def extract_date (mpesa_message):
    index_on = mpesa_message.index(' on ')
    index_at = mpesa_message.index('at')
    date = mpesa_message[index_on : index_at]
    date = date.replace(" on "  , "")
    date = date.split(" ")


    print(date)

message_1 = "TCO3V7DGN3 Confirmed. Ksh3,000 sent to FRANCIS Simeon on 24/3/25 at 8.02AM"

extract_date(message_1)
