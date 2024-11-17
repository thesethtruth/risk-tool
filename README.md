# Risk tool

## Technology Stack

- **Database**: MySQL – for structured storage of risk data and related tables.
- **Backend**: FastAPI – to handle API requests, process data, and serve the application logic.
- **Frontend**: Svelte.js (5) – to create a dynamic and responsive user interface.
- **Styling**: Tailwind CSS – for responsive design and rapid styling.
- **UI Components**: shadcn – to provide pre-styled and accessible UI components that integrate smoothly with Tailwind CSS.

## Starting the Project

### Backend

1. Navigate to the backend directory:

```bash
cd backend
```

2. Install the required dependencies:

```bash
poetry install
```

3. Start the FastAPI server:

```bash
fastapi dev
```

### Frontend

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install the required dependencies:

```bash
npm install
```

3. Start the Next.js development server:

```bash
npm run dev
```

Your application should now be running, with the backend available at `http://localhost:8000` and the frontend available at `http://localhost:5174`.
