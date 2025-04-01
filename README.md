# ChatGPT 4o Unofficial API Wrapper

A Python wrapper for the ChatGPT 4o API, providing easy access to the latest image generation capabilities.

## Quick Start

Just run the example script:

```bash
python3 example.py
```

This will demonstrate the image generation capabilities with a beautiful example.

## Features

- Simple and intuitive API interface
- Support for various image generation styles
- Real-time progress display
- Beautiful example showcasing the capabilities

## Example Usage

```python
from chatgpt_4o import ChatGPT4o

# Initialize the client
client = ChatGPT4o()

# Generate an image
response = client.generate_image(
    prompt="A magical forest with floating lanterns",
    style="default",
    size="1024x1024"
)

# The response contains the generated image URL
print(f"Generated image URL: {response['data']['url']}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
