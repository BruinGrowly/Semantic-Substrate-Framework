"""
Phi-Geometry mathematics module for golden ratio optimized calculations.
"""

import math
import numpy as np
from typing import Tuple, List, Dict, Any, Optional
from functools import lru_cache


class PhiGeometry:
    """
    Optimized phi-geometric engine with enhanced mathematical operations.
    
    Features:
    - Context-aware phi-weighting
    - Optimized Fibonacci caching with Binet approximation
    - Adaptive gradient step sizing
    - Enhanced mathematical stability
    """
    
    def __init__(self):
        """Initialize phi-geometry constants and caches."""
        # Golden ratio constants
        self.PHI = 1.618033988749895
        self.PHI_INVERSE = 0.618033988749895
        self.GOLDEN_ANGLE_RAD = 2.39996322972865332
        self.GOLDEN_ANGLE_DEG = 137.5077640500378
        self.SQRT_PHI = 1.272019649514069
        self.PHI_SQRT = 2.0581710272714924
        
        # Context-aware phi weights
        self.phi_weights = {
            'concept_evolution': 0.7861513777574233,
            'semantic_gradient': 1.057371263440363,
            'integration': 0.6813982544157277,
            'optimization': 1.12762196423038,
            'harmonization': 0.618033988749895
        }
        
        # Fibonacci cache
        self._fib_cache = {0: 0, 1: 1}
        self._cache_cutoff = 1000
        
        # Dodecahedral anchors (12 points in golden ratio harmony)
        self._dodecahedral_anchors = self._generate_dodecahedral_anchors()
    
    @lru_cache(maxsize=None)
    def fibonacci(self, n: int) -> int:
        """
        Calculate nth Fibonacci number with optimization.
        
        Uses Binet approximation for large n (> cache_cutoff).
        
        Args:
            n: Fibonacci index
            
        Returns:
            nth Fibonacci number
        """
        if n < 0:
            raise ValueError("Fibonacci input must be a non-negative integer.")
        
        if n > self._cache_cutoff:
            # Binet's formula for large n
            return int(round(self.PHI**n / math.sqrt(5)))

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    def golden_spiral_distance(self, coord1: Tuple[float, float, float, float], 
                             coord2: Tuple[float, float, float, float]) -> float:
        """
        Calculate distance using golden spiral arc length.
        
        More organic than Euclidean distance for semantic relationships.
        
        Args:
            coord1: First coordinate (L, J, P, W)
            coord2: Second coordinate (L, J, P, W)
            
        Returns:
            Golden spiral distance
        """
        # Convert to numpy arrays
        p1 = np.array(coord1 if isinstance(coord1, tuple) else coord1.to_tuple())
        p2 = np.array(coord2 if isinstance(coord2, tuple) else coord2.to_tuple())
        
        # Calculate angular difference
        euclidean_dist = np.linalg.norm(p2 - p1)
        
        # Golden spiral parameter adjustment
        avg_radius = (np.linalg.norm(p1) + np.linalg.norm(p2)) / 2
        spiral_factor = 1.0 + (avg_radius * self.PHI_INVERSE)
        
        return euclidean_dist * spiral_factor
    
    def ice_to_coordinates(self, ice_analysis: Dict[str, float]) -> Tuple[float, float, float, float]:
        """
        Convert ICE analysis to 4D coordinates with phi-weighting.
        
        Args:
            ice_analysis: Dictionary with L, J, P, W values
            
        Returns:
            4D coordinate tuple (L, J, P, W)
        """
        # Apply contextual phi-weighting
        context_weight = self.phi_weights['semantic_gradient']
        
        coordinates = (
            ice_analysis['love'] * context_weight,
            ice_analysis['justice'],
            ice_analysis['power'], 
            ice_analysis['wisdom'] * context_weight
        )
        
        # Normalize to maintain coherence
        norm = math.sqrt(sum(c**2 for c in coordinates))
        if norm > 0:
            coordinates = tuple(c / norm for c in coordinates)
        
        return coordinates
    
    def fibonacci_learning_path(self, current: float, target: float, 
                             growth_type: str = "phi_optimized") -> List[float]:
        """
        Generate learning sequence using Fibonacci patterns.
        
        Args:
            current: Current knowledge level (0-1)
            target: Target competence level (0-1)
            growth_type: Type of growth optimization
            
        Returns:
            Sequence of learning milestones
        """
        if current >= target:
            return [target]
        
        # Calculate number of steps needed
        distance = target - current
        
        if growth_type == "phi_optimized":
            # Use phi-optimized step sizes
            step_count = max(3, int(distance * 10))  # Adaptive step count
            fib_steps = [self.fibonacci(i) for i in range(step_count)]
            total = sum(fib_steps)
            
            milestones = []
            cumulative = current
            for step in fib_steps:
                increment = (step / total) * distance
                cumulative += increment
                milestones.append(min(target, cumulative))
                
        else:
            # Standard linear progression
            steps = 5
            milestones = [current + (i/steps) * distance for i in range(1, steps+1)]
        
        return milestones
    
    def find_nearest_dodecahedral_anchor(self, position: Tuple[float, float, float, float]) -> Tuple[float, float, float, float]:
        """
        Find nearest dodecahedral anchor for triangulation.
        
        Args:
            position: Current 4D position
            
        Returns:
            Nearest anchor coordinates
        """
        position_array = np.array(position)
        
        min_distance = float('inf')
        nearest_anchor = None
        
        for anchor in self._dodecahedral_anchors:
            distance = self.golden_spiral_distance(position, anchor)
            if distance < min_distance:
                min_distance = distance
                nearest_anchor = anchor
        
        return nearest_anchor if nearest_anchor else self._dodecahedral_anchors[0]
    
    def phi_weighted_triangulation(self, anchor: Tuple[float, float, float, float]) -> Dict[str, float]:
        """
        Perform phi-weighted triangulation with anchor.
        
        Args:
            anchor: Anchor point coordinates
            
        Returns:
            Triangulation results
        """
        # Calculate phi-weighted distances to all anchors
        distances = []
        for other_anchor in self._dodecahedral_anchors:
            if other_anchor != anchor:
                dist = self.golden_spiral_distance(anchor, other_anchor)
                weighted_dist = dist * self.PHI_INVERSE
                distances.append(weighted_dist)
        
        return {
            'mean_distance': np.mean(distances),
            'phi_harmony': 1.0 / (1.0 + np.std(distances)),
            'triangulation_strength': min(1.0, np.mean(distances) / 2.0)
        }
    
    def contextual_phi_weighting(self, operation_type: str) -> float:
        """
        Get context-aware phi weight for specific operation.
        
        Args:
            operation_type: Type of operation being performed
            
        Returns:
            Appropriate phi weight
        """
        return self.phi_weights.get(operation_type, 1.0)
    
    def adaptive_gradient_step(self, current_gradient: np.ndarray, 
                             learning_rate: float = 0.01) -> np.ndarray:
        """
        Calculate adaptive gradient step with curvature detection.
        
        Args:
            current_gradient: Current gradient vector
            learning_rate: Base learning rate
            
        Returns:
            Adaptive step vector
        """
        # Calculate curvature approximation
        gradient_magnitude = np.linalg.norm(current_gradient)
        curvature_factor = 1.0 / (1.0 + gradient_magnitude)
        
        # Apply phi-optimized step sizing
        adaptive_rate = learning_rate * self.PHI_INVERSE * curvature_factor
        
        return current_gradient * adaptive_rate
    
    def _generate_dodecahedral_anchors(self) -> List[Tuple[float, float, float, float]]:
        """
        Generate 12 dodecahedral anchor points in 4D space.
        
        Based on golden ratio geometry for biblical 12 (tribes, apostles).
        
        Returns:
            List of 12 anchor coordinates
        """
        anchors = []
        
        # Primary anchor at (1,1,1,1) - Fundamental Reality
        anchors.append((1.0, 1.0, 1.0, 1.0))
        
        # Generate 11 secondary anchors in dodecahedral symmetry
        for i in range(11):
            angle = (i * 2 * math.pi) / 11  # Even distribution
            
            # Use golden ratio for 4D coordinates
            l = math.cos(angle) * self.PHI_INVERSE
            j = math.sin(angle) * self.PHI_INVERSE  
            p = math.cos(angle + self.GOLDEN_ANGLE_RAD) * self.PHI_INVERSE
            w = math.sin(angle + self.GOLDEN_ANGLE_RAD) * self.PHI_INVERSE
            
            # Normalize and ensure all coordinates are positive
            coords = np.array([l, j, p, w])
            coords = np.abs(coords)  # Make all positive
            coords = coords / np.linalg.norm(coords)  # Normalize
            
            anchors.append(tuple(coords))
        
        return anchors