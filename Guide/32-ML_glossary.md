---
layout: guide
---

# Machine Learning Glossary

This glossary provides short definitions for common machine learning and data science terms discussed in CMSE 802. The goal is not to memorize every definition but to become familiar with the language used when discussing data-driven models.

## Observation

A single example or measurement in a dataset.

Examples:

- One weather measurement
- One patient record
- One image
- One experimental trial

Observations are often represented as rows in a table.

## Feature

A measurable property or characteristic of an observation.

Examples:

- Age
- Temperature
- Pressure
- Height
- Pixel intensity

Features are often represented as columns in a table.

## Label

The value a supervised learning model is attempting to predict.

Examples:

- House price
- Disease diagnosis
- Species name
- Product category

Labels are also called targets or outputs.

## Dataset

A collection of observations used for analysis or machine learning.

A dataset typically contains:

- observations (rows)
- features (columns)
- optional labels

## Model

A mathematical or computational representation learned from data.

A model is used to:

- make predictions
- identify patterns
- estimate relationships
- support decision making

## Training Set

The portion of a dataset used to build or fit a machine learning model.

The model learns from this data.

## Testing Set

The portion of a dataset used to evaluate model performance on previously unseen data.

Testing helps estimate how well a model will perform in practice.

## Validation Set

A separate dataset used while selecting models or tuning hyperparameters.

Validation data helps prevent accidentally overfitting the testing set.

## Supervised Learning

Machine learning using labeled examples.

The model learns a relationship between inputs and known outputs.

Examples:

- Predicting house prices
- Predicting equipment failure
- Classifying images

## Unsupervised Learning

Machine learning without labels.

The goal is often to discover structure, groups, or patterns in the data.

Examples:

- Clustering
- Anomaly detection
- Dimensionality reduction

## Classification

A supervised learning task that predicts categories.

Examples:

- Spam vs Not Spam
- Dog vs Cat
- Healthy vs Diseased

The output is a discrete category.

## Regression

A supervised learning task that predicts numerical values.

Examples:

- Temperature
- Stock prices
- Population size
- Blood pressure

The output is a continuous value.

## Clustering

An unsupervised learning technique that groups similar observations together.

Examples:

- Customer segmentation
- Identifying groups of galaxies
- Organizing documents by topic

## Hyperparameter

A setting chosen by the user before training begins.

Examples:

- Number of trees in a random forest
- Learning rate
- Maximum tree depth

Different hyperparameters can produce very different models.

## Overfitting

When a model learns the training data too well and fails to generalize to new data.

Symptoms include:

- Excellent training performance
- Poor testing performance

Overfitting is one of the most common machine learning problems.

## Underfitting

When a model is too simple to capture meaningful patterns in the data.

Symptoms include:

- Poor training performance
- Poor testing performance

## Generalization

A model's ability to perform well on new, unseen data.

Good machine learning models generalize beyond the examples used during training.

## Curse of Dimensionality

As the number of features increases, the amount of data required to train a reliable model often increases dramatically.

Consequences include:

- Increased overfitting risk
- Greater computational cost
- Reduced model reliability

More features are not always better.

## Rule of 10

A common machine learning heuristic:

> Aim for roughly 10 observations for every feature included in a model.

This is not a strict rule, but it helps researchers think critically about whether a dataset contains enough information to support a particular model.

## Cross Validation

A model evaluation technique that repeatedly splits a dataset into training and testing subsets.

Cross validation often provides a more reliable estimate of model performance than a single train/test split.

## Feature Engineering

The process of creating, selecting, or transforming features to improve model performance.

Examples:

- Normalization
- Log transforms
- Combining multiple measurements
- Creating new derived variables

## Dimensionality Reduction

Techniques that reduce the number of features while attempting to preserve useful information.

Examples:

- Principal Component Analysis (PCA)
- Autoencoders

## AutoML

Automated Machine Learning.

AutoML systems attempt to automate tasks such as:

- model selection
- hyperparameter tuning
- feature selection
- pipeline construction

Examples:

- TPOT
- AutoSklearn
- H2O AutoML

## Generative AI

AI systems that generate new content rather than simply making predictions.

Examples:

- ChatGPT
- Claude
- Gemini
- GitHub Copilot

Generative AI is often useful for working with unstructured information such as:

- text
- images
- code
- documents

## Foundation Model

A large model trained on broad datasets and later adapted to specific tasks.

Examples:

- GPT models
- Llama models
- Claude models

## Hallucination

When a generative AI system produces incorrect information while presenting it as if it were accurate.

Hallucinations are one reason that AI-generated content should always be reviewed and validated.

## Model Evaluation

The process of determining whether a model is useful and trustworthy.

Common evaluation questions include:

- How accurate is the model?
- Does it generalize?
- Is it overfitting?
- Is the model reproducible?
- Does the model make scientific sense?

## Ugly Duckling Principle

There is no universally best machine learning algorithm.

Different datasets, problems, and assumptions often favor different models.

As a result, researchers frequently:

- compare multiple algorithms
- tune multiple hyperparameters
- evaluate competing solutions

A model should be judged by its performance and suitability for the problem, not by its popularity.