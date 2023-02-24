"""
Script that generates email templates
"""
from datetime import date
recipients = ["Esha", "Alishay", "Filipe"]
awards = ["First place", "Second place", "Third place"]

details = {
    
}

for recipient, award in zip(recipients, awards):
    template = f"""Dear {recipient},

Body of email.
On {date.today()}, you won {award}!
"""
    with open(f"{recipient}.txt", mode="w", encoding="utf-8") as f:
        f.write(template)
