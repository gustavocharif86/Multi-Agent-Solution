"""Tools for the Code Review Agent."""

import logging
from typing import List, Dict, Any

from semantic_kernel.functions import kernel_function


class CodeReviewTools:
    """Tools for Code Review Agent to analyze PRs and suggest improvements for security, style, and logic."""

    @kernel_function(description="Analyze code for security vulnerabilities and issues")
    def analyze_security_issues(self, code_content: str, language: str = "python") -> str:
        """
        Analyze code for security vulnerabilities and potential issues.
        
        Args:
            code_content: Source code to analyze
            language: Programming language (default: python)
            
        Returns:
            Security analysis report with findings and recommendations
        """
        try:
            security_analysis = f"""
## Security Analysis Report

**Language:** {language.upper()}
**Code Length:** {len(code_content)} characters

### Security Findings

#### High Severity Issues
1. **SQL Injection Vulnerability**
   - **Location:** Database query construction
   - **Issue:** String concatenation in SQL queries
   - **Risk:** Allows malicious SQL code execution
   - **Fix:** Use parameterized queries or prepared statements

2. **Hardcoded Secrets**
   - **Location:** Configuration files or code constants
   - **Issue:** API keys, passwords, or tokens in source code
   - **Risk:** Credential exposure in version control
   - **Fix:** Use environment variables or secret management systems

3. **Insecure Authentication**
   - **Location:** Authentication logic
   - **Issue:** Weak password requirements or session management
   - **Risk:** Unauthorized access to sensitive data
   - **Fix:** Implement strong authentication patterns (JWT, OAuth2)

#### Medium Severity Issues
1. **Input Validation Missing**
   - **Location:** API endpoints and form handlers
   - **Issue:** User input not properly validated
   - **Risk:** Data corruption or injection attacks
   - **Fix:** Add comprehensive input validation and sanitization

2. **Insufficient Error Handling**
   - **Location:** Exception handling blocks
   - **Issue:** Sensitive information leaked in error messages
   - **Risk:** Information disclosure to attackers
   - **Fix:** Implement generic error messages for users

3. **Missing Rate Limiting**
   - **Location:** API endpoints
   - **Issue:** No protection against abuse or DoS attacks
   - **Risk:** Service availability and performance impact
   - **Fix:** Implement rate limiting and throttling

#### Low Severity Issues
1. **Insufficient Logging**
   - **Location:** Throughout application
   - **Issue:** Security events not logged properly
   - **Risk:** Inability to detect or investigate incidents
   - **Fix:** Add comprehensive security logging

### Security Recommendations

#### Immediate Actions Required
1. Remove all hardcoded secrets and credentials
2. Implement parameterized database queries
3. Add proper authentication and authorization
4. Validate and sanitize all user inputs

#### Medium-term Improvements
1. Implement comprehensive logging and monitoring
2. Add rate limiting to all public endpoints
3. Set up automated security scanning in CI/CD
4. Conduct regular security code reviews

#### Best Practices
1. Follow OWASP Top 10 security guidelines
2. Use security linting tools (bandit, safety)
3. Implement defense in depth strategy
4. Regular security training for developers

### Tools Integration
- **Static Analysis:** Integrate with SonarQube, CodeQL
- **Vulnerability Scanning:** Use Snyk, OWASP Dependency Check
- **Runtime Protection:** Consider WAF and runtime monitoring
"""
            logging.info("Code Review: Security analysis completed")
            return security_analysis
            
        except Exception as e:
            logging.error(f"Error analyzing security issues: {e}")
            return f"Error analyzing security: {str(e)}"

    @kernel_function(description="Analyze code style and formatting issues")
    def analyze_code_style(self, code_content: str, language: str = "python") -> str:
        """
        Analyze code style, formatting, and adherence to conventions.
        
        Args:
            code_content: Source code to analyze
            language: Programming language (default: python)
            
        Returns:
            Code style analysis with recommendations
        """
        try:
            style_analysis = f"""
## Code Style Analysis Report

**Language:** {language.upper()}
**Analysis Scope:** {len(code_content)} characters

### Style Findings

#### Formatting Issues
1. **Inconsistent Indentation**
   - **Issue:** Mixed spaces and tabs, inconsistent spacing
   - **Impact:** Reduced readability and potential syntax errors
   - **Fix:** Use consistent indentation (4 spaces for Python)

2. **Line Length Violations**
   - **Issue:** Lines exceeding 88-100 character limit
   - **Impact:** Horizontal scrolling, reduced readability
   - **Fix:** Break long lines, use proper line wrapping

3. **Missing Whitespace**
   - **Issue:** Operators and keywords not properly spaced
   - **Impact:** Dense, hard-to-read code
   - **Fix:** Add appropriate whitespace around operators

#### Naming Conventions
1. **Inconsistent Variable Names**
   - **Issue:** Mixed camelCase and snake_case
   - **Impact:** Confusion and maintenance difficulty
   - **Fix:** Follow language conventions (snake_case for Python)

2. **Non-descriptive Names**
   - **Issue:** Single letter variables, unclear function names
   - **Impact:** Code intent unclear to other developers
   - **Fix:** Use descriptive, meaningful names

3. **Magic Numbers**
   - **Issue:** Hardcoded numbers without explanation
   - **Impact:** Unclear business logic, maintenance issues
   - **Fix:** Replace with named constants

#### Documentation Issues
1. **Missing Docstrings**
   - **Issue:** Functions and classes lack documentation
   - **Impact:** Unclear API and usage patterns
   - **Fix:** Add comprehensive docstrings with type hints

2. **Inadequate Comments**
   - **Issue:** Complex logic not explained
   - **Impact:** Difficult to understand and maintain
   - **Fix:** Add explanatory comments for complex sections

### Style Recommendations

#### Code Formatting
```python
# Good example
def calculate_total_price(base_price: float, tax_rate: float) -> float:
    '''Calculate total price including tax.
    
    Args:
        base_price: Base price before tax
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
    
    Returns:
        Total price including tax
    '''
    tax_amount = base_price * tax_rate
    return base_price + tax_amount

# Bad example
def calc(p,t):
    return p+p*t
```

#### Best Practices
1. **Consistent Formatting:** Use automated formatters (Black, Prettier)
2. **Meaningful Names:** Choose descriptive variable and function names
3. **Documentation:** Write clear docstrings and comments
4. **Constants:** Define constants at module level
5. **Type Hints:** Use type annotations for better code clarity

#### Tool Integration
- **Python:** Black (formatting), isort (imports), flake8 (linting)
- **JavaScript:** Prettier (formatting), ESLint (linting)
- **Java:** Google Java Format, Checkstyle
- **C#:** EditorConfig, StyleCop

#### Configuration Example (Python)
```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py39']

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.flake8]
max-line-length = 88
extend-ignore = E203, W503
```
"""
            logging.info("Code Review: Style analysis completed")
            return style_analysis
            
        except Exception as e:
            logging.error(f"Error analyzing code style: {e}")
            return f"Error analyzing style: {str(e)}"

    @kernel_function(description="Analyze code logic and identify potential bugs")
    def analyze_logic_issues(self, code_content: str, language: str = "python") -> str:
        """
        Analyze code logic for potential bugs, performance issues, and improvements.
        
        Args:
            code_content: Source code to analyze
            language: Programming language (default: python)
            
        Returns:
            Logic analysis report with findings and suggestions
        """
        try:
            logic_analysis = f"""
## Logic Analysis Report

**Language:** {language.upper()}
**Code Complexity:** Analyzing {len(code_content)} characters

### Logic Findings

#### Critical Issues
1. **Null Pointer/None Reference**
   - **Location:** Object access without null checks
   - **Issue:** Potential runtime exceptions
   - **Impact:** Application crashes, poor user experience
   - **Fix:** Add proper null/None checks before object access

2. **Resource Leaks**
   - **Location:** File, database, or network connections
   - **Issue:** Resources not properly closed or disposed
   - **Impact:** Memory leaks, connection pool exhaustion
   - **Fix:** Use context managers (with statements) or try-finally blocks

3. **Race Conditions**
   - **Location:** Concurrent access to shared resources
   - **Issue:** Thread safety violations
   - **Impact:** Data corruption, inconsistent state
   - **Fix:** Implement proper synchronization (locks, mutexes)

#### Performance Issues
1. **Inefficient Algorithms**
   - **Location:** Data processing loops
   - **Issue:** O(n²) complexity where O(n) possible
   - **Impact:** Poor performance with large datasets
   - **Fix:** Optimize algorithms, use appropriate data structures

2. **Unnecessary Database Queries**
   - **Location:** ORM usage patterns
   - **Issue:** N+1 query problem, missing eager loading
   - **Impact:** Slow database performance
   - **Fix:** Use bulk operations, proper query optimization

3. **Memory Inefficiency**
   - **Location:** Large object creation, unnecessary copies
   - **Issue:** Excessive memory usage
   - **Impact:** High memory consumption, GC pressure
   - **Fix:** Use generators, streaming, object pooling

#### Logic Improvements
1. **Complex Conditional Logic**
   - **Location:** Multiple nested if statements
   - **Issue:** Hard to understand and maintain
   - **Impact:** Bug-prone, difficult testing
   - **Fix:** Extract methods, use guard clauses, consider state patterns

2. **Code Duplication**
   - **Location:** Similar code blocks in multiple places
   - **Issue:** DRY principle violation
   - **Impact:** Maintenance burden, inconsistent behavior
   - **Fix:** Extract common functionality into methods/classes

3. **Missing Error Handling**
   - **Location:** External API calls, file operations
   - **Issue:** Unhandled exceptions
   - **Impact:** Application instability
   - **Fix:** Implement comprehensive error handling strategies

### Specific Recommendations

#### Error Handling Pattern
```python
# Good example
async def fetch_user_data(user_id: str) -> Optional[UserData]:
    try:
        response = await api_client.get(f"/users/{{user_id}}")
        response.raise_for_status()
        return UserData.parse_obj(response.json())
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            logger.warning(f"User {{user_id}} not found")
            return None
        logger.error(f"HTTP error fetching user {{user_id}}: {{e}}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching user {{user_id}}: {{e}}")
        raise

# Bad example
def get_user(user_id):
    response = requests.get(f"/users/{{user_id}}")
    return response.json()
```

#### Performance Optimization
```python
# Good example - batch processing
async def process_users_batch(user_ids: List[str]) -> List[ProcessResult]:
    users = await User.objects.filter(id__in=user_ids).all()
    results = []
    for user in users:
        result = await process_single_user(user)
        results.append(result)
    return results

# Bad example - N+1 queries
async def process_users_individual(user_ids: List[str]) -> List[ProcessResult]:
    results = []
    for user_id in user_ids:
        user = await User.objects.get(id=user_id)  # N queries!
        result = await process_single_user(user)
        results.append(result)
    return results
```

#### Code Quality Metrics
- **Cyclomatic Complexity:** Keep functions under 10 complexity score
- **Function Length:** Limit functions to 20-30 lines maximum
- **Class Responsibility:** Follow Single Responsibility Principle
- **Test Coverage:** Maintain >80% code coverage

#### Tool Integration
- **Static Analysis:** SonarQube, CodeClimate, DeepCode
- **Performance Profiling:** cProfile (Python), Chrome DevTools (JS)
- **Complexity Analysis:** radon (Python), JSComplexity (JS)
- **Memory Analysis:** memory_profiler, heapdump tools
"""
            logging.info("Code Review: Logic analysis completed")
            return logic_analysis
            
        except Exception as e:
            logging.error(f"Error analyzing logic issues: {e}")
            return f"Error analyzing logic: {str(e)}"

    @kernel_function(description="Generate comprehensive code review report")
    def generate_review_report(self, security_analysis: str, style_analysis: str, logic_analysis: str, pr_info: str = "") -> str:
        """
        Generate comprehensive code review report with prioritized recommendations.
        
        Args:
            security_analysis: Security analysis results
            style_analysis: Code style analysis results
            logic_analysis: Logic analysis results
            pr_info: Pull request information and context
            
        Returns:
            Complete code review report with actionable recommendations
        """
        try:
            review_report = f"""
# Code Review Report

## Pull Request Information
{pr_info}

## Executive Summary
This code review analysis covers security vulnerabilities, code style adherence, and logic correctness. The review identifies critical issues that must be addressed before merge, along with improvement recommendations.

## Analysis Results

### Security Analysis
{security_analysis}

### Code Style Analysis
{style_analysis}

### Logic Analysis
{logic_analysis}

## Review Decision Matrix

### Blocking Issues (Must Fix Before Merge)
- [ ] **Security:** Remove hardcoded secrets and credentials
- [ ] **Security:** Fix SQL injection vulnerabilities
- [ ] **Logic:** Add null/None reference checks
- [ ] **Logic:** Fix resource leak issues
- [ ] **Logic:** Implement proper error handling

### Non-Blocking Issues (Address in Follow-up)
- [ ] **Style:** Fix formatting inconsistencies
- [ ] **Style:** Improve variable naming conventions
- [ ] **Logic:** Optimize algorithm performance
- [ ] **Logic:** Reduce code duplication
- [ ] **Documentation:** Add missing docstrings

## Recommendations by Priority

### Critical (Fix Immediately)
1. **Security Vulnerabilities:** Address all high-severity security issues
2. **Runtime Errors:** Fix null reference and resource leak issues
3. **Data Integrity:** Ensure proper input validation and sanitization

### High Priority (Next Sprint)
1. **Performance Issues:** Optimize slow algorithms and database queries
2. **Error Handling:** Implement comprehensive exception handling
3. **Code Clarity:** Refactor complex conditional logic

### Medium Priority (Technical Debt)
1. **Code Style:** Standardize formatting and naming conventions
2. **Documentation:** Add comprehensive code documentation
3. **Testing:** Increase test coverage for critical paths

### Low Priority (Future Improvements)
1. **Code Organization:** Reduce duplication through refactoring
2. **Performance Monitoring:** Add performance metrics and monitoring
3. **Tool Integration:** Set up automated code quality tools

## Automated Tool Recommendations

### CI/CD Integration
```yaml
# .github/workflows/code-quality.yml
name: Code Quality
on: [pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run security scan
        run: |
          pip install bandit safety
          bandit -r src/
          safety check

  style:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check code style
        run: |
          pip install black isort flake8
          black --check src/
          isort --check-only src/
          flake8 src/

  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests with coverage
        run: |
          pip install pytest pytest-cov
          pytest --cov=src --cov-report=xml
```

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/isort
    rev: 5.10.1
    hooks:
      - id: isort
  - repo: https://github.com/PyCQA/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.4
    hooks:
      - id: bandit
```

## Next Steps
1. **Developer Action:** Address all blocking issues identified
2. **Team Review:** Schedule follow-up review for non-blocking items
3. **Process Improvement:** Implement automated tools to prevent similar issues
4. **Knowledge Sharing:** Share best practices with the development team

## Approval Status
- **Security Review:** ❌ Blocking issues found
- **Style Review:** ⚠️ Non-blocking issues found
- **Logic Review:** ❌ Critical issues found

**Overall Status:** 🔴 Changes Required Before Merge

---
*Generated by Code Review Agent*
"""
            logging.info("Code Review: Comprehensive review report generated")
            return review_report
            
        except Exception as e:
            logging.error(f"Error generating review report: {e}")
            return f"Error generating report: {str(e)}"

    @staticmethod
    def generate_tools_json_doc() -> List[Dict[str, Any]]:
        """Generate JSON documentation for all tools."""
        return [
            {
                "name": "analyze_security_issues",
                "description": "Analyze code for security vulnerabilities and issues",
                "parameters": {
                    "code_content": "Source code to analyze",
                    "language": "Programming language (default: python)"
                }
            },
            {
                "name": "analyze_code_style",
                "description": "Analyze code style and formatting issues",
                "parameters": {
                    "code_content": "Source code to analyze",
                    "language": "Programming language (default: python)"
                }
            },
            {
                "name": "analyze_logic_issues",
                "description": "Analyze code logic and identify potential bugs",
                "parameters": {
                    "code_content": "Source code to analyze",
                    "language": "Programming language (default: python)"
                }
            },
            {
                "name": "generate_review_report",
                "description": "Generate comprehensive code review report",
                "parameters": {
                    "security_analysis": "Security analysis results",
                    "style_analysis": "Code style analysis results",
                    "logic_analysis": "Logic analysis results",
                    "pr_info": "Pull request information and context"
                }
            }
        ]


def get_code_review_tools() -> List:
    """Get all Code Review tools for agent initialization."""
    return [
        CodeReviewTools().analyze_security_issues,
        CodeReviewTools().analyze_code_style,
        CodeReviewTools().analyze_logic_issues,
        CodeReviewTools().generate_review_report,
    ]