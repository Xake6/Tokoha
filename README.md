🤖 Discord Price Bot

📌 Overview:

This project is a Discord bot developed in Python that automates the monitoring of card prices on Cardmarket using web scraping.

The main goal is to notify users when a target price is reached, helping automate a process that is normally done manually and repeatedly.

Although initially built to solve a personal need, the project is designed with the idea that it could be useful for other users with similar requirements.

⚙️ Features:

-🆕 Detection of new card listings from vendors (new singles added to inventory)
-🔎 Automated search of cards on Cardmarket
-📉 Price tracking and monitoring
-🔔 Discord private message notifications
-⏱ Configurable checking intervals
-🎯 Price target alerts


🧱 Current Implementation:

The project is currently implemented in a single Python file, where all logic is organized into clearly separated sections:

Discord bot handling
Web scraping logic (Selenium)
Price checking and comparison
Notification system

This approach was chosen for simplicity during development and to iterate quickly on functionality.



🚀 Future Improvements:

As the project evolves, the goal is to improve its structure and scalability. Planned improvements include:

Refactoring into a modular architecture (separating bot, scraper, and services)
Adding better configuration management
Improving error handling and logging system
Potential migration to API-based solutions if available
Adding persistence (database for price history)
Deploying in a cloud environment or Docker container


🧠 Motivation:

This project was created as a practical tool to automate a repetitive personal task: tracking card prices manually.

Beyond its immediate use, it also serves as a learning project to improve skills in:

Python development
Web scraping
Automation
API integration concepts
Real-world problem solving

The long-term goal is to continue improving it so it becomes a more robust and reusable tool.


🛠 Tech Stack:

Python 3
Selenium
Discord API
Web scraping techniques
👤 Author

Xavier Rodríguez Zaragoza
GitHub: [https://github.com/Xake6](https://github.com/Xake6)

📈 Note

This project is continuously evolving. While the current version prioritizes functionality over architecture, future iterations aim to improve maintainability, scalability, and code organization.
