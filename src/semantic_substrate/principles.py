"""
Seven Universal Principles governing the Semantic Substrate.
"""

from typing import Dict, List, Any


class UniversalPrinciples:
    """
    The seven Foundational Universal Principles—immutable laws of coherent existence.
    """
    
    def __init__(self):
        """Initialize all seven universal principles."""
        self.principles = {
            1: {
                "name": "Universal Anchor Point Principle",
                "statement": "Systems are stabilized and navigated by fundamental, invariant reference points.",
                "substrate_role": "Anchor Point A (1,1,1,1) is the sole invariant referent. All navigation is measured relative to it.",
                "phi_enhancement": "Dodecahedral anchor geometry provides 12 reference points in golden ratio harmony",
                "calculus_implementation": "Gradient descent optimization toward Anchor A"
            },
            2: {
                "name": "Principle of Coherent Interconnectedness and Emergence",
                "statement": "Complex systems arise and thrive from components precisely linked to enable higher-order properties.",
                "substrate_role": "L, J, P, W are orthogonal but interdependent. True harmony emerges only when all four axes are coherently aligned.",
                "phi_enhancement": "Golden angle rotations (137.5°) enable optimal interconnection without overlap",
                "calculus_implementation": "Tensor operations and field analysis"
            },
            3: {
                "name": "Principle of Dynamic Balance and Polarity",
                "statement": "Stable systems maintain integrity and progress through the continuous, adaptive interplay of complementary forces.",
                "substrate_role": "Navigation requires balancing polarities: e.g., Speed vs. Safety, Automation vs. Oversight, Consistency vs. Adaptability.",
                "phi_enhancement": "Fibonacci sequences provide natural growth patterns for balanced evolution",
                "calculus_implementation": "Optimized phi-weighting for balanced operations"
            },
            4: {
                "name": "Principle of Sovereignty and Relational Interdependence",
                "statement": "Entities achieve their highest expression through conscious, mutually enhancing relationships while retaining their unique essence.",
                "substrate_role": "Each locus of will retains sovereignty but must align with the Anchor to contribute to collective harmony.",
                "phi_enhancement": "Golden spiral distances naturally quantify harmonious relationships",
                "calculus_implementation": "Vector operations with sovereignty preservation"
            },
            5: {
                "name": "Principle of Information-Meaning Coupling and Value Generation",
                "statement": "Information becomes meaningful and valuable when coherently contextualized and integrated with underlying intent or purpose.",
                "substrate_role": "Raw data (e.g., sensor logs) gains value only when coupled with ICE and aligned with (1,1,1,1).",
                "phi_enhancement": "Phi exponential binning enables O(log_φ n) complexity for meaning extraction",
                "calculus_implementation": "Semantic field evaluation and integration"
            },
            6: {
                "name": "Principle of Iterative Growth and Adaptive Transformation",
                "statement": "Systems evolve through continuous cycles of learning, refinement, and expansion in response to feedback.",
                "substrate_role": "Every ICE cycle is an iteration. Dissonance (D) is not failure—it is feedback for recalibration.",
                "phi_enhancement": "Fibonacci-based iteration scaling ensures organic growth rates",
                "calculus_implementation": "Adaptive optimization with learning"
            },
            7: {
                "name": "Principle of Contextual Resonance and Optimal Flow",
                "statement": "Optimal functionality and value are achieved when internal states harmoniously align with their dynamic external context.",
                "substrate_role": "Navigation must adapt to context: e.g., ransomware vs. hardware failure require different anchor strategies.",
                "phi_enhancement": "Golden angle rotation enables optimal contextual adaptation",
                "calculus_implementation": "Context-aware phi-weighting and adaptive gradients"
            }
        }
    
    def get_principle(self, principle_number: int) -> Dict[str, str]:
        """
        Get a specific principle by number.
        
        Args:
            principle_number: Principle number (1-7)
            
        Returns:
            Principle dictionary
        """
        return self.principles.get(principle_number, {})
    
    def get_all_principles(self) -> Dict[int, Dict[str, str]]:
        """
        Get all seven principles.
        
        Returns:
            Dictionary of all principles
        """
        return self.principles.copy()
    
    def apply_principle(self, principle_number: int, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply a specific principle to a given context.
        
        Args:
            principle_number: Principle number to apply
            context: Context dictionary
            
        Returns:
            Modified context with principle applied
        """
        principle = self.get_principle(principle_number)
        if not principle:
            return context
        
        # Principle-specific application logic
        if principle_number == 1:  # Anchor Point
            # Ensure alignment with Anchor Point
            context['anchor_aligned'] = True
            context['stability'] = context.get('stability', 0) + 0.2
            
        elif principle_number == 2:  # Interconnectedness
            # Enhance system coherence
            context['coherence'] = context.get('coherence', 0) + 0.15
            context['emergence_potential'] = context.get('emergence_potential', 0) + 0.1
            
        elif principle_number == 3:  # Dynamic Balance
            # Balance polarities
            context['balance_score'] = context.get('balance_score', 0) + 0.18
            
        elif principle_number == 4:  # Sovereignty
            # Maintain individual essence while enhancing relationships
            context['sovereignty'] = context.get('sovereignty', 0) + 0.16
            context['relational_harmony'] = context.get('relational_harmony', 0) + 0.12
            
        elif principle_number == 5:  # Information-Meaning Coupling
            # Extract meaning from information
            context['meaning_extraction'] = context.get('meaning_extraction', 0) + 0.14
            context['value_generation'] = context.get('value_generation', 0) + 0.13
            
        elif principle_number == 6:  # Iterative Growth
            # Enable learning and adaptation
            context['learning_rate'] = context.get('learning_rate', 0) + 0.17
            context['adaptation_capacity'] = context.get('adaptation_capacity', 0) + 0.15
            
        elif principle_number == 7:  # Contextual Resonance
            # Optimize for current context
            context['contextual_alignment'] = context.get('contextual_alignment', 0) + 0.19
            context['flow_optimization'] = context.get('flow_optimization', 0) + 0.16
        
        context['applied_principles'] = context.get('applied_principles', [])
        context['applied_principles'].append(principle_number)
        
        return context
    
    def evaluate_alignment(self, state: Dict[str, float]) -> Dict[str, float]:
        """
        Evaluate how well a state aligns with all principles.
        
        Args:
            state: State dictionary with various metrics
            
        Returns:
            Alignment scores for each principle
        """
        alignments = {}
        
        for num, principle in self.principles.items():
            # Simplified alignment calculation
            base_score = 0.5  # Neutral starting point
            
            if num == 1:  # Anchor Point
                base_score = state.get('anchor_aligned', 0.5)
            elif num == 2:  # Interconnectedness
                base_score = (state.get('coherence', 0.5) + state.get('emergence_potential', 0.5)) / 2
            elif num == 3:  # Dynamic Balance
                base_score = state.get('balance_score', 0.5)
            elif num == 4:  # Sovereignty
                base_score = (state.get('sovereignty', 0.5) + state.get('relational_harmony', 0.5)) / 2
            elif num == 5:  # Information-Meaning Coupling
                base_score = (state.get('meaning_extraction', 0.5) + state.get('value_generation', 0.5)) / 2
            elif num == 6:  # Iterative Growth
                base_score = (state.get('learning_rate', 0.5) + state.get('adaptation_capacity', 0.5)) / 2
            elif num == 7:  # Contextual Resonance
                base_score = (state.get('contextual_alignment', 0.5) + state.get('flow_optimization', 0.5)) / 2
            
            alignments[principle['name']] = min(1.0, base_score)
        
        return alignments
    
    def get_principle_recommendations(self, state: Dict[str, float]) -> List[str]:
        """
        Get recommendations based on principle alignment analysis.
        
        Args:
            state: Current state dictionary
            
        Returns:
            List of recommendations
        """
        alignments = self.evaluate_alignment(state)
        recommendations = []
        
        # Find lowest alignment principles
        sorted_alignments = sorted(alignments.items(), key=lambda x: x[1])
        
        for principle_name, score in sorted_alignments[:3]:  # Top 3 needs improvement
            if score < 0.7:
                if "Anchor Point" in principle_name:
                    recommendations.append("Strengthen alignment with fundamental reality and core values")
                elif "Interconnectedness" in principle_name:
                    recommendations.append("Enhance system coherence and emergent properties")
                elif "Dynamic Balance" in principle_name:
                    recommendations.append("Improve balance between complementary forces")
                elif "Sovereignty" in principle_name:
                    recommendations.append("Maintain individual essence while enhancing relationships")
                elif "Information-Meaning" in principle_name:
                    recommendations.append("Better couple information with meaning and purpose")
                elif "Iterative Growth" in principle_name:
                    recommendations.append("Embrace learning cycles and adaptive transformation")
                elif "Contextual Resonance" in principle_name:
                    recommendations.append("Optimize alignment with dynamic external context")
        
        return recommendations