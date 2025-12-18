import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import display, HTML
import time
from tqdm import tqdm
from typing import Tuple


class QuantumMissionControl:
    """
    Quantum Mission Control
    -----------------------
    Simulation framework for time-dependent qubit fidelity under
    temperature fluctuations and correlated noise.

    Objective:
    Comparative analysis of Superconducting (SC) and Trapped-Ion (TI)
    qubits before and after Quantum Error Correction (QEC) activation.
    """

    def __init__(self, duration_days: int = 120, qec_day: int = 75, seed: int = 42):
        """
        Initialize simulation parameters.

        :param duration_days: Total simulation horizon (days)
        :param qec_day: QEC activation time (day index)
        :param seed: Random seed for reproducibility
        """
        if duration_days <= 0 or qec_day < 0 or qec_day > duration_days:
            raise ValueError("Invalid configuration: check duration_days and qec_day.")

        self.duration_days = duration_days
        self.ticks = duration_days * 24  # hourly resolution
        self.qec_day = qec_day
        np.random.seed(seed)

    def pink_noise(self, n: int) -> np.ndarray:
        """
        Generate pink (1/f) noise via frequency-domain shaping.

        :param n: Number of samples
        :return: Pink noise signal
        """
        white = np.random.randn(n)
        f = np.fft.rfftfreq(n)
        f[0] = 1.0  # numerical stability
        spectrum = np.fft.rfft(white) / np.sqrt(f)
        return np.fft.irfft(spectrum, n)

    def run_simulation(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Execute fidelity simulation with thermal drift and correlated noise.

        Optimization:
        - Vectorized computation
        - Single-pass noise generation

        :return: days, fidelity_sc, fidelity_ti, temperature
        """
        t = np.arange(self.ticks)
        days = t / 24.0

        # Ambient temperature model: daily oscillation + stochastic perturbation
        temp = 15 + 5 * np.sin(2 * np.pi * t / 24) + np.random.normal(0, 1, self.ticks)

        qec_active = (days >= self.qec_day)

        print("Running quantum system simulation...")

        noise = self.pink_noise(self.ticks) * 0.02

        # Baseline fidelity models
        base_sc = 0.70 - (temp - 15) * 0.012 + noise
        base_ti = 0.85 - (temp - 15) * 0.004 + noise * 0.5

        # QEC performance uplift
        base_sc[qec_active] += 0.22
        base_ti[qec_active] += 0.07

        fidelity_sc = np.clip(base_sc, 0, 1)
        fidelity_ti = np.clip(base_ti, 0, 1)

        # Progress indicator (non-computational)
        for _ in tqdm(range(10), desc="Simulation progress", ncols=80):
            time.sleep(0.05)

        return days, fidelity_sc, fidelity_ti, temp

    def plot_dashboard(self) -> None:
        """
        Render interactive dashboard:
        - Time evolution of qubit fidelity
        - Temperature–fidelity correlation
        """
        days, sc, ti, temp = self.run_simulation()

        fig = make_subplots(
            rows=2,
            cols=1,
            subplot_titles=(
                "Quantum Fidelity Over Time",
                "Temperature–Fidelity Correlation"
            ),
            vertical_spacing=0.12
        )

        fig.add_trace(
            go.Scatter(
                x=days,
                y=sc,
                name="Superconducting Qubits (SC)",
                line=dict(color='cyan', width=3),
                hovertemplate='Day: %{x:.1f}<br>Fidelity: %{y:.2f}'
            ),
            row=1,
            col=1
        )

        fig.add_trace(
            go.Scatter(
                x=days,
                y=ti,
                name="Trapped-Ion Qubits (TI)",
                line=dict(color='magenta', width=3),
                hovertemplate='Day: %{x:.1f}<br>Fidelity: %{y:.2f}'
            ),
            row=1,
            col=1
        )

        fig.add_vline(
            x=self.qec_day,
            line=dict(dash='dash', color='white'),
            annotation_text="QEC Activation",
            annotation_position="top left"
        )

        step = 50
        fig.add_trace(
            go.Scatter(
                x=temp[::step],
                y=sc[::step],
                mode='markers',
                name="SC vs Temperature",
                marker=dict(color='cyan', size=10, opacity=0.7)
            ),
            row=2,
            col=1
        )

        fig.add_trace(
            go.Scatter(
                x=temp[::step],
                y=ti[::step],
                mode='markers',
                name="TI vs Temperature",
                marker=dict(color='magenta', size=10, opacity=0.7)
            ),
            row=2,
            col=1
        )

        fig.update_layout(
            height=900,
            width=1200,
            template="plotly_dark",
            title=dict(
                text="Advanced Quantum System Simulation Dashboard",
                font_size=24
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            hovermode="x unified"
        )

        fig.update_xaxes(title_text="Days", row=1, col=1)
        fig.update_yaxes(title_text="Fidelity", row=1, col=1)
        fig.update_xaxes(title_text="Temperature (°C)", row=2, col=1)
        fig.update_yaxes(title_text="Fidelity", row=2, col=1)

        fig.show()

        # Statistical summary
        pre_sc = sc[days < self.qec_day]
        post_sc = sc[days >= self.qec_day]
        pre_ti = ti[days < self.qec_day]
        post_ti = ti[days >= self.qec_day]

        gain_sc = (post_sc.mean() - pre_sc.mean()) / pre_sc.mean() * 100
        gain_ti = (post_ti.mean() - pre_ti.mean()) / pre_ti.mean() * 100

        analysis = f"""
        <div style="background:#1e1e1e; padding:25px; border-radius:15px; font-family:Arial; color:#eee;">
            <h3 style="color:#00ffff;">Simulation Summary</h3>
            <ul>
                <li><b>SC Qubits:</b> {gain_sc:.1f}% mean fidelity improvement after QEC</li>
                <li><b>TI Qubits:</b> {gain_ti:.1f}% mean fidelity improvement after QEC</li>
            </ul>
            <p><i>Interpretation:</i> SC systems benefit strongly from QEC but remain
            temperature-sensitive, while TI systems exhibit superior intrinsic stability.</p>
        </div>
        """
        display(HTML(analysis))


if __name__ == "__main__":
    try:
        control = QuantumMissionControl(duration_days=120, qec_day=75)
        control.plot_dashboard()
    except Exception as e:
        print(f"Execution error: {str(e)}")
