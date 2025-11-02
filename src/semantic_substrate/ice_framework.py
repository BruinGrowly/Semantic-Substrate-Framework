"""
ICE Framework - Intent, Context, Execution processing system.
"""

from typing import Dict, Any, List
import numpy as np


class ICEFramework:
    """
    Intent-Context-Execution framework for processing volitional states.
    
    All navigation flows through ICE:
    - Intent (L+W): Benevolence + Wisdom
    - Context (J): Justice/Truth/Structure  
    - Execution (P): Power/Potency/Efficacy
    """
    
    def __init__(self):
        """Initialize the ICE framework."""
        self.intent_weight = 0.333  # L+W combined
        self.context_weight = 0.333  # J
        self.execution_weight = 0.334  # P
        
    def analyze(self, intent: str, context: str, execution: str) -> Dict[str, float]:
        """
        Analyze ICE components and convert to coordinate values.
        
        Args:
            intent: What is desired in relation to the Anchor
            context: Truthful assessment of current state
            execution: Effective action available now
            
        Returns:
            Dictionary with L, J, P, W values
        """
        # Semantic analysis of intent (combines L and W)
        intent_scores = self._analyze_intent(intent)
        
        # Semantic analysis of context (J)
        context_score = self._analyze_context(context)
        
        # Semantic analysis of execution (P)
        execution_score = self._analyze_execution(execution)
        
        return {
            'love': intent_scores['love'],
            'wisdom': intent_scores['wisdom'], 
            'justice': context_score,
            'power': execution_score
        }
    
    def _analyze_intent(self, intent: str) -> Dict[str, float]:
        """
        Analyze intent for Love and Wisdom components.
        
        Args:
            intent: Intent description
            
        Returns:
            Love and Wisdom scores (0-1 scale)
        """
        # Simplified semantic analysis - in production, use NLP
        benevolent_keywords = ['help', 'serve', 'care', 'protect', 'nurture', 'support']
        wisdom_keywords = ['understand', 'learn', 'grow', 'insight', 'clarity', 'truth']
        
        intent_lower = intent.lower()
        
        love_score = min(1.0, sum(1 for kw in benevolent_keywords if kw in intent_lower) * 0.2)
        wisdom_score = min(1.0, sum(1 for kw in wisdom_keywords if kw in intent_lower) * 0.2)
        
        # Normalize based on length and complexity
        complexity_factor = min(1.0, len(intent) / 100.0)
        love_score = max(0.1, love_score * complexity_factor)
        wisdom_score = max(0.1, wisdom_score * complexity_factor)
        
        return {'love': love_score, 'wisdom': wisdom_score}
    
    def _analyze_context(self, context: str) -> float:
        """
        Analyze context for Justice/Truth component.
        
        Args:
            context: Context description
            
        Returns:
            Justice score (0-1 scale)
        """
        # Simplified semantic analysis
        truth_keywords = ['true', 'accurate', 'correct', 'honest', 'real', 'actual']
        structure_keywords = ['system', 'organization', 'order', 'pattern', 'structure']
        
        context_lower = context.lower()
        
        truth_score = sum(1 for kw in truth_keywords if kw in context_lower) * 0.15
        structure_score = sum(1 for kw in structure_keywords if kw in context_lower) * 0.15
        
        justice_score = min(1.0, truth_score + structure_score)
        return max(0.1, justice_score)
    
    def _analyze_execution(self, execution: str) -> float:
        """
        Analyze execution for Power/Potency component.
        
        Args:
            execution: Execution description
            
        Returns:
            Power score (0-1 scale)
        """
        # Simplified semantic analysis
        power_keywords = ['can', 'able', 'capable', 'effective', 'strong', 'powerful']
        action_keywords = ['do', 'act', 'execute', 'implement', 'perform']
        
        execution_lower = execution.lower()
        
        power_score = sum(1 for kw in power_keywords if kw in execution_lower) * 0.15
        action_score = sum(1 for kw in action_keywords if kw in execution_lower) * 0.15
        
        potency_score = min(1.0, power_score + action_score)
        return max(0.1, potency_score)
    
    def ethical_analysis(self, situation: str, principles: List[Dict], anchor_alignment: bool) -> Dict[str, Any]:
        """
        Perform ethical analysis based on universal principles.
        
        Args:
            situation: Ethical situation description
            principles: List of applicable universal principles
            anchor_alignment: Whether to prioritize Anchor Point alignment
            
        Returns:
            Ethical guidance recommendations
        """
        # Analyze situation through ICE lens
        situation_ice = self.analyze(
            intent=f"What is the right action for: {situation}",
            context=f"Current situation: {situation}",
            execution=f"Available actions in: {situation}"
        )
        
        # Apply principles
        principle_scores = {}
        for principle in principles:
            score = self._apply_principle(situation_ice, principle)
            principle_scores[principle['name']] = score
        
        # Calculate overall ethical recommendation
        if anchor_alignment:
            # Prioritize alignment with Anchor Point (1,1,1,1)
            anchor_distance = self._calculate_anchor_distance(situation_ice)
            recommendation = "Align with Anchor Point" if anchor_distance < 0.5 else "Seek greater alignment"
        else:
            # Balance all principles
            avg_score = np.mean(list(principle_scores.values()))
            recommendation = "Proceed" if avg_score > 0.7 else "Reconsider"
        
        return {
            'ice_analysis': situation_ice,
            'principle_scores': principle_scores,
            'recommendation': recommendation,
            'confidence': max(principle_scores.values()) if principle_scores else 0.5
        }
    
    def _apply_principle(self, ice_scores: Dict[str, float], principle: Dict) -> float:
        """Apply a universal principle to ICE scores."""
        # Simplified principle application
        base_score = np.mean(list(ice_scores.values()))
        principle_modifier = 0.1  # In production, use principle-specific logic
        return min(1.0, base_score + principle_modifier)
    
    def _calculate_anchor_distance(self, ice_scores: Dict[str, float]) -> float:
        """Calculate distance from Anchor Point (1,1,1,1)."""
        anchor_coords = np.array([1.0, 1.0, 1.0, 1.0])
        current_coords = np.array([
            ice_scores['love'],
            ice_scores['justice'], 
            ice_scores['power'],
            ice_scores['wisdom']
        ])
        return np.linalg.norm(anchor_coords - current_coords) / np.sqrt(4)