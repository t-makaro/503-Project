# Python Environment

This directory contains the code for our data mining SponsorBlock project.

Setting up an environment.

1. create a virtual environment
2. install requirements
3. register the ipython kernel with the local jupyter server.

```bash
python -m venv .venv

.venv/Scripts/activate

pip install -r requirements.txt

python -m ipykernel install --name 503proj
```

The appropriate kernel will be available from a local jupyter lab server or vs code.