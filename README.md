# Python Command Git Action

A flexible GitHub Action to execute Python commands or scripts within your CI/CD workflows. This action allows you to run Python logic, process files, or interact with the GitHub environment easily.

## 📂 File Structure

This repository follows a standard Docker-containerized GitHub Action structure:

```text
.
├── .github/
│   └── workflows/
│       └── python-app.yml       # CI/CD workflow configuration
├── tasks/
│   ├── base/
│   │   ├── call_api_command.py  # Logic for handling API requests
│   │   └── command.py           # Base command structure/interface
│   └── main.py                  # Entry point script
└── README.md                    # Project documentation
