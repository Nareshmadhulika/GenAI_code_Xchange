# CodeXchange: AI-Powered Code Translation Tool

## Overview

CodeXchange is an innovative web application built with Streamlit that leverages Google's Generative AI to facilitate seamless code translation between different programming languages. It empowers developers to quickly adapt code for various platforms, enhance collaboration in multilingual teams, and promote code reusability across projects.

## Features

### Core Functionality
- **AI-Powered Translation**: Utilizes Google's Palm API to translate code snippets from one programming language to another.
- **User-Friendly Interface**: Simple web-based UI built with Streamlit for easy interaction.
- **Real-Time Results**: Instant translation with syntax highlighting for the target language.

### Use Cases
1. **Platform Transition**: Easily migrate applications between platforms (e.g., Python to JavaScript for web deployment).
2. **Multilingual Collaboration**: Enable team members using different programming languages to work together seamlessly.
3. **Code Reusability**: Adapt existing code for new projects by translating to different languages (e.g., Python to R for data analysis).

## Installation

### Prerequisites
- Python 3.7 or higher
- A Google Cloud API key with access to Generative AI (Palm API)

### Setup Steps
1. Clone or download this repository.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Obtain a Google Cloud API key from the [Google Cloud Console](https://console.cloud.google.com/).
4. Replace the API key in `app.py` with your own:
   ```python
   palm.configure(api_key="YOUR_API_KEY_HERE")
   ```

## Usage

1. Run the application:
   ```
   streamlit run app.py
   ```
2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).
3. Enter your code snippet in the text area.
4. Specify the target programming language.
5. Click "Translate" to get the translated code.

## Dependencies

- `streamlit==1.10.0`: Web app framework
- `google-generativeai`: Google's Generative AI library
- `altair==4.0`: Data visualization (used by Streamlit)

## Security Note

The current implementation has the API key hardcoded in the source code. For production use, consider using environment variables or secure key management systems to protect your API credentials.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is open-source. Please check the license file for details.
