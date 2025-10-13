'''
import streamlit as st
import google.generativeai as genai
import time
from typing import Generator

# Configure the page
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="centered"
)

# Initialize Gemini with your API key
API_KEY = "AIzaSyCrl_moHUUPBesjSH0lLAicxhjvd6DitSM"

def list_available_models():
    """List all available models"""
    try:
        genai.configure(api_key=API_KEY)
        models = genai.list_models()
        available_models = []
        for model in models:
            supported_methods = []
            if 'generateContent' in model.supported_generation_methods:
                supported_methods.append('generateContent')
            if supported_methods:
                available_models.append({
                    'name': model.name,
                    'description': model.description,
                    'methods': supported_methods
                })
        return available_models
    except Exception as e:
        st.error(f"Error listing models: {e}")
        return []

def initialize_gemini():
    """Initialize the Gemini model"""
    try:
        genai.configure(api_key=API_KEY)
        
        # Try the most common model names for Gemini Flash 2.5
        model_names = [
            "gemini-2.0-flash-exp",  # Most likely candidate
            "gemini-2.0-flash",      # Alternative name
            "gemini-1.5-flash",      # Original try
            "models/gemini-2.0-flash-exp",  # Full path
            "gemini-2.5-flash-exp",  # Another possibility
        ]
        
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                # Test with a simple prompt to verify it works
                response = model.generate_content("Hello", stream=False)
                st.sidebar.success(f"✅ Using model: {model_name}")
                return model
            except Exception:
                continue
        
        # If none of the above work, list available models
        st.sidebar.error("❌ Could not auto-detect model. Check available models below.")
        return None
        
    except Exception as e:
        st.error(f"Error initializing Gemini: {e}")
        return None

def main():
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .study-tips {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .ai-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Study Buddy</h1>', unsafe_allow_html=True)
    st.markdown("### Your personal AI tutor for any subject!")
    
    # Initialize the model
    if "model" not in st.session_state:
        st.session_state.model = initialize_gemini()
    
    # Study tips section
    with st.expander("💡 Study Tips & Prompt Ideas"):
        st.markdown("""
        **Try asking me to:**
        - Explain complex concepts in simple terms
        - Create study guides or summaries
        - Generate practice questions
        - Help with homework problems
        - Break down difficult topics
        - Provide real-world examples
        - Create mind maps or outlines
        
        **Example prompts:**
        - "Explain quantum physics like I'm 10 years old"
        - "Create a study plan for learning Python in 2 weeks"
        - "Give me 5 practice questions about World War II"
        - "Help me understand calculus derivatives"
        """)
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask your study question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display AI response
        with st.chat_message("assistant"):
            if st.session_state.model:
                try:
                    # Create a placeholder for streaming response
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    # Generate response with streaming
                    response = st.session_state.model.generate_content(
                        prompt,
                        stream=True
                    )
                    
                    # Stream the response
                    for chunk in response:
                        if chunk.text:
                            full_response += chunk.text
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                    
                    # Add AI response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                    
                except Exception as e:
                    st.error(f"Error generating response: {e}")
                    st.info("Trying alternative approach...")
                    
                    # Fallback: try without streaming
                    try:
                        response = st.session_state.model.generate_content(prompt, stream=False)
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    except Exception as e2:
                        st.error(f"Fallback also failed: {e2}")
            else:
                st.error("Gemini model not initialized. Please check your API key.")
    
    # Sidebar with additional features
    with st.sidebar:
        st.header("Study Tools")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()
        
        # Check available models button
        if st.button("🔍 Check Available Models"):
            available_models = list_available_models()
            if available_models:
                st.write("### Available Models:")
                for model in available_models:
                    st.write(f"**{model['name']}**")
                    st.write(f"Description: {model['description']}")
                    st.write(f"Methods: {', '.join(model['methods'])}")
                    st.write("---")
            else:
                st.error("No models found or error fetching models")
        
        # Study focus selector
        study_subject = st.selectbox(
            "Choose your study subject:",
            ["General", "Mathematics", "Science", "History", "Programming", "Languages", "Other"]
        )
        
        # Difficulty level
        difficulty = st.select_slider(
            "Explanation Level:",
            options=["Beginner", "Intermediate", "Advanced"]
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This AI Study Buddy uses Google's Gemini to help you learn and understand various subjects.
        
        **Features:**
        - Interactive Q&A
        - Step-by-step explanations
        - Study guidance
        - Practice questions
        """)

if __name__ == "__main__":
    main()
    '''


