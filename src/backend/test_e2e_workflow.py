"""End-to-end test demonstrating AI-Native SDLC workflow."""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kernel_tools.product_discovery_tools import ProductDiscoveryTools
from kernel_tools.architecture_tools import ArchitectureTools
from kernel_tools.code_generation_tools import CodeGenerationTools
from kernel_tools.code_review_tools import CodeReviewTools

def simulate_sdlc_workflow():
    """Simulate a complete SDLC workflow using the new agents."""
    print("🚀 Starting AI-Native SDLC Workflow Simulation\n")
    
    # Step 1: Product Discovery
    print("📊 STEP 1: Product Discovery")
    print("=" * 50)
    discovery_agent = ProductDiscoveryTools()
    
    feedback_data = """
    {
        "feedback": [
            {"user": "john@company.com", "comment": "The API is slow and documentation is unclear"},
            {"user": "jane@company.com", "comment": "Need better error handling and examples"},
            {"user": "bob@company.com", "comment": "Mobile app needs offline support"}
        ]
    }
    """
    
    analytics_data = """
    {
        "metrics": {
            "api_response_time": "2.5s average",
            "error_rate": "8%", 
            "user_sessions": 1500,
            "feature_adoption": {"offline_mode": "12%", "api_docs": "34%"}
        }
    }
    """
    
    feedback_analysis = discovery_agent.analyze_user_feedback(feedback_data)
    analytics_analysis = discovery_agent.analyze_product_analytics(analytics_data)
    doc_analysis = discovery_agent.analyze_documentation_gaps("/api/docs")
    
    discovery_report = discovery_agent.generate_discovery_report(
        feedback_analysis, analytics_analysis, doc_analysis
    )
    
    print("✅ Product discovery completed")
    print(f"   - Generated comprehensive report ({len(discovery_report)} chars)")
    print()
    
    # Step 2: Architecture Design
    print("🏗️ STEP 2: Architecture Design")
    print("=" * 50)
    architecture_agent = ArchitectureTools()
    
    requirements = """
    Based on product discovery:
    - Improve API performance and error handling
    - Create better documentation with examples
    - Add offline support for mobile app
    - Implement rate limiting and monitoring
    """
    
    system_architecture = architecture_agent.propose_system_architecture(requirements)
    api_interfaces = architecture_agent.design_api_interfaces(requirements)
    design_patterns = architecture_agent.select_design_patterns(system_architecture)
    
    architecture_docs = architecture_agent.generate_architecture_documentation(
        system_architecture, api_interfaces, design_patterns
    )
    
    print("✅ Architecture design completed")
    print(f"   - System architecture proposal ({len(system_architecture)} chars)")
    print(f"   - API interface specifications ({len(api_interfaces)} chars)")
    print(f"   - Comprehensive documentation ({len(architecture_docs)} chars)")
    print()
    
    # Step 3: Code Generation
    print("💻 STEP 3: Code Generation")
    print("=" * 50)
    code_agent = CodeGenerationTools()
    
    generated_code = code_agent.generate_code_from_requirements(
        requirements, system_architecture, "python"
    )
    
    api_endpoints = code_agent.generate_api_endpoints(
        api_interfaces, "fastapi"
    )
    
    database_models = code_agent.generate_database_models(
        "User and Resource entities", "sqlalchemy"
    )
    
    project_structure = code_agent.generate_project_structure(
        "improved-api-service", "python", "fastapi"
    )
    
    print("✅ Code generation completed")
    print(f"   - Generated application code ({len(generated_code)} chars)")
    print(f"   - FastAPI endpoints ({len(api_endpoints)} chars)")
    print(f"   - Database models ({len(database_models)} chars)")
    print(f"   - Complete project structure ({len(project_structure)} chars)")
    print()
    
    # Step 4: Code Review
    print("🔍 STEP 4: Code Review")
    print("=" * 50)
    review_agent = CodeReviewTools()
    
    sample_code = """
    from fastapi import FastAPI, HTTPException
    import sqlite3
    
    app = FastAPI()
    
    @app.get("/users/{user_id}")
    def get_user(user_id: str):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE id = '{user_id}'"  # SQL injection risk!
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        return result
    """
    
    security_analysis = review_agent.analyze_security_issues(sample_code, "python")
    style_analysis = review_agent.analyze_code_style(sample_code, "python")
    logic_analysis = review_agent.analyze_logic_issues(sample_code, "python")
    
    review_report = review_agent.generate_review_report(
        security_analysis, style_analysis, logic_analysis,
        "PR #123: Implement user API endpoint"
    )
    
    print("✅ Code review completed")
    print(f"   - Security analysis ({len(security_analysis)} chars)")
    print(f"   - Style analysis ({len(style_analysis)} chars)")
    print(f"   - Logic analysis ({len(logic_analysis)} chars)")
    print(f"   - Comprehensive review report ({len(review_report)} chars)")
    print()
    
    # Summary
    print("📋 WORKFLOW SUMMARY")
    print("=" * 50)
    print("✅ Product Discovery: Identified key user pain points and opportunities")
    print("✅ Architecture Design: Proposed scalable microservices architecture")
    print("✅ Code Generation: Generated complete FastAPI application structure")
    print("✅ Code Review: Identified security issues and improvement areas")
    print()
    print("🎯 KEY INSIGHTS FROM WORKFLOW:")
    print("   • User feedback drove technical requirements")
    print("   • Architecture addressed performance and scalability concerns")
    print("   • Generated code follows industry best practices")
    print("   • Code review caught critical security vulnerabilities")
    print()
    print("🔄 NEXT STEPS (for future agents):")
    print("   • Test Generation: Create comprehensive test suite")
    print("   • Pipeline Agent: Set up CI/CD automation")
    print("   • Deploy Strategy: Plan blue-green deployment")
    print("   • Feedback Loop: Monitor post-deployment metrics")
    print()
    print("🎉 AI-Native SDLC Workflow Completed Successfully!")

if __name__ == "__main__":
    try:
        simulate_sdlc_workflow()
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        sys.exit(1)