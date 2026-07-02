# Software Requirements Specification(SRS)

## 1.Introduction

### 1.1 Project Overview
This project aims to develop an AI-powered Reflection and Guidance Platform that help users understand their situation, reflect on their experiences and take meaningful next steps.
Unlike quote generators or generic chatbots, the platform combines Machine Learning , Natural Language Processing(NLP), Retrieval-Augmented Generation and Large Language Models(LLMs) to deliver context-aware, personalized and trustworthy guidance.
The system first understands the users's situations, detects emotions and intent, retrieves relevant knowledge from a curated knowledge base, and then generates a personalized response that includes explanation, practical guidance and one actionable step.
The platfrom is designed to support students, professionals and lifelong learners by encouraging reflection, learning and informed decision-making rather than providing random motivational content.

### 1.2 Purpose
The purpose of this platfrom is to provide meaningful AI-assisted guidance by understanding user situations instead of relying on generic motivational quotes.The system combines emotion detection, semantic retrieval and large language models to deliver grounded, explainable and personalized responses.
This platform emphasizes understanding, reflection and action while promoting responsible AI usage and user privacy.

### 1.3 Motivation
Many existing quote applications simply display random motivational quotes without understanding the user's actual situation or emotional state. Such responses often lack relevance, explainable and practical value.
This project was inspired by the need for an intelligent system that understands personal experiences, retrieves trustworthy knowledge and encourages thoughtful reflection instead of passive consumption of motivational content.
The goal is to create an AI platform that helps users gain clarity, perspective and confidence in making their next decision.

## 2. Problem Statement

People often seek guidance during challenging moments such as academic failures, career uncertainity, relationship issues, stress or personal setbacks.Existing quote generators and motivational applications typically provide random quotes without understanding the users's actual stuation, emotional state or intent.
Similarly, general-purpose AI chatbots may generate responses without grounding them in verified knowledge, making it  difficult to ensure reliability and explainability.
As a result, users receive advice that is often generic, repetitive or disconnected from their real-life experiences.

This project addresses these limitations by combining Machine Learning, Natural Language Processing (NLP), Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) to provide personalized, context-aware and explainable guidance. Instead of simply motivating users, the platform aims to help them understand their situations, reflect on them and take meaningful actions.

## 3. Vision
To build an intelligent AI-powered reflection platform that understands human situations, retrieves trustworthy knowledge and delivers personalized guidance that promotes self-awareness, learning and meaningful action.
The long-term vision is to create an AI companion that supports users in making thoughtful decisions while encouraging personal growth rather than dependency.

## 4. Objectives
The primary objectives of this project are:

- Understand the user's situation using Natural Language Processing.
- Detect emotions and user intent through Machine Learning models.
- Retrieve relevant knowledge using Retrieval-Augmented Generation (RAG).
- Generate personalized, context-aware guidance using Large Language Models.
- Explain why each recommendation or quote was selected.
- Suggest one practical action for the user.
- Encourage self-reflection through meaningful questions.
- Build a scalable, secure and user-friendly AI platform.
- Maintain transparency by distinguishing retrieved knowledge from AI-generated content.

## 5. Scope
The project focuses on providing AI-assisted guidance for users facing everyday challenges in areas such as education, career, relationships, productivity, personal development and decision-making.
The platform will include features such as emotion detection, intent analysis, semantic retrival, personalized guidance, AI journaling, recommendation systems and multilingual support.
This system is designed for educational and self-reflection purposes and is not intended to replace professional mental health, medical or legal advice.

## 6. Target Users
Primary Users                           |  Secondary Users
- Students                              | - Researchers
- Job seekers                           | - Entrepreneurs
- Young professionals                   | - Educators
- Software engineers                    | - Individuals interested in personal growth
- Lifelong learners                     
The platform is intended for users who seek thoughful guidance, structured reflection and practical next steps rather than generic motivational content.

## 7. Functional Requirements

### 7.1 User Management
- User Registration
- Secure Login
- Profile Management
- Personal Preferences

### 7.2 AI Reflection & Guidance
- Accept user situations in natural language.
- Detect emotions and user intent.
- Retrieve relevant knowledge using RAG.
- Generate personalized guidance using LLMs.
- Explain the reasoning behind recommendations.
- Suggest one actionable next step.

### 7.3 Knowledge Retrieval
- Retrieve relevant quotes.
- Retrieve philosophy concepts.
- Retrieve psychology insights.
- Retrieve historical examples.
- Retrieve books and learning resources.

