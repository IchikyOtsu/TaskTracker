# TaskTracker

```
python -m venv venv 
./venv/source/activate
pip install -r requirements.txt
python main.py
```

You will have a display of the commands.

You can type `python main.py [commands] --help`

## Description
TaskTracker is a Python-based application designed to help users manage their tasks efficiently. It allows users to create, update, and track tasks with various attributes such as status and timestamps.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To use the TaskTracker application, run the following command:
```bash
python main.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

## Contact Information
For any inquiries, please contact me !

## Testing 
python -m unittest discover tests
---

## 🚀 Future Improvements & Roadmap

This section outlines potential enhancements and features that could be added to TaskTracker. These are ideas for future development, not commitments, but represent possibilities for making the project even better.

### 🎯 Code Quality
- [ ] Improve error handling with specific exceptions instead of bare `except` clauses
- [ ] Add proper logging system to replace print statements
- [ ] Implement input validation for task IDs and names
- [ ] Standardize naming conventions and code style consistency
- [ ] Add type hints throughout the codebase

### 🧪 Testing
- [x] Create comprehensive unit tests for all utility functions
- [ ] Add integration tests for CLI commands
- [ ] Set up pytest and measure code coverage
- [ ] Test edge cases and error scenarios

### 🏗️ Architecture & Features
- [ ] Move hardcoded paths to configuration file
- [ ] Consider migrating from JSON to SQLite for better performance
- [ ] Add database backup/restore functionality
- [ ] Implement task priority levels
- [ ] Support due dates and reminders
- [ ] Add task categories/tags
- [ ] Support subtasks and task dependencies
- [ ] Add search and filter capabilities

### 🚀 User Experience
- [ ] Add colored terminal output using Click's styling
- [ ] Improve task list formatting (tables with `rich` or `tabulate`)
- [ ] Add confirmation prompts for destructive operations
- [ ] Implement task update/edit command
- [ ] Add export functionality (CSV, Markdown, etc.)
- [ ] Show task statistics and completion rates
- [ ] Add pagination for long task lists
- [ ] Create interactive TUI mode

### 🛠️ DevOps & Distribution
- [X] Fix typo: rename `requirement.txt` to `requirements.txt`
- [X] Add `.gitignore` file
- [ ] Set up code formatting with `black` and linting with `flake8`
- [ ] Configure pre-commit hooks
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Package for PyPI distribution
- [ ] Add proper versioning and changelog

### 📚 Documentation
- [X] Add examples of all CLI commands in README
- [ ] Include screenshots or demo GIFs
- [ ] Add troubleshooting section
- [ ] Include badges (build status, coverage, version)
- [ ] Add module-level docstrings

### 🔒 Security & Reliability
- [ ] Implement file locking for concurrent access prevention
- [ ] Add atomic writes for database updates
- [ ] Create automatic backups before modifications
- [ ] Add data validation on read operations

---

*Note: This roadmap represents potential improvements and is subject to change. Contributions implementing any of these features are welcome!*


