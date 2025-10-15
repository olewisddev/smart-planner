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


## Scope

Features covered:

- Table with filtering (by platform and by objective)
- Chart for CPU (grouped by platform and insight)
- Chart for cost composition
- Upload CSV of campaigns
- Insights per platform and per objective
- Insights of cost composition

Assumptions:

- No pagination for table
- No support for multiple clients
- Uses in-memory database
