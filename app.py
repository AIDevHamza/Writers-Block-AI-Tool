import streamlit as st
from langchain.llms import OpenAI  # Import LangChain's LLM module


def count_words(text):
    # Split the text into words and count them
    words = text.split()
    return len(words)




# Sidebar for taking user API key
st.sidebar.header("API Key")
api_key = st.sidebar.text_input("Enter your API key", type="password")

# Add a heading to the sidebar
st.sidebar.header("About Me")

# Wrote a short introduction of my self
st.sidebar.write(
    """Hamza Athar is a emerging figure in the world of artificial intelligence. As the co-founder of Wepronex and the founder of ToLearnAI, he aims to revolutionize the world of AI. Hamza is not only an enthusiast of artificial intelligence but also an adept AI developer with a passion for creating applications using large language models (LLMs). His expertise lies in prompt engineering, where he demonstrates an exceptional ability to craft precise and effective prompts for AI systems. 
    """
)

# Added links to your social profiles
st.sidebar.write(
    "[LinkedIn](https://www.linkedin.com/in/aidevhamza/) | [Twitter](https://twitter.com/aidevhamza) | [GitHub](https://github.com/aidevhamza)"
)

# Adding an if statement so the UI will not be rendered unless an API key is entered
if api_key:
    # Initialize LangChain's LLM module
    llm = OpenAI(
        openai_api_key=api_key,
        max_tokens=1000,
    )


    col1, col2 = st.columns(2)


    # Set the title of your app
    st.title("📝✨ AI Writing Assistant")

    # Input field for the user's text
    user_input = st.text_area("Enter your text to continue writing")
    
    #Input field for Custom Instructions
    instructions = st.text_input("Enter your custom instructions (Optional)")

    # Slider for specifying the length of generated text (up to 500 words)
    text_length = st.slider("Desired Text Length (Words)", min_value=1, max_value=500, value=100)
    
    # List of writing tones with emojis
    writing_tones = {
        "Neutral 😐": "neutral",
        "Formal 🎩": "formal",
        "Casual 😎": "casual",
        "Creative 🎨": "creative",
        "Professional 📊": "professional",
        "Friendly 😃": "friendly",
    }

    # Dropdown menu for selecting the writing tone
    selected_tone = st.selectbox("Select Writing Tone", list(writing_tones.keys()))
    
    # Get the selected writing tone from the dropdown menu
    tone_option = writing_tones[selected_tone]

    
    # Inside the Streamlit app logic
    if st.button("Continue Writing"):
        # Validate that user input is not empty
        if not user_input:
            st.warning("Please enter some text to continue writing.")
        else:
            # Construct a prompt for text continuation based on user input
            prompt = f"You are a Expert writer with a decade of experience, Over the years you proved yourself by writing continuation for various pieces of text. Your clients value your ability to seamlessly extend the narrative without losing the context. Today, you have been tasked with continuing the following passage in tone:{tone_option} while following these instructions if any:{instructions} using no more than {text_length} words: {user_input}"

            # Call the LangChain LLM to generate the continuation
            generated_text = llm.predict(prompt)
            
            # Count the words in the generated text
            word_count = count_words(generated_text)
            
            #Warning of inaccurate word counts
            st.warning("These AI Models often make mistakes in word counts, thats why I implemented a word counter to verify results")

            # Display the generated text
            st.subheader(f"Generated Text (Word Count: {word_count})")
            st.write(generated_text)
else:
    st.warning("Please enter your API Key")
