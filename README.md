# Cryptography & Data Security

Welcome to the Cryptography module of my security portfolio. This space is dedicated to exploring fundamental and advanced cryptographic primitives, secure communication protocols, and implementation labs involving data encryption, hashing, and key management.

## 🚀 Learning & Project Roadmap

This branch is structured into distinct sub-modules tracking my hands-on labs, comparative analysis, and automated pipelines:

### 1. Symmetric Cryptography (`/symmetric-crypto`)
Focuses on high-speed data encryption using standard block and stream ciphers, emphasizing algorithm execution and secure parameters.
* **Featured Lab:** *Implementation of AES using OpenSSL* – Configuring and executing Advanced Encryption Standard (AES) configurations via OpenSSL to secure sensitive data.

### 2. Asymmetric Cryptography & PKI (`/asymmetric-crypto`)
Exploring public-key infrastructure, digital signatures, and asymmetric mathematical foundations.
* **Featured Labs:**
  * *Implementation of RSA using OpenSSL* – Generating RSA key pairs, managing public/private keys, and executing asymmetric encryption/decryption.
  * *Implementation of DSA using OpenSSL* – Implementing the Digital Signature Algorithm (DSA) to facilitate message authentication and non-repudiation.

### 3. Message Integrity & Data Hiding (`/integrity-stego`)
Focuses on verifying data authenticity, preventing tampering, and exploring covert communication channels.
* **Featured Labs:**
  * *Implementation of Hashing Algorithms* – Deploying cryptographic hash functions (e.g., SHA-256, SHA-3) to generate secure message digests.
  * *Steganography Implementation and Code* – Developing scripts to conceal secret payloads within digital media without altering the perceived file integrity.

---

## 🔬 Featured Capstone Project
### **Cryptographic Primitive Comparison & Secure Pipeline Simulation**
A comprehensive research and practical project evaluating the efficiency, security, and deployment of modern vs. legacy cryptographic algorithms.
* **Algorithm Benchmarking:** Direct performance and security comparison between symmetric primitives (**AES vs. DES**) and asymmetric primitives (**RSA vs. DSA**).
* **Integrity Checking Simulations:** Building automated workflows that utilize **RSA digital signatures** and **cryptographic hashes** to verify file integrity and detect data tampering.
* **Secure Pipeline Implementation:** Integrating these implementation scripts into an automated CI/CD pipeline environment to demonstrate DevSecOps best practices.

---

## 🛠️ Toolstack & Technologies
* **Languages:** C++, Python, Bash scripting
* **Tools & Libraries:** OpenSSL, Steganography utilities (e.g., Steghide, custom Python scripts)
* **DevSecOps Automation:** Docker, Jenkins CI/CD

---

## 📈 Objectives
* Understand mathematical foundations of symmetric/asymmetric encryption, hashing, and digital signatures.
* Mitigate common cryptographic vulnerabilities (e.g., weak legacy algorithms like DES, improper IV reuse).
* Integrate cryptographic tools and integrity verification seamlessly into automated deployment environments.
