# CGM-AIDCryptographicMethodAnalysis

Author - Suhasini Prakash
Mentor - Sabina Sokol
Organization - Institute for Computing in Research

---  

## Goal

This project aims to simulate various encryption methods used to communicate between the continuous glucose monitor (CGM) and automated insulin delivery (AID) system.

---  

## Quick Start - Run the Simulation

Note: the terminal commands below are suited for a Linux/macOS system

### 1. Clone Repository & Setup

```bash
git clone https://github.com/hasinivp/CGM-AIDCryptographicMethodAnalysis.git

cd CGM_Simulation/

```

### 2. Install Dependencies

Due to the potential for system-level dependency conflicts, using a venv for this simmulation is recommended. 

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install pycryptodome cryptography pandas
```

### 3. Run Simulation + Generate Results

```bash
python3 main.py
```
Running this will generate a results.csv file

### 4. Plot Results 

```bash
python3 results_plot.py
```
