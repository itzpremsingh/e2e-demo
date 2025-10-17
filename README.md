# 🔐 Python End-to-End (E2E) Encryption Demo

**Python E2E Encryption Demo** is a simple project to show how **end-to-end encryption** works using **public-private key pairs**. Messages sent from **User A** to **User B** remain private — even the server cannot read them.

---

## ✨ Features

- Generate **public and private keys** for each user.
- Encrypt messages with the **receiver’s public key**.
- Decrypt messages with the **receiver’s private key**.
- Demonstrates the **core concept of E2E encryption** in a simple way.

---

## 🛠️ How It Works

1. **Key Generation**
   Each user creates their own public and private key pair.

2. **Message Encryption**
   Sender encrypts the message using the **receiver’s public key**.

3. **Message Decryption**
   Receiver decrypts the message using their **private key**.

4. **Privacy**
   Even if the message is intercepted, it cannot be read without the receiver’s private key.

---

## 📦 Example Usage

1. Generate keys for User A and User B.
2. User A encrypts a message using User B’s public key.
3. User B decrypts the message using their private key.
4. User B can reply securely using User A’s public key.

---

## 🏃 How to Run

1. Start the **server**:

```bash
python main.py server
```

2. Start a **client**:

```bash
python main.py client
```

3. Follow the prompts to send encrypted messages between clients.

---

## 🖼️ Flow Diagram

```
User A (sender)         Server           User B (receiver)
  Public/Private Key                         Public/Private Key
          |                                     |
          | Encrypt message using B's public key
          |----------------------------------->|
          |                                 Receive encrypted message
          |                                     |
          |                                 Decrypt using B's private key
          |                                     |
       Plain message                        Plain message
```

---

## ⚠️ Notes

- This project is for **learning purposes** only.
- For real-world security, use a **trusted crypto library**.
