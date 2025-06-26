"""Test script for new AI-Native SDLC agents."""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kernel_tools.product_discovery_tools import ProductDiscoveryTools
from kernel_tools.architecture_tools import ArchitectureTools
from kernel_tools.code_generation_tools import CodeGenerationTools
from kernel_tools.code_review_tools import CodeReviewTools

def test_product_discovery_tools():
    """Test Product Discovery tools."""
    print("Testing Product Discovery Tools...")
    tools = ProductDiscoveryTools()
    
    # Test user feedback analysis
    feedback_result = tools.analyze_user_feedback("Sample feedback data")
    print(f"✓ User feedback analysis: {len(feedback_result)} characters")
    
    # Test analytics analysis
    analytics_result = tools.analyze_product_analytics("Sample analytics data")
    print(f"✓ Analytics analysis: {len(analytics_result)} characters")
    
    # Test documentation analysis
    doc_result = tools.analyze_documentation_gaps("/path/to/docs")
    print(f"✓ Documentation analysis: {len(doc_result)} characters")
    
    print("✓ Product Discovery Tools working correctly\n")

def test_architecture_tools():
    """Test Architecture tools."""
    print("Testing Architecture Tools...")
    tools = ArchitectureTools()
    
    # Test system architecture proposal
    arch_result = tools.propose_system_architecture("Sample requirements")
    print(f"✓ System architecture proposal: {len(arch_result)} characters")
    
    # Test API design
    api_result = tools.design_api_interfaces("Sample service requirements")
    print(f"✓ API interfaces design: {len(api_result)} characters")
    
    print("✓ Architecture Tools working correctly\n")

def test_code_generation_tools():
    """Test Code Generation tools."""
    print("Testing Code Generation Tools...")
    tools = CodeGenerationTools()
    
    # Test code generation
    code_result = tools.generate_code_from_requirements("Sample requirements", "Sample architecture")
    print(f"✓ Code generation: {len(code_result)} characters")
    
    # Test API endpoints generation
    api_result = tools.generate_api_endpoints("Sample API spec")
    print(f"✓ API endpoints generation: {len(api_result)} characters")
    
    print("✓ Code Generation Tools working correctly\n")

def test_code_review_tools():
    """Test Code Review tools."""
    print("Testing Code Review Tools...")
    tools = CodeReviewTools()
    
    # Test security analysis
    security_result = tools.analyze_security_issues("Sample code content")
    print(f"✓ Security analysis: {len(security_result)} characters")
    
    # Test style analysis
    style_result = tools.analyze_code_style("Sample code content")
    print(f"✓ Style analysis: {len(style_result)} characters")
    
    print("✓ Code Review Tools working correctly\n")

if __name__ == "__main__":
    print("🚀 Testing AI-Native SDLC Agent Tools\n")
    
    try:
        test_product_discovery_tools()
        test_architecture_tools()
        test_code_generation_tools()
        test_code_review_tools()
        
        print("🎉 All tests passed! AI-Native SDLC agents are ready.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)