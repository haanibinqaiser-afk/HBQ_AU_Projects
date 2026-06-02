# Automated Cryptographic Pipeline via Jenkins & Docker 🚀
**Course:** Secure Software Design and Development  
**Date:** June 1, 2026  
**Academic Level:** BS Cyber Security (4th Semester) — Air University  

---

## 📋 Project Overview
This project establishes a fully automated, containerized Continuous Integration (CI) pipeline that handles text encryption and decryption using a classic Caesar Cipher algorithm. By incorporating **Pipeline as Code** (Jenkinsfile) and **Infrastructure as Code** (Dockerfile), the cryptographic environment executes entirely isolated within a secure Docker container, removing any dependencies on the host machine's local runtime.

### Key Features:
*   **Pipeline as Code:** Fully managed via a declarative `Jenkinsfile` tracked in SCM.
*   **Containerized Isolation:** Employs a lightweight Python Docker container to execute the cryptographic logic securely.
*   **Secure SCM Integration:** Configured as a multibranch pipeline using GitHub personal access tokens.
*   **Ephemeral Environment Cleanup:** Automatically purges temporary Docker images post-execution to avoid resource bloat.

---

## 🛠️ Requirements & Environment Setup

### 1. Docker & WSL Integration
The system uses Ubuntu on Windows Subsystem for Linux (WSL) integrated with Docker Desktop to build and manage container lifecycles.
*   **WSL Installation:** Downloaded via the Microsoft Store.
*   **Docker Integration:** Docker Desktop configured to leverage the default WSL Ubuntu distribution.

![](assets/ubuntu_wsl_setup.png)  
*Figure 1: Initializing Ubuntu via the Microsoft Store.*

### 2. Jenkins Automation Server
The local Jenkins server runs alongside a Java Development Kit (JDK 25) environment. Secure automation parameters are explicitly configured within the system tools:
*   **Git Path Verification:** Explicitly mapped to `git.exe` inside global tool configurations.
*   **Required Plugins:** `Docker Pipeline` and `GitHub Integration` plugins active.

![](assets/jenkins_dashboard_tools.png)  
*Figure 2: Active local Jenkins environment dashboard.*

### 3. Secure Source Control Management (SCM)
A private SCM repository was established. To maintain zero-trust access principles, authentication with Jenkins is handled explicitly via a **GitHub Classic Personal Access Token (PAT)** rather than raw password parameters.

![](assets/github_repo_creation.png)  
*Figure 3: Configuring the private Git repository control parameters.*

---

## 💻 Pipeline Architecture & Implementation

The repository structure holds three critical files at its root level:
1.  `cipher.py`: Handles core Caesar Cipher encryption/decryption routines.
2.  `Dockerfile`: Configures a minimalistic `python:3.11-slim` runtime environment.
3.  `Jenkinsfile`: Controls individual build stages and automation behaviors.

├── assets/                  # Project screenshots and documentation graphics
├── cipher.py                # Core Python script for Caesar Cipher algorithm
├── Dockerfile               # Container setup script (python:3.11-slim)
└── Jenkinsfile              # Declarative multi-stage automation script


### Automation Workflow Lifecycle:
1.  **Verify Docker Accessibility:** Polls the local environment to confirm the active Docker daemon engine status.
2.  **Build Cipher Image:** Compiles the runtime environment into a temporary execution layer (`caesar-cipher:latest`).
3.  **Encryption Stage:** Passes raw text strings into the spinning container to output the computed cipher matrix.
4.  **Decryption Stage:** Reverse-processes the ciphertext string back into plaintext to verify algorithm parity.
5.  **Post-Actions (Cleanup):** Automatically runs a forced image removal (`docker rmi`) to maintain a clean container environment.

---

## 📊 Compilation, Execution, & Output Logs

Once SCM scanning successfully hooks into the repository branch tracking parameters, the execution path builds seamlessly.

![](assets/jenkins_scan_repo.png)  
*Figure 4: Jenkins scanning the repository branch structure.*

![](assets/successful_builds.png)  
*Figure 5: Build status page highlighting successful automation workflows.*

### Real-Time Console Output Logs:
```text
[Pipeline] Stage (Verify Docker Accessibility)
> docker --version 
Docker version 29.5.2, build 79eb04c

[Pipeline] Stage (Build Cipher Image)
> docker build -t caesar-cipher:latest . 
#1 [internal] load build definition from Dockerfile
#6 [2/3] WORKDIR /app
#7 [3/3] COPY cipher.py .
#8 naming to docker.io/library/caesar-cipher:latest done

[Pipeline] Stage (Encryption Stage)
Original Text: DevOps with Jenkins, Docker Desktop, and WSL!
Encrypting...
Encrypted Output: KlcVwz dpao Qlurpuz, Kvjrly Klzravw, huk DZS!

[Pipeline] Stage (Decryption Stage)
Passing Encrypted Text to Decryption Stage...
Decrypted Output: DevOps with Jenkins, Docker Desktop, and WSL!

[Pipeline] Stage (Declarative: Post Actions)
Cleaning up local Docker images...
> docker rmi caesar-cipher:latest --force 
Untagged: caesar-cipher:latest
Finished: SUCCESS
