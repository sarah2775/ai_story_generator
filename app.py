import streamlit as st
from transformers import pipeline
generator = pipeline("text-generation", model="gpt2-large")
st.set_page_config(page_title="AI Story Generator")
st.title(" AI Story Generator")

prompt = st.text_input("Enter a story prompt:", "The world is captured by robots but one secretly sides with humans")
max_len = st.slider("Max story length (tokens)", 50, 300, 100)
temperature = st.slider("Creativity (temperature)", 0.1, 1.0, 0.7)

if st.button("Generate Story"):
    with st.spinner("Generating..."):
        result = generator(prompt, max_length=max_len, temperature=temperature)
        story = result[0]["generated_text"]
        st.subheader("Generated Story:")
        st.write(story)
        st.download_button("Download Story", story, file_name="story.txt")
