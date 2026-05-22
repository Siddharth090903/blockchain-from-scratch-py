# Blockchain Architecture from Scratch 

This repository contains a fundamental, ground-up implementation of a blockchain system using pure Python.

## Objective
To manually build a blockchain architecture to deeply understand block generation, cryptographic hashing (SHA-256), and the Proof-of-Work (PoW) consensus mechanism.

## Tech Stack
* **Python 3.x**
* **Hashlib** (for SHA-256 cryptographic hashing)
* **Time Module** (for timestamping blocks)

## Core Components Implemented
1. **Block Class**: Index, time stamp, data, previous hash and hash of the current block.
2. **Blockchain Class**: Ledger manager responsible for the genesis block, appending new blocks, and validating the chain’s integrity.
3. **Proof-of-Work**: A basic mining algorithm that is used to regulate the creation of blocks.


