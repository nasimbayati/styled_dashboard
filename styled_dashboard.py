# styled_dashboard.py
import numpy as np
import matplotlib.pyplot as plt

class StyledDashboard:
    """
    Generates a 2x2 matplotlib dashboard with uniquely styled subplots using custom curves
    and layout formatting for educational and presentation purposes.
    """

    @staticmethod
    def render():
        x = np.linspace(-10, 10, 400)

        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        fig.suptitle("Styled Function Plot Dashboard", fontsize=16, color='navy')

        # Subplot 1 – Custom oscillation curve
        y1 = np.sin(x) * np.exp(-x**2 / 20)
        axs[0, 0].plot(x, y1, color='tomato', linestyle='--', linewidth=2, label='Damped Sine')
        axs[0, 0].set_title("Damped Oscillation")
        axs[0, 0].legend()
        axs[0, 0].grid(True)
        axs[0, 0].set_facecolor('#fdf6e3')

        # Subplot 2 – Wavy ramp curve
        y2 = np.sin(x / 2) + x / 5
        axs[0, 1].plot(x, y2, color='mediumseagreen', linestyle='-', linewidth=2, label='Ramp Wave')
        axs[0, 1].set_title("Oscillating Ramp")
        axs[0, 1].legend()
        axs[0, 1].grid(True)
        axs[0, 1].set_facecolor('#e6f2ff')

        # Subplot 3 – Quadratic envelope
        y3 = np.tanh(x) * x**2 / 10
        axs[1, 0].plot(x, y3, color='darkviolet', linewidth=2, label='Tanh Envelope')
        axs[1, 0].set_title("Nonlinear Growth")
        axs[1, 0].legend()
        axs[1, 0].grid(True)
        axs[1, 0].set_facecolor('#f0e6ff')

        # Subplot 4 – Exponential dip
        y4 = np.exp(-np.abs(x)) * np.cos(2 * x)
        axs[1, 1].plot(x, y4, color='darkorange', linewidth=2, label='Exponential Cosine')
        axs[1, 1].set_title("Exponential Modulated Cosine")
        axs[1, 1].legend()
        axs[1, 1].grid(True)
        axs[1, 1].set_facecolor('#fff5e6')

        for ax in axs.flat:
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Y Axis")

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()


if __name__ == "__main__":
    StyledDashboard.render()