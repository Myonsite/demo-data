# Contributing to Demo Data Generator

Thank you for your interest in contributing to the Demo Data Generator! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please be respectful and inclusive in all interactions.

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive criticism
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Git
- Docker and Docker Compose (optional)
- PostgreSQL (for local development)

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/demo-data.git
   cd demo-data
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/Myonsite/demo-data.git
   ```

4. **Install dependencies**
   ```bash
   npm install
   ```

5. **Set up environment**
   ```bash
   cp config/example.yaml config/local.yaml
   # Edit config/local.yaml with your settings
   ```

6. **Run tests**
   ```bash
   npm test
   ```

## Development Process

### Branch Naming

- `feature/` - New features (e.g., `feature/add-fhir-export`)
- `fix/` - Bug fixes (e.g., `fix/memory-leak`)
- `docs/` - Documentation updates (e.g., `docs/update-readme`)
- `refactor/` - Code refactoring (e.g., `refactor/generator-architecture`)
- `test/` - Test additions or fixes (e.g., `test/add-integration-tests`)

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
type(scope): subject

body

footer
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test additions or modifications
- `chore`: Build process or auxiliary tool changes

Examples:
```bash
feat(generator): add support for FHIR R4 export
fix(validation): correct age validation for pediatric patients
docs(api): update API documentation for new endpoints
```

### Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests and linting**
   ```bash
   npm test
   npm run lint
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat(scope): add new feature"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Process

1. **Before submitting**
   - Ensure all tests pass
   - Update documentation
   - Add entries to CHANGELOG.md
   - Rebase on latest main branch

2. **PR Title Format**
   - Use conventional commit format
   - Be descriptive but concise
   - Example: `feat(generator): add support for clinical trial data generation`

3. **PR Description Template**
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests pass
   - [ ] Integration tests pass
   - [ ] Manual testing completed

   ## Checklist
   - [ ] My code follows the project style guidelines
   - [ ] I have performed a self-review
   - [ ] I have added tests for my changes
   - [ ] I have updated the documentation
   ```

4. **Review Process**
   - PRs require at least one approval
   - Address all feedback promptly
   - Keep PRs focused and reasonably sized

## Coding Standards

### TypeScript Guidelines

```typescript
// Use meaningful variable names
const patientAge = calculateAge(birthDate);  // ✓ Good
const a = calc(bd);                         // ✗ Bad

// Use async/await over promises
async function fetchData() {
  try {
    const data = await api.get('/patients');
    return data;
  } catch (error) {
    logger.error('Failed to fetch patients', error);
    throw error;
  }
}

// Document complex functions
/**
 * Generates realistic vital signs based on patient demographics
 * @param patient - Patient entity with age and conditions
 * @param options - Generation options
 * @returns Generated vital signs
 */
export function generateVitalSigns(
  patient: Patient,
  options: VitalSignOptions = {}
): VitalSigns {
  // Implementation
}
```

### File Organization

```
src/
├── generators/        # Data generators
│   ├── base/         # Base classes
│   ├── medical/      # Medical data generators
│   └── demographic/  # Demographic generators
├── validators/       # Data validators
├── exporters/       # Export engines
├── scenarios/       # Business scenarios
└── utils/           # Utilities
```

## Testing

### Test Structure

```typescript
describe('PatientGenerator', () => {
  describe('generateDemographics', () => {
    it('should generate age-appropriate data', () => {
      // Test implementation
    });

    it('should respect configuration constraints', () => {
      // Test implementation
    });
  });
});
```

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- patient-generator.test.ts

# Run in watch mode
npm run test:watch
```

### Test Requirements

- Unit tests for all new functions
- Integration tests for scenarios
- Minimum 80% code coverage
- Performance tests for large datasets

## Documentation

### Code Documentation

- Use JSDoc for all public APIs
- Include examples in documentation
- Document complex algorithms
- Keep README.md updated

### API Documentation

```typescript
/**
 * @api {post} /generate Generate demo data
 * @apiName GenerateData
 * @apiGroup Generator
 * 
 * @apiParam {String} scenario Scenario name
 * @apiParam {Object} config Generation configuration
 * 
 * @apiSuccess {String} jobId Background job ID
 * @apiSuccess {String} status Job status
 * 
 * @apiExample {curl} Example usage:
 *     curl -X POST http://localhost:3000/generate \
 *       -H "Content-Type: application/json" \
 *       -d '{"scenario": "healthcare-clinic", "config": {...}}'
 */
```

## Community

### Getting Help

- Check existing issues and discussions
- Join our Discord server
- Read the documentation
- Ask questions in discussions

### Reporting Issues

When reporting issues, include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information
- Relevant logs or error messages

### Feature Requests

- Check if already requested
- Provide use case and context
- Explain why it would benefit others
- Be open to alternative solutions

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to Demo Data Generator! 🎉 