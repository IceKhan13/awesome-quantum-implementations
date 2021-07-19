<p align="center">
  <a href="https://qiskit.org/">
    <img alt="Qiskit" src="https://qiskit.org/images/qiskit-logo.png" width="70" />
  </a>
</p>

Awesome quantum
===============

Curated by community list of implementations of quantum algorithms, software packages, 

## Repositories:

### Core

- https://github.com/Qiskit/qiskit-terra
- https://github.com/Qiskit/qiskit-machine-learning
- https://github.com/Qiskit/qiskit-experiments
- https://github.com/Qiskit/qiskit-aer 
- https://github.com/Qiskit/qiskit-nature
- https://github.com/Qiskit/qiskit-tutorials
- https://github.com/Qiskit/qiskit.org


### Community
{% for repo in repos %}
- {{ repo.link }} by {{ repo.author }}
{% endfor %}
  

### Requirements for project

Any project should follow submission guidelines: 
- tests
- documentation
- coverage



