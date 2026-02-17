# 🍎 Automated App Store Reviews Monitoring (iOS)


## 🧠 Overview
This project automates the monitoring and processing of new user reviews from the Apple App Store (iOS).

It replaces the manual process of checking App Store Connect by automatically:

* Fetching the latest reviews via App Store Connect API
* Authenticating using JWT (JSON Web Token)
* Identifying newly submitted reviews
* Logging them into a structured spreadsheet
* Classifying sentiment (positive, negative or neutral)
* Sending formatted WhatsApp notifications

The automation ensures continuous visibility of user feedback and structured documentation of all new reviews.


## 🎯 Project Objective
The main goal was to build a reliable, secure and recurring review monitoring pipeline for iOS applications.

Impact:

* Eliminates manual monitoring in App Store Connect
* Ensures no review is missed
* Automatically catalogs new reviews in a centralized spreadsheet
* Classifies sentiment for prioritization
* Sends near real-time WhatsApp alerts for new feedback
* Runs automatically every 3 hours between 07:00 and 22:00


## 🧱 High-Level Architecture
1. Scheduled trigger
* n8n Cron job executes every 3 hours between 07:00 and 22:00

2. Pipeline initialization
* n8n sends an HTTPS request to a serverless endpoint hosted on Vercel
* The Apple review pipeline is triggered

3. Authentication
* The pipeline generates a JWT (JSON Web Token)
* JWT is signed using the App Store Connect private key (.p8)
* The token is used to authenticate with the App Store Connect API

4. Data ingestion
* The App Store API returns the latest app reviews
* Reviews are sent back to n8n via Webhook

5. Deduplication process
* n8n retrieves already registered review IDs from Google Sheets
* Compares stored IDs with incoming API response
* Filters only new reviews

6. Data persistence
* New reviews are appended to Google Sheets
* Each review includes:
  * Rating
  * Review text
  * Timestamp
  * Review ID
  * Sentiment classification (positive, negative or neutral)

7. Notification system
* New reviews are formatted into structured WhatsApp messages
* WhatsApp notification is triggered with review details


## 🔐 Security Considerations
* JWT-based authentication for secure machine-to-machine communication
* Private key (.p8) stored securely via environment configuration
* Secrets managed through environment variables
* Stateless serverless architecture
* Secure HTTPS communication between services


## 🛠 Technologies & Tools
* Language: Python
* Authentication: JWT (App Store Connect API)
* Integrations: App Store Connect API
* Automation: n8n (Cron + Webhook)
* Infrastructure: Serverless deployment (Vercel)
* Data storage: Google Sheets
* Notification: WhatsApp API
* Data format: JSON
* Version control: Git


## 📚 Key Learnings
* Implementing JWT authentication with ES256 signing for Apple APIs
* Working with App Store Connect API structure and review endpoints
* Handling paginated API responses
* Designing deduplication logic to avoid duplicate entries
* Implementing lightweight sentiment classification logic
* Building event-driven automation pipelines with external orchestration (n8n)
