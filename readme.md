# CryptoCore: Post-Quantum Threat Simulator & Library

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Phase_1_(Active)-orange)

## 📌 Overview
CryptoCore is an ongoing exploration of Post-Quantum Cryptography (PQC) and the ethical implications of modern data security. It serves as both a simulator for emerging cryptographic threats and a foundation for implementing quantum-resistant algorithms.

Currently, the project focuses on simulating the **"Harvest Now, Decrypt Later" (HNDL)** threat model, demonstrating the vulnerability of classical encryption (like RSA and ECC) to future quantum hardware.

## ⚠️ The Problem: "Harvest Now, Decrypt Later"
We are currently in a critical cryptographic transition period. While classical encryption algorithms are secure against modern supercomputers, they are fundamentally vulnerable to Shor's Algorithm running on a sufficiently powerful Cryptographically Relevant Quantum Computer (CRQC). 

State-sponsored actors and advanced persistent threats (APTs) are actively executing HNDL attacks. They intercept and store heavily encrypted, high-value data today with the intention of decrypting it a decade from now when quantum hardware matures. 

**The Ethical Dilemma:** If highly sensitive data has a required secrecy lifespan of 20 years, but a CRQC arrives in 10 years, that data is already compromised today.

## 🗺️ Project Roadmap

### Phase 1: Threat Simulation (Current)
- [x] Classical RSA and ECC vulnerability assessment.
- [x] Mock interception and storage of ciphertext (HNDL simulation).
- [x] Quantum vulnerability estimation based on Shor's Algorithm.
- [x] Dynamic CLI inputs for variable key and curve sizes.

### Phase 2: Quantum-Resistant Implementation (Upcoming)
- [ ] Transition from Python prototyping to C++ for performance optimization.
- [ ] Implementation of simplified Lattice-based cryptography primitives.
- [ ] Demonstration of the Learning With Errors (LWE) mathematical problem.

### Phase 3: Hybrid Architecture (Upcoming)
- [ ] Python bindings for optimized C++ cryptographic modules.
- [ ] A hybrid CLI utility allowing simultaneous encryption with standard AES and a post-quantum algorithm.

## ⚙️ Installation & Usage

### Prerequisites
* Python 3.8 or higher.
* `cryptography` library.

### Setup & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aayanrashid995/CryptoCore.git](https://github.com/aayanrashid995/CryptoCore.git)
   cd CryptoCore
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simulator with default settings:**
   ```bash
   python harvest_simulator.py
   ```

4. **Run with custom key sizes:**
   ```bash
   # Test against high-security RSA-4096 and ECC-384 targets
   python harvest_simulator.py --rsa-size 4096 --ecc-size 384
   ```

## 🧮 Quantum Vulnerability Assessment: The Math

### RSA Vulnerability
To factor an integer representing an RSA public key using Shor's algorithm, a quantum computer requires roughly $2N$ logical qubits for a key size of $N$ bits.
* **RSA-2048:** ~4,096 logical qubits.
* **Overhead:** With error correction (surface codes), this necessitates millions of physical qubits.

### ECC Vulnerability (The Discrete Log Problem)
Interestingly, Elliptic Curve Cryptography is more vulnerable to Shor’s algorithm than RSA. Breaking an ECC key of $N$ bits requires roughly $6N$ logical qubits. 
* **ECC-256:** ~1,536 logical qubits.
* **Takeaway:** Despite having "stronger" classical security per bit, ECC will likely fall to quantum computers sooner than RSA-2048. This project highlights why modern standards like TLS 1.3 and Bitcoin (Secp256k1) are at immediate risk from HNDL attacks.

## 🤝 Contributing
This project is open for collaboration, especially in the areas of C++ optimization, lattice-based mathematical modeling, and documentation of cryptographic ethics. Feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
```

