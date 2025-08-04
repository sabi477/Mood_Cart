import streamlit as st
import json
import os
import streamlit.components.v1 as components


st.set_page_config(page_title="Bugünki Mood Kartın", page_icon="🎴")
st.title("Bugünki Mood Kartın 🎴")
st.subheader("Her gün için bir mood kartı! Moduna uygun yeni bir şarkı keşfet!")

user_input = st.text_input("Bugün için mood kartını seç (örneğin: 'mutlu', 'üzgün', 'heyecanlı'):")

def load_mood_cards():
    with open("moods.json", "r", encoding="utf-8") as file:
        return json.load(file)

mood_cards = load_mood_cards()

def find_mood_card(user_text):
    user_text = user_text.lower()
    for mood in mood_cards:
        if any(keyword in user_text for keyword in mood["keywords"]):
            return mood
    return None

if user_input:
    mood_card = find_mood_card(user_input)
    if mood_card:
        st.markdown(f"### {mood_card['mood']}")
        image_path = mood_card["image"]
        if os.path.exists(image_path):
            st.image(image_path, width=300)
        st.write(mood_card["description"])
      
        spotify_embed_url = mood_card['song']['url'].replace("open.spotify.com/track", "open.spotify.com/embed/track") 
        components.iframe(spotify_embed_url, height=80)
        
    else:
        st.warning("Sana uygun mood kartını bulamadım. Lütfen tekrar dene.")