### 7.4 User Dashboard
- View previous conversations.
- Save favorite responses.
- Track reflection history.
- View personalized recommendations.

### 7.5 Search
- Search by topic.
- Search by emotion.
- Search by author.
- Search by keyword.

### 7.6 AI Journal
- Daily reflection.
- Mood tracking.
- Personal notes.
- Growth history.

### 7.7 Recommendation System
- Recommend similar wisdom.
- Recommend books.
- Recommend articles.
- Recommend TED Talks.

### 7.8 Explainability
- Explain retrieved knowledge.
- Explain AI-generated responses.
- Display source attribution where available.

## 8. Non - Functional Requirements

### 8.1 Performance
- The system should respond to user requests within a reasonable time.
- AI-generated responses should typically be delivered within 3-5 seconds, depending on the selected language model.
- The platform should efficiently retrieve relevant information from the vector database.

### 8.2 Scalability
- The architecture should support increasing numbers of users.
- New datasets, knowledge sources and AI models should be added without major system redesign.
- The backend should support horizontal scaling when deployed.

### 8.3 Security
- User authentication must be secure.
- Passwords must be encrypted before storage.
- User data should be transmitted using HTTPS.
- API keys and secrets must never be exposed in the frontend.

### 8.4 Privacy
- User conversations and journal entries must remain private.
- Personal information should not be shared with third parties without user consent.
- The platform should allow users to delete their stored data.

### 8.5 Reliability
- The system should remain available even under moderate traffic.
- Errors should be handled gracefully with meaningful messages.
- AI failures should provide fallback responses instead of crashing the application.

### 8.6 Explainability
- The platform should explain why guidance was generated.
- Retrieved knowledge should include source attribution where available.
- Users should be able to distinguish retrieved knowledge from AI-generated reasoning.

### 8.7 Usability
- The interface should be intuitive and beginner-friendly.
- Navigation should remain consistent across all pages.
- Users should be able to complete major tasks with minimal effort.

### 8.8 Accessibility
- The platform should support responsive layouts for desktop and mobile devices.
- Text should be readable with appropriate contrast.
- Keyboard navigation should be supported where prcatical.

### 8.9 Maintainability
- The project should follow a modular architecture.
- Code should be well documented and organized.
- Components should be reusable whenever possible.

### 8.10 Availability
- The deployed application should aim for high availability.
- Logs should be maintained for debugging and monitoring.

## 9. Artificial Intelligence Components
The platform integrates multiple Artificial Intelligence and Machine Learning technologies to understand user situations, retrieve trustworthy knowledge and generate personalized guidance. These components work together to provide context-aware, explainable and actionable responses.

### 9.1 Natural Language Processing (NLP)
- Situation understanding
- Text preprocessing
- Intent recognition

### 9.2 Machine Learning
- Emotion Detection
- Sentiment Analysis
- Intent Classification

### 9.3 Retrieval-Augmented Generation (RAG)
- Knowledge Base
- Embedding Generation
- Vector Search
- Context Retrieval

### 9.4 Large Language Models
- Personalized guidance generation
- Explaination generation
- Reflection question generation
- Action-step recommendation.

### 9.5 Recommendation System
- Similar wisdom recommendation
- Book recommendation
- Article recommendation
- Learning resource recommendation

### 9.6 Explainable AI
The platform emphasizes transparency in AI-generated guidance by:
- Explaining why a recommendation was generated.
- Distinguishing retrieved knowledge from AI-generated reasoning.
- Providing source attribution whenever possible.
- Displaying confidence information for emotion detection where applicable.

## 10. System Architecture
The platform follows a modular architecture where each component is responsible for a specific task. The architecture seperates the user interface, backend services, machine learning models and large language model to improve scalability, maintainability and performance.

### 10.1 High-Level Architecture

User
  |
  v 
React Frontend
  |
  v
FastAPI Backend
  |
  v
Authentication & API Layer
  |
  v
AI Engine

- Emotion Detection(ML)
- Intent Classification
- Sentiment Analysis

- RAG Retrieval Engine
- Embedding Model
- Vector Database

- LLM Response Generator
- Recommendation Engine
  
  |
  v
PostgreSQL Database
  |
  v
Response to User

## 10.2 Workflow

1. The user enters a situation or problem.
2. The frontend sends the request to the FastAPI backend.
3. The backend performs authentication and validation.
4. The Machine Learning engine detects emotion and intent.
5. The RAG engine retrieves relevant knowledge from the vector database.
6. The retrieved context and user information are combined into a prompt.
7. The LLM generates personalized guidance.
8. The recommendation engine suggests related resources.
9. The response is returned to the user and optionally stored for future reference.

