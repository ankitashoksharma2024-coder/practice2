DOCKER PRACTICAL TEMPLATE — SINGLE APP.PY

You asked for no separate logic.py. All six question types are in app.py.
In the assessment, open app.py and DELETE the sections for the five questions you do not get. Keep only:
- the functions for your question
- the route logic for your question
- the shared Flask setup and /health endpoint

Keep the Dockerfile, workflow, deployment.yaml, service.yaml and requirements.txt unchanged unless your instructor's environment requires changes.

QUESTIONS / SECTIONS IN app.py:
Q1 calculator: add, subtract, multiply, divide
Q2 grades: calculate_marks
Q3 shopping: calculate_bill
Q4 temperature: c_to_f, f_to_c
Q5 banking: deposit, withdraw
Q6 library: add_book, view_books, issue_book

Then update test_app.py to test only the functions/routes you kept.

TEST:
pip install -r requirements.txt
pytest
python app.py
Open http://localhost:5000

GITHUB PUSH PROCESS:
Create an empty GitHub repository, then in the project terminal:
git init
git branch -M main
git add .
git commit -m "Initial version"
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main

For Push 2, change app.py and test_app.py, then:
git add .
git commit -m "Add second-stage features"
git push origin main

GITHUB SECRETS REQUIRED:
DOCKERHUB_USERNAME = Docker Hub username
DOCKERHUB_TOKEN = Docker Hub access token
KUBE_CONFIG_B64 = base64-encoded kubeconfig for a Kubernetes cluster reachable from GitHub-hosted Actions runners

Create a Docker Hub repository named practical-app.
A local Kubernetes cluster on your laptop is normally not reachable from a GitHub-hosted runner. Use the cluster/access method supplied by your instructor.
The workflow uses the GitHub run number for unique image tags; if extra workflow runs occur, tags may skip v1/v2 but remain unique.