import streamlit as st
import google.generativeai as genai
from typing import Generator
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the page
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="centered"
)

def initialize_gemini():
    """Initialize the Gemini model"""
    try:
        # Get API key from environment variable
        API_KEY = os.getenv("GEMINI_API_KEY")
        
        if not API_KEY:
            st.error("❌ API key not found. Please check your .env file")
            return None
            
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        return model
    except Exception as e:
        st.error(f"Error initializing Gemini: {e}")
        return None

def main():
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .study-tips {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Study Buddy</h1>', unsafe_allow_html=True)
    st.markdown("### Your personal AI tutor for any subject!")
    
    # Initialize the model
    if "model" not in st.session_state:
        with st.spinner("Initializing AI Study Buddy..."):
            st.session_state.model = initialize_gemini()
        if st.session_state.model:
            st.sidebar.success("✅ AI Study Buddy is ready!")
    
    # Study tips section
    with st.expander("💡 Study Tips & Prompt Ideas", expanded=True):
        st.markdown("""
        **Try asking me to:**
        - 📚 Explain complex concepts in simple terms
        - 📝 Create study guides or summaries
        - ❓ Generate practice questions
        - 🏠 Help with homework problems
        - 🔍 Break down difficult topics
        - 🌍 Provide real-world examples
        - 🗺️ Create mind maps or outlines
        
        **Example prompts:**
        - "Explain quantum physics like I'm 10 years old"
        - "Create a study plan for learning Python in 2 weeks"
        - "Give me 5 practice questions about World War II"
        - "Help me understand calculus derivatives"
        - "Break down the water cycle step by step"
        """)
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm your AI Study Buddy. I'm here to help you learn and understand any subject. What would you like to study today?"}
        ]
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask your study question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display AI response
        with st.chat_message("assistant"):
            if st.session_state.model:
                try:
                    # Create a placeholder for streaming response
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    # Generate response with streaming
                    response = st.session_state.model.generate_content(
                        prompt,
                        stream=True
                    )
                    
                    # Stream the response
                    for chunk in response:
                        if chunk.text:
                            full_response += chunk.text
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                    
                    # Add AI response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                    
                except Exception as e:
                    st.error(f"Error generating response: {e}")
                    st.info("Please try again or rephrase your question.")
            else:
                st.error("AI Study Buddy is not initialized. Please refresh the page.")
    
    # Sidebar with additional features
    with st.sidebar:
        st.header("🎯 Study Tools")
        
        # Study focus selector
        study_subject = st.selectbox(
            "Choose your study subject:",
            ["General", "Mathematics", "Science", "History", "Programming", "Languages", "Business", "Arts", "Other"]
        )
        
        # Difficulty level
        difficulty = st.select_slider(
            "Explanation Level:",
            options=["Beginner", "Intermediate", "Advanced"],
            value="Intermediate"
        )
        
        # Study session context
        st.subheader("Study Session Context")
        study_topic = st.text_input("Current study topic (optional):", placeholder="e.g., Calculus, World History, Python")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi! I'm your AI Study Buddy. What would you like to learn about now?"}
            ]
            st.rerun()
        
        # Study session stats
        st.subheader("Session Stats")
        st.write(f"Messages exchanged: {len(st.session_state.messages)}")
        
        st.markdown("---")
        st.markdown("### 📖 About")
        st.markdown("""
        **AI Study Buddy** uses Google's Gemini to provide:
        - Interactive Q&A sessions
        - Step-by-step explanations
        - Personalized study guidance
        - Practice questions and exercises
        - Real-world examples and applications
        
        *Perfect for students of all levels!*
        """)

if __name__ == "__main__":
    main()