# TravelBuddies Project Structure

This project is a dynamic web application using **React** for frontend development and **Python** (strict with **MyPy**) for backend development. The site provides different user experiences based on authentication status, utilizing APIs for data fetching, user interaction, and booking functionalities.

---

## Table of Contents

- [Project Requirements](#project-requirements)
- [Pages and Redirections](#pages-and-redirections)
- [API Endpoints](#api-endpoints)
- [Development Rules](#development-rules)
- [Environment Setup](#environment-setup)
- [Database](#database)
- [Testing and Validation](#testing-and-validation)
- [Security Practices](#security-practices)
- [Deployment Strategy](#deployment-strategy)

---

## Project Requirements

- **Frontend**: 
  - Developed using **React**.
  - Strict JavaScript with `'use strict';`.
  - Single-page application with dynamic routing based on user authentication.
  
- **Backend**: 
  - Hosted at `backend.travelbuddies.me`.
  - Developed in **Python** with **FastAPI** or **Flask**.
  - Uses **MyPy** for strict type-checking.
  - Exposes RESTful APIs for all data operations.

- **Authentication**: 
  - Each user is uniquely identified by `app_id`.
  - Passed as a **Bearer token** in the `Authorization` header.

## Pages and Redirections

- `/`: Redirects to `/home`.
- `/home`: 
  - **Logged-in users**: 
    - Shown a **dashboard** with personalized data and an info page.
  - **Unlogged-in users**: 
    - Shown a **sign-up button**, an **About Us** section, and general information.

---

## API Endpoints

### 1. **Get Data**
   - **Endpoint**: `GET backend.travelbuddies.me/get-data`
   - **Authorization**: Requires Bearer token.
   - **Parameters**: 
     - `searchSchema`: JSON object
       ```json
       {
         "db": "the-db-needed",
         "key": "key",
         "value": "value",
         "forUser": "user"
       }
       ```

### 2. **Add Data**
   - **Endpoint**: `POST backend.travelbuddies.me/add-data`
   - **Authorization**: Requires Bearer token.
   - **Parameters**: 
     - `searchSchema`: JSON object
       ```json
       {
         "db": "the-db-you-wanna-append-to",
         "aKey": "append key",
         "aValue": "append value",
         "forUser": "user",  # or 'global' if global is true
         "global": {
           "ChangeAuth": "change-auth-token",
           "globalval": "new global value"
         }
       }
       ```

### 3. **App-Specific Endpoints**
   - **Base URL**: `backend.travelbuddies.me/app?AppId={app_id}`
   - **Sub-Endpoints**:
     - `/scan_qr`: Scans a QR code.
     - `/pay`: Processes payment transactions.

### 4. **Book a Hotel**
   - **Endpoint**: `POST backend.travelbuddies.me/book-hotel`
   - **Authorization**: Requires Bearer token.
   - **Parameters**: 
     - `hotel`: Specifies the hotel to book, along with other details.

### 5. **Available Hotels**
   - **Endpoint**: `GET backend.travelbuddies.me/available-hotels?q={query}`

### 6. **Book Flights**
   - **Endpoint**: `POST backend.travelbuddies.me/flights/book`
   - **Authorization**: Requires Bearer token.
   - **Parameters**: 
     - `airline`: Specifies the flight details.

---

## Development Rules

### Frontend (React)

- Strict mode enforced with:
  ```javascript
  'use strict';
