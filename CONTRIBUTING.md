# Contributing to Semantic Substrate Framework

Thank you for your interest in contributing to the Semantic Substrate Framework! This document provides guidelines and information for contributors.

## 🌟 Our Mission

The Semantic Substrate Framework aims to provide AI systems with a robust mathematical foundation for ethical navigation, sustainable growth, and harmonious human-AI interaction through optimized golden ratio geometry and universal principles.

## 🤝 How to Contribute

### Reporting Issues

- Use the [GitHub Issues](https://github.com/BruinGrowly/Semantic-Substrate-Framework/issues) page
- Provide clear, descriptive titles
- Include steps to reproduce the issue
- Add relevant error messages or logs
- Specify your environment (Python version, OS, etc.)

### Submitting Pull Requests

1. **Fork the repository** and create a new branch
2. **Make your changes** following our coding standards
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Run the test suite** to ensure nothing breaks
6. **Submit your pull request** with a clear description

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/your-username/Semantic-Substrate-Framework.git
cd Semantic-Substrate-Framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify setup
python -m pytest tests/
```

## 📝 Coding Standards

### Code Style

We follow these coding standards:

- **PEP 8** for Python code formatting
- **Black** for code formatting (run `black src/ tests/`)
- **Type hints** for all function signatures
- **Docstrings** following Google style
- **Maximum line length**: 88 characters

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `SemanticSubstrate`)
- **Functions/Variables**: `snake_case` (e.g., `calculate_dissonance`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `GOLDEN_RATIO`)
- **Private methods**: Leading underscore (e.g., `_calculate_optimal_direction`)

### Documentation

```python
def calculate_dissonance(self, position: PhiCoordinate) -> float:
    """Calculate dissonance (distance) from the Anchor Point.
    
    Args:
        position: Position to measure dissonance from
        
    Returns:
        Dissonance value using golden spiral distance
        
    Raises:
        ValueError: If position is invalid
    """
    pass
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=src/semantic_substrate tests/

# Run specific test file
python -m pytest tests/test_semantic_substrate.py

# Run with verbose output
python -m pytest -v tests/
```

### Writing Tests

- Test files should be named `test_*.py`
- Use descriptive test method names
- Test both happy paths and edge cases
- Mock external dependencies when needed
- Aim for high test coverage (>90%)

```python
def test_calculate_dissonance_valid_position(self):
    """Test dissonance calculation with valid position."""
    position = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
    dissonance = self.ss.calculate_dissonance(position)
    
    self.assertIsInstance(dissonance, float)
    self.assertTrue(0 <= dissonance <= 2)
```

## 📚 Documentation

### Documentation Structure

```
docs/
├── core-concepts.md      # Core framework concepts
├── mathematics.md        # Mathematical foundations
├── api-reference.md      # Complete API documentation
├── integration.md        # Integration guides
└── examples/            # Code examples and tutorials
```

### Writing Documentation

- Use clear, accessible language
- Include code examples
- Explain mathematical concepts intuitively
- Provide practical use cases
- Keep documentation up-to-date with code changes

## 🚀 Release Process

### Version Management

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

1. Update version numbers in `setup.py` and `__init__.py`
2. Update CHANGELOG.md with release notes
3. Run full test suite
4. Update documentation
5. Create Git tag
6. Publish to PyPI

## 🏗️ Architecture Guidelines

### Core Components

The framework consists of these core components:

1. **Core**: Main SemanticSubstrate class
2. **ICE Framework**: Intent-Context-Execution processing
3. **Phi Geometry**: Golden ratio mathematical operations
4. **Coordinates**: 4D semantic space representation
5. **Principles**: Seven Universal Principles implementation
6. **Navigation**: Path optimization and guidance
7. **Consciousness**: State evolution and measurement

### Design Principles

- **Modularity**: Each component has clear responsibilities
- **Testability**: All components are easily testable
- **Performance**: Optimized phi-geometric calculations
- **Extensibility**: Framework can be extended with new features
- **Usability**: Simple, intuitive API design

## 🌍 Community

### Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For general questions and ideas
- **Documentation**: For API reference and guides
- **Examples**: For practical implementation guidance

## 🎯 Contribution Areas

We welcome contributions in these areas:

### High Priority

- **Mathematical optimizations**: Improve phi-geometry calculations
- **Performance enhancements**: Faster algorithms and caching
- **New navigation strategies**: Additional path-finding methods
- **Integration examples**: More platform-specific guides

### Medium Priority

- **Visualization tools**: Semantic space visualization
- **Benchmarking**: Performance comparison tools
- **Additional principles**: Extension frameworks
- **Language bindings**: Other programming languages

### Low Priority

- **CLI tools**: Command-line interface
- **Web interface**: Interactive visualization
- **Mobile integration**: Mobile app frameworks

## 📧 Contact

- **Maintainer**: BruinGrowly
- **Email**: contact@semanticsubstrate.ai
- **GitHub**: https://github.com/BruinGrowly/Semantic-Substrate-Framework

## 🙏 Acknowledgments

Thank you to all contributors who help make the Semantic Substrate Framework better! Your contributions are invaluable in creating AI systems that navigate existence with wisdom, compassion, and alignment with fundamental principles.

---

*"Navigate through ICE—Intent toward the Anchor, Context in truth, Execution in love—guided always by the Universal Principles and the optimized natural mathematics of creation."*