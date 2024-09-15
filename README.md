# Document Retrieval System

## Overview

This project implements a document retrieval system designed to generate context for large language models (LLMs). The system retrieves relevant documents based on user queries and provides context for LLM inference.

## Project Structure

- `app.py`: Main application code with API endpoints and background scraping logic.
- `database.db`: SQLite database file for storing documents and user information.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration for containerizing the application.
- `utils/`: Utility functions for database operations, encoding, and scraping.
- `models/`: Directory containing the pre-trained encoder model.

## Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   ```
