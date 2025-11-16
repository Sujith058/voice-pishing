from gtts import gTTS
import os

def generate_dataset():
    os.makedirs("dataset/phishing", exist_ok=True)
    os.makedirs("dataset/genuine", exist_ok=True)

    # --- 20 realistic phishing samples ---
    phishing_texts = [
        "This is your bank calling. Please verify your account by sharing your one time password.",
        "Your ATM card has been blocked. Kindly provide your PIN number to reactivate it.",
        "Congratulations, you won a free iPhone. Please provide your card details for shipping verification.",
        "Your Amazon account has been locked. Press one to unlock your account immediately.",
        "This is a call from the IRS. You have pending taxes that need to be paid right now.",
        "Your computer has been hacked. Please call this number to fix the issue immediately.",
        "We detected suspicious activity on your PayPal account. Confirm your credentials to protect it.",
        "Your social security number has been compromised. Press one to speak to an agent.",
        "This is the credit card department. You are eligible for a lower interest rate. Share your card number.",
        "Your Netflix subscription is about to expire. Please update your payment information.",
        "You have unpaid electricity bills. Immediate payment required to avoid disconnection.",
        "You have won a lottery. Kindly pay the registration fee to claim your reward.",
        "Your bank account will be frozen. Please verify your details immediately.",
        "We detected fraud on your credit card. Confirm your card number for safety verification.",
        "This is Microsoft Support. Your computer is infected with a virus. Pay to renew your protection.",
        "You are entitled to a refund. Please give your bank account details.",
        "We noticed unauthorized login attempts. Please provide your password to secure your account.",
        "This is a legal call from the enforcement department. Immediate response required.",
        "You are selected for a government grant. Send your ID proof now.",
        "Your phone number was used in criminal activity. Pay a fine to avoid arrest."
    ]

    # --- 20 genuine customer-care samples ---
    genuine_texts = [
        "Hello, thank you for calling customer support. How may I assist you today?",
        "Your appointment is confirmed for tomorrow at 2 PM.",
        "We received your payment of twenty dollars. Thank you for choosing our service.",
        "Your package has been shipped and will arrive by Friday.",
        "Please stay on the line while I connect you to a representative.",
        "This is a reminder about your doctor’s appointment scheduled for next week.",
        "Your order number one zero two has been successfully processed.",
        "Welcome to the helpdesk. Please state your issue clearly.",
        "We appreciate your patience. An agent will be with you shortly.",
        "Your service request has been logged and is under process.",
        "Your account has been verified successfully. Have a great day.",
        "Thank you for calling billing support. How can I help you today?",
        "This is an automated reminder for your upcoming interview.",
        "Your ticket has been resolved. Please confirm if you are satisfied.",
        "We’re happy to assist you. Thank you for contacting us.",
        "Please rate our service once your issue is resolved.",
        "This call is being recorded for quality assurance purposes.",
        "Your feedback has been recorded successfully.",
        "We have extended your subscription by one month as requested.",
        "Thank you for being a valued customer. Have a wonderful day ahead."
    ]

    def save_tts(texts, folder, prefix):
        for i, text in enumerate(texts):
            tts = gTTS(text=text, lang='en', slow=False)
            filename = f"{prefix}_{i+1}.wav"
            tts.save(os.path.join(folder, filename))

    print("🔊 Generating phishing samples...")
    save_tts(phishing_texts, "dataset/phishing", "phishing")

    print("🎧 Generating genuine samples...")
    save_tts(genuine_texts, "dataset/genuine", "genuine")

    print("✅ Dataset generated successfully with 40 audio files!")

if __name__ == "__main__":
    generate_dataset()
