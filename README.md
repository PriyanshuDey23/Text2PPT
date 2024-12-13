# Text2PPT

# PowerPoint Presentation Generator 

This project allows users to generate professional PowerPoint presentations using Google’s Gemini AI model. The application leverages Streamlit for the user interface and Google Generative AI to create dynamic slide titles and content based on the provided topic, tone, language, and number of slides. The generated presentation is saved in PowerPoint format and can be downloaded directly from the app.

## Features

- **Dynamic Slide Titles**: Automatically generates slide titles based on the given topic.
- **Tailored Content**: Content is generated based on the selected tone (Formal, Informal, Persuasive) and language (English, Hindi, Spanish).
- **Customizable Slide Count**: Allows users to specify the number of slides they want in the presentation.
- **Professional Formatting**: The presentation is formatted with consistent fonts and layout to ensure readability and visual appeal.
- **Content Overflow Handling**: Long content is split into multiple slides automatically to ensure content fits within slide limits.
- **Downloadable PPT**: Once the presentation is generated, users can download the PowerPoint file directly from the app.

## Prerequisites

Before running the application, make sure you have the following installed:

- **Python 3.10**
- **Streamlit**
- **Google Generative AI SDK**
- **Python-PPTX**
- **dotenv** (for environment variable management)

### Install Dependencies

To install the required Python libraries, run:

```bash
pip install streamlit google-generativeai python-pptx python-dotenv
```

### Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/Text2PPT.git
   cd ChatAudio
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **API Key Setup**:  
   This project uses Google's Generative AI API. You need to set up your Google API key in your environment.

   - Create a `.env` file in the project root directory.
   - Add your API key as follows:

     ```txt
     GOOGLE_API_KEY=your_api_key_here
     ```

2. **Environment Variables**:  
   The `dotenv` library loads environment variables from the `.env` file to configure the API key for Google Generative AI. Make sure the key is set correctly to avoid any errors when interacting with the API.

## Usage

1. **Start the App**:  
   Run the following command to launch the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. **App Interface**:  
   - **Topic**: Enter the topic for the presentation.
   - **Language**: Choose the language for the presentation (English, Hindi, Spanish).
   - **Tone**: Select the tone for the presentation (Formal, Informal, Persuasive).
   - **Number of Slides**: Adjust the slider to specify the number of slides (1-10).

3. **Generate the Presentation**:  
   Once you’ve filled in the details, click **Generate Presentation**. The app will process the input and generate the slides accordingly.

4. **Download the PPT**:  
   After the presentation is generated, you can download the PowerPoint file directly by clicking the provided download link.

## Code Structure

- **`app.py`**: The main Streamlit application where the user interface is defined and interactions with the Generative AI model are managed.
- **`Text2PPT/prompt.py`**: Contains the prompt templates used for generating slide titles and content.
- **`generated_ppt/`**: Directory where the generated PowerPoint presentations are saved temporarily.

## Troubleshooting

- **API Key Error**: If you encounter an error regarding the API key, ensure that the `.env` file is correctly set up and the key is valid.
- **Content Overflow**: The content is split across multiple slides if it exceeds the maximum length, but if you experience issues with presentation formatting, you can adjust the `MAX_CONTENT_LENGTH` or modify the layout settings in the code.

## Contributing

We welcome contributions to improve this project. If you’d like to contribute, please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Generative AI**: For powering the content generation capabilities.
- **Streamlit**: For providing the platform to create interactive web applications.
- **Python-PPTX**: For handling PowerPoint file creation and manipulation.
