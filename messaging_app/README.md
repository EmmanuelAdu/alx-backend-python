# Build a messaging App with django rest framework

## Database Specification

### Entities and Attributes

### User
user_id (Primary Key, UUID, Indexed)
first_name (VARCHAR, NOT NULL)
last_name (VARCHAR, NOT NULL)
email (VARCHAR, UNIQUE, NOT NULL)
password_hash (VARCHAR, NOT NULL)
phone_number (VARCHAR, NULL)
role (ENUM: 'guest', 'host', 'admin', NOT NULL)
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

### Message
message_id (Primary Key, UUID, Indexed)
sender_id (Foreign Key, references User(user_id))
message_body (TEXT, NOT NULL)
sent_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
  Conversation
    conversation_id (Primary Key, UUID, Indexed)
    participants_id (Foreign Key, references User(user_id)
    created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)


## Constraints:
User Table: Unique constraint on email, non-null constraints on required fields.
Property Table: Foreign key constraint on host_id, non-null constraints on essential attributes.
Booking Table: Foreign key constraints on property_id and user_id, status must be one of pending, confirmed, or canceled.
Payment Table: Foreign key constraint on booking_id, ensuring payment is linked to valid bookings.
Review Table: Constraints on rating values and foreign keys for property_id and user_id.
Message Table: Foreign key constraints on sender_id and recipient_id.
Indexing:
Primary Keys: Indexed automatically.
Additional Indexes: Indexes on email (User), property_id (Property and Booking), and booking_id (Booking and Payment)

## Tasks
0. project set up

Objective: create a new django project and install django rest framework

Instructions:

Initialize a new django project django-admin startproject messaging_app

Install django REST Framework and set it up in the settings.py

Create a new app for the messaging functionality. (python manage.py startapp chats)

1. Define data Models
mandatory
Objective: Design the models for users, messages, and conversations.

Instructions:

Using the tables definition described above,

Create the user Model an extension of the Abstract user for values not defined in the built-in Django User model
Create the conversation model that tracks which users are involved in a conversation
Create the message model containing the sender, conversation as defined in the shared schema attached to this project

2. create serializers to define the many to many relationships
mandatory
Objective: build serializers for the models

Instructions:

Create Serializers for Users, conversation and message

Ensure nested relationships are handled properly, like including messages within a conversation

3. Build api endpoints with views
mandatory
Objective: implement API endpoints for conversations and messages

Instructions:

Using viewsets from rest-framework Create viewsets for listing conversations (ConversationViewSet) and messages (MessageViewSet)

Implement the endpoints to create a new conversation and send messages to an existing one

4. set up url routing
mandatory
Objective: configure URLS for the conversations and messages

Instructions:

Using Django rest framework DefaultRouter to automatically create the conversations and messages for your viewsets

Navigate to the main project’s urls.py i.e messaging_app/urls.py and include your created routes with path as api


5. Run the application to fix errors
mandatory
Objective: run and test the applications

Instructions:

Run python manage.py makemigrations, python manage.py migrate, python manage.py runserver to test and run the application

Fix any error or bugs produced