## 11. Machine Learning Pipeline
The Machine Learning pipeline is responsible for understanding the user's emotional state and intent before any response is generated.

### 11.1 Text Preprocessing
- Remove unwanted characters
- Normalize text
- Tokenization
- Input Validation

### 11.2 Emotion Detection
The system predicts emotions such as:
- Joy
- Sadness
- Anger
- Fear
- Love
- Surprise
- Neutral

Recommended Model:
-DistilBERT

Dataset:
- GoEmotions

### 11.3 Sentiment Analysis
The sentiment of the user's purpose, including:

- Seeking motivation
- Looking for advice
- Decision making
- Self-reflection
- Learning
- Career guidance
- Relationship guidance

## 12. RAG Pipeline
The platform uses Retrieval-Augmented Generation(RAG) to provide trustworthy and context-aware guidance instead of relying solely on the language model.

### 12.1 Knowledge Base
The knowledge base contains:
- Verified quotes
- Philosophy
- Psychology
- Historical examples
- Scientific concepts
- Leadership lessons
- Books
- Research papers
- Life experiences

### 12.2 Embedding Model
Recommended Model:
- all-MiniLM-L6-v2

Alternative Models:
- BGE-small
- E5-small

### 12.3 Vector Database
Recommended: 
- FAISS

Alternative:
- ChromaDB

### 12.4 Retrieval Process

User
  |
  v
Embedding Generation
  |
  v
Vector Search
  |
  v
Top-K Similar Documents
  |
  v
Context Retrieval
  |
  v
LLM Prompt

## 13. Large Language Model (LLM)
The Large Language Model generates personalized guidance using the user's situation, detected emotions, retrieved knowledge and conversation context.

### Responsibilities
- Situation Understanding
- Personalized guidance
- Reflection generation
- Explanation generation
- Action-step recommendation
- Context-aware conversation

Recommended Models:

Development:
- Gemini API

Future:
- Llama 3
- Mistral
- OpenAI-compatible local models

## 14. Database Design
The platform uses a rational database to manage user information, conversations, journals, preferences, feedback and AI generated responses. The database is designed to ensure scalability, consistency and efficient retrieval of structured data.

### 14.1 Users Table
Stores user account information.

Fields:
- user-id (Primary Key)
- full_name
- email
- password_hash
- profile_picture
- preferred_language
- created_at
- updtaed_at

### 14.2 User Preferences Table
Stores personalization settings.

Fields:
- preference_id
- user_id (Foreign Key)
- preferred_categories
- notification_categories
- theme
- language

### 14.3 Conversations Table
Stores all AI conversations.

Fields:
- conversation_id
- user_id
- detected_emotion
- detected_intent
- ai_response
- created_at

### 14.4 Journal Entries Table
Stores daily reflections.

Fields:
- journal_id
- user_id
- journal_text
- detected_mood
- reflection_summary
- created_at

### 14.5 Saved Guidance Table
Stores user-saved AI guidance.

Fields:
- saved_id
- user_id
- conversation_id
- rating
- comments
- created_at

### 14.6 Feedback Table
Stores user feedback.

Fields:
- feedback_id
- user_id
- conversation_id
- rating
- comments
- created_at

### 14.7 Knowledge Base Metadata
Stores metadata for RAG documents.

Fields:
- document_id
- title
- category
- source
- author
- keywords
- embedding_reference

## 15. API Design
The backend exposes RESTFul APIs for communication between the frontend and AI services.

### Authentication APIs
- POST / signup
- POST / login
- POST / logout

### User APIs
- GET / profile
- PUT /profile

### AI APIs
- POST / analyze
- POST / generate-guidance
- POST / journal-analysis

### Search APIs
- GET / search

### Recommendation APIs
- GET / recommendations
 
### Feedback APIs
- POST / feedback

### History APIs
- GET / history

## 16. Technology Stack

### Frontend
- React
- Tailwind CSS

### Backend
- FastAPI
- Python

### Machine Learning
- PyTorch
- Hugging Face Transformers
- Sentence Transformers
- scikit-learn

### Retrieval-Augmented Generation
- LangChain
- FAISS
- ChromaDB

### Database
- Postgre SQL

### Authentication
- JWT
- OAuth (Future)

### Deployment
- Docker
- Render
- Vercel

### Version Control
- Git
- GitHub