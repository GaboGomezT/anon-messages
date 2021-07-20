from infrastructure.mongo import db
import random


def send_signal(email: str, title: str, message: str):
    result = db.signals.insert_one({
        "email": email,
        "title": title,
        "message": message,
        "recieved": False
    })

    # Add that id to the users sent signal list
    user = db.users.find_one({"email": email})
    sent_signals = user.get("sent_signals")
    sent_signals.append(result.inserted_id)
    db.users.update_one(
        {"email": email},
        {
            "$set": { "sent_signals": sent_signals}
        },
    )


def look_for_signal(email: str) -> dict:
    # First get all signals that are not yours and that have not been read
    results = list(db.signals.find({"email":{"$ne": email}, "recieved": False}))
    if len(results) == 0:
        return None
    
    # Then choose one randomly
    signal = random.choice(results)

    # Update that document so that no one else can read it
    signal_id = signal.get('_id')
    db.signals.update_one(
        {"_id": signal_id},
        {
            "$set": { "recieved": True}
        },
    )

    # Add that id to the users recieved signal list
    user = db.users.find({"email": email}).next()
    recieved_signals = user.get("recieved_signals")
    recieved_signals.append(signal_id)
    db.users.update_one(
        {"email": email},
        {
            "$set": { "recieved_signals": recieved_signals}
        },
    )

    return signal