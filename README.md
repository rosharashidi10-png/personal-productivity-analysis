
🌌 Quantum Mission Control: Simulating the Future from Arak
A Comparative Study of Qubit Fidelity & Error Correction Resilience
> "In a city with no quantum labs, I turned my laptop into one."
> This project is born out of curiosity and a refusal to let geographical boundaries limit scientific exploration. As a student in Arak, Iran, I built this simulator to understand how we might keep quantum states alive in a noisy, warm world.
> 
🎯 The Research Challenge
Quantum computers are incredibly fragile. A slight change in temperature or the "Pink Noise" of the universe can destroy a calculation. This simulator explores:
 * Architecture Sensitivity: How Superconducting (SC) vs. Trapped-Ion (TI) qubits handle thermal drift and correlated noise.
 * Mitigation Efficacy: The quantitative impact of Quantum Error Correction (QEC) protocols on preserving quantum information.
🔬 Scientific & Technical Features
 * Realistic Noise Modeling: Implementation of Pink Noise (1/f) via frequency-domain Fourier shaping to mimic realistic environmental decoherence.
 * Thermal Dynamics: A time-dependent model simulating daily temperature oscillations and its impact on qubit fidelity based on established literature coefficients.
 * Deterministic Simulation: Engineered for reproducibility using fixed random seeds and fully vectorized NumPy pipelines for high-performance computation.
 * Interactive Visualization: A dual-pane Plotly dashboard for real-time analysis of fidelity evolution and temperature-noise correlations.
📈 Key Insights
 * Superconducting (SC) Qubits: Highly sensitive to thermal fluctuations, yet show a significant ~30% mean fidelity improvement upon QEC activation.
 * Trapped-Ion (TI) Qubits: Exhibit superior intrinsic stability; they remain the "steady runners" under thermal stress with lower baseline error rates.
 * The Verdict: The simulation validates that QEC is a fundamental necessity for scaling superconducting architectures in non-cryogenic-perfect environments.
🧠 The Learning Journey & AI Ethics
Facing limited access to specialized labs or mentors, I utilized AI as a "Collaborative Digital Tutor" to master advanced concepts:
 * Agency: I conceived the research framework, designed the simulation architecture, and implemented the core physical logic.
 * Methodology: AI was used to bridge knowledge gaps in complex mathematics (FFT for noise shaping) and to refine the efficiency of data processing.
   This project stands as a testament to ethical AI-assisted learning—leveraging tools to enhance, not replace, human curiosity and effort.
🚀 Execution
# Clone the repository
git clone https://github.com/rosharashidi10-png/quantum-mission-control.git

# Install requirements
pip install -r requirements.txt

# Run simulation
python quantum_simulator.py

Built with ❤️ and Python by Rosha Rashidi | Arak, Iran Dedicated to democratizing quantum education through open-source exploration.
