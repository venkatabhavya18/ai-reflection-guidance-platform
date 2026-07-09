# API Design

## 1. Introduction
The AI Reflection & Guidance PLatform follows a RESTful API architecture. The backend exposes secure endpoints that allow the frontend to communicate with authentication services, AI modules, user data, journals and analytics.
The API are designed to be modular, scalable and easily extensible for future AI features.

## 2. API Objectives
The API layer is responsible for:

- User authentication
- Processing user reflections
- Communicating with AI modules
- Managing journals
- Saving AI guidance
- Retrieving conversations histor
- Managing user preferences
- Collecting feedback

## 3. API Architecture
The platform follows a client-server architecture.

Frontend (React)
      |
      v
Rest API (FastAPI)
      |
      V
Business Logic
      |
      v
Machine Learning
      |
      v
     RAG
      |
      V
     LLM
      |
      V
  Database

## 4. Authentication APIs

### POST / auth / register
Registers a new user.

#### Request
- Full name
- Email
- Password

#### Response
- User ID
- Success Message

### POST / auth / login
Authenticates an existing user.

#### Response
- JWT Access Token
- User Information

## POST / auth / logout
Logs out the currenr user.

### GET / auth / profile
Returns the authenticated user's profile.

## 5. Reflection APIs

### POST / reflection / analyze
Accepts a user's situation and initiates the AI workflow.

#### Request
- User Input

#### Response
- Emotion
- Intent
- AI Guidance
- Reflection Question
- Action Step

## 6. Journal APIs

### POST / journal
Create a journal entry.

### GET / journal
Retrieve all journal entries.

### PUT / journal / {id}
Update a journal entry.

### DELETE / journal / {id}
Delete a journal entry