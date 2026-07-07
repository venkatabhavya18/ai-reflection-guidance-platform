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
Stores all user conversation with the AI