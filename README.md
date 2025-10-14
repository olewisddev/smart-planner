# smart-planner
Prototype for campaign planning dashboard. Backend is built with FastAPI while frontend is built with VueJS.

## Running locally

First run the backend. This requires `uv` package manager.

```
cd <project-directory>/backend
uv run ./app/main.py
```

Then run the front end.

```
cd <project-directory>/frontend
npm run dev
```

By default, app is accessible from `http://localhost:5000/`.


## Run with docker

```
docker build -t <container-name> -f Dockerfile.dev .
docker run -p 8000:8000 -p 5000:5000 <container-name>
```

App is accessible from `http://localhost:5000/`.