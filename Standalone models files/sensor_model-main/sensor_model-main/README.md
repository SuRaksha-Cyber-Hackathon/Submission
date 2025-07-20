# sensor_model

## Overview

`sensor_model` is a Jupyter Notebook-based project for behavioral biometric authentication using sensor and interaction event data from devices. It builds and tests a Siamese neural network that distinguishes between real and impostor users based on multi-modal sensor data, such as accelerometer, gyroscope, and user interactions (taps, swipes, keypresses).

## Features

- **Sensor Data Processing**: Extracts fixed-length, time-windowed features from raw JSON data including accelerometer, gyroscope, tap, swipe, and keypress events.
- **Siamese Neural Network**: Implements and trains a Siamese network for user verification.
- **Contrastive Loss**: Uses contrastive loss to optimize the embedding distance for same/different user pairs.
- **Threshold Tuning**: Systematically tests and tunes distance thresholds for distinguishing genuine users from imposters.
- **Test/Validation**: Includes utilities for running and evaluating model performance on multiple users.

## Requirements

- Python 3.x
- Jupyter Notebook
- PyTorch (`torch`)
- NumPy

Install dependencies (example with pip):

```bash
pip install torch numpy jupyter
```

## Usage

1. **Prepare Data**: Place your behavioral data in a JSON file (e.g., `data_store1.json`), following the expected format with user IDs and sensor/interactions events.

2. **Feature Extraction**: The notebook extracts time-windowed features for each user using accelerometer, gyroscope, and interaction events.

3. **Training**: Run the notebook to initialize and train the Siamese network:

    - Feature vectors are grouped into positive (same user) and negative (different user) pairs.
    - The model is trained using contrastive loss.

4. **Testing**: The notebook provides code for:

    - Loading the trained model.
    - Running verification tests for same/different user pairs.
    - Experimenting with different threshold values to find the best separation between genuine and impostor attempts.

5. **Threshold Selection**: Analyze test results to choose an optimal distance threshold (e.g., 1.2 separates real vs anomaly in example output).

## Example Output

```
📌 TEST RESULTS
[SAME USER]   Distance: 1.0530 | Match: False
[DIFF USER]   Distance: 1.7755 | Match: False

📊 Running multi-user tests with threshold = 1.2

🔁 SAME-USER PAIRS
[User: bbc7f6] Distance: 1.0530 | Match: True
[User: c9f16b] Distance: 0.5300 | Match: True

⚔️ DIFFERENT-USER PAIRS
[Users: bbc7f6 vs c9f16b] Distance: 1.7755 | Match: False
```

## File Structure

- `sensor_model.ipynb`: Main Jupyter Notebook with all code for data loading, feature extraction, model training, and evaluation.
- `README.md`: Project documentation (this file).

## Notes

- Make sure your data JSON matches the structure expected in the notebook.
- The code is designed for research and prototyping; further improvements may be needed for production use.

## License

*No license specified yet. Please add a LICENSE file if you intend to share or reuse this code.*

---

For questions or contributions, open an issue or pull request in the repository.
