---

# Ollama Dashboard

Ollama Dashboard is a simple yet powerful graphical user interface (GUI) designed to control and manage the Ollama service for `Linux users`. This tool provides an intuitive interface for users to easily turn on, turn off, and open Ollama with just a few clicks.

## Features

- **Easy Control**: Toggle the Ollama service with the "Turn ON" and "Turn OFF" buttons.
- **Open Hollama**: Quickly launch Hollama directly from the dashboard using the "Open Hollama" button.

## Installation

To get started with Ollama Dashboard, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/ollama-dashboard.git
    cd ollama-dashboard
    ```

2. **Dependencies**:
    Ensure you have Python, [ollama](https://github.com/ollama/ollama), [hollama](https://github.com/fmaclen/hollama) installed on your system.

3. **Run the Application**:
    Execute the following command to start the Ollama Dashboard:
    ```sh
    chmod +x runollama.py
    ./runollama.py
    ```

## Usage

1. **Turn ON/OFF Ollama**:
    - Click the "Turn ON" button to start the Ollama service.
    - Click the "Turn OFF" button to stop the Ollama service.

2. **Open Hollama**:
    - Click the "Open Hollama" button to launch Hollama using the configured path.

## Customization

- **Button Styling**: You can customize the appearance of buttons by modifying the configuration in the `runollama.py` file.
- **Command Execution**: The application executes system commands using the `subprocess.run` functions. Ensure you have the necessary permissions to run these commands.

## Contributing

We welcome contributions from the community! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details.

---
