
# 🛡️ Mantle Sentinel
**AI-Powered On-Chain Anomaly Detection for Mantle Network**

*Submission for The Turing Test Hackathon 2026 (Track: AI Alpha & Data)*

## 📖 Overview
Mantle Sentinel is an autonomous AI agent designed to safeguard the Mantle ecosystem. By continuously monitoring on-chain metrics, mempool data, and sequencer latency, Sentinel uses machine learning baselines to detect network congestion, unexpected gas spikes, and anomalous smart contract outflows in real-time. When an anomaly is detected, it instantly routes actionable alerts to developers via Telegram/Discord, minimizing downtime and mitigating potential exploits before they escalate.

## ✨ Key Features
*   **Latency Monitor:** Continuously tracks block generation time to detect sequencer lagging or node failures.
*   **Gas Spike Detector:** Identifies abnormal network congestion and potential spam attacks by monitoring Gwei fluctuations.
*   **Automated Alerting System:** Generates real-time logs and pushes critical alerts to development teams.

## ⚙️ Proof of Concept (PoC)
The `main.py` script included in this repository demonstrates the core logic of the Sentinel agent. It connects directly to the Mantle RPC, listens for new blocks, evaluates the metrics against predefined safety thresholds, and triggers localized alerts.
