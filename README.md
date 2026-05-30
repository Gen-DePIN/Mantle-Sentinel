# 🛡️ Mantle Sentinel

🏆 **Built for The Turing Test 2026 Hackathon** <p align="center">
  <video src="sentinel-demo.mp4" autoplay loop muted playsinline width="100%"></video>
</p>

> **Autonomous AI-Driven On-Chain Anomaly Detection & Network Guardian for the Mantle Ecosystem.**

Mantle Sentinel is an intelligent network monitoring agent engineered to safeguard smart contracts, protocols, and decentralized infrastructure running on the Mantle Network. By leveraging real-time data streaming from Mantle RPC nodes, the Sentinel analyzes transaction flows, sequencer latency, and gas market fluctuations to isolate anomalies and mitigate exploits before they escalate.

---

## 🌍 Impact on the Mantle Ecosystem
Security is the foundation of TVL (Total Value Locked) growth. Mantle Sentinel provides:
* **For DeFi Protocols:** Proactive warnings against flash-loan attacks and liquidity drains.
* **For Infrastructure Providers:** Real-time alerts on sequencer delays or RPC desynchronization.
* **For the Ecosystem:** A safer environment that attracts institutional capital by shifting security from *reactive* (post-exploit analysis) to *proactive* (real-time prevention).

---

## 📖 Table of Contents
1. [System Architecture & AI Stack](#-system-architecture--ai-stack)
2. [Key Features](#-key-features)
3. [Repository Structure](#-repository-structure)
4. [Quick Start & Installation](#-quick-start--installation)
5. [Proof of Concept (PoC) Logic](#-proof-of-concept-poc-logic)
6. [Future Roadmap](#-future-roadmap)

---

## ⚙️ System Architecture & AI Stack
The agent is built using a modular pipeline design, integrating standard Web3 tooling with Machine Learning primitives:

1. **Data Ingestion Layer (Web3.py):** Connects directly to the Mantle JSON-RPC provider to listen for newly minted blocks and pending state transitions.
2. **Feature Extraction:** Extracts core performance and financial primitives: gas price variance, block time intervals, and contract interaction densities.
3. **AI Anomaly Isolation Model:** * Utilizes Unsupervised Machine Learning (e.g., Isolation Forests / dynamic thresholding via `scikit-learn`) to establish a baseline of "normal" network behavior.
   * Continuously evaluates extracted primitives against this model to detect statistical deviations representing automated spam vectors or exploit signatures.
4. **Alert Routing Gateway:** Formulates actionable JSON-payload security logs and dispatches instant webhooks (Discord/Telegram) to infrastructure maintainers.

---

## ✨ Key Features
* **⏱️ Sequencer Latency Tracking:** Continuously monitors the exact timestamp deltas between blocks to flag sequencer lagging, node desynchronization, or infrastructure downtime.
* **⛽ Gas Spike Volatility Engine:** Identifies abnormal network congestion, front-running clusters, or automated spam vectors by isolating aggressive Gwei deviations.
* **🔒 Smart Contract Outflow Sentinel:** Designed to trace transaction sizes to detect abnormal, large-scale drain anomalies from liquidity pools or cross-chain bridges.

---

## 🛠️ Repository Structure
```bash
├── app.py           # FastAPI server for frontend integration and mock data endpoints
├── main.py          # Core Python application containing the AI Agent logic and RPC loop
├── sentinel-demo.mp4# Cinematic demo visualization of the AI Agent threat isolation
├── requirements.txt # Dependencies (Web3.py, FastAPI, scikit-learn, etc.)
├── README.md        # Comprehensive technical documentation and architecture overview
└── .env.example     # Configuration blueprint for network endpoints and private credentials
