# System Architecture

## 1. Introduction
The AI Reflection & Guidance Platform follows a modular, scalable and service-oriented architecture.
Instead of functioning as a traditional quote generator, the platform understands the user's situation, retrieves trustworthy knowledge, reasons over the retrieved context and generates personalized guidance that encourages reflection and meaningful action.
The architecture seperates the frontend, backend, artificial intelligence modules, databases and deployment components into independent layers to improve scalability, maintainability and future extensibility.

## 2. Architecture Goals
The system has been designed with the following goals:

- Scalability : The architecture should support increasing numbers of users and future AI models.
- Modularity : Every componenet should work independently and be replaceable without affecting the remaining system.
- Explainability : The AI should explain why a recommendation was generated instead of producing unexplained outputs.
- Reliability : The platform should continue functioninh even when one component temporarily fails.
- Security : Protect user data, authentication and API communication.
- Maintainability : Developers should easily understand, extend and improve the project.
- Human-Centered AI : The system should assist users in reflection and growth rather than replacing human judgement.

## 3. High-Level Architecture
The platform consists of the following major layers.

1. Presentation Layer
2. Backend Layer
3. Authentication Layer
4. AI Decision Layer
5. Retrieval Layer (RAG)
6. Large Language Model Layer
7. Recommedation Layer
8. Database Layer
9. Analytics Layer
  
## 4. Complete Architecture
                       USER
                         |
                         V
                   React Frontend
                         |
                         v
                   FastAPI Backend
        _________________|___________________
        |                |                   |
        v                v                   v
  Authentication     User Database      Analytics
        |
        v
**AI DECISION ENGINE**
        |
        v
Situation UNderstanding
        |
        v
Emotion Detection (ML)
        |
        V
Intent Classification
        |
        v
Semantic Search (RAG)
        |
        v
Perspective Selection
        |
        v
Reflection Engine
        |
        v
Action Planner
        |
        v
    Gemini LLM
        |
        V
Personalized Guidance
        |
        v
Conversation Storage

## 5. AI Decision Engine
The AI Decision Engine is the central intelligence coordinator of the platform. Rather than allowing the Large Language Models (LLM) to directly generate responses from user input, the Decision Engine first analyzes the user's situation and determines the most appropriate sequence of AI modules to execute.

The Decision Engine is responsible for:
- Understanding the user's situation.
- Coordinating Machine Learning models.
- Identifying emotions and user intent.
- Selecting the appropriate knowledge domain.
- Retrieving relevant information through the RAG pipeline.
- Passing Structured context to the LLM.
- Generating explainable and personalized guidance.
- Recording user interactings for future imrpovements.

### Why is the AI Decision Engine Important?
Traditional AI assistants typically follow a simple workflow:
User Input -> LLM -> Response

In contrast, this platform follows an intelligent decision-making process:
User Input -> AI Decision Engine -> ML Analysis -> Knowledge Retrieval -> Action Planning -> LLM -> Personalized Guidance

This architecture improves the quality, relevance, explainability and trustworthiness of the generated responses.

## 6.Component Description
The AI Reflection & Guidance Platform is composed of multiple interconnected components. Each component has a specific responsibility and communicates with other modules through well-defined interfaces.

### 6.1 Frontend Layer
The Frontend Layer provides the user interface for interacting with the platform.

#### Responsibilities
- User Registeration and Login
- Reflection Chat Interface
- Dashboard
- Journal Management
- Saved Guidance
- Search Functionality
- Analytics Dashboard
- User Profile Management

#### Technology
- React.js
- Tailwind CSS
 
#### Input
- User situations
- Journal entries
- Search queries
- User feedback

#### Output
- Personalized guidance
- Reflection questions
- Recommended actions
- Analytics visualization

### 6.2 Backend Layer
The Backend Layer acts as the central coordinator of the platform.

#### Responsibilities
- API Management
- User Authentication
- Session Management
- AI Workflow Coordination
- Database Communication
- Error Handling
- Logging

#### Technology
- FastAPI
- Python

#### Input
Requests from the frontend.

#### Output
Processed responses from AI modules.

### 6.3 Machine Learning Layer
The Machine Learning Layer analyzes the user's input before any guidance is generated.

#### Responsibilities
- Emotion Detection
- Sentiment Analysis
- Intent Classification
- Situation Classification (Future Enhancement)

#### Models
- DistilBERT
- RoBERTa
- BERT (optional)

#### Dataset
- GoEmotions Dataset

#### Output
- Emotion Label
- Confidence Score
- User Intent
- Situation Category

### 6.4 Retrieval-Augmented Generation (RAG) Layer
The RAG Layer retrieves trustworthy knowledge relevant to the user's situation before the LLM generates a response.

#### Responsibilities
- Generate text embeddings
- Semantic Search
- Retrieve relevant knowledge
- Build context for the LLM

#### Knowledge Sources
- Quotes
- Psychology
- Philosophy
- Leadership
- Historical Events
- Scientific Concepts
- Books
- Real-life Examples

#### Technology
- LangChain
- FAISS
- Sentence Transformers

### 6.5 Large Language Model Layer
The Large Language Model generates personalized guidance using the user's context and retrieved knowledge.

#### Responsibilities
- Situation Understanding
- Guidance Generation
- Reflection Question Generation
- Explaination Generation
- Action Recommendation

#### Developement Model
- Gemini API

#### Future Models
- Llama 3
- Mistral
- Self-hosted Open Source Models

### 6.6 Database Layer
The Database Layer stores application data securely.

#### Stores
- User Accounts
- Conversations
- Journal Entries
- Saved Guidance
- User Feedback
- Preferences
- Analytics Data

#### Technology
- PostgreSQL

### 6.7 Analytics Layer
The Analytics Layer provides insights into user interactions and platform performance while respecting user privacy.

#### Responsibilities
- Reflection statistics
- User engagement
- Growth trends
- Popular guidance categories
- System performance monitoring
The analytics data helps improve the platform without exposing personal user information.

