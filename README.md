# Anonymous Feedback Collection System

This repository contains the implementation of the Anonymous Feedback Collection System, designed to allow administrators to create and manage anonymous feedback forms and view raw user submissions, ensuring complete user anonymity.

## Project Overview

The system is built on a microservices architecture, deployed on Google Cloud Platform (GCP) using Docker and Kubernetes (GKE). It comprises three core services: Form Management, Feedback Submission, and Admin Reporting.

## Architecture Highlights

*   **Microservices:** Modular and scalable services for form management, feedback submission, and admin reporting.
*   **Frontend:** Public-facing UI for anonymous feedback submission and an authenticated Admin Dashboard.
*   **Data Storage:**
    *   **Form Configuration DB (SQL):** For structured form definitions.
    *   **Feedback Data Store (NoSQL):** For flexible and scalable storage of anonymous feedback submissions.
*   **Cloud Native:** Leverages GCP services, Docker for containerization, and GKE for orchestration.
*   **Security & Anonymity:** Strict measures to prevent PII collection, data encryption, and robust access control for admins.

## Getting Started

### Prerequisites

*   Docker
*   Kubernetes (kubectl configured for GKE access)
*   Python 3.9+
*   Google Cloud SDK (gcloud)

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/p67428378-afk/anonymous-feedback-system.git
    cd anonymous-feedback-system
    ```
2.  **Configure Environment Variables:**
    Create a `.env` file based on `.env.example` and fill in the necessary values.

3.  **Build Docker Images:**
    Navigate to each service directory (e.g., `services/form-management`) and build its Docker image:
    ```bash
    docker build -t <your-gcr-repo>/form-management-service:latest .
    ```

4.  **Deploy to GKE:**
    Use Kubernetes manifests (to be provided in `kubernetes/` directory) to deploy the services to your GKE cluster.

### Usage

*   **Public Feedback UI:** Access the deployed public UI to submit anonymous feedback.
*   **Admin Dashboard:** Log in to the admin dashboard (requires authentication) to create forms and view submissions.

## Development

### Local Development

Each service can be run independently for local development. Refer to the `README.md` within each service directory for specific instructions.

### CI/CD

The project utilizes an automated CI/CD pipeline for building, testing, and deploying services to various environments (Dev, Staging, Production).

## Contributing

Please refer to the contributing guidelines (to be added).

## License

This project is licensed under the MIT License (to be added).
