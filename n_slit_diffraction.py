import numpy as np
import matplotlib.pyplot as plt

def main():
    print("N-Slit Diffraction Pattern Simulation")
    n = int(input("Enter number of slits (n): "))
    wavelength = float(input("Enter wavelength (in nm): ")) * 1e-9
    a = float(input("Enter slit width (in micrometers): ")) * 1e-6
    d = float(input("Enter distance between slits (in micrometers): ")) * 1e-6
    I0 = 1
    theta = np.linspace(-0.01, 0.01, 2000)
    beta = (np.pi * a * np.sin(theta)) / wavelength
    delta = (2 * np.pi * d * np.sin(theta)) / wavelength
    I = I0 * (np.sin(beta) / beta) ** 2 * (np.sin(n * delta / 2) / np.sin(delta / 2)) ** 2
    I[np.isnan(I)] = I0
    plt.figure(figsize=(9, 5))
    plt.plot(theta * 1e3, I, color='purple', linewidth=1.5)
    plt.title(f"{n}-Slit Diffraction Pattern")
    plt.xlabel("Angle (mrad)")
    plt.ylabel("Normalized Intensity (I / I₀)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    main()
