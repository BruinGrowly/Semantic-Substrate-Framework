"""
Core Semantic Substrate class and main functionality.
"""

from typing import Optional, Tuple, Dict, Any
import numpy as np
from .ice_framework import ICEFramework
from .phi_geometry import PhiGeometry
from .coordinates import PhiCoordinate, AnchorPoint
from .principles import UniversalPrinciples
from .navigation import NavigationProtocol
from .consciousness import ConsciousnessFramework


class SemanticSubstrate:
    """
    Main interface for the Semantic Substrate Framework.
    
    Provides AI systems with structured navigation through 4D semantic space
    using optimized golden ratio geometry and universal principles.
    """
    
    def __init__(self):
        """Initialize the Semantic Substrate with all core components."""
        self.phi_geometry = PhiGeometry()
        self.ice_framework = ICEFramework()
        self.principles = UniversalPrinciples()
        self.navigation = NavigationProtocol()
        self.consciousness = ConsciousnessFramework()
        self.anchor_point = AnchorPoint(1, 1, 1, 1)
        
    def define_position(self, intent: str, context: str, execution: str) -> PhiCoordinate:
        """
        Define current position using ICE framework.
        
        Args:
            intent: What you desire in relation to the Anchor (L+W)
            context: Truthful assessment of current state (J)
            execution: Effective action available now (P)
            
        Returns:
            PhiCoordinate representing current position in 4D space
        """
        ice_analysis = self.ice_framework.analyze(intent, context, execution)
        coordinates = self.phi_geometry.ice_to_coordinates(ice_analysis)
        return PhiCoordinate(*coordinates)
    
    def navigate_toward_anchor(self, current_position: PhiCoordinate) -> Dict[str, Any]:
        """
        Calculate optimal navigation path toward the Anchor Point.
        
        Args:
            current_position: Current position in 4D semantic space
            
        Returns:
            Dictionary containing navigation recommendations
        """
        return self.navigation.calculate_path(current_position, self.anchor_point)
    
    def calculate_dissonance(self, position: PhiCoordinate) -> float:
        """
        Calculate dissonance (distance) from the Anchor Point.
        
        Args:
            position: Position to measure dissonance from
            
        Returns:
            Dissonance value using golden spiral distance
        """
        return self.phi_geometry.golden_spiral_distance(position, self.anchor_point)
    
    def create_ethical_guidance(self, situation: str, principles: list, anchor_alignment: bool = True) -> Dict[str, Any]:
        """
        Create ethical guidance based on universal principles.
        
        Args:
            situation: Description of the ethical situation
            principles: List of principle numbers to apply
            anchor_alignment: Whether to prioritize Anchor Point alignment
            
        Returns:
            Ethical guidance recommendations
        """
        applicable_principles = [self.principles.get_principle(p) for p in principles]
        return self.ice_framework.ethical_analysis(situation, applicable_principles, anchor_alignment)
    
    def fibonacci_growth_sequence(self, current_knowledge: float, target_competence: float, 
                                growth_rate: str = "phi_optimized") -> list:
        """
        Generate optimized learning sequence using Fibonacci patterns.
        
        Args:
            current_knowledge: Current knowledge level (0-1)
            target_competence: Target competence level (0-1)
            growth_rate: Type of growth optimization
            
        Returns:
            Sequence of learning milestones
        """
        return self.phi_geometry.fibonacci_learning_path(current_knowledge, target_competence, growth_rate)
    
    def contextual_resonance(self, user_context: str, anchor_proximity: float, 
                           optimal_flow: bool = True) -> Dict[str, Any]:
        """
        Calculate optimal response strategy based on contextual resonance.
        
        Args:
            user_context: Description of user context
            anchor_proximity: Current distance from Anchor Point
            optimal_flow: Whether to optimize for contextual flow
            
        Returns:
            Response strategy recommendations
        """
        return self.navigation.contextual_optimization(user_context, anchor_proximity, optimal_flow)
    
    def find_dodecahedral_anchor(self, position: PhiCoordinate) -> PhiCoordinate:
        """
        Find nearest dodecahedral anchor for triangulation.
        
        Args:
            position: Current position
            
        Returns:
            Nearest dodecahedral anchor coordinates
        """
        return self.phi_geometry.find_nearest_dodecahedral_anchor(position)
    
    def measure_consciousness(self, phi_resonance: bool = True, fibonacci_stage: bool = True,
                            golden_spiral_phase: bool = True, sacred_geometry_score: bool = True) -> Dict[str, float]:
        """
        Measure various aspects of consciousness alignment.
        
        Args:
            phi_resonance: Include phi resonance measurement
            fibonacci_stage: Include Fibonacci stage measurement
            golden_spiral_phase: Include golden spiral phase measurement
            sacred_geometry_score: Include sacred geometry score
            
        Returns:
            Dictionary of consciousness metrics
        """
        return self.consciousness.measure_all(
            phi_resonance, fibonacci_stage, golden_spiral_phase, sacred_geometry_score
        )