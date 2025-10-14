# AI Study Buddy 🤖📚

A smart, interactive AI-powered study companion built with Streamlit and Google's Gemini AI. Get personalized help with any subject, from mathematics to history, with real-time explanations and study guidance.

![AI Study Buddy](https://img.shields.io/badge/AI-Study%20Buddy-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

## 🌟 Features

- **🤖 Smart AI Tutor**: Powered by Google's Gemini Flash 2.5 for intelligent responses
- **💬 Interactive Chat**: Real-time streaming responses with chat history
- **📚 Multi-Subject Support**: Mathematics, Science, History, Programming, Languages, and more
- **🎯 Personalized Learning**: Adjustable difficulty levels (Beginner to Advanced)
- **📝 Study Tools**: Practice questions, explanations, and study guides
- **📱 Responsive Design**: Works perfectly on desktop and mobile devices
- **🔒 Secure**: API keys managed through environment variables

## 🚀 Live Demo

Check out the live application: [AI Study Buddy on Render](https://ai-study-buddy-s89h.onrender.com)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-study-buddy.git
   cd ai-study-buddy
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501`

## 📦 Deployment

### Deploy on Render

1. **Fork this repository** to your GitHub account

2. **Create a new Web Service** on [Render](https://render.com)

3. **Connect your GitHub repository**

4. **Configure the service:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py`

5. **Add environment variable:**
   - Go to Environment tab
   - Add `GEMINI_API_KEY` with your Gemini API key

6. **Deploy!** 🎉

### Alternative: Deploy on Streamlit Cloud

1. **Push your code to GitHub**

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Create new app from repository**

4. **Set secrets in Streamlit Cloud dashboard:**
   ```toml
   GEMINI_API_KEY = "your_gemini_api_key_here"
   ```

## 🔧 Configuration

### Getting Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your environment variables

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

## 💡 Usage Examples

Try these prompts with your AI Study Buddy:

- **"Explain quantum physics like I'm 10 years old"**
- **"Create a study plan for learning Python in 2 weeks"**
- **"Give me 5 practice questions about World War II"**
- **"Help me understand calculus derivatives"**
- **"Break down the water cycle step by step"**
- **"Create a mind map for cellular respiration"**

## 🏗️ Project Structure

```
ai-study-buddy/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── .streamlit/           # Streamlit configuration
│   └── config.toml       # Streamlit settings
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## 🛡️ Security Notes

- 🔐 **Never commit API keys** to version control
- 🌐 Use environment variables for all sensitive data
- 📁 Add `.env` to your `.gitignore` file
- 🔒 Regularly rotate your API keys

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini AI](https://deepmind.google/technologies/gemini/) for the powerful AI capabilities
- [Streamlit](https://streamlit.io) for the amazing web framework
- [Render](https://render.com) for seamless deployment

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/shysai/ai-study-buddy/issues) page
2. Create a new issue with detailed description
3. Contact the maintainers

---

**Made with ❤️ for students everywhere**

*Happy Learning! 🎓*
