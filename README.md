# Unofficial ChatGPT-4o API Wrapper

A Python wrapper for the unofficial ChatGPT-4o API, providing a simple interface for image generation.

## Features

- Simple and intuitive API
- Real-time status updates
- Error handling
- Progress tracking
- Session management

## Installation

```bash
pip install chatgpt-4o-unofficial-api
```

## Quick Start

```python
from chatgpt_4o import ChatGPT4o

# Initialize the client
client = ChatGPT4o()

# Generate an image
response = client.generate_image(
    prompt="A magical forest with floating lanterns in Ghibli style",
    style="default",
    size="1024x1024"
)

# Access the generated image URL
image_url = response['data']['url']
```

## Usage

The `generate_image` method accepts the following parameters:

- `prompt` (str): The text description of the image you want to generate
- `style` (str, optional): The style of the image. Defaults to "default"
- `size` (str, optional): The size of the generated image. Defaults to "1024x1024"
- `quality` (str, optional): The quality of the generated image. Defaults to "standard"
- `model` (str, optional): The model to use for generation. Defaults to "default"

## Example

```python
from chatgpt_4o import ChatGPT4o

def main():
    client = ChatGPT4o()

    response = client.generate_image(
        prompt="A cozy house in the clouds with a magical cat bus, Ghibli style",
        style="default",
        size="1024x1024"
    )

    print(f"Generated image URL: {response['data']['url']}")

if __name__ == "__main__":
    main()
```

## Error Handling

The wrapper includes built-in error handling for common issues:

```python
from chatgpt_4o import ChatGPT4o, ChatGPT4oError

try:
    client = ChatGPT4o()
    response = client.generate_image(prompt="Your prompt here")
except ChatGPT4oError as e:
    print(f"Error: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Follow Me

Follow me on X (Twitter) for updates and more: [@triplethata](https://x.com/triplethata)
