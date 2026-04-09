import json
import os
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def generate_keys(key_size=2048):
    """Generates standard classical RSA keys."""
    print(f"[*] Generating standard RSA-{key_size} keys...")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    public_key = private_key.public_key()
    return private_key, public_key

def intercept_and_store(public_key, message, db_filename="harvested_database.json"):
    """Simulates a threat actor intercepting traffic and storing it for the future."""
    print("\n[!] Threat Actor: Intercepting transmission...")
    
    # Encrypting the message
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Simulating the adversary storing the encrypted data
    record = {
        "timestamp": time.time(),
        "target_encryption": "RSA-2048",
        "ciphertext_hex": ciphertext.hex()
    }
    
    mode = 'a' if os.path.exists(db_filename) else 'w'
    with open(db_filename, mode) as f:
        f.write(json.dumps(record) + "\n")
        
    print(f"[+] Data successfully harvested and archived in {db_filename}")
    return ciphertext

def quantum_vulnerability_estimate(key_size):
    """Calculates the theoretical qubits needed to break the encryption."""
    print("\n=== Quantum Vulnerability Assessment ===")
    
    # Shor's algorithm generally requires ~2N logical qubits to factor an N-bit integer
    logical_qubits = 2 * key_size
    
    # Assuming a fault-tolerant surface code architecture, the physical to logical ratio is high
    physical_qubits = logical_qubits * 1000 
    
    print("Threat Model: Shor's Algorithm")
    print(f"Target Architecture: RSA-{key_size}")
    print(f"Estimated Logical Qubits Required: {logical_qubits:,}")
    print(f"Estimated Physical Qubits Required: ~{physical_qubits:,}")
    print("Verdict: Currently secure against classical attacks. Highly vulnerable to future quantum decryption.")

if __name__ == "__main__":
    print("=== CryptoCore: Post-Quantum Threat Simulator ===")
    
    # 1. Setup Classical Encryption
    target_key_size = 2048
    priv_key, pub_key = generate_keys(target_key_size)
    
    # 2. Simulate Sensitive Data
    secret_data = "CONFIDENTIAL: State secrets, intellectual property, and long-term infrastructure designs."
    print(f"\n[+] Original Transmission: '{secret_data}'")
    
    # 3. Execute the "Harvest Now" attack
    intercept_and_store(pub_key, secret_data)
    
    # 4. Assess the future threat
    quantum_vulnerability_estimate(target_key_size)