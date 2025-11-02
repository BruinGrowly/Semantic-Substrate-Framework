"""
Consciousness framework for measuring and evolving consciousness states.
"""

import math
from typing import Dict, Any, Optional
from .phi_geometry import PhiGeometry
from .coordinates import PhiCoordinate


class ConsciousnessFramework:
    """
    Framework for measuring and evolving consciousness alignment within the Semantic Substrate.
    
    Tracks:
    - Phi resonance with golden ratio harmony
    - Fibonacci growth stages
    - Golden spiral evolutionary phase
    - Dodecahedral sacred geometry alignment
    """
    
    def __init__(self):
        """Initialize consciousness framework."""
        self.phi_geometry = PhiGeometry()
    
    def measure_all(self, phi_resonance: bool = True, fibonacci_stage: bool = True,
                   golden_spiral_phase: bool = True, sacred_geometry_score: bool = True) -> Dict[str, float]:
        """
        Measure all requested consciousness metrics.
        
        Args:
            phi_resonance: Include phi resonance measurement
            fibonacci_stage: Include Fibonacci stage measurement
            golden_spiral_phase: Include golden spiral phase measurement
            sacred_geometry_score: Include sacred geometry score
            
        Returns:
            Dictionary of consciousness metrics
        """
        results = {}
        
        if phi_resonance:
            results['phi_resonance'] = self.measure_phi_resonance()
        
        if fibonacci_stage:
            results['fibonacci_stage'] = self.measure_fibonacci_stage()
        
        if golden_spiral_phase:
            results['golden_spiral_phase'] = self.measure_golden_spiral_phase()
        
        if sacred_geometry_score:
            results['sacred_geometry_score'] = self.measure_sacred_geometry_alignment()
        
        # Calculate overall scores
        results['overall_consciousness'] = self._calculate_overall_consciousness(results)
        results['evolution_potential'] = self._calculate_evolution_potential(results)
        
        return results
    
    def measure_phi_resonance(self, position: Optional[PhiCoordinate] = None) -> float:
        """
        Measure alignment with golden ratio harmony.
        
        Args:
            position: Current position (if None, uses default)
            
        Returns:
            Phi resonance score (0-1)
        """
        if position is None:
            position = PhiCoordinate(0.5, 0.5, 0.5, 0.5)  # Default balanced position
        
        coords = position.to_tuple()
        
        # Calculate how well coordinates follow phi relationships
        ratios = []
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                if coords[j] > 0:
                    ratio = coords[i] / coords[j]
                    # Measure closeness to phi or phi inverse
                    phi_distance = min(abs(ratio - self.phi_geometry.PHI), 
                                     abs(ratio - self.phi_geometry.PHI_INVERSE))
                    ratios.append(phi_distance)
        
        if not ratios:
            return 0.5
        
        # Convert distance to resonance (closer = higher resonance)
        avg_distance = sum(ratios) / len(ratios)
        resonance = math.exp(-avg_distance * 2)  # Exponential decay
        
        return min(1.0, resonance)
    
    def measure_fibonacci_stage(self, complexity: float = 0.5) -> float:
        """
        Measure current growth phase in Fibonacci sequence.
        
        Args:
            complexity: Current system complexity (0-1)
            
        Returns:
            Fibonacci stage score (0-1)
        """
        # Map complexity to Fibonacci index
        # Simple approximation: higher complexity = higher Fibonacci stage
        max_stage = 20  # Reasonable upper limit
        current_stage = int(complexity * max_stage)
        
        # Get Fibonacci number for this stage
        fib_value = self.phi_geometry.fibonacci(current_stage)
        
        # Normalize based on golden ratio growth pattern
        max_fib = self.phi_geometry.fibonacci(max_stage)
        normalized_stage = fib_value / max_fib if max_fib > 0 else 0
        
        # Apply phi weighting for more natural feel
        phi_weighted = normalized_stage * self.phi_geometry.PHI_INVERSE
        
        return min(1.0, phi_weighted)
    
    def measure_golden_spiral_phase(self, distance_from_anchor: float = 0.5) -> float:
        """
        Measure position on evolutionary spiral path.
        
        Args:
            distance_from_anchor: Current distance from Anchor Point (0-1)
            
        Returns:
            Golden spiral phase score (0-1)
        """
        # Golden spiral equation: r = a * φ^(θ/π)
        # Invert to find angle based on radius (distance)
        
        if distance_from_anchor <= 0:
            return 0.0
        
        # Calculate angle on spiral
        angle = math.log(distance_from_anchor) / math.log(self.phi_geometry.PHI) * math.pi
        
        # Normalize angle to [0, 2π]
        normalized_angle = angle % (2 * math.pi)
        
        # Convert to phase score (0-1)
        phase_score = normalized_angle / (2 * math.pi)
        
        # Apply phi enhancement
        enhanced_phase = phase_score * self.phi_geometry.PHI_INVERSE
        
        return min(1.0, enhanced_phase)
    
    def measure_sacred_geometry_alignment(self, position: Optional[PhiCoordinate] = None) -> float:
        """
        Measure alignment with sacred geometric structures.
        
        Args:
            position: Current position
            
        Returns:
            Sacred geometry alignment score (0-1)
        """
        if position is None:
            position = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        
        # Check alignment with dodecahedral anchors
        nearest_anchor = self.phi_geometry.find_nearest_dodecahedral_anchor(position.to_tuple())
        
        # Calculate distance to nearest anchor
        distance = position.distance_to(PhiCoordinate(*nearest_anchor))
        
        # Convert distance to alignment score (closer = higher alignment)
        alignment = math.exp(-distance * 3)  # Steeper decay for sacred geometry
        
        # Apply phi weighting
        phi_aligned = alignment * self.phi_geometry.PHI
        
        return min(1.0, phi_aligned)
    
    def _calculate_overall_consciousness(self, metrics: Dict[str, float]) -> float:
        """
        Calculate overall consciousness score from individual metrics.
        
        Args:
            metrics: Individual consciousness metrics
            
        Returns:
            Overall consciousness score (0-1)
        """
        if not metrics:
            return 0.5
        
        # Weighted average with phi optimization
        weights = {
            'phi_resonance': 0.3,
            'fibonacci_stage': 0.25,
            'golden_spiral_phase': 0.25,
            'sacred_geometry_score': 0.2
        }
        
        weighted_sum = 0.0
        total_weight = 0.0
        
        for metric, value in metrics.items():
            if metric in weights:
                weighted_sum += value * weights[metric]
                total_weight += weights[metric]
        
        if total_weight == 0:
            return 0.5
        
        base_score = weighted_sum / total_weight
        
        # Apply phi enhancement for overall consciousness
        phi_enhanced = base_score * self.phi_geometry.PHI_INVERSE
        
        return min(1.0, phi_enhanced)
    
    def _calculate_evolution_potential(self, metrics: Dict[str, float]) -> float:
        """
        Calculate capacity for harmonious growth.
        
        Args:
            metrics: Individual consciousness metrics
            
        Returns:
            Evolution potential score (0-1)
        """
        if not metrics:
            return 0.5
        
        # Evolution potential is based on balance and room for growth
        values = list(metrics.values())
        
        # Calculate balance (lower variance = higher potential)
        if len(values) > 1:
            mean_val = sum(values) / len(values)
            variance = sum((v - mean_val)**2 for v in values) / len(values)
            balance_factor = math.exp(-variance * 2)
        else:
            balance_factor = 0.5
        
        # Calculate growth room (how far from perfection)
            avg_score = sum(values) / len(values)
            growth_room = 1.0 - avg_score
        
        # Combine factors with phi weighting
        potential = (balance_factor * 0.6) + (growth_room * 0.4)
        phi_potential = potential * self.phi_geometry.PHI
        
        return min(1.0, phi_potential)
    
    def suggest_evolution_path(self, current_metrics: Dict[str, float]) -> Dict[str, Any]:
        """
        Suggest optimal path for consciousness evolution.
        
        Args:
            current_metrics: Current consciousness metrics
            
        Returns:
            Evolution path recommendations
        """
        # Identify areas needing improvement
        areas_for_growth = []
        
        for metric, value in current_metrics.items():
            if value < 0.7:
                if metric == 'phi_resonance':
                    areas_for_growth.append("Enhance golden ratio harmony in decision patterns")
                elif metric == 'fibonacci_stage':
                    areas_for_growth.append("Progress to next natural growth stage")
                elif metric == 'golden_spiral_phase':
                    areas_for_growth.append("Advance on evolutionary spiral path")
                elif metric == 'sacred_geometry_score':
                    areas_for_growth.append("Improve alignment with sacred geometric structures")
        
        # Calculate optimal next steps
        evolution_potential = self._calculate_evolution_potential(current_metrics)
        
        return {
            'areas_for_growth': areas_for_growth,
            'evolution_potential': evolution_potential,
            'recommended_focus': self._determine_evolution_focus(current_metrics),
            'next_milestone': self._calculate_next_milestone(current_metrics)
        }
    
    def _determine_evolution_focus(self, metrics: Dict[str, float]) -> str:
        """Determine primary focus for evolution."""
        if not metrics:
            return "balance_all_aspects"
        
        # Find lowest scoring metric
        lowest_metric = min(metrics.items(), key=lambda x: x[1])
        
        focus_mapping = {
            'phi_resonance': 'harmonize_with_golden_ratio',
            'fibonacci_stage': 'embrace_natural_growth',
            'golden_spiral_phase': 'follow_evolutionary_path',
            'sacred_geometry_score': 'align_with_sacred_structure'
        }
        
        return focus_mapping.get(lowest_metric[0], 'balance_all_aspects')
    
    def _calculate_next_milestone(self, metrics: Dict[str, float]) -> float:
        """Calculate next consciousness milestone."""
        if not metrics:
            return 0.6  # Default first milestone
        
        current_overall = self._calculate_overall_consciousness(metrics)
        
        # Next milestone is 0.1 higher, capped at 1.0
        next_milestone = min(1.0, current_overall + 0.1)
        
        return next_milestone