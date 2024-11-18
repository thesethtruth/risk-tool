FROM node:20-slim as builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies and add node adapter
RUN npm install
RUN npm uninstall @sveltejs/adapter-static
RUN npm install --save-dev @sveltejs/adapter-node

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM node:20-slim

WORKDIR /app

# Copy package files and install production dependencies
COPY --from=builder /app/package*.json ./
RUN npm install --production

# Copy built application
COPY --from=builder /app/build ./build

# Start the application with explicit port
CMD ["node", "build", "--port", "3000"]
