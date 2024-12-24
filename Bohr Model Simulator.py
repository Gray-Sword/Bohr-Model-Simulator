import matplotlib.pyplot as plt
import numpy as np

# Constants
PLANCK_CONSTANT = 6.626e-34  # (J·s)
SPEED_OF_LIGHT = 3.0e8       # (m/s)
RYDBERG_CONSTANT = 1.097e7   # (m^-1)

def calculate_wavelength(n1, n2):
   
    if n1 == n2:
        raise ValueError("Initial and final energy levels must be different.")
    
    inverse_wavelength = RYDBERG_CONSTANT * (1 / n2**2 - 1 / n1**2)
    wavelength = 1 / inverse_wavelength
    return wavelength

def visualize_bohr_model():
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    levels = [1, 2, 3, 4, 5]
    for n in levels:
        circle = plt.Circle((0, 0), n, color='blue', fill=False, linestyle='dotted', linewidth=0.8)
        ax.add_artist(circle)
        ax.text(0, -n - 0.1, f"n={n}", fontsize=10, ha='center')
    
    x = np.linspace(0, 4, 100)
    y = np.sqrt(4**2 - x**2)  # Equation for a semicircle
    
    ax.plot(x, y, linestyle='--', color='red', label="Sample Transition (n=4 -> n=2)")
    ax.plot(-x, y, linestyle='--', color='red')
    
    # Graph settings
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.set_title("Bohr Model of the Hydrogen Atom", fontsize=16)
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def main():
    print("Welcome to the Bohr Model Simulator!")
    print("This program calculates the wavelength of light emitted or absorbed during electron transitions in a hydrogen atom.")
    
    try:
        n1 = int(input("Enter the initial energy level (n1): "))
        n2 = int(input("Enter the final energy level (n2): "))
        if n1 <= 0 or n2 <= 0:
            raise ValueError("Energy levels must be positive integers.")
        
        wavelength = calculate_wavelength(n1, n2)
        wavelength_nm = wavelength * 1e9  # Convert to nanometers
        
        print(f"\nTransition: n={n1} -> n={n2}")
        print(f"Wavelength: {wavelength:.2e} meters ({wavelength_nm:.2f} nanometers)")
        print("Visualizing the Bohr model...")
        
        visualize_bohr_model()
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
