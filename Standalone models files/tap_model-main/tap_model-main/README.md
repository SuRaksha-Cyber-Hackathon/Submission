# Tap Model - User Behavior Prediction System 

A sophisticated machine learning system that analyzes user tap patterns and behavior to predict user interactions across different application screens. This project implements a Siamese neural network for one-shot learning and user behavior classification.

## Project Overview

This project was developed for the **SuRaksha Cyber Hackathon** and focuses on analyzing user interaction patterns to build predictive models for cybersecurity and user authentication applications. The system can identify users based on their unique tap patterns and predict their behavior across different application contexts.

## Features

- **User Behavior Analysis**: Analyzes tap coordinates, duration, and context screens
- **Siamese Neural Network**: Implements one-shot learning for user identification
- **Multi-Screen Support**: Handles various application screens (dashboard, transfer, payments, etc.)
- **TensorFlow Lite Export**: Model optimization for mobile deployment
- **Real-time Prediction**: Fast inference for live user behavior analysis

## Dataset Features

The system analyzes the following user interaction features:

- **Spatial Coordinates**: X, Y tap positions (normalized)
- **Temporal Data**: Tap duration in milliseconds
- **Context Information**: Application screen context
- **User Identification**: Encoded user IDs
- **Session Grouping**: Aggregated user sessions

### Supported Screen Contexts:
- `RegisterPage`
- `dashboard`
- `transfer_page` 
- `pay_bills`
- `add_funds`
- `profile`
- `statements`

## Technical Architecture

### Machine Learning Pipeline:
1. **Data Preprocessing**: Label encoding and normalization
2. **Feature Engineering**: Session aggregation and feature extraction
3. **Model Training**: Siamese network with distance-based learning
4. **Model Export**: TensorFlow Lite conversion for deployment

### Key Components:
- **Siamese Neural Network**: For similarity learning and user identification
- **Label Encoders**: For categorical feature encoding
- **Feature Normalization**: Coordinate and duration scaling
- **Session Aggregation**: User behavior pattern extraction

## Requirements

```python
tensorflow-cpu==2.12.0
numpy>=1.23.5
pandas
scikit-learn
matplotlib
jax>=0.4.30
keras==2.12.0
```

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/SuRaksha-Cyber-Hackathon/tap_model.git
cd tap_model

# Install required packages
pip install tensorflow-cpu==2.12.0 numpy pandas scikit-learn matplotlib
```

### Usage

1. **Data Preparation**:
   ```python
   # Load and preprocess your tap data
   # Ensure data includes: user_id, x, y, duration_ms, timestamp, context_screen
   ```

2. **Model Training**:
   ```python
   # Run the Jupyter notebook
   jupyter notebook tap_model.ipynb
   ```

3. **Model Deployment**:
   ```python
   # The trained model is automatically saved as:
   # - siamese_model.keras (full model)
   # - tap_model.tflite (optimized for mobile)
   ```

## 📈 Model Performance

The Siamese neural network architecture provides:
- **One-shot Learning**: Ability to recognize users with minimal training examples
- **Distance-based Classification**: Euclidean distance metric for similarity measurement
- **Real-time Inference**: Optimized for low-latency predictions

## 🔧 Model Architecture

```
Input Layer (4 features: x, y, duration_ms, screen_enc)
    ↓
Dense Layer (128 neurons, ReLU)
    ↓
Dense Layer (64 neurons, ReLU)
    ↓
Dense Layer (32 neurons, ReLU)
    ↓
Output Layer (Embedding dimension)
    ↓
Distance Calculation (Euclidean)
    ↓
Classification/Prediction
```

## Mobile Deployment

The project includes TensorFlow Lite conversion for mobile deployment:

```python
# Convert to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save the optimized model
with open('tap_model.tflite', 'wb') as f:
    f.write(tflite_model)
```

## Use Cases

- **Behavioral Biometrics**: User authentication through tap patterns
- **Fraud Detection**: Identifying unusual user behavior
- **User Experience**: Personalizing interfaces based on usage patterns
- **Security Applications**: Continuous authentication systems
- **Mobile App Analytics**: Understanding user interaction patterns

## Data Format

Expected input data format:

```csv
user_id,id,x,y,duration_ms,timestamp,context_screen
user_1,1,0.25,0.45,150,1640995200000,dashboard
user_1,2,0.75,0.30,200,1640995201000,transfer_page
...
```

## License

This project is part of the SuRaksha Cyber Hackathon submission.

## Hackathon Context

**Event**: SuRaksha Cyber Hackathon  
**Focus**: Cybersecurity and User Behavior Analysis  
**Objective**: Develop innovative solutions for user authentication and behavior prediction

## Contact

For questions or collaboration opportunities related to this hackathon project, please reach out through the GitHub repository.

---

*Built with ❤️ for cybersecurity innovation*
