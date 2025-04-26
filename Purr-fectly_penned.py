# Purrfectly Penned - Card Generator

def get_user_inputs():
    occasion = input("🐾 What's the occasion? (Birthday, Thinking of You, etc.): ")
    relationship = input("🐾 What's your relationship with them? (Friend, Family, Partner, N/A): ")
    personal_details = input("🐾 One or two unique things or memories about them? (Optional): ")
    tone = input("🐾 What tone do you want? (Warm, Funny, Sweet, Uplifting, Sarcastic, Nostalgic): ")
    return occasion, relationship, personal_details, tone

def craft_message(occasion, relationship, personal_details, tone):
    message = f"Sending you a purrfect hello on this {occasion.lower()} — "
    if relationship != "N/A":
        message += f"thinking of my amazing {relationship.lower()}, "
    if personal_details:
        message += f"remembering {personal_details}, "
    message += "and hoping your day feels as cozy as a cat curled in a sunny window. 🐾"
    
    if tone.lower() == "funny":
        message += " P.S. If cats ruled the world, you'd definitely be getting extra treats today!"
    
    return message

def generate_image_prompt(occasion, tone, personal_details):
    prompt = f"A {tone.lower()} digital illustration of a cat for a {occasion.lower()} card."
    if personal_details:
        prompt += f" Include hints of: {personal_details.lower()}."
    prompt += " Soft cozy colors, no text, whimsical and heartwarming."
    return prompt

def main():
    print("🐾 Welcome to Purrfectly Penned! 🐾")
    occasion, relationship, personal_details, tone = get_user_inputs()
    
    card_message = craft_message(occasion, relationship, personal_details, tone)
    print("\n✨ Here’s your card message:")
    print(f'"{card_message}"')
    
    image_prompt = generate_image_prompt(occasion, tone, personal_details)
    print("\n🎨 Suggested image generation prompt:")
    print(f'"{image_prompt}"')

if __name__ == "__main__":
    main()

