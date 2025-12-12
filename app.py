import streamlit as st
import google.generativeai as palm

# Configure the API with your API key
palm.configure(api_key="AIzaSyBs09D5WTHnJPtwKu92klKnDvHd9gQoBGg")

# Define the model to use
model_name = "models/chat-bison-001"

# Function to translate code from one language to another
def translate_code(code_snippet, target_language):
    prompt = f"Translate the following code to {target_language}:\n\n\n\n{code_snippet}"
    response = palm.chat(model=model_name, messages=[{"content": prompt}])
    return response.candidates[0]["content"]

# Streamlit application
def main():
    st.title("CodeXchange: AI-Powered Code Translation Tool")
    
    st.markdown("""
                <h2>Project Description</h2>
                <p>CodeXchange is an innovative web application designed to streamline code translation and facilitate seamless collaboration among developers.</p>
                """, unsafe_allow_html=True)
    
    st.markdown("""
                <h2>Scenario 1: Platform Transition</h2>
                <p>CodeXchange assists developers in transitioning applications from one platform to another. For instance, a team working on an application written in Python can easily translate the code to JavaScript for a web-based platform.</p>
                """, unsafe_allow_html=True)
    
    st.markdown("""
                <h2>Scenario 2: Multilingual Collaboration</h2>
                <p>In a collaborative project where team members use different programming languages, CodeXchange facilitates seamless integration by translating code snippets into the preferred languages of different developers.</p>
                """, unsafe_allow_html=True)
    
    st.markdown("""
                <h2>Scenario 3: Code Reusability Across Projects</h2>
                <p>CodeXchange promotes code reusability by enabling developers to translate existing code into different languages for new projects. For example, a Python script can be translated to R for data analysis in a new project.</p>
                """, unsafe_allow_html=True)

    # User input for code translation
    code_snippet = st.text_area("Enter the code snippet you want to translate:")
    target_language = st.text_input("Enter the target programming language:")

    if st.button("Translate"):
        if code_snippet and target_language:
            translated_code = translate_code(code_snippet, target_language)
            st.code(translated_code, language=target_language)
        else:
            st.error("Please provide both a code snippet and a target language.")

if __name__ == "__main__":
    main()

