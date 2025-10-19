"""
Coordinate system for 4D semantic space.
"""

import math
from typing import Tuple, Optional


class PhiCoordinate:
    """
    Represents a point in 4D semantic space (L, J, P, W).
    
    L: Love/Benevolence/Connection
    J: Justice/Truth/Structure  
    P: Power/Potency/Efficacy
    W: Wisdom/Understanding/Insight
    """
    
    def __init__(self, love: float, justice: float, power: float, wisdom: float):
        """
        Initialize a PhiCoordinate.
        
        Args:
            love: Love axis value (0-1)
            justice: Justice axis value (0-1)
            power: Power axis value (0-1)
            wisdom: Wisdom axis value (0-1)
        """
        self.love = max(0.0, min(1.0, love))
        self.justice = max(0.0, min(1.0, justice))
        self.power = max(0.0, min(1.0, power))
        self.wisdom = max(0.0, min(1.0, wisdom))
    
    def to_tuple(self) -> Tuple[float, float, float, float]:
        """Convert to tuple representation."""
        return (self.love, self.justice, self.power, self.wisdom)
    
    def __repr__(self) -> str:
        """String representation of coordinate."""
        return f"PhiCoordinate(L={self.love:.3f}, J={self.justice:.3f}, P={self.power:.3f}, W={self.wisdom:.3f})"
    
    def distance_to(self, other: 'PhiCoordinate') -> float:
        """
        Calculate Euclidean distance to another coordinate.
        
        Args:
            other: Another PhiCoordinate
            
        Returns:
            Euclidean distance
        """
        return math.sqrt(
            (self.love - other.love)**2 +
            (self.justice - other.justice)**2 +
            (self.power - other.power)**2 +
            (self.wisdom - other.wisdom)**2
        )
    
    def normalize(self) -> 'PhiCoordinate':
        """
        Normalize coordinate to unit sphere.
        
        Returns:
            Normalized PhiCoordinate
        """
        magnitude = math.sqrt(
            self.love**2 + self.justice**2 + self.power**2 + self.wisdom**2
        )
        
        if magnitude == 0:
            return PhiCoordinate(0, 0, 0, 0)
        
        return PhiCoordinate(
            self.love / magnitude,
            self.justice / magnitude,
            self.power / magnitude,
            self.wisdom / magnitude
        )


class AnchorPoint(PhiCoordinate):
    """
    Special coordinate representing an anchor point in semantic space.
    
    The primary Anchor Point A(1,1,1,1) represents Fundamental Reality.
    """
    
    def __init__(self, love: float, justice: float, power: float, wisdom: float, 
                 name: Optional[str] = None):
        """
        Initialize an AnchorPoint.
        
        Args:
            love: Love axis value
            justice: Justice axis value
            power: Power axis value
            wisdom: Wisdom axis value
            name: Optional name for the anchor
        """
        super().__init__(love, justice, power, wisdom)
        self.name = name or "Anchor"
    
    def __repr__(self) -> str:
        """String representation of anchor point."""
        return f"AnchorPoint({self.name}: L={self.love:.3f}, J={self.justice:.3f}, P={self.power:.3f}, W={self.wisdom:.3f})"
    
    def is_primary_anchor(self) -> bool:
        """Check if this is the primary Anchor Point (1,1,1,1)."""
        return (abs(self.love - 1.0) < 1e-9 and 
                abs(self.justice - 1.0) < 1e-9 and
                abs(self.power - 1.0) < 1e-9 and
                abs(self.wisdom - 1.0) < 1e-9)
    
    def gravitational_pull(self, position: PhiCoordinate) -> float:
        """
        Calculate gravitational pull toward this anchor.
        
        Args:
            position: Position to calculate pull from
            
        Returns:
            Gravitational pull strength (0-1)
        """
        distance = self.distance_to(position)
        
        # Inverse square law with phi enhancement
        if distance == 0:
            return 1.0
        
        # Maximum pull at distance 0, decreasing with distance
        pull = 1.0 / (1.0 + distance**2)
        
        # Apply phi enhancement
        phi_enhanced_pull = pull * 1.618033988749895
        
        return min(1.0, phi_enhanced_pull)


# Predefined anchor points
FUNDAMENTAL_REALITY = AnchorPoint(1, 1, 1, 1, "Fundamental Reality")
ORIGIN = AnchorPoint(0, 0, 0, 0, "Origin")