from flask import Flask, render_template, request
import yaml

app = Flask(__name__)

def generate_deployment_yaml(name, image, requests_cpu, requests_memory, limits_cpu, limits_memory, ports, label_key, label_value, env_key, env_value):
    resources = {
        'requests': {
            'cpu': requests_cpu,
            'memory': requests_memory,
        },
        'limits': {
            'cpu': limits_cpu,
            'memory': limits_memory,
        },
    }
    labels = {label_key: label_value}
    env = {env_key: env_value}

    deployment = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': name,
            'labels': labels,
        },
        'spec': {
            'replicas': 1,
            'selector': {
                'matchLabels': labels,
            },
            'template': {
                'metadata': {
                    'labels': labels,
                },
                'spec': {
                    'containers': [
                        {
                            'name': name,
                            'image': image,
                            'resources': resources,
                            'ports': [{'containerPort': port} for port in ports],
                            'env': [{'name': key, 'value': value} for key, value in env.items()],
                        },
                    ],
                },
            },
        },
    }

    return yaml.dump(deployment)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        image = request.form.get('image')
        requests_cpu = request.form.get('requests_cpu')
        requests_memory = request.form.get('requests_memory')
        limits_cpu = request.form.get('limits_cpu')
        limits_memory = request.form.get('limits_memory')
        ports = list(map(int, request.form.get('ports').split(',')))
        label_key = request.form.get('label_key')
        label_value = request.form.get('label_value')
        env_key = request.form.get('env_key')
        env_value = request.form.get('env_value')

        yaml_data = generate_deployment_yaml(name, image, requests_cpu, requests_memory, limits_cpu, limits_memory, ports, label_key, label_value, env_key, env_value)
        return render_template('index.html', yaml_data=yaml_data)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
