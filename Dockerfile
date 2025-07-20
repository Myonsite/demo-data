# Multi-stage build for Demo Data Generator
FROM node:20-alpine AS builder

# Install build dependencies
RUN apk add --no-cache python3 make g++

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./
COPY tsconfig.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY src ./src
COPY config ./config
COPY templates ./templates

# Build TypeScript
RUN npm run build

# Production stage
FROM node:20-alpine

# Install runtime dependencies
RUN apk add --no-cache postgresql-client redis

# Create non-root user
RUN addgroup -g 1001 -S appuser && \
    adduser -S appuser -u 1001

# Set working directory
WORKDIR /app

# Copy built application
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

# Copy configuration and templates
COPY config ./config
COPY templates ./templates
COPY data/schemas ./data/schemas

# Create directories
RUN mkdir -p output logs data/local && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Set environment variables
ENV NODE_ENV=production
ENV LOG_LEVEL=info

# Expose port for API (if needed)
EXPOSE 3000

# Default command
CMD ["node", "dist/cli.js"] 