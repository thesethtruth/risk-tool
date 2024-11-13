# Tool Stack Specification

## Technology Stack

- **Database**: MySQL – for structured storage of risk data and related tables.
- **Backend**: FastAPI – to handle API requests, process data, and serve the application logic.
- **Frontend**: Next.js – to create a dynamic and responsive user interface.
- **Styling**: Tailwind CSS – for responsive design and rapid styling.
- **UI Components**: shadcn – to provide pre-styled and accessible UI components that integrate smoothly with Tailwind CSS.

## Copilot Workspace Instructions

### Initialize the Backend with FastAPI

1. Set up a FastAPI project as the backend.
2. Configure MySQL as the database, using SQLAlchemy or an ORM of choice to define the data models for Risk, Measures, Mapping, and Scoring.
3. Implement API endpoints for creating, reading, updating, and deleting risk data, with routes that follow RESTful principles.
4. Add endpoints specifically for fetching rubrix data, saving risk entries, and managing related measures.

### Database Setup with MySQL

1. Connect FastAPI to a MySQL database instance.
2. Define and migrate the database models, creating tables for Risk, Measures, Mapping, and Scoring.
3. Ensure relationships are correctly set up, especially the many-to-many relationship between Risk and Measures.

### Develop the Frontend with Next.js and Tailwind CSS

1. Initialize a Next.js project as the frontend.
2. Use Tailwind CSS to design a responsive layout, ensuring that components adapt well across devices.
3. Set up views as described:
   - Risk Input View with columns and input fields as per the project requirements.
   - Metadata Form for entering project information.

### Use shadcn for UI Components

1. Integrate shadcn components within the Next.js project to handle elements like buttons, tables, modals, and form inputs.
2. Apply Tailwind CSS classes to shadcn components to maintain styling consistency and enhance component interactivity.

### Testing and API Integration

1. Create API calls in Next.js to interact with the FastAPI backend, using Axios or Fetch for HTTP requests.
2. Test all endpoints for creating, updating, and retrieving data from MySQL, ensuring seamless data flow between the frontend and backend.

## Installation and Setup

### Initialize a New Next.js Project

If you don't have an existing Next.js project, create one using the following command:

```bash
npx create-next-app@latest my-app --typescript --tailwind --eslint
```

This command sets up a new Next.js project with TypeScript, Tailwind CSS, and ESLint configured.

### Install shadcn

Navigate to your project directory and initialize shadcn:

```bash
cd my-app
npx shadcn@latest init
```

During initialization, you'll be prompted to select options such as style, base color, and whether to use CSS variables. Choose according to your project's design requirements.

### Add Components

After setting up shadcn, you can add components to your project. For example, to add a button component:

```bash
npx shadcn@latest add button
```

This command adds the Button component to your project, which you can import and use in your application.

### Import and Use Components

In your application, import the components as needed. For instance, to use the Button component:

```javascript
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  );
}
```

This setup integrates Tailwind CSS and shadcn into your Next.js project, allowing you to utilize pre-designed components and customize them as needed.

## Starting the Project

### Backend

1. Navigate to the backend directory:

```bash
cd backend
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:

```bash
uvicorn main:app --reload
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

Your application should now be running, with the backend available at `http://localhost:8000` and the frontend available at `http://localhost:3000`.
