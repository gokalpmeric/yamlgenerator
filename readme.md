# Kubernetes YAML Generator

This is a simple web-based Kubernetes Deployment YAML generator. You can use this application to create Deployment YAMLs by filling out the fields in the GUI.

## Features

- User-friendly GUI to input Deployment configurations
- Generates a formatted Kubernetes Deployment YAML
- Validates all input fields to ensure they are not empty

## Fields

- Name: The name of the Deployment and the app.
- Image: The Docker image to use for the Deployment.
- Requests CPU: The CPU resource requests for the Deployment.
- Requests Memory: The memory resource requests for the Deployment.
- Limits CPU: The CPU resource limits for the Deployment.
- Limits Memory: The memory resource limits for the Deployment.
- Ports: The container ports to open for the Deployment, separated by commas (no spaces).
- Label Key: The label key for the Deployment.
- Label Value: The label value for the Deployment.
- Environment Variable Key: The environment variable key for the Deployment.
- Environment Variable Value: The environment variable value for the Deployment.

## Usage

1. Clone the repository and navigate to the project directory.
2. Install Flask if you haven't already: `pip install flask`
3. Run the application: `python main.py`
4. Open a web browser and go to `http://localhost:5000`.
5. Fill out the fields in the GUI and click "Generate" to generate the Deployment YAML.

## Note

This application is intended for simple use cases and does not support all possible Kubernetes configurations. Always check the generated YAML to ensure it meets your needs before applying it to a Kubernetes cluster.


