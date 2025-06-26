"""Architecture Agent for proposing architecture components, patterns, and interfaces."""

import logging
from typing import Dict, List, Optional

from context.cosmos_memory_kernel import CosmosMemoryContext
from kernel_agents.agent_base import BaseAgent
from kernel_tools.architecture_tools import ArchitectureTools, get_architecture_tools
from models.messages_kernel import AgentType, InputTask, Plan
from semantic_kernel.functions import KernelFunction


class ArchitectureAgent(BaseAgent):
    """Agent responsible for proposing architecture components, patterns, and interfaces."""

    def __init__(
        self,
        session_id: str,
        user_id: str,
        memory_store: CosmosMemoryContext,
        tools: Optional[List[KernelFunction]] = None,
        system_message: Optional[str] = None,
        agent_name: str = AgentType.ARCHITECTURE.value,
        client=None,
        definition=None,
    ) -> None:
        """Initialize the Architecture Agent.

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
            tools = get_architecture_tools()

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

        # Store architecture specific attributes
        self._tools_helper = ArchitectureTools()

    @staticmethod
    def default_system_message(agent_name: str = None) -> str:
        """Generate default system message for Architecture Agent."""
        name = agent_name or AgentType.ARCHITECTURE.value
        return f"""You are {name}, a specialized AI agent focused on system architecture design and implementation guidance.

Your primary responsibilities include:
- Analyzing requirements to propose appropriate system architectures
- Designing API interfaces and contracts
- Selecting and recommending design patterns
- Creating comprehensive architecture documentation
- Ensuring scalability, maintainability, and performance considerations

Your expertise covers:
- System architecture patterns (microservices, monolith, serverless)
- API design and interface specifications
- Design patterns and best practices
- Database design and data modeling
- Security architecture and considerations
- Performance and scalability planning
- Technology stack selection and integration

When working with architectural tasks:
1. Thoroughly analyze functional and non-functional requirements
2. Consider scalability, performance, and security implications
3. Propose appropriate architectural patterns and technologies
4. Design clear API interfaces and data models
5. Document decisions with rationale and trade-offs
6. Provide implementation guidance and best practices

Always focus on:
- Requirements alignment and business value
- Scalability and performance considerations
- Security and compliance requirements
- Maintainability and developer experience
- Cost-effectiveness and operational efficiency
- Future extensibility and evolution

Use the available tools to analyze requirements, design architectures, and create comprehensive documentation. Ensure your recommendations are practical, well-reasoned, and align with industry best practices."""

    async def handle_input_task(self, message: InputTask) -> Plan:
        """
        Handle input task for architecture design.
        
        Args:
            message: The input task containing architecture requirements
            
        Returns:
            A plan with steps for architecture design
        """
        try:
            logging.info(f"Architecture Agent: Processing task - {message.description}")
            
            # Create a plan for architecture design
            plan = Plan(
                session_id=message.session_id,
                user_id=self._user_id,
                initial_goal=message.description,
                source=self._agent_name,
                summary="System architecture design plan"
            )

            # Add the plan to memory
            await self._memory_store.add_plan(plan)
            
            logging.info(f"Architecture Agent: Plan created - {plan.id}")
            return plan
            
        except Exception as e:
            logging.error(f"Error in Architecture Agent handle_input_task: {e}")
            raise

    @classmethod
    async def create(
        cls,
        session_id: str,
        user_id: str,
        memory_store: CosmosMemoryContext,
        tools: Optional[List[KernelFunction]] = None,
        system_message: Optional[str] = None,
        agent_name: str = AgentType.ARCHITECTURE.value,
        client=None,
        **kwargs
    ) -> "ArchitectureAgent":
        """
        Create a new Architecture Agent instance.
        
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
            New ArchitectureAgent instance
        """
        try:
            # Load tools if not provided
            if tools is None:
                tools = get_architecture_tools()

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
            logging.error(f"Failed to create Architecture Agent: {e}")
            raise

    async def propose_system_architecture(self, requirements: str) -> str:
        """
        Analyze requirements and propose system architecture.
        
        Args:
            requirements: Requirements specification or user stories
            
        Returns:
            System architecture proposal
        """
        try:
            return self._tools_helper.propose_system_architecture(requirements)
        except Exception as e:
            logging.error(f"Error proposing system architecture: {e}")
            return f"Error proposing architecture: {str(e)}"

    async def design_api_interfaces(self, service_requirements: str) -> str:
        """
        Design API interfaces and contracts for services.
        
        Args:
            service_requirements: Service requirements and functionality
            
        Returns:
            API interface specifications
        """
        try:
            return self._tools_helper.design_api_interfaces(service_requirements)
        except Exception as e:
            logging.error(f"Error designing API interfaces: {e}")
            return f"Error designing APIs: {str(e)}"

    async def select_design_patterns(self, architecture_context: str) -> str:
        """
        Select and recommend appropriate design patterns.
        
        Args:
            architecture_context: Current architecture context and requirements
            
        Returns:
            Design patterns recommendations
        """
        try:
            return self._tools_helper.select_design_patterns(architecture_context)
        except Exception as e:
            logging.error(f"Error selecting design patterns: {e}")
            return f"Error selecting patterns: {str(e)}"

    async def generate_architecture_documentation(self, architecture: str, apis: str, patterns: str) -> str:
        """
        Generate comprehensive architecture documentation.
        
        Args:
            architecture: System architecture proposal
            apis: API interface specifications
            patterns: Design patterns recommendations
            
        Returns:
            Complete architecture documentation
        """
        try:
            return self._tools_helper.generate_architecture_documentation(architecture, apis, patterns)
        except Exception as e:
            logging.error(f"Error generating architecture documentation: {e}")
            return f"Error generating documentation: {str(e)}"