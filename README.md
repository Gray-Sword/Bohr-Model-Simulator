# Bohr Model Simulator

## Project Description
The Bohr Model Simulator is a Python-based application that visualizes the Bohr model of the hydrogen atom and calculates the wavelength of light emitted or absorbed during electron transitions. This project helps users understand atomic energy levels and their relationship to light's wavelength.

---

## Features
- **Electron Transition Wavelength Calculation**: Calculates the wavelength of light (in meters and nanometers) using the Rydberg formula.
- **Energy Level Visualization**: Displays a 2D representation of the hydrogen atom's energy levels (`n=1` to `n=5`) as concentric circles.
- **Sample Transition Illustration**: Highlights a specific electron transition path (e.g., `n=4 -> n=2`) with dashed lines.

---



## How to Use
1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the script:
   ```bash
   python bohr_model_simulator.py
   ```
4. Input the initial (`n1`) and final (`n2`) energy levels when prompted.
5. View the calculated wavelength in the terminal and the visualized Bohr model in a pop-up window.

---

## Example Input and Output
**Input:**
```
Enter the initial energy level (n1): 4
Enter the final energy level (n2): 2
```

**Output:**
```
Transition: n=4 -> n=2
Wavelength: 4.86e-07 meters (486.00 nanometers)
Visualizing the Bohr model...
```
A graphical window will display the Bohr model with highlighted energy levels and transitions.

---

## Formula Used
The simulator employs the Rydberg formula to compute wavelengths:
\[
\frac{1}{\lambda} = R_H \left( \frac{1}{n_2^2} - \frac{1}{n_1^2} \right)
\]
Where:
- \(\lambda\) = wavelength of light (in meters)
- \(R_H\) = Rydberg constant (1.097 \(\times\) 10\(^7\) m\(^{-1}\))
- \(n_1, n_2\) = energy levels (integers, \(n_1 > n_2\))
