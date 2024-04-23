# lats-api-gateway

## Overview
lats-api-gateway is an API gateway that provides users with access to internal data and a remote API along with certain data item persistance. Users authenticate against the remote
API, receive an auth token and query and make changes to internal data before posting those changes along with the auth token, back to the remote API.

## Features
• Provides authentication and logout for remote API
• Queries and returns data from an internal database to the frontend
• Persists certain user data in a separate database
• Forwards user changes to a remote API

## Architecture
This application is built using the following technologies:

• Flask (Python)
• SqlAlchemy (ORM)
• Alembic (Migrations)

## Data Flow
1. User enters credentials.
2. Credentials are sent to remote API.
3. An authorization token is generated and received from remote API.
4. Token is stored in local MongoDb and used to maintain state.
5. User is redirected from Login page to dashboard.
6. User makes one of several selections and submits those to backend.
7. Backend queries local Oracle DB and returns data to user.
8. User makes changes and submits data.
9. Changes are persisted in local MySQL database.
10. Changes are POSTed to remote API.
11. Remote API acknowledeges either with a 200 or 500 response.
12. User is updated on status of POST request.
13. When complete, user logs out. Session data in MongoDb is remvoed.

## APIs
• POST /api/login: Login and authenticate user against remote API
• POST /api/logout: Logout user both locally and from remote API
• POST /api/reset_password: Reset password for remote API
• POST /api/forgot_password: Create new password for remote API
• GET /api/get_user_data: Gets user session data in MongoDb
• POST /api/set_user_data: Sets user session data in MongoDb
• POST /api/add_to_batch: Builds a batch of changes to upload to remote API
• POST /api/get_batch: Queries local Oracle DB and returns data for creating a batch
• GET /api/get_status: Queries remote API for approval status of uploaded batch(es).

## Dependencies
• Flask
• Alembic
• SQLAlchemy
• MySQL
• Oracle
• MongoDb




