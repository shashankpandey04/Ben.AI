# Ben.AI - The Exceptional AI Personal Assistant

Ben.AI is an advanced, intelligent personal assistant designed to break the limitations of conventional personal assistants. Built using Python, MongoDB, and powered by AI models, Ben.AI can assist with a wide variety of tasks, learn from interactions, and adapt to your unique preferences.

---

## Features

- **Intelligent Task Management**: Manage tasks, schedules, reminders, and to-do lists seamlessly.
- **Smart Data Handling**: Securely store and retrieve data using MongoDB, ensuring information is easily accessible.
- **AI-Powered Conversations**: Engage in natural, context-aware dialogues with the assistant.
- **Customizable**: Tailor Ben.AI's functionalities and responses according to your needs.
- **Context-Aware**: Understands the context of requests, offering personalized and relevant responses.
- **Machine Learning Integration**: Continuously improves its performance through machine learning.

---

## Table of Contents

- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

To get started with **Ben.AI**, follow the instructions below to install it on your local machine.

### Prerequisites

- Python 3.6+
- MongoDB installed and running
- A working API key or model setup for AI processing (e.g., OpenAI, Hugging Face, etc.)

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/Ben.AI.git
cd Ben.AI
```

### Step 2: Install required dependencies
It's recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Now, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Set up MongoDB

Download and install MongoDB from MongoDB's official website.
Start MongoDB using the following command:

```bash
mongod
```

Create a new database in MongoDB (e.g., benai).

### Step 4: Configure API and Database

Create a .env file in the root directory of the project and add the necessary environment variables. For example:

```env
MONGO_URI = 
ENV = 
PASSWORD = 
API_KEY =
```

## Setup Instructions

1. Ensure MongoDB is running and accessible.
2. Install all dependencies and configure the environment variables as mentioned above.
3. Run the initial setup script to set up the database collections:

```bash
python setup.py
```

This will initialize the necessary collections in MongoDB, such as tasks, contacts, reminders, shedules, etc.

## Usage

Once set up, you can start interacting with Ben.AI using the following command:

```bash
python main.py
```

This will start the assistant, and you can begin typing in commands or tasks. Ben.AI will respond and assist with whatever you ask.

# Common Commands

- `Create a task for tomorrow at 3 PM`: Adds a new task.
- `Remind me to call John at 2 PM`: Adds a reminder.
- `What's my schedule for today?`: Retrieves a list of tasks and events for the day.
- `Tell me a joke`: Get a random joke from the assistant.
- `How is the weather tomorrow?`: Ben.AI can also integrate with weather APIs for external information.4

## Contributing

I welcome contributions! If you'd like to contribute to the development of Ben.AI, follow these steps:

1. Fork this repository.
2. Clone your fork:
```bash
git clone https://github.com/shashankpandey04/Ben.AI.git
```
3. Create a feature branch:
```bash
git checkout -b feature/your-feature
```
4. Make your changes and commit them:
```bash
git commit -m "Add a new feature"
```
5. Push to your fork:
```bash
git push origin feature/your-feature
```
6. git push origin feature/your-feature

_Note: Make sure to sign your commits with GPG Keys_

## License

Ben.AI is open source and available under the [MIT License](https://opensource.org/license/mit)

## Acknowledgements

- MongoDB for database management.
- Python for building the core functionality.
- YouTube Creators for teaching basics of AI & Personal Assistants.

## Roadmap

- [] Add voice recognition and processing.
- [] Integrate more APIs (weather, news, finance, etc.).
- [] Improve machine learning models for smarter task handling and recommendations.
- [] Create UI for Assistant.

