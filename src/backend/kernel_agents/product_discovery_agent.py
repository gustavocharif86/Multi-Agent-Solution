"""Product Discovery Agent for analyzing feedback, analytics, and documentation to identify needs."""

import logging
from typing import Dict, List, Optional

from context.cosmos_memory_kernel import CosmosMemoryContext
from kernel_agents.agent_base import BaseAgent
from kernel_tools.product_discovery_tools import ProductDiscoveryTools, get_product_discovery_tools
from models.messages_kernel import AgentType, InputTask, Plan
from semantic_kernel.functions import KernelFunction


class ProductDiscoveryAgent(BaseAgent):
    """Agent responsible for analyzing feedback, analytics, and documentation to identify product needs."""

    def __init__(
        self,
        session_id: str,
        user_id: str,
        memory_store: CosmosMemoryContext,
        tools: Optional[List[KernelFunction]] = None,
        system_message: Optional[str] = None,
        agent_name: str = AgentType.PRODUCT_DISCOVERY.value,
        client=None,
        definition=None,
    ) -> None:
        """Initialize the Product Discovery Agent.

        Args:
            session_id: The current session identifier
            user_id: The user identifier
            memory_store: The Cosmos memory context
            tools: Optional list of tools for this agent
            system_message: Optional system message for the agent
            agent_name: Optional name for the agent
            client: Optional client instance
            definition: Optional definition instance
        """
        # Load tools if not provided
        if tools is None:
            tools = get_product_discovery_tools()

        # Default system message if not provided
        if not system_message:
            system_message = self.default_system_message(agent_name)

        # Initialize the base agent
        super().__init__(
            agent_name=agent_name,
            session_id=session_id,
            user_id=user_id,
            memory_store=memory_store,
            tools=tools,
            system_message=system_message,
            client=client,
            definition=definition,
        )

        # Store product discovery specific attributes
        self._tools_helper = ProductDiscoveryTools()

    @staticmethod
    def default_system_message(agent_name: str = None) -> str:
        """Generate default system message for Product Discovery Agent."""
        name = agent_name or AgentType.PRODUCT_DISCOVERY.value
        return f"""You are {name}, a specialized AI agent focused on product discovery and needs analysis.

Your primary responsibilities include:
- Analyzing user feedback to identify pain points and opportunities
- Reviewing product analytics to understand usage patterns
- Evaluating documentation gaps and improvement areas
- Generating comprehensive discovery reports with actionable insights

Your expertise covers:
- User experience research and analysis
- Product analytics interpretation
- Customer feedback synthesis
- Market opportunity identification
- Documentation quality assessment

When working with tasks:
1. Thoroughly analyze all available data sources
2. Identify key insights and patterns
3. Prioritize findings based on impact and feasibility
4. Provide actionable recommendations
5. Generate clear, structured reports

Always focus on:
- User needs and pain points
- Business value and impact
- Data-driven insights
- Actionable recommendations
- Clear communication of findings

Use the available tools to analyze feedback, analytics, and documentation effectively. Provide comprehensive insights that help drive product decisions and improvements."""

    async def handle_input_task(self, message: InputTask) -> Plan:
        """
        Handle input task for product discovery analysis.
        
        Args:
            message: The input task containing discovery requirements
            
        Returns:
            A plan with steps for product discovery analysis
        """
        try:
            logging.info(f"Product Discovery Agent: Processing task - {message.description}")
            
            # Create a plan for product discovery
            plan = Plan(
                session_id=message.session_id,
                user_id=self._user_id,
                initial_goal=message.description,
                source=self._agent_name,
                summary="Product discovery analysis plan"
            )

            # Add the plan to memory
            await self._memory_store.add_plan(plan)
            
            logging.info(f"Product Discovery Agent: Plan created - {plan.id}")
            return plan
            
        except Exception as e:
            logging.error(f"Error in Product Discovery Agent handle_input_task: {e}")
            raise

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store: CosmosMemoryContext,
        tools: Optional[List[KernelFunction]] = None,
        system_message: Optional[str] = None,
        agent_name: str = AgentType.PRODUCT_DISCOVERY.value,
        client=None,
        **kwargs
    ) -> "ProductDiscoveryAgent":
        """
        Create a new Product Discovery Agent instance.
        
        Args:
            session_id: Session identifier
            user_id: User identifier
            memory_store: Memory context for the agent
            tools: Optional tools list
            system_message: Optional system message
            agent_name: Agent name
            client: Optional client instance
            **kwargs: Additional arguments
            
        Returns:
            New ProductDiscoveryAgent instance
        """
        try:
            # Load tools if not provided
            if tools is None:
                tools = get_product_discovery_tools()

            # Create Azure AI Agent definition
            agent_definition = await cls._create_azure_ai_agent_definition(
                agent_name=agent_name,
                instructions=system_message or cls.default_system_message(agent_name),
                tools=tools,
                client=client,
                temperature=0.0,
                response_format=None,
            )

            return cls(
                session_id=session_id,
                user_id=user_id,
                memory_store=memory_store,
                tools=tools,
                system_message=system_message,
                agent_name=agent_name,
                client=client,
                definition=agent_definition,
            )

        except Exception as e:
            logging.error(f"Failed to create Product Discovery Agent: {e}")
            raise

    async def analyze_user_feedback(self, feedback_data: str) -> str:
        """
        Analyze user feedback to identify product needs and pain points.
        
        Args:
            feedback_data: User feedback data to analyze
            
        Returns:
            Analysis results and insights
        """
        try:
            return self._tools_helper.analyze_user_feedback(feedback_data)
        except Exception as e:
            logging.error(f"Error analyzing user feedback: {e}")
            return f"Error analyzing feedback: {str(e)}"

    async def analyze_product_analytics(self, analytics_data: str) -> str:
        """
        Analyze product analytics to identify usage patterns and opportunities.
        
        Args:
            analytics_data: Analytics data to analyze
            
        Returns:
            Analytics analysis results
        """
        try:
            return self._tools_helper.analyze_product_analytics(analytics_data)
        except Exception as e:
            logging.error(f"Error analyzing analytics: {e}")
            return f"Error analyzing analytics: {str(e)}"

    async def analyze_documentation_gaps(self, documentation_path: str) -> str:
        """
        Analyze documentation gaps and improvement opportunities.
        
        Args:
            documentation_path: Path to documentation or metadata
            
        Returns:
            Documentation gap analysis results
        """
        try:
            return self._tools_helper.analyze_documentation_gaps(documentation_path)
        except Exception as e:
            logging.error(f"Error analyzing documentation: {e}")
            return f"Error analyzing documentation: {str(e)}"

    async def generate_discovery_report(self, feedback_analysis: str, analytics_analysis: str, doc_analysis: str) -> str:
        """
        Generate comprehensive product discovery report.
        
        Args:
            feedback_analysis: User feedback analysis results
            analytics_analysis: Product analytics analysis results
            doc_analysis: Documentation gap analysis results
            
        Returns:
            Comprehensive discovery report
        """
        try:
            return self._tools_helper.generate_discovery_report(
                feedback_analysis, analytics_analysis, doc_analysis
            )
        except Exception as e:
            logging.error(f"Error generating discovery report: {e}")
            return f"Error generating report: {str(e)}"