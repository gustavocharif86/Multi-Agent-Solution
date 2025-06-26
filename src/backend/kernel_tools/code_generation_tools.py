"""Tools for the Code Generation Agent."""

import logging
from typing import List, Dict, Any

from semantic_kernel.functions import kernel_function


class CodeGenerationTools:
    """Tools for Code Generation Agent to write code based on prompts, architecture, and file structure."""

    @kernel_function(description="Generate code based on requirements and architecture")
    def generate_code_from_requirements(self, requirements: str, architecture: str, language: str = "python") -> str:
        """
        Generate code based on requirements and architectural specifications.
        
        Args:
            requirements: Functional requirements or user stories
            architecture: Architecture specifications and design patterns
            language: Target programming language (default: python)
            
        Returns:
            Generated code with documentation and structure
        """
        try:
            code_template = self._get_language_template(language)
            
            generated_code = f"""
# Generated Code - {language.upper()}

## Requirements Implementation
Based on requirements: {requirements[:100]}...
Following architecture: {architecture[:100]}...

{code_template}

## Code Structure

### Main Application
```{language}
{self._generate_main_application_code(language, requirements)}
```

### Service Layer
```{language}
{self._generate_service_layer_code(language)}
```

### Data Models
```{language}
{self._generate_data_models_code(language)}
```

### API Endpoints
```{language}
{self._generate_api_endpoints_code(language)}
```

### Configuration
```{language}
{self._generate_configuration_code(language)}
```

## Implementation Notes
- Code follows {language} best practices and conventions
- Includes proper error handling and logging
- Implements security measures and validation
- Uses dependency injection for testability
- Follows SOLID principles

## Next Steps
1. Review generated code for business logic accuracy
2. Add unit tests for all components
3. Integrate with existing codebase
4. Set up CI/CD pipeline
"""
            logging.info(f"Code Generation: {language} code generated from requirements")
            return generated_code
            
        except Exception as e:
            logging.error(f"Error generating code from requirements: {e}")
            return f"Error generating code: {str(e)}"

    @kernel_function(description="Generate API endpoints based on specifications")
    def generate_api_endpoints(self, api_spec: str, framework: str = "fastapi") -> str:
        """
        Generate API endpoints based on API specifications.
        
        Args:
            api_spec: API specification (OpenAPI/Swagger format)
            framework: Web framework to use (default: fastapi)
            
        Returns:
            Generated API endpoint code
        """
        try:
            if framework.lower() == "fastapi":
                endpoints_code = f"""
# FastAPI Endpoints Generated from API Specification

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import logging

app = FastAPI(title="Generated API", version="1.0.0")

# Data Models
class User(BaseModel):
    id: Optional[str] = None
    email: str
    name: str
    role: str

class UserCreate(BaseModel):
    email: str
    name: str
    role: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None

# Dependency Injection
async def get_current_user():
    # Implement authentication logic
    pass

# API Endpoints
@app.get("/api/v1/users", response_model=List[User])
async def list_users(current_user: User = Depends(get_current_user)):
    '''List all users with pagination and filtering.'''
    try:
        # Implement user listing logic
        users = []  # Replace with actual database query
        return users
    except Exception as e:
        logging.error(f"Error listing users: {{e}}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/api/v1/users", response_model=User)
async def create_user(user_data: UserCreate, current_user: User = Depends(get_current_user)):
    '''Create a new user.'''
    try:
        # Implement user creation logic
        new_user = User(id="generated-id", **user_data.dict())
        return new_user
    except Exception as e:
        logging.error(f"Error creating user: {{e}}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/v1/users/{{user_id}}", response_model=User)
async def get_user(user_id: str, current_user: User = Depends(get_current_user)):
    '''Get user by ID.'''
    try:
        # Implement user retrieval logic
        user = None  # Replace with actual database query
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error getting user: {{e}}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.put("/api/v1/users/{{user_id}}", response_model=User)
async def update_user(user_id: str, user_data: UserUpdate, current_user: User = Depends(get_current_user)):
    '''Update user by ID.'''
    try:
        # Implement user update logic
        updated_user = None  # Replace with actual database update
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error updating user: {{e}}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/api/v1/users/{{user_id}}")
async def delete_user(user_id: str, current_user: User = Depends(get_current_user)):
    '''Delete user by ID.'''
    try:
        # Implement user deletion logic
        success = True  # Replace with actual database deletion
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {{"message": "User deleted successfully"}}
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error deleting user: {{e}}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health Check
@app.get("/health")
async def health_check():
    return {{"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}}
"""
            else:
                endpoints_code = f"# {framework} framework not yet implemented"
                
            logging.info(f"Code Generation: API endpoints generated for {framework}")
            return endpoints_code
            
        except Exception as e:
            logging.error(f"Error generating API endpoints: {e}")
            return f"Error generating endpoints: {str(e)}"

    @kernel_function(description="Generate database models and schemas")
    def generate_database_models(self, schema_spec: str, orm: str = "sqlalchemy") -> str:
        """
        Generate database models based on schema specifications.
        
        Args:
            schema_spec: Database schema specification
            orm: ORM framework to use (default: sqlalchemy)
            
        Returns:
            Generated database model code
        """
        try:
            if orm.lower() == "sqlalchemy":
                models_code = f"""
# SQLAlchemy Database Models

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    resources = relationship("Resource", back_populates="owner")
    
    def __repr__(self):
        return f"<User(id={{self.id}}, email={{self.email}}, name={{self.name}})>"

class Resource(Base):
    __tablename__ = 'resources'
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, nullable=False, default='active')
    owner_id = Column(String, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    owner = relationship("User", back_populates="resources")
    
    def __repr__(self):
        return f"<Resource(id={{self.id}}, title={{self.title}}, status={{self.status}})>"

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    action = Column(String, nullable=False)
    resource_type = Column(String, nullable=False)
    resource_id = Column(String)
    changes = Column(Text)  # JSON string of changes
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String)
    user_agent = Column(String)
    
    def __repr__(self):
        return f"<AuditLog(id={{self.id}}, action={{self.action}}, resource_type={{self.resource_type}})>"

# Database Configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConfig:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
    
    def get_session(self):
        return self.SessionLocal()

# Repository Pattern Implementation
from abc import ABC, abstractmethod
from typing import Optional, List

class BaseRepository(ABC):
    def __init__(self, session):
        self.session = session
    
    @abstractmethod
    def get_by_id(self, id: str):
        pass
    
    @abstractmethod
    def create(self, obj):
        pass
    
    @abstractmethod
    def update(self, obj):
        pass
    
    @abstractmethod
    def delete(self, id: str):
        pass

class UserRepository(BaseRepository):
    def get_by_id(self, id: str) -> Optional[User]:
        return self.session.query(User).filter(User.id == id).first()
    
    def get_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()
    
    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def update(self, user: User) -> User:
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def delete(self, id: str) -> bool:
        user = self.get_by_id(id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
    
    def list_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.session.query(User).offset(skip).limit(limit).all()
"""
            else:
                models_code = f"# {orm} ORM not yet implemented"
                
            logging.info(f"Code Generation: Database models generated for {orm}")
            return models_code
            
        except Exception as e:
            logging.error(f"Error generating database models: {e}")
            return f"Error generating models: {str(e)}"

    @kernel_function(description="Generate complete project structure with configuration")
    def generate_project_structure(self, project_name: str, language: str = "python", framework: str = "fastapi") -> str:
        """
        Generate complete project structure with configuration files.
        
        Args:
            project_name: Name of the project
            language: Programming language
            framework: Framework to use
            
        Returns:
            Complete project structure and configuration
        """
        try:
            structure = f"""
# Project Structure: {project_name}

## Directory Structure
```
{project_name}/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── users.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_users.py
│   └── integration/
│       ├── __init__.py
│       └── test_api.py
└── scripts/
    ├── setup.sh
    └── deploy.sh
```

## Configuration Files

### requirements.txt
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
alembic==1.13.0
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
```

### .env.example
```
# Database
DATABASE_URL=sqlite:///./test.db

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API
API_V1_STR=/api/v1
PROJECT_NAME={project_name}

# Logging
LOG_LEVEL=INFO
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/{project_name}
    depends_on:
      - db
    volumes:
      - ./src:/app/src

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: {project_name}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY scripts/ ./scripts/

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### pyproject.toml
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Generated project for {project_name}"
authors = [{{name = "Generated", email = "generated@example.com"}}]
license = {{text = "MIT"}}
dependencies = [
    "fastapi>=0.104.1",
    "uvicorn[standard]>=0.24.0",
    "sqlalchemy>=2.0.23",
    "pydantic>=2.5.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.black]
line-length = 88
target-version = ['py311']
include = '\\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
```

## Setup Instructions
1. Clone the repository
2. Copy .env.example to .env and configure
3. Install dependencies: `pip install -r requirements.txt`
4. Run database migrations: `alembic upgrade head`
5. Start the application: `uvicorn src.main:app --reload`

## Development Workflow
1. Create feature branch
2. Write tests first (TDD)
3. Implement feature
4. Run tests and linting
5. Create pull request
6. Deploy after review
"""
            logging.info(f"Code Generation: Project structure generated for {project_name}")
            return structure
            
        except Exception as e:
            logging.error(f"Error generating project structure: {e}")
            return f"Error generating structure: {str(e)}"

    def _get_language_template(self, language: str) -> str:
        """Get code template for specific language."""
        templates = {
            "python": "# Python implementation with best practices",
            "javascript": "// JavaScript implementation with modern ES6+ features",
            "java": "// Java implementation with Spring Boot framework",
            "csharp": "// C# implementation with .NET Core framework"
        }
        return templates.get(language.lower(), "# Generic implementation")

    def _generate_main_application_code(self, language: str, requirements: str) -> str:
        """Generate main application code."""
        if language.lower() == "python":
            return """
from fastapi import FastAPI
from src.api.endpoints import users
from src.config.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Generated API application"
)

app.include_router(users.router, prefix="/api/v1", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
"""
        return f"// {language} main application code"

    def _generate_service_layer_code(self, language: str) -> str:
        """Generate service layer code."""
        if language.lower() == "python":
            return """
from typing import List, Optional
from src.models.database import User, UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        return self.user_repo.create(user)
    
    async def get_user(self, user_id: str) -> Optional[User]:
        return self.user_repo.get_by_id(user_id)
    
    async def list_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.user_repo.list_users(skip, limit)
"""
        return f"// {language} service layer code"

    def _generate_data_models_code(self, language: str) -> str:
        """Generate data models code."""
        if language.lower() == "python":
            return """
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str
    role: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    role: Optional[str] = None

class User(UserBase):
    id: str
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
"""
        return f"// {language} data models code"

    def _generate_api_endpoints_code(self, language: str) -> str:
        """Generate API endpoints code."""
        if language.lower() == "python":
            return """
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.services.user_service import UserService
from src.models.database import User, UserCreate, UserUpdate

router = APIRouter()

@router.get("/users", response_model=List[User])
async def list_users(skip: int = 0, limit: int = 100):
    return await UserService().list_users(skip, limit)

@router.post("/users", response_model=User)
async def create_user(user: UserCreate):
    return await UserService().create_user(user.dict())
"""
        return f"// {language} API endpoints code"

    def _generate_configuration_code(self, language: str) -> str:
        """Generate configuration code."""
        if language.lower() == "python":
            return """
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Generated API"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
"""
        return f"// {language} configuration code"

    @staticmethod
    def generate_tools_json_doc() -> List[Dict[str, Any]]:
        """Generate JSON documentation for all tools."""
        return [
            {
                "name": "generate_code_from_requirements",
                "description": "Generate code based on requirements and architecture",
                "parameters": {
                    "requirements": "Functional requirements or user stories",
                    "architecture": "Architecture specifications and design patterns",
                    "language": "Target programming language (default: python)"
                }
            },
            {
                "name": "generate_api_endpoints",
                "description": "Generate API endpoints based on specifications",
                "parameters": {
                    "api_spec": "API specification (OpenAPI/Swagger format)",
                    "framework": "Web framework to use (default: fastapi)"
                }
            },
            {
                "name": "generate_database_models",
                "description": "Generate database models based on schema specifications",
                "parameters": {
                    "schema_spec": "Database schema specification",
                    "orm": "ORM framework to use (default: sqlalchemy)"
                }
            },
            {
                "name": "generate_project_structure",
                "description": "Generate complete project structure with configuration",
                "parameters": {
                    "project_name": "Name of the project",
                    "language": "Programming language",
                    "framework": "Framework to use"
                }
            }
        ]


def get_code_generation_tools() -> List:
    """Get all Code Generation tools for agent initialization."""
    return [
        CodeGenerationTools().generate_code_from_requirements,
        CodeGenerationTools().generate_api_endpoints,
        CodeGenerationTools().generate_database_models,
        CodeGenerationTools().generate_project_structure,
    ]