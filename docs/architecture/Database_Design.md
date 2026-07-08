# Database Design

## 1. Introduction
The AI Reflection & Guidance Platform stores structured information related to users, conversations, journals, AI responses, recommendations and feedback..
The database is designed to support scalability, security and efficient retrieval while maintaining user privacy.
PostgreSQL is selected as the primary relational database due to its reliability, ACID compliance and excellent support for structured data.

## 2. Database Objectives
The database is designed to:
- Store user accounts securely
- Maintain conversation history
- Store journal entries
- Save AI-generated guidance
- Store user feedback
- Support analytics
- Enable future recommendation models.

## 3. Main Entities
The database contains the following primary entities:
- Users
- Conversations
- Journal Entries
- AI Responses
- Saved Guidance
- Feedback
- User Preferences
- Analytics Logs

## 4. Database Tables

### 4.1 Users
Stores registered user information

|   Field            |    Type    |  Description           |   
------------------------------------------------------------
| user_id            |     UUID   | Primary Key            |
| full_name          |   VARCHAR  | User's name            |
|  email             |   VARCHAR  | Unique email           |
| password_hash      |   VARCHAR  | Encrypted password     |
| profile_picture    |    TEXT    | Optional profile image |
| preferred_language |  VARCHAR   | Selected language      |
| created_at         | TIMESTAMP  | Account creation date  |
| updated_at         | TIMESTAMP  | Last profile update    |

### 4.2 Conversations
Stores all user conversation with the AI.

|            Field               |       Type          |         Description              |
-------------------------------------------------------------------------------------------
|       conversation_id          |        UUID         |         Primary key              |
|        user_id                 |        UUID         |         Foreign key              |
|        user_input              |        TEXT         |   Situation entered by user      |
|    detected_emotion            |      VARCHAR        |         ML prediction            |
|    detected_intent             |      VARCHAR        |    Intent Classification         |
|   retrieved_context            |       TEXT          |    RAG retrieved knowledge       |
|          ai_response           |       TEXT          |     Final AI guidance            |
|       created_at               |     TIMESTAMP       |            Timestamp             |

### 4.3 Journal Entries
Stores personal reflection journals.

|        Field           |     Type       |      Description           |
------------------------------------------------------------------------
|      journal_id        |     UUID       |    Primary key             |
|       user_id          |     UUID       |    Foreign key             |
|        title           |   VARCHAR      |    Journal title           |
|       content          |     TEXT       |    User reflection         |
|     detceted_emotion   |   VARCHAR      |    ML prediction           |
|      created_at        |  TIMESTAMP     |    Creation date           |

### 4.4 Saved Guidance
Stores AI responses by users.

|        Field            |   Type      |     Description            |
----------------------------------------------------------------------
|      saved_id           |   UUID      |     Primary key            |
|      user_id            |   UUID      |      user_id               |
|   conversation_id       |   UUID      |  Related conversation      |
|     created_at          | TIMESTAMP   |      Save date             |

### 4.5 Feedback 
Stores user feedback on AI responses.

|        Field       |       Type       |       Description       |
-------------------------------------------------------------------
|  feedback_id       |      UUID        |     Primary key         |
|  conversation_id   |      UUID        |  Related conversation   |
|  rating            |    INTEGER       |  Rating (1-5)           |
|  comment           |      TEXT        |  Optional feedback      |
|  created_at        |    TIMESTAMP     |  Feedback date          |

### 4.6 User Preferences
|      Field           |     Type       |     Description         |
-------------------------------------------------------------------
|  preference_id       |     UUID       |      Primary key        |
|   user_id            |     UUID       |      Foreign key        |
| preferred_language   |    VARCHAR     |       Language          |
|    theme             |    VARCHAR     |      Light/Dark         |
| notification_enabled |    BOOLEAN     |      Notification       |

## 5. Entity