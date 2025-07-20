# One Shot Learning Keystroke Authentication

A one-shot learning approach for keystroke dynamics authentication that can learn to authenticate users from minimal training data.

## Overview

This project implements a one-shot learning model for keystroke authentication, designed to authenticate users based on their typing patterns with minimal training samples. Unlike traditional approaches that require extensive training data, this system can learn user patterns from just a few examples.

## Current Implementation

### Data Loading
```python
import pandas as pd
df = pd.read_csv('keypress_events.csv')
df.head()
```

### Dataset Structure
The system expects keystroke data with the following format:
- User keystroke events with timing information
- Minimal samples per user (suitable for one-shot learning)
- Features extracted from typing dynamics

## Requirements

```bash
pip install pandas numpy torch scikit-learn matplotlib
```

## Dataset Format

Expected CSV structure for `keypress_events.csv`:
- `user_id`: Unique identifier for each user
- `key_code`: Numeric code for pressed keys
- `key_label`: Human-readable key labels
- `duration_ms`: Key hold duration
- `timestamp`: Keystroke timing

## Planned Architecture

### One-Shot Learning Approach
- **Siamese Networks**: Learn similarity between keystroke patterns
- **Prototypical Networks**: Create user prototypes from few examples
- **Meta-Learning**: Learn to learn from limited data
- **Distance Metrics**: Compare keystroke dynamics efficiently

### Key Components (To Be Implemented)
1. **Few-Shot Enrollment**: Register users with minimal samples
2. **Similarity Learning**: Compare new samples to enrolled patterns
3. **Adaptive Thresholding**: Dynamic authentication thresholds
4. **Fast Inference**: Real-time authentication decisions

## Development Status

**Current Phase**: Initial data exploration and loading

**Next Steps**:
1. Feature engineering for one-shot learning
2. Implement Siamese network architecture
3. Create few-shot training pipeline
4. Develop evaluation metrics for one-shot scenarios

## Expected Benefits

- **Low Data Requirements**: Authenticate with 1-5 samples per user
- **Fast Enrollment**: Quick user registration
- **Scalable**: Easy addition of new users
- **Efficient**: Minimal computational overhead

## Use Cases

- **Quick User Onboarding**: Immediate authentication setup
- **Emergency Authentication**: When limited training data available  
- **Dynamic Environments**: Frequently changing user base
- **Resource-Constrained Systems**: Low memory/computation requirements

## File Structure

```
├── keypress_events.csv      # Keystroke dataset
├── one_shot_model.py        # One-shot learning implementation (planned)
├── utils.py                 # Utility functions (planned)
└── README.md               # This file
```

## Future Implementation

### Planned Features
- Siamese network for keystroke similarity
- Support vector one-class classification
- Metric learning approaches
- Cross-user generalization
- Real-time adaptation

### Expected Performance
- Authentication with 1-3 keystroke samples
- Fast inference (< 100ms)
- Competitive accuracy with minimal data
- Easy user enrollment process

## Contributing

This project is in early development phase. The one-shot learning model architecture and implementation are currently being designed and developed.

---

**Status**: Under Development - One-shot learning implementation in progress
